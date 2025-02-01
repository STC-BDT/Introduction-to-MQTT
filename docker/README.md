# Eclispe mosquitto docker compose

This repository contains an example of a docker compose containing  a MQTT broker. This example is based on this [article](https://medium.com/@tomer.klein/docker-compose-and-mosquitto-mqtt-simplifying-broker-deployment-7aaf469c07ee)

## Run the broker

```bash
docker compose up -d
```

The broker will be available on port 1883. The configured user has the username `user1` and the password `password`.