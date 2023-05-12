from paho.mqtt.client import Client 
from time import sleep
import random 


def on_message(client,data,msg):   
    if data['status'] == 0:
        numero = round(float(msg.payload))
        if (numero %2) == 0:
            print('El número es par, por lo que se pasa a escuchar humidity')
            data['pares'].append(numero)
            client.subscribe('humidity')
            data['status'] = 1
       
    elif data['status'] == 1:
        data['humedad'].append(float(msg.payload))
        suma = sum(data['pares'])
        if suma > len(data['humedad']):
            client.publish("clients/publicaciones",str(sum)+str(len(data['humedad'])))
            data['pares']=[]
            data['humedad']=[]
            data['status']=0
        sleep(random.randint(1,5))  
        client.subscribe('numbers')
            
    
def on_log(mqttc, data, level, string):
    print(f'LOG: {data}: {string}')
    
def main(broker):

    data = {"pares" : [] , "humedad":[], "status" : 0 }
    mqttc = Client(userdata=data)
    mqttc.on_message = on_message
    mqttc.enable_logger()
    mqttc.connect(broker)
    mqttc.subscribe('numbers')
    mqttc.loop_forever()
if __name__ == "__main__":
    import sys
    if len(sys.argv)<2:
        print(f"Usage: {sys.argv[0]} broker")
        sys.exit(1)
    broker = sys.argv[1]
    main(broker)