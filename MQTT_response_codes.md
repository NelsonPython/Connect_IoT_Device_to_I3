# MQTT response codes

When you send an mqtt CONNECT packet, you should receive a CONNACK response. This response contains one of the following codes:

0 - success, connection accepted 

1 - connection refused, bad protocol 

2 - refused, client-id error 

3 - refused, service unavailable 

4 - refused, bad username or password 

5 - refused, not authorized - you will get this code when your username and login are invalid


