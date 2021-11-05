
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
key:[null], properties:[key=1636142420856], content:{"plugins":"PDF Viewer, Chrome PDF Viewer, Chromium PDF Viewer, Microsoft Edge PDF Viewer, WebKit built-in PDF, ","screen":"1792,1120,1792,1051,30,30","cores":"12 cores","downinfo":"5.85 Mb/s","rtt":"50 ms","effectiveInfo":"4g","saveData":false,"product":"product","productSize":"555","comment":"comment"}

```


### Reference

* https://pulsar.apache.org/docs/en/client-libraries-websocket/
* https://javascript.info/websocket
