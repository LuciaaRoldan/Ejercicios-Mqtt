

from threading import Lock 
from paho.mqtt.client import Client
from time import sleep

def on_message(mqttc, data, msg):
    print ('MESSAGE', msg.topic, msg.payload)
    n = len('temperature/')
    lock = data['lock']
    lock.acquire()
    try:
        sensor = msg.topic[n:]
        if sensor in data:
            data['temperatura'][sensor].append(int(msg.payload))
        else:
            data['temperatura'][sensor]=[int(msg.payload)]
    finally:
        lock.release()
    print ('on_message', data)
def main(broker):
    data  = {'semaforo':Lock(), 'temperatura':{}}
    mqttc = Client(userdata=data)
    mqttc.on_message = on_message
    mqttc.connect(broker)
    mqttc.subscribe('temperature/#')
    mqttc.loop_start()
    while True:
        sleep(4)
        maximo_total = []
        minimo_total = []
        media_total = []
        for sensor  in data['temperatura'].values()[1]:
            temperaturas = sensor.values()
            maximo = max(temperaturas)
            maximo_total.append(maximo)
            minimo = min(temperaturas)
            minimo_total.append(minimo)
            media = sum(temperaturas)/len(temperaturas)
            media_total.append(media)            
            print(f'maximo {sensor} :{maximo},minimo {sensor} : {minimo},media {sensor}: {media}')
            data[sensor]=[]
        maximo = max(maximo_total)
        minimo = min(minimo_total)
        media = sum(media_total)/len(media_total)
        print(f'maximo total :{maximo},minimo total : {minimo},media total: {media}')
            
if __name__ == "__main__":
    import sys
    if len(sys.argv)<2:
        print(f"Usage: {sys.argv[0]} broker")
        sys.exit(1)
    broker = sys.argv[1]
    main(broker)

