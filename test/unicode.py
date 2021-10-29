"""
Generate unicode tests.
"""

char = chr(int('0x0393', 16))
print("here is your checkmark: " + char)

myunicodes=''.join(open('src/cfg/unicode.tex', 'r').readlines())
print(myunicodes)

f = open('test/unicode.sty', 'r').readlines()
newkcodes = []
for j in f:
	j = j.strip()
	if len(j) == 0:
		continue
	if '%' in j.strip()[0]:
		continue
	if 'DeclareUnicodeCharacter' not in j or '\\def' in j:
		continue
	kcode = j.split('}{')[0].split('{')[1]
	if f'{kcode}' in myunicodes:
		print(f'{kcode} repeated')
		continue
	newkcodes.append(j)

print('New kcodes')
for j in newkcodes:
	print(j)

# Iterate through unicodes
f = open('test/unicode.tex', 'w')
f.write('Ejemplos:\n\\begin{itemize}\n')
added = []
for j in myunicodes.split('\n'):
	if 'DeclareUnicodeCharacter' not in j or '\\def' in j or '\\ifdefined' in j:
		continue
	kcode = j.split('}{')[0].split('{')[1]
	if kcode not in added:
		added.append(kcode)
	else:
		print(f'Error, {kcode} repeated')
	char = chr(int(f'0x{kcode}', 16))
	f.write(f'\t\\item {char}\t% '+kcode+'\n')
f.write('\end{itemize}')
f.close()