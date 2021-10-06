# FLiP-Mobile

Building Mobile and Web Apps Utilizing Web Sockets and Apache Pulsar

## Web Sockets <-> Mobile App

```
ws://broker-service-url:8080/path?token=token
```

## Build a subscription and test that data is in the topic

```
bin/pulsar-client consume energy -s "energy-checker"


```

## Example Running SPA

![image](https://raw.githubusercontent.com/tspannhw/FLiP-Mobile/main/pulsarsockets.jpg)

## Example Streaming Links

```

ws://broker-service-url:8080/ws/v2/producer/persistent/:tenant/:namespace/:topic
ws://broker-service-url:8080/ws/v2/consumer/persistent/:tenant/:namespace/:topic/:subscription

```

## Resources

* https://github.com/tspannhw/FLiP-Energy
* https://github.com/tspannhw/FLiP-Transit
* https://pulsar.apache.org/docs/en/client-libraries-websocket/
* https://github.com/amiravni/MSGEQ7_ESP8266_WS2812/blob/master/ver2.0_ardIDE/webPage/webSocketScript.js
* https://github.com/dannyvai/plotly_websocket_example/blob/master/plot_graphs_from_websocket.html
* https://medium.com/front-end-weekly/websocket-and-data-visualization-be3613c880db
* https://github.com/ignoreintuition/websocket
