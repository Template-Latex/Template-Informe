"""
Generate unicode tests.
"""

myunicodes=''.join(open('src/cfg/unicode.tex', 'r', encoding='utf8').readlines())

f = open('test/unicode.sty', 'r', encoding='utf8').readlines()
newkcodes = []
for j in f:
	j = j.strip()
	if len(j) == 0:
		continue
	if '%' in j.strip()[0]:
		continue
	if 'DeclareUnicodeCharacter' not in j or '\\def' in j or '\\newcommand' in j:
		continue
	kcode = j.split('}{')[0].split('{')[1]
	if f'{kcode}' in myunicodes:
		# print(f'{kcode} repeated')
		continue
	if '%' in j:
		j = j.split('%')[0].strip()
	newkcodes.append(j)

newkcodes.sort()
print('New kcodes')
for j in newkcodes:
	print(j)

# Iterate through unicodes
write_test = True

if write_test:
	f = open('test/unicode.tex', 'w', encoding='utf8')
	f.write('Ejemplos:\n\\begin{itemize}\n')
	added = []
	for j in myunicodes.split('\n'):
		if 'DeclareUnicodeCharacter' not in j or '\\def' in j or '\\ifdefined' in j or '\ifx' in j:
			continue
		if j[0] == '%':
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

f = open('test/unicode_replacer.py', 'w', encoding='utf8')
cmd = []
notcmd = []
addedjval = []
for j in myunicodes.split('\n'):
	if 'DeclareUnicodeCharacter' not in j or '\\def' in j or '\\ifdefined' in j or '\ifx' in j:
		continue
	jsp = j.split('}{')
	kcode = jsp.pop(0).split('{')[1]
	jval = '}{'.join(jsp).strip()[0:-1]
	char = chr(int(f'0x{kcode}', 16))
	if '\\ensuremath' in jval:
		jval = jval.replace('\\ensuremath{', '')[0:-1]
	if jval[0] == '{':
		continue
	if 'NOT' in jval or 'NONE' in jval or '\LOCALunknownchar' in jval:
		continue
	if '\hbox' in jval or '\else' in jval or '{ }' in jval or '\\,' in jval or '\\text{' in jval or '!' in jval:
		continue
	jval = jval.replace('\\', '\\\\')
	if jval in addedjval:
		# print(f'REPEATED {jval}')
		continue
	addedjval.append(jval)
	txt = f"\t('{jval}', '{char}'),\n"
	if jval == char:
		continue
	if '\\' not in jval:
		if len(jval) == 1 or "'" in jval:
			continue
		notcmd.append(txt)
	else:
		cmd.append(txt)
cmd.sort(key=lambda v: v.upper())
notcmd.sort(key=lambda v: v.upper())
for j in cmd:
	f.write(j)
for j in notcmd:
	f.write(j)
f.close()