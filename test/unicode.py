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
write_test = False

if write_test:
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

f = open('test/unicode_replacer.py', 'w')
notcmd = []
for j in myunicodes.split('\n'):
	if 'DeclareUnicodeCharacter' not in j or '\\def' in j or '\\ifdefined' in j:
		continue
	kcode = j.split('}{')[0].split('{')[1]
	jval = j.split('}{')[1].strip()[0:-1]
	char = chr(int(f'0x{kcode}', 16))
	if '\\ensuremath' in jval:
		jval = jval.replace('\\ensuremath{', '')[0:-1]
	if jval[0] == '{':
		continue
	if 'NOT' in jval or 'NONE' in jval:
		continue
	if '\hbox' in jval or '\else' in jval or '{ }' in jval:
		continue
	jval = jval.replace('\\', '\\\\')
	txt = f"\t('{jval}', '{char}'),\n"
	if jval == char:
		continue
	if '\\' not in jval:
		notcmd.append(txt)
		continue
	f.write(txt)
for j in notcmd:
	f.write(j)
f.close()