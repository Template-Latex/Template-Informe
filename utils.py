# coding=utf-8
"""
Clases y funciones utilitarias.

Autor: PABLO PIZARRO @ github.com/ppizarror
Fecha: ABRIL-JUNIO 2017
Licencia: MIT
"""

# Importación de librerías
from __future__ import print_function
from matplotlib.ticker import MaxNLocator
from scipy import stats
import matplotlib.pyplot as plt
import os
import zipfile


class Zip(object):
    """
    Clase para administrar archivos zip
    """

    def __init__(self, filename):
        """
        Constructor, crea un archivo zipfile con un nombre
        :param filename: Nombre del archivo
        """

        if '.zip' not in filename:
            filename += '.zip'

        # Crea un objeto zipfile
        self._zip = zipfile.ZipFile(filename, 'w', zipfile.ZIP_DEFLATED)

        # Lista de excepciones
        self._excptfiles = []

    def add_excepted_file(self, filename):
        """
        Agrega un archivo a la lista de excepciones
        
        :param filename: Nombre del archivo
        :type filename: str
        :return: None
        """
        self._excptfiles.append(filename)

    def _check_excepted_file(self, filename):
        """
        Indica si el archivo está dentro de la lista de excepciones
        
        :param filename: Nombre del archivo
        :type filename: str
        :return: Booleano
        :rtype: bool
        """
        filebasename = os.path.basename(filename)
        for f in self._excptfiles:
            if filebasename == f:
                return True
        return False

    def save(self):
        """
        Guarda el archivo zip
        
        :return: None
        """
        self._zip.close()

    def add_file(self, ufile):
        """
        Añade un archivo al zip
        
        :param ufile: Ubicación del archivo
        :type ufile: str
        :return: None
        """
        self._zip.write(ufile)

    def add_folder(self, folder):
        """
        Agrega una carpeta al archivo zip
        
        :param folder: Carpeta
        :type folder: str
        :return: None
        """
        for f in os.listdir(folder):
            full_path = os.path.join(folder, f)
            if os.path.isfile(full_path):
                if not self._check_excepted_file(full_path):
                    self.add_file(full_path)
            elif os.path.isdir(full_path):
                self.add_folder(full_path)


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
    return -1


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


def generate_statline(statid, version, time, date, lc):
    """
    Genera una línea de estadísticas.

    :param statid: ID de la línea
    :param version: Versión
    :param time: Tiempo de compilación
    :param date: Fecha de compilación
    :param lc: Número de líneas
    :return:
    """
    statid = str(statid).ljust(6)
    version = str(version).ljust(18)
    time = str(time).ljust(10)
    date = str(date).ljust(14)
    lc = str(lc).ljust(0)

    return '{0}{1}{2}{3}{4}'.format(statid, version, time, date, lc)


# noinspection PyBroadException,PyUnboundLocalVariable
def add_stat(statfile, version, time, date, lc, test=False):
    """
    Agrega una entrada al archivo de estadísticas.

    :param test: Indica testeo
    :param statfile: Archivo de estadísticas
    :param version: Versión del template
    :param time: Tiempo de compilación
    :param date: Fecha de compilación
    :param lc: Total de líneas de código
    :return:
    """

    # Se carga el archivo y se encuentra la última entrada
    dataarr = []
    try:
        data = open(statfile)
        for i in data:
            dataarr.append(i)
        lastentrypos = len(dataarr) - 1
    except:
        data = open(statfile, 'w')
        lastentrypos = -1
    if lastentrypos >= 0:
        lastentry = split_str(dataarr[lastentrypos].strip(), ' ')
        lastid = int(lastentry[0])
        lastver = lastentry[1].split('.')
        if len(lastver) == 4:
            lastverid = int(lastver[3])
            lastver = lastentry[1]
            lastver = lastver.replace('.' + str(lastverid), '')
        else:
            lastverid = 0
            lastver = lastentry[1]

        dataarr[lastentrypos] = '{0}\n'.format(dataarr[lastentrypos])
    else:
        lastid = 0
        lastver = ''
        dataarr.append(generate_statline('ID', 'VERSION', 'CTIME', 'FECHA',
                                         'LINEAS\n'))
    data.close()

    # Se comprueba que la version sea distinta
    if version == lastver:
        version = '{0}.{1}'.format(version, lastverid + 1)

    # Se crea una nueva línea
    newentry = generate_statline(lastid + 1, version, str(time)[0:5], date, lc)
    dataarr.append(newentry)

    # Se guarda el nuevo archivo
    if not test:
        data = open(statfile, 'w')
        for i in dataarr:
            data.write(i)
        data.close()


def plot_stats(statfile):
    """
    Grafica las estadísticas.

    :param statfile: Archivo de estadísticas
    :return:
    """
    data = open(statfile)
    numcomp = []
    timecomp = []
    lcode = []
    k = 0
    for i in data:
        if k > 0:
            j = split_str(i.strip(), ' ')
            numcomp.append(int(j[0]))
            timecomp.append(float(j[2]))
            lcode.append(int(j[4]))
        k += 1
    nlen = len(numcomp)
    lastid = numcomp[nlen - 1]
    if nlen >= 3:
        # Tiempo de compilación
        tme = stats.tmean(timecomp)
        trc = stats.trim_mean(timecomp, 0.15)
        plt.figure(1)
        fig, ax = plt.subplots()
        ax.plot(numcomp, timecomp, 'c', label=u'Tiempo compilación (s)')
        ax.plot([numcomp[0], numcomp[nlen - 1]], [tme, tme], 'r--',
                label=u'Tiempo medio ({0:.3g}s)'.format(tme))
        ax.plot([numcomp[0], numcomp[nlen - 1]], [tme, tme], 'b--',
                label=u'Media acotada ({0:.3g}s)'.format(trc))
        ax.xaxis.set_major_locator(MaxNLocator(integer=True))
        ax.set_xlabel(u'Número de compilación')
        ax.set_ylabel(u'Tiempo de compilación [s]')
        ax.set_title(u'Estadísticas')
        plt.xlim(1, lastid)
        ax.legend()
        fig.savefig('stats/stats-ctime.png', dpi=600)

        # Líneas de código
        fig, ax = plt.subplots()
        ax.plot(numcomp, lcode)
        ax.set_xlabel(u'Número de compilación')
        ax.set_ylabel(u'Líneas de código')
        ax.set_title(u'Estadísticas')
        plt.ylim([min(lcode) * 0.97, max(lcode) * 1.03])
        ax.xaxis.set_major_locator(MaxNLocator(integer=True))
        plt.xlim(1, lastid)
        fig.savefig('stats/stats-lcode.png', dpi=600)

    data.close()


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


if __name__ == '__main__':
    plot_stats('stats/stats.txt')
