from paho.mqtt.client import Client

def on_message(mqttc, data, msg):
    print (f'message:{msg.topic}:{msg.payload}:{data}')
    
    if data['status'] == 0:
        temp = int(msg.payload) 
        if temp>data['K0']:
            print('se pasa a escuchar humidity')
            mqttc.subscribe('humidity')
            data['status'] = 1
            
    elif data['status'] == 1:
        
        if msg.topic=='humidity':
            humidity = int(msg.payload)
            if humidity>data['K1']:
                print('Se deja de escuchar humidity')
                mqttc.unsubscribe('humidity') 
                data['status'] = 0
                
        elif 'temperature' in msg.topic:
            temp = int(msg.payload)
            if temp<=data['K0']:
                print('Se deja de escuchar humidity')
                data['status']=0
                mqttc.unsubscribe('humidity')
                
def on_log(mqttc, data, level, mensaje):
    print(f'LOG: {data}:{mensaje}')
    
def main(broker):
    data = {'K0':10, #temperatura a partir de la cual se escuchará humidity
            'K1':50, #humedad a partir de la cual se deja de escuchar humidity
            'status': 0} 
    mqttc = Client(userdata=data)
    mqttc.on_message = on_message
    mqttc.enable_logger()
    mqttc.connect(broker)
    mqttc.subscribe(f'temperature/t1')
    mqttc.loop_forever()
if __name__ == "__main__":
    import sys
    if len(sys.argv)<2:
        print(f"Usage: {sys.argv[0]} broker")
        sys.exit(1)
    broker = sys.argv[1]
    main(broker)

