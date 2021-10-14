# Compila el archivo de estilo propio

import datetime

langs = {
	'en': {
		'[CHAPTER]': 'ch.~',
		'[EDITOR]': ', ed.',
		'[EDITORS]': ', eds.',
		'[IN_OBJECT_M]': 'In ',
		'[IN_OBJECT]': 'in ',
		'[IN]': ' in ',
		'[LANG_AND]': ' and ',
		'[LANG_ET_AL]': 'et~al.',
		'[NO._IN]': 'No.~',
		'[NO._MID]': 'no.~',
		'[OF]': ' of ',
		'[PAGE]': 'p.~',
		'[PAGES]': 'pp.~',
		'[TECH_REP]': 'Tech. Rep.',
		'[VISITED_ON]': 'visited on',
		'[VOLUME_M]': 'Vol.~',
		'[VOLUME]': 'vol.~'
	},
	'es': {
		'[CHAPTER]': 'cap.~',
		'[EDITOR]': ', ed.',
		'[EDITORS]': ', eds.',
		'[IN_OBJECT_M]': 'En ',
		'[IN_OBJECT]': 'en ',
		'[IN]': ' en ',
		'[LANG_AND]': ' y ',
		'[LANG_ET_AL]': 'et~al.',
		'[NO._IN]': 'No.~',
		'[NO._MID]': 'no.~',
		'[OF]': ' de ',
		'[PAGE]': 'p.~',
		'[PAGES]': 'pp.~',
		'[TECH_REP]': 'Rep. Tec.',
		'[VISITED_ON]': 'visitado el',
		'[VOLUME_M]': 'Vol.~',
		'[VOLUME]': 'vol.~'
	}
}

def format(lang, outputfile, url, description):
	f = open('natnum_source.bst', 'r')
	data = f.readlines()

	# Check version
	date = datetime.datetime.now()
	for w in range(len(data)):
		if 'Versión:' in data[w]:
			data[w] = data[w].strip()
			data[w] += f' ({date.day}/{date.month}/{date.year})\n'
			break
	
	# Transform to text
	data = ''.join(data)

	# Remove urls
	if not url:
		data = data.replace('    output.links\n    new.block\n', '')

	# Replace description
	data = data.replace('[NATNUM_DESCRIPTION]', description)

	# Replace tokens
	for token in langs[lang].keys():
		data = data.replace(token, langs[lang][token])
	f.close()

	# Write
	f = open(outputfile, 'w')
	for w in data:
		f.write(w)
	f.close()


# Guarda los formatos
format('es', 'natnumurl.bst', True, 'Archivo de estilos simple numerados + url (doi, arxivId) [es]')
format('es', 'natnum.bst', False, 'Archivo de estilos simple numerados [es]')

format('en', 'natnumurl_en.bst', True, 'Archivo de estilos simple numerados + url (doi, arxivId) [en]')
format('en', 'natnum_en.bst', False, 'Archivo de estilos simple numerados [en]')