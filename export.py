# coding=utf-8
"""
Exporta main.tex a informe.tex (template sin archivos externos).
Cambia versión y fecha a archivos.
"""

# Importación de librerías
import time
from subprocess import call

# Constantes
CODEVERSION = '\def\\templateversion{0}               % Versión del template\n'
CODEVERSIONPOS = 19
EXAMPLEFILE = 'ejemplo.tex'
HEADERSIZE = 13
HEADERVERSIONPOS = 2
MAINFILE = 'main.tex'
MAINFILESINGLE = 'informe.tex'
VERSIONHEADER = '% Versión:      {0} ({1})\n'

# Archivos a revisar
FILES = {
    'lib/config.tex': [],
    'lib/finalconf.tex': [],
    'lib/functions.tex': [],
    'lib/imports.tex': [],
    'lib/index.tex': [],
    'lib/initconf.tex': [],
    'lib/pageconf.tex': [],
    'lib/portrait.tex': [],
    'lib/styles.tex': [],
    'abstract.tex': [],
    EXAMPLEFILE: [],
    MAINFILE: []
}

# Se pide la versión
version = raw_input('Ingrese la nueva version: ')
version = version.strip()

# Se obtiene el día
dia = time.strftime("%d/%m/%Y")

# Se crea el header de la version
versionhead = VERSIONHEADER.format(version, dia)
versioncode = CODEVERSION.format('{' + version + '}')

# Carga los archivos y cambia las versiones
for f in FILES.keys():
    data = FILES[f]
    # noinspection PyBroadException
    try:
        fl = open(f, 'r')
        for line in fl:
            data.append(line)
        fl.close()
    except:
        print('Error al cargar el archivo {0}'.format(f))

    # Se cambia la versión
    data[HEADERVERSIONPOS] = versionhead

    # Sólo para el archivo principal se cambia la version
    if f == MAINFILE:
        data[CODEVERSIONPOS] = versioncode

    # Se reescribe el archivo
    newfl = open(f, 'w')
    for j in data:
        newfl.write(j)
    newfl.close()

# Se crea el archivo unificado
fl = open(MAINFILESINGLE, 'w')
data = FILES[MAINFILE]
data.pop(1)  # Se elimina el tipo de documento del header
data.insert(1, '% Advertencia:  Documento generado automáticamente a partir '
               'del main.tex y los\n%               archivos .tex de la '
               'carpeta lib/ para crear un sólo archivo.\n')
line = 0
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
                libr = libr + '.tex'
                if libr != EXAMPLEFILE:

                    # Se escribe desde el largo del header en adelante
                    libdata = FILES[libr]
                    for libdatapos in range(HEADERSIZE, len(libdata)):
                        fl.write(libdata[libdatapos])
                    fl.write('\n')  # Se agrega espacio vacío

                else:
                    fl.write(d)
                write = False
        except Exception, e:
            pass
        # Se agrega un espacio en blanco a la pagina despues del comentario
        if line >= CODEVERSIONPOS + 1 and write:
            if d[0:2] == '% ' and d[3] != ' ':
                fl.write('\n')
                d = d.replace('IMPORTACIÓN', 'DECLARACIÓN')
                fl.write(d)
            else:
                fl.write(d)

    # Aumenta la linea
    line += 1

fl.close()

# Compila el archivo
call(['pdflatex', MAINFILESINGLE])
