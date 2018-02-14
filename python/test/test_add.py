#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Este test es de prueba
import sys
sys.path.append('../')

import add

#Prueba para usar pytest
#Funcion suma
def test_add():
	assert add.add(4,5)==9