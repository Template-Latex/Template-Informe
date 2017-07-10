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
from utils import *
import hashlib
import time


def request_version():
    """
    Pide la versión al usuario.

    :return: Version
    """
    # noinspection PyCompatibility
    return raw_input('\nINGRESE NUEVA VERSION: ')


# noinspection PyBroadException
def get_last_ver(statfile):
    """
    Retorna la última versión compilada.

    :param statfile:
    :return:
    """
    try:
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
    except:
        return '0.0.0 (NO_DATE)'

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

    if '.' in version or '-' in version or len(version) < 3:
        raise Exception('No pueden existir signos de puntiacion')

    if not (version[0].isdigit() and version[1].isdigit() and version[2].isdigit()):
        raise Exception('Tres primeros caracteres deben ser digitos')

    versionf = version[0] + '.' + version[1] + '.' + version[2]
    versiondev = ''
    if len(version) < 3 or len(version) > 10:
        raise Exception('Minimo 3 digitos, maximo 10')

    elif len(version) >= 4:
        if version[3].isdigit():
            versiondev = version[3:]
        elif version[3] in ['a', 'b', 'p']:
            if version[3] == 'a':
                versiondev = 'alpha-' + version[4:]
            elif version[3] == 'b':
                versiondev = 'beta-' + version[4:]
            elif version[3] == 'p':
                versiondev = 'pre-' + version[4:]
            for j in range(4, len(version)):
                if not version[j].isdigit():
                    raise Exception('Solo se aceptan digitos tras a,b,p')
        else:
            raise Exception('Formato de version incorrecto')

    # Retorna las versiones
    if versiondev is not '':
        versiondev = versionf + '-' + versiondev
    else:
        versiondev = versionf

    # Crea el id de compilación
    m = hashlib.md5()
    m.update(versiondev)
    m.update(time.strftime('%d/%m/%Y %H:%M:%S'))

    return versionf, versiondev, m.hexdigest().upper()


def validate_ver(newver, lastver):
    """
    Entrega True/False si la versión nueva es válida o no.

    :param newver: Versión nueva
    :param lastver: Versión anterior
    :return:
    """

    # noinspection PyUnusedLocal
    def _split1(u):
        return [int(u[0]), int(u[1]), int(u[2])]

    # noinspection PyUnusedLocal
    def _check1(u, v):
        a = u[0] == v[0] and u[1] == v[1] and u[2] > v[2]
        b = u[0] == v[0] and u[1] > v[1]
        c = u[0] > v[0]
        return a or b or c

    if len(lastver) == 5:
        lastver += '-0'
    if len(newver) == 5:
        newver += '-0'

    lastver = [lastver[0:5], lastver[6:]]
    newver = [newver[0:5], newver[6:]]

    # Se comprueba la primera parte
    lv1 = _split1(lastver[0].split('.'))
    nv1 = _split1(newver[0].split('.'))

    if _check1(nv1, lv1):
        return True
    else:
        lv2 = lastver[1]
        nv2 = newver[1]
        if len(nv2) > 1 and len(lv2) == 1:
            return True
        elif len(nv2) == 1 and len(lv2) > 1:
            return False
        else:
            if len(nv2) == 1 and len(lv2) == 1:
                return int(nv2) > int(lv2)
            else:
                lv3 = lv2.split('-')[0]
                nv3 = nv2.split('-')[0]

                if nv3 == 'pre' and lv3 != 'pre':
                    return True
                if nv3 == 'pre' and lv3 == 'pre':
                    return int(nv2.split('-')[1]) > int(lv2.split('-')[1])
                else:
                    if nv3 == 'beta' and lv3 == 'alpha':
                        return True
                    else:
                        if nv3 == 'alpha' and lv3 == 'alpha':
                            return int(nv2.split('-')[1]) > int(lv2.split('-')[1])
                        else:
                            return False
