#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Codigo que envia parametros mediante metodo GET
# a la direccion localhost:7015/api/id/:id

# Importar modulo
import requests

def sendGet(host,port,id_num):
	url_endpoint='/api/id'
	url='http://'+host+':'+str(port)+url_endpoint

	payload = {"id":id_num}

	response = requests.get(url+"/"+str(payload["id"]), json=payload, timeout=500)
	return response