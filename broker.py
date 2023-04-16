
from paho.mqtt.client import Client

def on_message(client, userdata, msg):
    print("MESSAGE:", userdata, msg.topic, msg.payload)
    client.publish('prueba/tema', msg.payload)

def main(broker, topic):
    client = Client()
    client.on_message = on_message
    client.connect(broker)
    client.subscribe(topic)
    client.loop_forever()

if __name__ == "__main__":
    import sys
    if len(sys.argv)<3:
        print(f"Usage: {sys.argv[0]} broker topic")
        sys.exit(1)
    broker = sys.argv[1]
    topic = sys.argv[2]
    main(broker, topic)


