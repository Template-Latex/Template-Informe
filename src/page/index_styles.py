import itertools

_totals = ['']
_elems = ['e', 'c', 'f', 't']

def append_permutation(p):
    _k = ''
    for c in p:
        _k += c
    if _k not in _totals:
        _totals.append(_k)

def process_permutation(s):
    for j in itertools.permutations(s):
        append_permutation(j)

for i in range(len(_elems)):
    for j in itertools.combinations(_elems, i+1):
        process_permutation([*j])

def move_first(item):
    if item in _totals:
        _totals.pop(_totals.index(item))
    _totals.insert(0, item)


# Procesa las permutaciones
move_first('ftc')
print(_totals)

# Genera el string
indexs = ''
_end = ''
for o in _totals:
    _inst = o.replace('f', '\LoIf').replace(
        'c', '\LoIc').replace('t', '\LoIt').replace('e', '\LoIe')
    indexs += '\ifthenelse{\equal{\indexstyle}{'+o+'}}{%\n\t'+_inst+'\n}{\n'
    _end += '}'
_last = '\t\\throwbadconfig{Estilo desconocido del indice}{\indexstyle}{'+','.join(_totals)+'}'

print(indexs+_last+_end)
