# coding=utf-8
"""
LATEX
Funciones utilitarias para el manejo de comandos y código LaTeX.

Autor: PABLO PIZARRO @ github.com/ppizarror
Fecha: 2017
Licencia: MIT
"""


def find_command(data, commandname):
    """
    Busca las lineas de la función en un archivo.

    :param data: Datos del archivo
    :param commandname: Nombre de la función
    :return:
    """
    data.seek(0)
    k = 0
    commandline = '\\newcommand{\\' + commandname + '}'
    foundcommand = -1
    for i in data:
        if foundcommand == -1:
            if commandline in i.strip():
                foundcommand = k
        else:
            if i.strip() == '}':
                return [foundcommand, k]
        k += 1
    return [-1, -1]


def replace_argument(line, argnum, new, arginitsep='{', argendsep='}'):
    """
    Reemplaza el argumento entre llaves de una determinada línea.

    :param argendsep: Keyword al finalizar argumento
    :param arginitsep: Keyword al iniciar argumento
    :param new: Nuevos datos
    :param line: Linea a reemplazar
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
