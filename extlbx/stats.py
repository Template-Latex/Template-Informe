# coding=utf-8
"""
STATS
Estadísticas de compilación.

Autor: PABLO PIZARRO @ github.com/ppizarror
Fecha: 2017
Licencia: MIT
"""

# Importación de librerías
from __future__ import print_function
from matplotlib.ticker import MaxNLocator
from scipy import stats
import matplotlib.pyplot as plt
from utils import split_str


def generate_statline(statid, version, time, date, lc, vh):
    """
    Genera una línea de estadísticas.

    :param statid: ID de la línea
    :param version: Versión
    :param time: Tiempo de compilación
    :param date: Fecha de compilación
    :param lc: Número de líneas
    :param vh: Version hash
    :return:
    """
    statid = str(statid).ljust(6)
    version = str(version).ljust(18)
    time = str(time).ljust(10)
    date = str(date).ljust(14)
    lc = str(lc).ljust(10)
    vh = str(vh).ljust(0)

    return '{0}{1}{2}{3}{4}{5}'.format(statid, version, time, date, lc, vh)


# noinspection PyBroadException,PyUnboundLocalVariable
def add_stat(statfile, version, time, date, lc, vh, test=False):
    """
    Agrega una entrada al archivo de estadísticas.

    :param test: Indica testeo
    :param statfile: Archivo de estadísticas
    :param version: Versión del template
    :param time: Tiempo de compilación
    :param date: Fecha de compilación
    :param lc: Total de líneas de código
    :param vh: Version hash
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
                                         'LINEAS', 'HASH\n'))
    data.close()

    # Se comprueba que la version sea distinta
    if version == lastver:
        version = '{0}.{1}'.format(version, lastverid + 1)

    # Se crea una nueva línea
    newentry = generate_statline(lastid + 1, version, str(time)[0:5], date,
                                 lc, vh)
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


if __name__ == '__main__':
    plot_stats('../stats/stats.txt')
