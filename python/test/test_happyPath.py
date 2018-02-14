import json
import ConfigParser
import pytest

#Obtener archivo de configuracion
cfg=ConfigParser.ConfigParser()
cfg.read("./config/config.cfg")
#Obtener variables desde archivo de configuracion
host=cfg.get("client","host")
port=cfg.get("client","port")
id_num=1

#Path
import sys
sys.path.append('../')
print sys.path

from main_server import client

nombre_esperado='jose'
saldo_esperado='1000'
numero_telefono_esperado=756392876
minutos_esperado=100

def test_happyPath():
	
	respuesta = client.sendGet(str(host),port,id_num)
	datos = json.loads(respuesta.text)
	
	assert datos['nombre']==nombre_esperado
	assert datos['saldo']==saldo_esperado
	assert datos['numero_telefono']==numero_telefono_esperado
	assert datos['minutos']==minutos_esperado