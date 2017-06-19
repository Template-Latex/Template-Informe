# coding=utf-8
"""
VERSION
Funciones para pedir versión de cada compilación.

Autor: PABLO PIZARRO @ github.com/ppizarror
Fecha: 2017
Licencia: MIT
"""

# Importación de librerías
from __future__ import print_function
from utils import split_str


def request_version():
    """
    Pide la versión al usuario.

    :return: Version
    """
    # noinspection PyCompatibility
    return raw_input('\nINGRESE NUEVA VERSION: ')


def get_last_ver(statfile):
    """
    Retorna la última versión compilada.

    :param statfile:
    :return:
    """
    data = open(statfile)
    datal = []
    for d in data:
        datal.append(d.strip())
    lastline = split_str(datal[len(datal) - 1], ' ')
    ver = lastline[1]
    vtime = lastline[3]
    if ver.count('.') == 3:
        ver = ver.split('.')
        ver = '{0}.{1}.{2}-{3}'.format(ver[0], ver[1], ver[2], ver[3])
    lastver = '{0} ({1})'.format(ver, vtime)
    data.close()

    return lastver


def mk_version(version):
    """
    Genera el tag de versión.

    :param version: Str de la versión
    :return:
    """
    if len(version) == 0:
        exit()

    version = version.strip().lower()

    if '.' in version or '-' in version:
        raise Exception('Formato de version incorrecto')

    versionf = version[0] + '.' + version[1] + '.' + version[2]
    versiondev = ''
    if len(version) < 3:
        Exception('Formato de version incorrecto')
    elif len(version) >= 4:
        if version[3].isdigit():
            versiondev = version[3:]
        elif version[3] == 'a':
            versiondev = 'alpha-' + version[4:]
        elif version[3] == 'b':
            versiondev = 'beta-' + version[4:]
        elif version[3] == 'p':
            versiondev = 'pre-' + version[4:]
        else:
            Exception('Formato de version incorrecto')

    # Retorna las versiones
    if versiondev is not '':
        versiondev = versionf + '-' + versiondev
    else:
        versiondev = versionf
    return versionf, versiondev
