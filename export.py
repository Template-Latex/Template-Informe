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
import time
from subprocess import call
from utils import *

# Archivos
CONFIGFILE = 'lib/config.tex'
EXAMPLEFILE = 'example.tex'
MAINFILE = 'main.tex'
MAINFILESINGLE = 'informe.tex'

# Constantes
main_data = open(MAINFILE)
main_data.read()
CODEVERSION = '\def\\templateversion{0}{1}% Versión del template\n '
CODEVERSIONPOS = find_line(main_data, '\def\\templateversion')
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
    'lib/functions.tex': [],
    'lib/greekenum.sty': [],
    'lib/imports.tex': [],
    'lib/index.tex': [],
    'lib/initconf.tex': [],
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
    'lib/functions.tex': True,
    'lib/imports.tex': True,
    'lib/index.tex': True,
    'lib/initconf.tex': True,
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
    'lib/functions.tex': True,
    'lib/imports.tex': True,
    'lib/index.tex': True,
    'lib/initconf.tex': True,
    'lib/pageconf.tex': True,
    'lib/portrait.tex': True,
    'lib/styles.tex': True,
    'lib/environments.tex': True,
    EXAMPLEFILE: False,
    MAINFILE: False
}

# noinspection PyCompatibility
version = raw_input('Ingrese la nueva version: ')  # Se pide la versión
version = version.strip()
versionf = version.split('-')
versiondev = version
version = versionf[0]
if len(version) == 0:
    exit()

# Se obtiene el día
dia = time.strftime("%d/%m/%Y")

# Se crea el header de la version
versionhead = VERSIONHEADER.format(version, dia)
versionstrlen = max(0, 15 - (len(version) - 5))
versioncode = CODEVERSION.format('{' + version + '}', ' ' * versionstrlen)

# Carga los archivos y cambia las versiones
t = time.time()
print('\nGenerando archivos ... ', end='')
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

    # Sólo para el archivo principal se cambia la versión
    if f == MAINFILE:
        data[CODEVERSIONPOS] = versioncode.replace('\n ', '\n')

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
    if line < CODEVERSIONPOS + 1:
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
        if line >= CODEVERSIONPOS + 1 and write:
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
        print('Compilando ... ', end='')
        call(['pdflatex', MAINFILESINGLE], stdout=FNULL)
        t1 = time.time() - t
        call(['pdflatex', MAINFILESINGLE], stdout=FNULL)
        t2 = time.time() - t
        tmean = (t1 + t2) / 2
        print('OK [t {0:.3g}]'.format(tmean))

    # Se agregan las estadísticas
    addstat('stats/stats.txt', versiondev, tmean, dia, lc)

    # Se plotean las estadísticas
    if PLOTSTATS:
        plot_stats('stats/stats.txt')

# Se exporta el proyecto normal
export_normal = Zip('release/Template-Informe.zip')
export_normal.add_excepted_file('greekenum.sty')
export_normal.add_file('main.tex')
export_normal.add_folder('images')
export_normal.add_folder('lib')
export_normal.add_file(EXAMPLEFILE)
export_normal.save()

# Se exporta el proyecto único
export_single = Zip('release/Template-Informe-Single.zip')
export_single.add_file('informe.tex')
export_single.add_folder('images')
export_single.add_file(EXAMPLEFILE)
export_single.save()
