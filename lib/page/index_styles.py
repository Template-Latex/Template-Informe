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


# Process all permutations
print(_totals)
