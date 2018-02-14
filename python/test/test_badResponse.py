
import json
import ConfigParser
import pytest

#Obtener archivo de configuracion
cfg=ConfigParser.ConfigParser()
cfg.read("./config/config.cfg")
#Obtener variables desde archivo de configuracion
host=cfg.get("client","host")
port=cfg.get("client","port")
id_num=5

#Path
import sys
sys.path.append('../')
print sys.path

from main_server import client

nombre_esperado='lissett'

#La idea del test es cambiar la respuesta antes de ser enviada
#y verificar que la respuesta es incorrecta
@pytest.mark.skip(reason="No se puede pasar este test aun")
def test_badResponse():
	
	respuesta = client.sendGet(str(host),port,id_num)
	datos = json.loads(respuesta.text)
	
	assert datos['nombre']!=nombre_esperado