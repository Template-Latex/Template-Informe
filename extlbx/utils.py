# coding=utf-8
"""
UTILS
Funciones utilitarias generales.

Autor: PABLO PIZARRO @ github.com/ppizarror
Fecha: 2017
Licencia: MIT
"""


def find_line(data, line, returnline=False):
    """
    Encuentra la linea en un archivo y devuelve su ubicación.

    :param returnline: Indica si retorna también la línea buscada
    :param data: Datos del archivo
    :param line: Línea a buscar
    :return:
    """
    k = 0
    if str(type(data)) == "<type 'file'>":
        data.seek(0)
    for i in data:
        if line in i.strip() or line == i.strip():
            if returnline:
                return k, i
            else:
                return k
        k += 1
    if returnline:
        return [-1, '']
    else:
        return -1


def split_str(s, t):
    """
    Divide una cadena s por un término t retornando los elementos no vacíos.

    :param s: String
    :param t: Elemento a dividir la cadena
    :return: Lista de elementos
    """
    s = s.split(t)
    e = list()
    for k in s:
        if k is not '':
            e.append(k)
    return e
