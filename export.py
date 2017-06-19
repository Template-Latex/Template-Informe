# coding=utf-8
"""
Exporta main.tex a informe.tex (template sin archivos externos).
Cambia versión y fecha a archivos.

Autor: PABLO PIZARRO @ github.com/ppizarror
Fecha: ABRIL 2017
Licencia: MIT
"""

# Importación de librerías
from __future__ import print_function
from extlbx import *
from subprocess import call
import pyperclip
import time

# Archivos
CONFIGFILE = 'lib/config.tex'
EXAMPLEFILE = 'lib/example.tex'
EXAMPLEFILECOMPACT = 'example.tex'
INITCONFFILE = 'lib/initconf.tex'
MAINFILE = 'main.tex'
MAINFILESINGLE = 'informe.tex'
STATSFILE = 'stats/stats.txt'

# Constantes
main_data = open(MAINFILE)
main_data.read()
INITDOCUMENTLINE = find_line(main_data, '\\usepackage[utf8]{inputenc}') + 1
CODETABLEWIDTHPOS = find_line(main_data, '\\begin{minipage}{0.976\\textwidth}')
HEADERSIZE = find_line(main_data, '% Licencia MIT:') + 2
HEADERVERSIONPOS = find_line(main_data, '% Versión:      ')
ITABLEORIGINAL = '0.976\\textwidth'
ITABLENEW = '1.012\\textwidth'
VERSIONHEADER = '% Versión:      {0} ({1})\n'
main_data.close()

# Configuraciones
AUTOCOMPILE = True
ADDWHITESPACE = False
DELETECOMMENTS = True
PLOTSTATS = True

# Archivos a revisar
FILES = {
    'lib/config.tex': [],
    'lib/finalconf.tex': [],
    'lib/function/core.tex': [],
    'lib/function/elements.tex': [],
    'lib/function/equation.tex': [],
    'lib/function/image.tex': [],
    'lib/function/title.tex': [],
    'lib/greekenum.sty': [],
    'lib/imports.tex': [],
    'lib/index.tex': [],
    INITCONFFILE: [],
    'lib/pageconf.tex': [],
    'lib/portrait.tex': [],
    'lib/styles.tex': [],
    'lib/environments.tex': [],
    EXAMPLEFILE: [],
    MAINFILE: [],
    'example-chapternumber.tex': [],
    'test.tex': [],
    'test-functions.tex': [],
    'test-math.tex': []
}
FILEDELCOMMENTS = {
    'lib/config.tex': False,
    'lib/finalconf.tex': True,
    'lib/function/core.tex': True,
    'lib/function/elements.tex': True,
    'lib/function/equation.tex': True,
    'lib/function/image.tex': True,
    'lib/function/title.tex': True,
    'lib/imports.tex': True,
    'lib/index.tex': True,
    INITCONFFILE: True,
    'lib/pageconf.tex': True,
    'lib/portrait.tex': True,
    'lib/styles.tex': True,
    'lib/environments.tex': True,
    EXAMPLEFILE: False,
    MAINFILE: False
}
FILESTRIP = {
    'lib/config.tex': False,
    'lib/finalconf.tex': True,
    'lib/function/core.tex': True,
    'lib/function/elements.tex': True,
    'lib/function/equation.tex': True,
    'lib/function/image.tex': True,
    'lib/function/title.tex': True,
    'lib/imports.tex': True,
    'lib/index.tex': True,
    INITCONFFILE: True,
    'lib/pageconf.tex': True,
    'lib/portrait.tex': True,
    'lib/styles.tex': True,
    'lib/environments.tex': True,
    EXAMPLEFILE: False,
    MAINFILE: False
}

print('ULTIMA VERSION:\t' + get_last_ver(STATSFILE))
version = request_version()  # Se pide la versión
version, versiondev = mk_version(version)

# Se obtiene el día
dia = time.strftime("%d/%m/%Y")

# Se crea el header de la versión
versionhead = VERSIONHEADER.format(version, dia)
versionstrlen = max(0, 15 - (len(version) - 5))

# Se buscan números de lineas de hyperref
initconf_data = open(INITCONFFILE)
initconf_data.read()
l_tvdev, d_tvdev = find_line(initconf_data, 'Template.Version.Dev', True)
l_tvrel, d_tvrel = find_line(initconf_data, 'Template.Version.Release', True)
l_tdate, d_tdate = find_line(initconf_data, 'Template.Fecha', True)
l_ttype, d_ttype = find_line(initconf_data, 'Template.Tipo', True)
initconf_data.close()

# Se actualizan líneas de hyperref
d_tvdev = replace_argument(d_tvdev, 1, versiondev + '-N')
d_tvrel = replace_argument(d_tvrel, 1, version)
d_tdate = replace_argument(d_tdate, 1, dia)
d_ttype = replace_argument(d_ttype, 1, 'Normal')

# Carga los archivos y cambian las versiones
t = time.time()
print('\nGENERANDO ARCHIVOS ... ', end='')
for f in FILES.keys():
    data = FILES[f]
    # noinspection PyBroadException
    try:
        fl = open(f)
        for line in fl:
            data.append(line)
        fl.close()
    except:
        print('Error al cargar el archivo {0}'.format(f))

    # Se cambia la versión
    data[HEADERVERSIONPOS] = versionhead

    # Se actualiza la versión en initconf
    if f == INITCONFFILE:
        data[l_tvdev] = d_tvdev
        data[l_tvrel] = d_tvrel
        data[l_tdate] = d_tdate
        data[l_ttype] = d_ttype

    # Se reescribe el archivo
    newfl = open(f, 'w')
    for j in data:
        newfl.write(j)
    newfl.close()

# Se obtiene la cantidad de líneas de código
lc = 0
for f in FILES.keys():
    if f not in ['lib/greekenum.sty', 'example-chapternumber.tex', 'test.tex',
                 'test-functions.tex', 'test-math.tex']:
        lc += len(FILES[f])

# Se modifican propiedades líneas data
data = FILES[INITCONFFILE]
d_tvdev = replace_argument(d_tvdev, 1, versiondev + '-C')
d_ttype = replace_argument(d_ttype, 1, 'Compacto')
data[l_tvdev] = d_tvdev
data[l_ttype] = d_ttype

# Se crea el archivo de ejemplo unificado
fl = open(EXAMPLEFILECOMPACT, 'w')
data = FILES[EXAMPLEFILE]
data.pop(1)  # Se elimina el tipo de documento del header
data.insert(1, '% Advertencia:  Documento generado automáticamente a partir '
               'del archivo\n%               {0}\n'.format(EXAMPLEFILE))
for d in data:
    fl.write(d)
fl.close()

# Se crea el archivo unificado
fl = open(MAINFILESINGLE, 'w')
data = FILES[MAINFILE]
data.pop(1)  # Se elimina el tipo de documento del header
data.insert(1, '% Advertencia:  Documento generado automáticamente a partir '
               'del main.tex y\n%               los archivos .tex de la '
               'carpeta lib/\n')
data[CODETABLEWIDTHPOS] = data[CODETABLEWIDTHPOS].replace(
    ITABLEORIGINAL, ITABLENEW)
line = 0
stconfig = False  # Indica si se han escrito comentarios en configuraciones

# Se recorren las líneas del archivo
for d in data:
    write = True
    if line < INITDOCUMENTLINE:
        fl.write(d)
        write = False
    # Si es una línea en blanco se agrega
    if d == '\n' and write:
        fl.write(d)
    else:
        # Si es un import pega el contenido
        # noinspection PyBroadException
        try:
            if d[0:6] == '\input':
                libr = d.replace('\input{', '').replace('}', '').strip()
                libr = libr.split(' ')[0]
                libr += '.tex'
                if libr != EXAMPLEFILE:

                    # Se escribe desde el largo del header en adelante
                    libdata = FILES[libr]  # Datos del import
                    libstirp = FILESTRIP[libr]  # Eliminar espacios en blanco
                    libdelcom = FILEDELCOMMENTS[libr]  # Borrar comentarios

                    for libdatapos in range(HEADERSIZE, len(libdata)):
                        srclin = libdata[libdatapos]

                        # Se borran los comentarios
                        if DELETECOMMENTS and libdelcom:
                            if '%' in srclin:
                                if libr == CONFIGFILE:
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
                                    srclin = srclin.replace('%' + comments[1],
                                                            '')
                                    if libdatapos != len(libdata) - 1:
                                        srclin = srclin.strip() + '\n'
                                    else:
                                        srclin = srclin.strip()
                            elif srclin.strip() is '':
                                srclin = ''
                        else:
                            if libr == CONFIGFILE:
                                # noinspection PyBroadException
                                try:
                                    if libdata[libdatapos + 1][0] == '%' and \
                                                    srclin.strip() is '':
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
                    fl.write(d)
                write = False

        except Exception as e:
            pass
        # Se agrega un espacio en blanco a la página después del comentario
        if line >= INITDOCUMENTLINE and write:
            if d[0:2] == '% ' and d[3] != ' ' and d != '% CONFIGURACIONES\n':
                if d != '% FIN DEL DOCUMENTO\n' and ADDWHITESPACE:
                    fl.write('\n')
                d = d.replace('IMPORTACIÓN', 'DECLARACIÓN')
                if d == '% RESUMEN O ABSTRACT\n':
                    d = '% =========================== RESUMEN O ABSTRACT ' \
                        '===========================\n'
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
if AUTOCOMPILE:
    t = time.time()
    with open(os.devnull, 'w') as FNULL:
        print('COMPILANDO ... ', end='')
        call(['pdflatex', MAINFILESINGLE], stdout=FNULL)
        t1 = time.time() - t
        call(['pdflatex', MAINFILESINGLE], stdout=FNULL)
        t2 = time.time() - t
        tmean = (t1 + t2) / 2
        print('OK [t {0:.3g}]'.format(tmean))

    # Se agregan las estadísticas
    add_stat(STATSFILE, versiondev, tmean, dia, lc)

    # Se plotean las estadísticas
    if PLOTSTATS:
        plot_stats(STATSFILE)

# Se exporta el proyecto normal
export_normal = Zip('release/Template-Informe.zip')
export_normal.add_excepted_file('greekenum.sty')
export_normal.add_file('main.tex')
export_normal.add_folder('images')
export_normal.add_folder('lib')
export_normal.save()

# Se exporta el proyecto único
export_single = Zip('release/Template-Informe-Single.zip')
export_single.add_file('informe.tex')
export_single.add_folder('images')
export_single.add_file(EXAMPLEFILECOMPACT)
export_single.save()

# noinspection PyBroadException
try:
    pyperclip.copy('Version ' + versiondev)
except:
    pass
