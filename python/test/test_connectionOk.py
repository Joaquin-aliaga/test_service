
import json
import ConfigParser

#Obtener archivo de configuracion
cfg=ConfigParser.ConfigParser()
cfg.read("./config/config.cfg")
#Obtener variables desde archivo de configuracion
host=cfg.get("client","host")
port=cfg.get("client","port")
id_num=cfg.get("client","id")
#Path
import sys
sys.path.append('../')
print sys.path

from main_server import client

codigo_esperado=200

def test_connectionOk():
	
	respuesta=client.sendGet(str(host),port,id_num)
	
	assert respuesta.status_code==codigo_esperado