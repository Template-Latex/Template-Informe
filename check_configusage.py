# Chequea el total de configuraciones utilizados
# uso (win): py -3 check_configusage.py ..\Template-Tesis
# uso (mac): python3 Template-Informe/check_configusage.py Template-Poster
import sys
assert len(sys.argv) == 2, 'Debe pasar path'
p = sys.argv[1]

import os
assert os.path.isdir(p), 'Argumento de función "{0}" debe ser una carpeta con el template'.format(p)

# Busca el archivo del template
os.chdir(p)
templf = 'template.tex'
conff = 'template_config.tex'
assert os.path.exists(templf), 'Archivo template.tex dentro de directorio no existe'
assert os.path.exists(conff), 'Archivo template_config.tex dentro de directorio no existe'

tdata = []
f = open(templf, 'r', encoding = 'utf8')
for j in f:
    tdata.append(j.strip())
f.close()

def count_def(x) -> int:
    k = 0
    for w in tdata:
        if x in w:
            k += 1
    return k

# Abre el archivo de configuraciones
f = open(conff, 'r', encoding = 'utf8')
conf = []
for j in f:
    j = j.split('{')
    if len(j)>0:
        j = j[0]
    if '\\def' not in j:
        continue
    j = j.replace('\\def', '').replace('\\', '').replace(' ', '').strip()
    conf.append(j)
conf.sort()

# Finalmente, por cada configuración, cuenta las entradas
print('Resultados análisis para {0} ({1} configuraciones):'.format(p, len(conf)))
for j in conf:
    k = '\\{0}'.format(j).ljust(30)
    r = count_def(j)
    print('{0}{1}{2}'.format(k, r, ' <===' if r == 0 else ''))