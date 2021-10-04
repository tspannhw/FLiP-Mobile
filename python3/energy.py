from pyHS100 import Discover
import json
import datetime
import os
import os.path
import socket
import time
import uuid
from time import gmtime, strftime
import psutil
import requests
import websocket, base64, json

scheme = 'ws'
TOPIC = scheme + '://192.168.1.181:8080/ws/v2/producer/persistent/public/default/energy'
ws = websocket.create_connection(TOPIC)

# Get MAC address of a local interfaces
def psutil_iface(iface):
    # type: (str) -> Optional[str]
    import psutil
    nics = psutil.net_if_addrs()
    if iface in nics:
        nic = nics[iface]
        for i in nic:
            if i.family == psutil.AF_LINK:
                return i.address

headers = {'content-type': 'application/json'}

print('---')
for dev in Discover.discover().values():
        now = datetime.datetime.now()
        row = {}
        year = now.year
        month = now.month
        start = time.time()
        sysinfo = dev.get_sysinfo()
        uuid2 = '{0}_{1}'.format(strftime("%Y%m%d%H%M%S", gmtime()), uuid.uuid4())

        for k, v in dev.get_emeter_realtime().items():
            row["%s" % k] = v

        for k, v in sysinfo.items():
            row["%s" % k] = v

        emeterdaily = dev.get_emeter_daily(year=year, month=month)
        for k, v in emeterdaily.items():
            row["day%s" % k] = v

        hwinfo = dev.hw_info

        for k, v in hwinfo.items():
            row["%s" % k] = v

        timezone = dev.timezone

        for k, v in timezone.items():
            row["%s" % k] = v

        emetermonthly = dev.get_emeter_monthly(year=year)

        for k, v in emetermonthly.items():
            row["month%s" % k] = v

        row['host'] = dev.host
        row['current_consumption'] = dev.current_consumption()
        row['alias'] = dev.alias
        row['devicetime'] = dev.time.strftime('%m/%d/%Y %H:%M:%S')
        row['ledon'] = dev.led
        end = time.time()
        row['end'] = '{0}'.format(str(end))
        row['te'] = '{0}'.format(str(end - start))
        row['systemtime'] = datetime.datetime.now().strftime('%m/%d/%Y %H:%M:%S')
        row['cpu'] = psutil.cpu_percent(interval=1)
        row['memory'] = psutil.virtual_memory().percent
        usage = psutil.disk_usage("/")
        row['diskusage'] = "{:.1f}".format(float(usage.free) / 1024 / 1024)
        row['uuid'] = str(uuid2)
        row['macaddress'] = psutil_iface('wlan0')
        print(json.dumps(row))

        #   texdt style message = ''.join(['%s: %s' % (key, value) for (key, value) in row.items()])
        message = str(json.dumps(row) )
        message_bytes = message.encode('ascii')
        base64_bytes = base64.b64encode(message_bytes)
        base64_message = base64_bytes.decode('ascii')
        ws.send(json.dumps({ 'payload' : base64_message, 'properties': { 'device' : 'jetson2gb', 'protocol' : 'websockets' },'key': str(uuid2), 'context' : 5 }))

        response =  json.loads(ws.recv())
        if response['result'] == 'ok':
            print ('Message published successfully')
        else:
            print ('Failed to publish message:', response)
        ws.close()
