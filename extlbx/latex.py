# coding=utf-8
"""
LATEX
Funciones utilitarias para el manejo de comandos y código LaTeX.

Autor: PABLO PIZARRO @ github.com/ppizarror
Fecha: 2017
Licencia: MIT
"""

# Importación de librerías
from __future__ import print_function
import types


def find_block(data, initstr, blankend=False):
    """
    Busca el bloque de texto en una lista y devuelve el número de las líneas.

    :param blankend: Indica si el bloque termina en blanco
    :param data: Lista de un archivo
    :param initstr: Texto inicial del bloque
    :return:
    """
    j = 0
    i = -1
    f = -1
    for k in data:
        k = decodeline(k)
        if initstr.lower() in k.strip().lower() and i < 0:
            i = j
        if not blankend:
            if i >= 0 and ((k.strip() == '}' and len(k.strip()) == 1) or k.strip() == '%ENDBLOCK'):
                f = j
                break
        else:
            if i >= 0 and k.strip() == '':
                f = j
                break
        j += 1
    return i, f


def find_line(data, initstr, blankend=False):
    """
    Busca una línea.

    :param blankend: Indica si el bloque termina en blanco
    :param data: Lista de un archivo
    :param initstr: Texto inicial de la línea
    :return:
    """
    i, _ = find_block(data, initstr, blankend)
    return i


def find_command(data, commandname):
    """
    Busca las líneas de la función en un archivo.

    :param data: Datos del archivo
    :param commandname: Nombre de la función
    :return:
    """
    data.seek(0)
    k = 0
    commandline = '\\newcommand{\\' + commandname + '}'
    foundcommand = -1
    for i in data:
        i = decodeline(i)
        if foundcommand == -1:
            if commandline in i.strip():
                foundcommand = k
        else:
            if i.strip() == '}':
                return [foundcommand, k]
        k += 1
    return [-1, -1]


def decodeline(line):
    """
    Convierte de unicode a utf8.

    :param line: Línea
    :return:
    """
    if isinstance(type(line), types.UnicodeType):
        return line.encode('utf-8')
    else:
        return str(line)


def replace_argument(line, argnum, new, arginitsep='{', argendsep='}'):
    """
    Reemplaza el argumento entre llaves de una determinada línea.

    :param argendsep: Keyword al finalizar argumento
    :param arginitsep: Keyword al iniciar argumento
    :param new: Nuevos datos
    :param line: Línea a reemplazar
    :param argnum: Número del argumento
    :return: String
    """
    if argnum < 1:
        raise Exception('Numero de argumento invalido')
    n = len(line)
    c = False
    ki = -1
    ke = 0
    a = []
    line = decodeline(line)
    for k in range(0, n):
        if line[k] is arginitsep and c is not True:
            c = True
            k += 1
            ki = k
            a.append([line[ke:ki], False])
        elif line[k] is argendsep and c:
            c = False
            ke = k
            k += 1
            if ke < ki:
                raise Exception('Error al encontrar cierre parametro')
            a.append([line[ki:ke], True])
    a.append([line[ke:n], True])

    d = 0
    f = False
    for k in range(0, len(a)):
        if a[k][1]:
            d += 1
        if d == argnum:
            a[k][0] = new
            f = True
            break
    if not f:
        raise Exception('No se encontro el numero de argumento')
    z = ''
    for k in a:
        z += k[0]
    return z
