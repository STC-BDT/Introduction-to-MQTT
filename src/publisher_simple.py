import paho.mqtt.publish as publish

s = input("type your message here: ")

publish.single(
    topic="bdtstc",
    payload=s,
    hostname="broker.hivemq.com",
    port=8883,
    tls={"insecure": True}
)