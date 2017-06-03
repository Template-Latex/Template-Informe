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


def find_line(data, line):
    """
    Encuentra la linea en un archivo y devuelve su ubicación.

    :param data: Datos del archivo
    :param line: Línea a buscar
    :return:
    """
    k = 0
    if str(type(data)) == "<type 'file'>":
        data.seek(0)
    for i in data:
        if line in i.strip() or line == i.strip():
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


# noinspection PyBroadException
def addstat(statfile, version, time, date, lc):
    """
    Agrega una entrada al archivo de estadísticas.

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
        lastentry = dataarr[lastentrypos].strip().split('\t')
        lastid = int(lastentry[0])
        dataarr[lastentrypos] = '{0}\n'.format(dataarr[lastentrypos])
    else:
        lastid = 0
        dataarr.append('ID\tVERSION\t\tCTIME\t\tFECHA\t\tLINEAS\n')
    data.close()

    # Se crea una nueva línea
    time = str(time)[0:5]
    newentry = '{0}\t{1}\t\t{2}\t\t{3}\t{4}'.format(lastid + 1, version,
                                                    time, date, lc)
    dataarr.append(newentry)

    # Se guarda el nuevo archivo
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
            j = i.strip().replace('\t\t', '\t').split('\t')
            numcomp.append(int(j[0]))
            timecomp.append(float(j[2]))
            lcode.append(int(j[4]))
        k += 1
    if len(numcomp) >= 3:
        plt.figure(1)
        fig, ax = plt.subplots()
        ax.plot(numcomp, timecomp)
        ax.xaxis.set_major_locator(MaxNLocator(integer=True))
        ax.set_xlabel(u'Número de compilación')
        ax.set_ylabel(u'Tiempo de compilación [s]')
        ax.set_title(u'Estadísticas')
        fig.savefig('stats-ctime.png', dpi=600)
        plt.figure(2)
        plt.plot(numcomp, lcode)
        plt.xlabel(u'Número de compilación')
        plt.ylabel(u'Líneas de código')
        plt.title(u'Estadísticas')
        plt.ylim([min(lcode) * 0.97, max(lcode) * 1.03])
        plt.savefig('stats-lcode.png', dpi=600)

    data.close()


if __name__ == '__main__':
    plot_stats('stats.txt')
