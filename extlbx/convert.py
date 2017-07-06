# coding=utf-8
"""
CONVERT
Convierte los archivos y exporta versiones.

Autor: PABLO PIZARRO @ github.com/ppizarror
Fecha: 2017
Licencia: MIT
"""

# Importación de librerías
from __future__ import print_function
from latex import *
from releases import RELEASES
from stats import *
from subprocess import call
from utils import *
from version import *
from ziputils import *
import copy
import time


# noinspection PyBroadException
def export_informe(dosave=True, docompile=True, addwhitespace=True, deletecoments=True, plotstats=True):
    """
    Exporta el archivo principal, actualiza version.

    :param addwhitespace: Añade espacios en blanco al comprimir archivos
    :param deletecoments: Borra comentarios
    :param docompile: Compila automáticamente
    :param dosave: Guarda o no los archivos
    :param plotstats: Plotea las estadísticas
    :return:
    """

    # Tipo release
    release = RELEASES['INFORME']

    if dosave is False:
        docompile = False

    # Obtiene archivos
    configfile = release['CONFIGFILE']
    examplefile = release['EXAMPLEFILE']
    filedelcoments = release['FILEDELCOMENTS']
    files = release['FILES']
    filestrip = release['FILESTRIP']
    initconffile = release['INITCONFFILE']
    mainfile = release['MAINFILE']
    mainsinglefile = release['SINGLEFILE']
    stat = release['STATS']

    # Constantes
    main_data = open(mainfile)
    main_data.read()
    initdocumentline = find_line(main_data, '\\usepackage[utf8]{inputenc}') + 1
    codetablewidthpos = find_line(main_data, '\\begin{minipage}{0.976\\textwidth}')
    headersize = find_line(main_data, '% Licencia MIT:') + 2
    headerversionpos = find_line(main_data, '% Versión:      ')
    itableoriginal = '0.976\\textwidth'
    itablenew = '1.0126\\textwidth'
    versionheader = '% Versión:      {0} ({1})\n'
    main_data.close()

    print('ULTIMA VERSION:\t' + get_last_ver(stat['FILE']))
    ver = request_version()  # Se pide la versión
    ver, versiondev, versionhash = mk_version(ver)

    # Se obtiene el día
    dia = time.strftime('%d/%m/%Y')

    # Se crea el header de la versión
    versionhead = versionheader.format(ver, dia)

    # Se buscan números de lineas de hyperref
    initconf_data = open(initconffile)
    initconf_data.read()
    l_tdate, d_tdate = find_line(initconf_data, 'Template.Fecha', True)
    l_thash, d_thash = find_line(initconf_data, 'Template.Version.Hash', True)
    l_ttype, d_ttype = find_line(initconf_data, 'Template.Tipo', True)
    l_tvdev, d_tvdev = find_line(initconf_data, 'Template.Version.Dev', True)
    l_tvrel, d_tvrel = find_line(initconf_data, 'Template.Version.Release', True)
    l_vcmtd, d_vcmtd = find_line(initconf_data, 'pdfproducer', True)
    initconf_data.close()

    # Se actualizan líneas de hyperref
    d_tdate = replace_argument(d_tdate, 1, dia)
    d_thash = replace_argument(d_thash, 1, versionhash)
    d_ttype = replace_argument(d_ttype, 1, 'Normal')
    d_tvdev = replace_argument(d_tvdev, 1, versiondev + '-N')
    d_tvrel = replace_argument(d_tvrel, 1, ver)
    d_vcmtd = replace_argument(d_vcmtd, 1, latex_verline(ver))

    # Carga los archivos y cambian las versiones
    t = time.time()
    print('\nCREANDO TEMPLATE-INFORME')
    print('GENERANDO ARCHIVOS ... ', end='')
    for f in files.keys():
        data = files[f]
        # noinspection PyBroadException
        try:
            fl = open(f)
            for line in fl:
                data.append(line)
            fl.close()
        except:
            print('Error al cargar el archivo {0}'.format(f))

        # Se cambia la versión
        data[headerversionpos] = versionhead

        # Se actualiza la versión en initconf
        if f == initconffile:
            data[l_tdate] = d_tdate
            data[l_thash] = d_thash
            data[l_ttype] = d_ttype
            data[l_tvdev] = d_tvdev
            data[l_tvrel] = d_tvrel
            data[l_vcmtd] = d_vcmtd

        # Se reescribe el archivo
        newfl = open(f, 'w')
        for j in data:
            newfl.write(j)
        newfl.close()

    # Se obtiene la cantidad de líneas de código
    lc = 0
    for f in files.keys():
        lc += len(files[f])

    # Se modifican propiedades líneas data
    data = files[initconffile]
    d_ttype = replace_argument(d_ttype, 1, 'Compacto')
    d_tvdev = replace_argument(d_tvdev, 1, versiondev + '-C')
    data[l_thash] = d_thash
    data[l_ttype] = d_ttype
    data[l_tvdev] = d_tvdev

    # Se crea ejemplo generado automáticamente
    fl = open(release['EXAMPLECLONE'], 'w')
    data = files[examplefile]
    for k in data:
        fl.write(k)
    fl.close()

    # Se crea el archivo unificado
    fl = open(mainsinglefile, 'w')
    data = files[mainfile]
    data.pop(1)  # Se elimina el tipo de documento del header
    data.insert(1, '% Advertencia:  Documento generado automáticamente a partir del main.tex y\n%               los archivos .tex de la carpeta lib/\n')
    data[codetablewidthpos] = data[codetablewidthpos].replace(itableoriginal, itablenew)
    line = 0
    stconfig = False  # Indica si se han escrito comentarios en configuraciones

    # Se recorren las líneas del archivo
    for d in data:
        write = True
        if line < initdocumentline:
            fl.write(d)
            write = False
        # Si es una línea en blanco se agrega
        if d == '\n' and write:
            fl.write(d)
        else:
            # Si es un import pega el contenido
            try:
                if d[0:6] == '\input':
                    libr = d.replace('\input{', '').replace('}', '').strip()
                    libr = libr.split(' ')[0]
                    if '.tex' not in libr:
                        libr += '.tex'
                    if libr != examplefile:

                        # Se escribe desde el largo del header en adelante
                        libdata = files[libr]  # Datos del import
                        libstirp = filestrip[libr]  # Eliminar espacios en blanco
                        libdelcom = filedelcoments[libr]  # Borrar comentarios

                        for libdatapos in range(headersize, len(libdata)):
                            srclin = libdata[libdatapos]

                            # Se borran los comentarios
                            if deletecoments and libdelcom:
                                if '%' in srclin:
                                    if libr == configfile:
                                        if srclin.upper() == srclin:
                                            if stconfig:
                                                fl.write('\n')
                                            fl.write(srclin)
                                            stconfig = True
                                            continue
                                    comments = srclin.strip().split('%')
                                    if comments[0] is '':
                                        srclin = ''
                                    else:
                                        srclin = srclin.replace('%' + comments[1], '')
                                        if libdatapos != len(libdata) - 1:
                                            srclin = srclin.strip() + '\n'
                                        else:
                                            srclin = srclin.strip()
                                elif srclin.strip() is '':
                                    srclin = ''
                            else:
                                if libr == configfile:
                                    try:
                                        if libdata[libdatapos + 1][0] == '%' and srclin.strip() is '':
                                            srclin = ''
                                    except:
                                        pass

                            # Se ecribe la línea
                            if srclin is not '':
                                # Se aplica strip dependiendo del archivo
                                if libstirp:
                                    fl.write(srclin.strip())
                                else:
                                    fl.write(srclin)

                        fl.write('\n')  # Se agrega espacio vacío
                    else:
                        fl.write(d.replace('lib/', ''))
                    write = False
            except:
                pass

            # Se agrega un espacio en blanco a la página después del comentario
            if line >= initdocumentline and write:
                if d[0:2] == '% ' and d[3] != ' ' and d != '% CONFIGURACIONES\n':
                    if d != '% FIN DEL DOCUMENTO\n' and addwhitespace:
                        fl.write('\n')
                    d = d.replace('IMPORTACIÓN', 'DECLARACIÓN')
                    if d == '% RESUMEN O ABSTRACT\n':
                        d = '% ======================= RESUMEN O ABSTRACT =======================\n'
                    fl.write(d)
                elif d == '% CONFIGURACIONES\n':
                    pass
                else:
                    fl.write(d)

        # Aumenta la línea
        line += 1

    print('OK [t {0:.3g}]'.format(time.time() - t))
    fl.close()

    # Compila el archivo
    if docompile:
        t = time.time()
        with open(os.devnull, 'w') as FNULL:
            print('COMPILANDO ... ', end='')
            call(['pdflatex', mainsinglefile], stdout=FNULL)
            t1 = time.time() - t
            call(['pdflatex', mainsinglefile], stdout=FNULL)
            t2 = time.time() - t
            tmean = (t1 + t2) / 2
            print('OK [t {0:.3g}]'.format(tmean))

        # Se agregan las estadísticas
        add_stat(stat['FILE'], versiondev, tmean, dia, lc, versionhash)

        # Se plotean las estadísticas
        if plotstats:
            plot_stats(stat['FILE'], stat['CTIME'], stat['LCODE'])

    # Se exporta el proyecto normal
    czip = release['ZIP']['NORMAL']
    export_normal = Zip(czip['FILE'])
    export_normal.add_excepted_file(czip['EXCEPTED'])
    export_normal.add_file(czip['ADD']['FILE'])
    export_normal.add_folder(czip['ADD']['FOLDER'])
    export_normal.save()

    # Se exporta el proyecto único
    czip = release['ZIP']['COMPACT']
    export_single = Zip(czip['FILE'])
    export_single.add_file(czip['ADD']['FILE'], 'lib/')
    export_single.add_folder(czip['ADD']['FOLDER'])
    export_single.save()

    try:
        pyperclip.copy('Version ' + versiondev)
    except:
        pass
