
import json
import ConfigParser
import pytest

#Obtener archivo de configuracion
cfg=ConfigParser.ConfigParser()
cfg.read("./config/config.cfg")
#Obtener variables desde archivo de configuracion
host=cfg.get("client","host")
port=cfg.get("client","port")
id_num=105

#Path
import sys
sys.path.append('../')
print sys.path

from main_server import client

codigo_esperado=1005
@pytest.mark.skip(reason="No se puede pasar este test aun")
def test_DB_CDR_Timeout():
	
	respuesta = client.sendGet(str(host),port,id_num)
	datos = json.loads(respuesta.text)
	
	assert datos['codigo']==codigo_esperado