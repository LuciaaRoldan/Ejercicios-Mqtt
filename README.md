# Ejercicios-Mqtt
En este repositorio se pueden encontrar 6 archivos de python.
## Broker
En este apartado se encuentra el esquema bbásico de un broker donde los usuarios se conectan y pueden enviar y recibir mensajes.
## Números 
En este apartado el cliente lee el topic 'numbers' y comprueba si el número leído es entero y de serlo comprueba si es primo.

## Temperaturas 
En este apartado el cliente lee los subtopics de 'temperature' y en un intervalo de 4 segundos calcual la temperatura máxima, mínima y media de cada sensor y de todos los sensores.
## Temperatura y humedad 
En este apartado el cliente escucha uno de los sensores de temperature, si su valor supera K0 entonces eschará el topic 'humidity' y si baja de K0 o el valor de humidity sube de K1 dejará de escuchar el topic 'humidity'.
## Temporizador 
En este apartado el cliente leerá mensajes en los que se indicarán: tiempo de espera, topic y mensaje a publicar una vez pasado el tiempo de espera. El cliente espera el tiempo indicado y luego publicar el mensaje en el topic correspondiente.
## Encadena_clientes
En este apartado se debían encadenar comportamientos de las soluciones anteriores. En esta propuesta de solución se conecta al topic 'numbers' y cuando escucha un número par se activa un temporizador donde escuchará el topic 'humidity' y comprobará si la suma de los pares almacenados es mayor que la longitud de humedades almacenadas. De serlo publica el dato de la suma de los pares y de la longitud de las humedades y reinicia a vacío la lista donde almacenaba esos datos y vuelve a comenzar.
