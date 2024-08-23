# Compila el archivo de estilo propio

import copy
import datetime

langs = {
	'en': {
		'[CHAPTER]': 'ch.~',
		'[EDITOR]': ', ed.',
		'[EDITORS]': ', eds.',
		'[ERROR_BOOKLET]': 'empty title in ',
		'[ERROR_EITHER_OR_CHECK_1]': 'can\'t use both ',
		'[ERROR_EITHER_OR_CHECK_2]': ' fields in ',
		'[ERROR_EMPTY_MISC]': 'all relevant fields are empty in ',
		'[ERROR_FORMAT_ARTICLE_CROSSREF_1]': 'need key or journal for ',
		'[ERROR_FORMAT_ARTICLE_CROSSREF_2]': ' to crossref ',
		'[ERROR_FORMAT_BOOK_CROSSREF_1]': 'empty volume in ',
		'[ERROR_FORMAT_BOOK_CROSSREF_2]': ' to crossref ',
		'[ERROR_FORMAT_BOOK_CROSSREF_3]': 'need editor, key, or series for ',
		'[ERROR_FORMAT_DATE]': 'there\'s a month but no year in ',
		'[ERROR_FORMAT_INCOLL_INPROC_CROSSREF_1]': 'need editor, key, or booktitle for ',
		'[ERROR_FORMAT_INCOLL_INPROC_CROSSREF_2]': ' to crossref ',
		'[ERROR_FORMAT_NUMBER_SERIES]': 'there\'s a number but no series in ',
		'[ERROR_OUTPUT_CHECK_1]': 'empty ',
		'[ERROR_OUTPUT_CHECK_2]': ' in ',
		'[FORMAT_NAMES_F]': '{vv~}{ll}{, jj}{, f.}',
		'[FORMAT_NAMES_SEP]': '',
		'[FORMAT_NAMES_SEP2]': ',',
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
		'[TITLE_F_END_TITLE.P]': ".''",
		'[TITLE_F_END_TITLE]': ",''",
		'[TITLE_F_START]': '``',
		'[VISITED_ON_LAST]': ')',
		'[VISITED_ON]': ' (visited on ',
		'[VOLUME_M]': 'Vol.~',
		'[VOLUME]': 'vol.~'
	},
	'es': {
		'[CHAPTER]': 'cap.~',
		'[EDITOR]': ', ed.',
		'[EDITORS]': ', eds.',
		'[ERROR_BOOKLET]': 'titulo vacio en ',
		'[ERROR_EITHER_OR_CHECK_1]': 'no se pueden usar ambos ',
		'[ERROR_EITHER_OR_CHECK_2]': ' campos en ',
		'[ERROR_EMPTY_MISC]': 'todos los campos relevantes estan vacios en ',
		'[ERROR_FORMAT_ARTICLE_CROSSREF_1]': 'se necesita key o journal en ',
		'[ERROR_FORMAT_ARTICLE_CROSSREF_2]': ' para validar crossref ',
		'[ERROR_FORMAT_BOOK_CROSSREF_1]': 'volumen vacio en ',
		'[ERROR_FORMAT_BOOK_CROSSREF_2]': 'para validar crossref ',
		'[ERROR_FORMAT_BOOK_CROSSREF_3]': 'se necesita editor, key o series en ',
		'[ERROR_FORMAT_DATE]': 'existe mes pero no año en ',
		'[ERROR_FORMAT_INCOLL_INPROC_CROSSREF_1]': 'se necesita editor, key o booktitle en ',
		'[ERROR_FORMAT_INCOLL_INPROC_CROSSREF_2]': ' para validar crossref ',
		'[ERROR_FORMAT_NUMBER_SERIES]': 'existe numero pero no serie en ',
		'[ERROR_OUTPUT_CHECK_1]': 'vacio ',
		'[ERROR_OUTPUT_CHECK_2]': ' en ',
		'[FORMAT_NAMES_F]': '{vv~}{ll}{, jj}{, f.}',
		'[FORMAT_NAMES_SEP]': '',
		'[FORMAT_NAMES_SEP2]': ',',
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
		'[TITLE_F_END_TITLE.P]': "''.",
		'[TITLE_F_END_TITLE]': "'',",
		'[TITLE_F_START]': '``',
		'[VISITED_ON_LAST]': ')',
		'[VISITED_ON]': ' (visitado el ',
		'[VOLUME_M]': 'Vol.~',
		'[VOLUME]': 'vol.~'
	}
}

# Genera elsarticle
en_els = langs['en_elsarticle'] = copy.copy(langs['en'])
es_els = langs['es_elsarticle'] = copy.copy(langs['es'])

en_els['[FORMAT_NAMES_F]'] = es_els['[FORMAT_NAMES_F]'] = '{f.~}{vv~}{ll}{, jj}'
en_els['[FORMAT_NAMES_SEP]'] = es_els['[FORMAT_NAMES_SEP]'] = ','
en_els['[FORMAT_NAMES_SEP2]'] = es_els['[FORMAT_NAMES_SEP2]'] = ''
en_els['[LANG_AND]'] = es_els['[LANG_AND]'] = ' '
en_els['[TITLE_F_END_TITLE.P]'] = es_els['[TITLE_F_END_TITLE.P]'] = '.'
en_els['[TITLE_F_END_TITLE]'] = es_els['[TITLE_F_END_TITLE]'] = ','
en_els['[TITLE_F_START]'] = es_els['[TITLE_F_START]'] = ''
en_els['[VISITED_ON_LAST]'] = es_els['[VISITED_ON_LAST]'] = '.'
en_els['[VISITED_ON]'] = '. Accessed '
es_els['[VISITED_ON]'] = '. Visitado el '

# Define formato
def format(lang, outputfile, url, description):
	f = open('.natnum_source.bst', 'r', encoding='utf8')
	data = f.readlines()

	# Chequea la versión
	date = datetime.datetime.now()
	for w in range(len(data)):
		if 'Versión:' in data[w]:
			data[w] = data[w].strip()
			data[w] += f' ({date.day:02d}/{date.month:02d}/{date.year})\n'
			break
	
	# Transforma el texto
	data = ''.join(data)

	# Elimina urls
	if not url:
		data = data.replace('    output.links\n    new.block\n', '')

	# Reemplaza la descripción
	data = data.replace('[NATNUM_DESCRIPTION]', description)

	# Reemplaza tokens
	for token in langs[lang].keys():
		data = data.replace(token, langs[lang][token])
	f.close()

	# Escribe
	f = open(outputfile, 'w', encoding='utf8')
	for w in data:
		f.write(w)
	f.close()


# Guarda los formatos
format('es', 'natnumurl.bst', True, 'Archivo de estilos simple numerados + url (doi, arxivId) [es]')
format('es', 'natnum.bst', False, 'Archivo de estilos simple numerados [es]')
format('es_elsarticle', 'elsartnumurl.bst', True, 'Estilo elsarticle numerado + url (doi, arxivId) [es]')
format('es_elsarticle', 'elsartnum.bst', False, 'Estilo elsarticle numerado [es]')

format('en', 'natnumurl_en.bst', True, 'Archivo de estilos simple numerados + url (doi, arxivId) [en]')
format('en', 'natnum_en.bst', False, 'Archivo de estilos simple numerados [en]')
format('en_elsarticle', 'elsartnumurl_en.bst', True, 'Estilo elsarticle numerado + url (doi, arxivId) [en]')
format('en_elsarticle', 'elsartnum_en.bst', False, 'Estilo elsarticle numerado [en]')