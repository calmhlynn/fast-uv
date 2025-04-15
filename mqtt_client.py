import paho.mqtt.client as mqtt

class MQTTClient:
    def __init__(self, broker_address: str, topic: str, client_id: str):
        self.broker_address = broker_address
        self.topic = topic
        self.client_id = client_id
        self.client = mqtt.Client(client_id)

        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message

    def on_connect(self, client, userdata, flags, rc):
        print(f"Connected with result code {rc}")
        # Subscribe to the topic
        client.subscribe(self.topic)

    def on_message(self, client, userdata, msg):
        print(f"Message received: {msg.topic} {msg.payload.decode()}")

    def connect(self):
        self.client.connect(self.broker_address)

    def publish(self, message: str):
        self.client.publish(self.topic, message)

    def start(self):
        # Start the loop to process network traffic and dispatch callbacks
        self.client.loop_start()

    def stop(self):
        # Stop the loop and disconnect
        self.client.loop_stop()
        self.client.disconnect()

if __name__ == "__main__":
    broker = "broker.hivemq.com"
    topic = "test/topic"
    client_id = "P1"

    mqtt_client = MQTTClient(broker_address=broker, topic=topic, client_id=client_id)
    mqtt_client.connect()
    mqtt_client.start()

    mqtt_client.publish("Hello MQTT")

