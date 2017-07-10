# coding=utf-8
"""
Toolbox para exportar el template.

Autor: PABLO PIZARRO @ github.com/ppizarror
Fecha: 2017
Licencia: MIT
"""

# noinspection PyUnresolvedReferences
from releases import RELEASES
# noinspection PyUnresolvedReferences
import convert
# noinspection PyUnresolvedReferences
from version import *
# noinspection PyUnresolvedReferences
from sound import Sound

# noinspection PyCompatibility,PyUnresolvedReferences
from Tkinter import *
# noinspection PyCompatibility,PyUnresolvedReferences
import tkFont
# noinspection PyUnresolvedReferences,PyCompatibility
import tkMessageBox

# noinspection PyUnresolvedReferences
from vframe import VerticalScrolledFrame

# Archivo de configuraciones
__actualpath = str(os.path.abspath(os.path.dirname(__file__))).replace('\\', '/')
EXTLBX_CONFIGS = __actualpath + '/config.json'

# Archivo de licencia
EXTLBX_LICENSE = __actualpath + '/LICENSE'


# noinspection PyCompatibility
def reload_extlbx():
    """
    Vuelve a cargar funciones.
    """
    reload(convert)
