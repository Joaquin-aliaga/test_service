#Autor: Joaquin Aliaga
#Este codigo es el primer test, usando modulo "request"
#Hace una peticion a un servidor (localhost:10000) e imprime en pantalla
#ciertos resultados. Luego hace assert del estado y del texto de la pagina

import requests 
#Obtenemos la informacion del servidor
try:
	req=requests.get('http://localhost:10000',timeout=0.1)
except Exception as e:
	print "Timeout Error"
	raise e

#Chequeamos que existe conexion,. 200 if true
print req.status_code 

#Obtenemos el contenido
print req.headers

#Obtenemos el texto de la pagina
texto=req.text
print texto

#Tiempo de respuesta
milliseconds=req.elapsed.microseconds/1000.
print req.elapsed
print milliseconds


#Asserting
#Conexion hecha
assert req.status_code==200

#La respuesta es texto
assert texto=='Hola mundo: Soy el servidor en Node.js', 'Error, la respuesta no es la esperada'

