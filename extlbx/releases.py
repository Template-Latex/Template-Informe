# coding=utf-8
"""
RELEASES
Contiene archivos de cada release.

Autor: PABLO PIZARRO @ github.com/ppizarror
Fecha: 2017
Licencia: MIT
"""

# Importación de librerías
import json
import os

# Se carga json
__actualpath = str(os.path.abspath(os.path.dirname(__file__))).replace('\\', '/')
with open(__actualpath + '/releases.json') as json_data:
    RELEASES = json.load(json_data)

# Constantes
REL_AUXILIAR = 'AUXILIAR'
REL_CONTROLES = 'CONTROLES'
REL_INFORME = 'INFORME'
