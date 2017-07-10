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

# Se carga json
with open('extlbx/releases.json') as json_data:
    RELEASES = json.load(json_data)

# Constantes
REL_AUXILIAR = 'AUXILIAR'
REL_CONTROLES = 'CONTROLES'
REL_INFORME = 'INFORME'
