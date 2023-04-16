#LUCÍA ROLDÁN RODRÍGUEZ

from paho.mqtt.client import Client
import math

def is_prime(n):
    for i in range(2,int(math.sqrt(n))+1):
        if (n%i) == 0:
            return False
    return True

    
def on_message(mqttc, data, msg):
    print(f"MESSAGE:data:{data}, msg.topic:{msg.topic}, payload:{msg.payload}")
    try:
        numero = msg.payload
        if int(numero)  == float (numero):
            print('El número es entero')
            if is_prime(int(numero)):
                print('El número es primo')
            else:
                print('El número no es primo')
        else:
            print('El número no es entero')
                
    except ValueError as e:
        print(e)
        pass
    
def on_log(mqttc, userdata, level, string):
    print("LOG", userdata, level, string)
    
def main(broker):
    data = {'client':None,
            'broker': broker}
    mqttc = Client(userdata=data)
    data['client'] = mqttc
    mqttc.enable_logger()
    mqttc.on_message = on_message
    mqttc.on_log = on_log
    mqttc.connect(broker)
    mqttc.subscribe('numbers')
    mqttc.loop_forever()
    
if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} broker")
        sys.exit(1)
    broker = sys.argv[1]
    main(broker)
