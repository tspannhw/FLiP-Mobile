
### Create Topic

```

bin/pulsar-admin topics create persistent://public/default/clickstream

```

### Consume Data

```

bin/pulsar-client consume "persistent://public/default/clickstream" -s click-reader -n 0

```

### Data

```

----- got message -----
key:[null], properties:[key=1636144174694], content:{"battery":"battery.level=1,battery.charging=true","plugins":"PDF Viewer, Chrome PDF Viewer, Chromium PDF Viewer, Microsoft Edge PDF Viewer, WebKit built-in PDF, ","screen":"1792,1120,1792,1051,30,30","cores":"12 cores","downinfo":"2.45 Mb/s","rtt":"50 ms","effectiveInfo":"4g","saveData":false,"product":"product name test","productSize":"252355","comment":"comment\nline\nline2\nline3\nline4555"}
16:29:40.369 [pulsar-timer-5-1] INFO  org.apache.pulsar.client.impl.ConsumerStatsRecorderImpl - [persistent://public/default/clickstream] [click-reader] [2a3ac] Prefetched messages: 0 --- Consume throughput received: 0.03 msgs/s --- 0.00 Mbit/s --- Ack sent rate: 0.03 ack/s --- Failed messages: 0 --- batch messages: 0 ---Failed acks: 0

```
### Send Data From Web Page via Websockets through Apache Pulsar

* https://github.com/tspannhw/FLiP-Mobile/blob/main/ws.html

### Reference

* https://pulsar.apache.org/docs/en/client-libraries-websocket/
* https://javascript.info/websocket
