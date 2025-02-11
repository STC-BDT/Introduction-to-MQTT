import paho.mqtt.subscribe as subscribe

def on_message_print(client, userdata, message):
    print("%s %s" % (message.topic, message.payload))
    userdata["message_count"] += 1
    # if userdata["message_count"] >= 5:
    #     # it's possible to stop the program by disconnecting
    #     client.disconnect()

subscribe.callback(on_message_print, "bdtstc/team/#",
                   hostname="broker.hivemq.com",
                   port=8883,
                   tls={"insecure": True},
                   userdata={"message_count": 0}
                   )