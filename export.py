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
import time
import copy

"""
TEMPLATE-INFORMES.
A PARTIR DE ESTE SE GENERARÁN LOS SUBRELEASES.
"""

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

# Subreleases
SUBRELEASE = {
    'AUXILIAR': 'subreleases/Template-Auxiliares/'
}

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
version, versiondev, versionhash = mk_version(version)

# Se obtiene el día
dia = time.strftime('%d/%m/%Y')
diahora = time.strftime('%d/%m/%Y %H:%M:%S')

# Se crea el header de la versión
versionhead = VERSIONHEADER.format(version, dia)
versionstrlen = max(0, 15 - (len(version) - 5))

# Se buscan números de lineas de hyperref
initconf_data = open(INITCONFFILE)
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
d_tvrel = replace_argument(d_tvrel, 1, version)
d_vcmtd = replace_argument(d_vcmtd, 1, latex_verline(version))

# Carga los archivos y cambian las versiones
t = time.time()
print('\nCREANDO TEMPLATE-INFORME')
print('GENERANDO ARCHIVOS ... ', end='')
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
for f in FILES.keys():
    if f not in ['lib/greekenum.sty', 'example-chapternumber.tex', 'test.tex',
                 'test-functions.tex', 'test-math.tex']:
        lc += len(FILES[f])

# Se modifican propiedades líneas data
data = FILES[INITCONFFILE]
d_ttype = replace_argument(d_ttype, 1, 'Compacto')
d_tvdev = replace_argument(d_tvdev, 1, versiondev + '-C')
data[l_thash] = d_thash
data[l_ttype] = d_ttype
data[l_tvdev] = d_tvdev

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
    add_stat(STATSFILE, versiondev, tmean, dia, lc, versionhash)

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

"""
TEMPLATE-AUXILIARES
"""
SUBRL_FOLDER = SUBRELEASE['AUXILIAR']
t = time.time()
print('\nCREANDO TEMPLATE-AUXILIARES')
print('GENERANDO ARCHIVOS ... ', end='')

# Crea la lista de archivos
AUXF = {
    'main.tex': copy.copy(FILES[MAINFILE]),
    'lib/function/core.tex': copy.copy(FILES['lib/function/core.tex']),
    'lib/function/elements.tex': copy.copy(FILES['lib/function/elements.tex']),
    'lib/function/equation.tex': copy.copy(FILES['lib/function/equation.tex']),
    'lib/function/image.tex': copy.copy(FILES['lib/function/image.tex']),
    'lib/function/title.tex': copy.copy(FILES['lib/function/title.tex']),
    'lib/function/auxiliar.tex': file_to_list('lib/function/auxiliar.tex'),
    'lib/example.tex': file_to_list('auxiliar_example.tex'),
    'lib/initconf.tex': copy.copy(FILES['lib/initconf.tex']),
    'lib/config.tex': copy.copy(FILES['lib/config.tex']),
    'lib/finalconf.tex': copy.copy(FILES['lib/finalconf.tex']),
    'lib/pageconf.tex': copy.copy(FILES['lib/pageconf.tex']),
    'lib/styles.tex': copy.copy(FILES['lib/styles.tex']),
    'lib/imports.tex': copy.copy(FILES['lib/imports.tex']),
}

# MODIFICA EL MAIN
main_auxiliar = file_to_list('auxiliar_main.tex')
ia, ja = find_block(main_auxiliar, '\def\equipodocente')
nb = extract_block_from_list(main_auxiliar, ia, ja)
nb.append('\n\n')
i, j = find_block(AUXF[MAINFILE], '\def\\tablaintegrantes')
AUXF[MAINFILE] = replace_block_from_list(AUXF[MAINFILE],
                                         nb, i, j)
AUXF[MAINFILE][1] = '% Documento:    Archivo principal\n'
ra, rb = find_block(AUXF[MAINFILE], '% PORTADA', True)
AUXF[MAINFILE] = del_block_from_list(AUXF[MAINFILE], ra, rb)
ra, rb = find_block(AUXF[MAINFILE], '% RESUMEN O ABSTRACT', True)
AUXF[MAINFILE] = del_block_from_list(AUXF[MAINFILE], ra, rb)
ra, rb = find_block(AUXF[MAINFILE], '% TABLA DE CONTENIDOS - ÍNDICE',
                    True)
AUXF[MAINFILE] = del_block_from_list(AUXF[MAINFILE], ra, rb)
ra, rb = find_block(AUXF[MAINFILE], '% IMPORTACIÓN DE ENTORNOS', True)
AUXF[MAINFILE] = del_block_from_list(AUXF[MAINFILE], ra, rb)
ra, rb = find_block(AUXF[MAINFILE], 'nombredelinforme')
AUXF[MAINFILE][ra] = '\def\\tituloauxiliar {Título de la auxiliar}\n'
ra, rb = find_block(AUXF[MAINFILE], 'temaatratar')
AUXF[MAINFILE][ra] = '\def\\temaatratar {Tema de la auxiliar}\n'

# MODIFICA ARCHIVO FUNCIONES
FL = 'lib/function/title.tex'
FDEL = ['\sectionanumnoi', '\sectionanumheadless', '\sectionanumnoiheadless',
        '\subsectionanumnoi', '\subsubsectionanumnoi', '\insertindextitle']
for fdel in FDEL:
    ra, rb = find_block(AUXF[FL], fdel, True)
    AUXF[FL] = del_block_from_list(AUXF[FL], ra - 1, rb)
AUXF[FL][len(AUXF[FL]) - 1] = AUXF[FL][len(AUXF[FL]) - 1].strip()

# MODIFICA CONFIGURACIIONES
FL = 'lib/config.tex'
CDEL = ['addemptypagetwosides', 'nomlttable', 'nomltsrc', 'nomltfigure',
        'nomltcont', 'nameportraitpage', 'nameabstract', 'indextitlecolor',
        'portraittitlecolor', 'fontsizetitlei', 'styletitlei',
        'firstpagemargintop', 'romanpageuppercase']
for cdel in CDEL:
    ra, rb = find_block(AUXF[FL], cdel, True)
    AUXF[FL].pop(ra)
ra, rb = find_block(AUXF[FL], '% CONFIGURACIÓN DEL ÍNDICE', True)
AUXF[FL] = del_block_from_list(AUXF[FL], ra - 1, rb)
ra, rb = find_block(AUXF[FL], '% CONFIGURACIÓN PORTADA Y HEADERS', True)
AUXF[FL] = del_block_from_list(AUXF[FL], ra - 1, rb)
for cdel in ['namereferences', 'nomltwsrc', 'nomltwfigure', 'nomltwtable']:
    ra, rb = find_block(AUXF[FL], cdel, True)
    AUXF[FL][ra] = AUXF[FL][ra].replace('    %', '%')
ra, rb = find_block(AUXF[FL], 'showdotontitles', True)
nconf = replace_argument(AUXF[FL][ra], 1, 'false').replace(' %', '%')
AUXF[FL][ra] = nconf
ra, rb = find_block(AUXF[FL], 'pagemargintop', True)
nconf = replace_argument(AUXF[FL][ra], 1, '2.30').replace(' %', '%')
AUXF[FL][ra] = nconf

# CAMBIA IMPORTS
FL = 'lib/imports.tex'
IDEL = ['usepackage{notoccite}']
for idel in IDEL:
    ra, rb = find_block(AUXF[FL], idel, True)
    AUXF[FL].pop(ra)

# CAMBIO INITCONF
FL = 'lib/initconf.tex'
ra, rb = find_block(AUXF[FL], '\checkvardefined{\\nombredelinforme}')
AUXF[FL][ra] = '\checkvardefined{\\tituloauxiliar}\n'
ra, rb = find_block(AUXF[FL], '\g@addto@macro\\nombredelinforme\\xspace')
AUXF[FL][ra] = '\t\g@addto@macro\\tituloauxiliar\\xspace\n'
ra, rb = find_block(AUXF[FL], '\ifthenelse{\isundefined{\\tablaintegrantes}}{')
AUXF[FL][ra] = '\ifthenelse{\isundefined{\\equipodocente}}{\n'
ra, rb = find_block(AUXF[FL], '\errmessage{LaTeX Warning: Se borro la '
                              'variable \\noexpand\\tablaintegrantes, creando una vacia}')
AUXF[FL][
    ra] = '\t\errmessage{LaTeX Warning: Se borro la variable ' \
          '\\noexpand\\equipodocente, creando una vacia}\n'
ra, rb = find_block(AUXF[FL], '\def\\tablaintegrantes {}')
AUXF[FL][
    ra] = '\t\def\\equipodocente {}\n'

# Cambia encabezado archivos
for fl in AUXF.keys():
    data = AUXF[fl]
    data[0] = '% Template:     Template auxiliar LaTeX\n'
    data[10] = '% Sitio web del proyecto: [' \
               'http://ppizarror.com/Template-Auxiliares/]\n'
    data[11] = '% Licencia MIT:           [' \
               'https://opensource.org/licenses/MIT]\n'
    data[HEADERVERSIONPOS] = versionhead

# Guarda los archivos
for fl in AUXF.keys():
    data = AUXF[fl]
    newfl = open(SUBRL_FOLDER + fl, 'w')
    for j in data:
        newfl.write(j)
    newfl.close()
