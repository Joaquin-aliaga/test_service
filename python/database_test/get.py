#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Codigo que envia parametros mediante metodo GET
#a la direccion localhost:8080/api/id/:id
#Recibe el numero de telefono del usuario
#Tiene un set de posibles errores

#Importar modulo
import requests
import json

#Definir URL
url='http://localhost:8080/api/id'

#Los parametros se envian dentro del atributo "payload"

#Ciclo for para probar id's
#for i in range(4):
id= 1;
payload = {"id":str(id)}

#Se Envian datos en formato json
#Se define timeout en segundos
try:
	response = requests.get(url+"/"+payload["id"], json=payload, timeout=1000)
except Exception as e:
	print "Timeout Error "
	raise e

#Tambien se puede enviar como data=json.dumps(payload)
#Para que lleguen en el atributo "data" en formato json

#Assert de Codigos recibidos
codigo_respuesta=response.status_code
print codigo_respuesta

if(codigo_respuesta==200):
	print("Conexion correcta")
elif codigo_respuesta==404:
	raise NameError("No se envió ningun dato")
else:
	raise NameError("Error en la conexión")

headers_response=response.headers
print headers_response

#Obtener datos de respuesta
data=json.loads(response.text)
#print data

#Test de usuario existente
assert data["results"]!=[], "El id no tiene asociado un usuario"
for datos in data["results"]:
	print 'Nombre:',datos["nombre"],",",'Número telefono:', datos["numero_telefono"]
#El tiempo transcurrido es del metodo requests.get() independiente de 
#en que lugar del codigo se ponga.

milliseconds=response.elapsed.microseconds/1000.
print 'Tiempo transcurrido despues de get:',milliseconds,'ms'