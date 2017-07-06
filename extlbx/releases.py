# coding=utf-8
"""
RELEASES
Contiene archivos de cada release.

Autor: PABLO PIZARRO @ github.com/ppizarror
Fecha: 2017
Licencia: MIT
"""

RELEASES = {
    'INFORME': {
        'FILES': {
            'lib/config.tex': [],
            'lib/finalconf.tex': [],
            'lib/function/core.tex': [],
            'lib/function/elements.tex': [],
            'lib/function/equation.tex': [],
            'lib/function/image.tex': [],
            'lib/function/title.tex': [],
            'lib/imports.tex': [],
            'lib/index.tex': [],
            'lib/initconf.tex': [],
            'lib/pageconf.tex': [],
            'lib/portrait.tex': [],
            'lib/styles.tex': [],
            'lib/environments.tex': [],
            'lib/example.tex': [],
            'main.tex': []
        },
        'FILEDELCOMENTS': {
            'lib/config.tex': False,
            'lib/finalconf.tex': True,
            'lib/function/core.tex': True,
            'lib/function/elements.tex': True,
            'lib/function/equation.tex': True,
            'lib/function/image.tex': True,
            'lib/function/title.tex': True,
            'lib/imports.tex': True,
            'lib/index.tex': True,
            'lib/initconf.tex': True,
            'lib/pageconf.tex': True,
            'lib/portrait.tex': True,
            'lib/styles.tex': True,
            'lib/environments.tex': True,
            'lib/example.tex': False,
            'main.tex': False
        },
        'FILESTRIP': {
            'lib/config.tex': False,
            'lib/finalconf.tex': True,
            'lib/function/core.tex': True,
            'lib/function/elements.tex': True,
            'lib/function/equation.tex': True,
            'lib/function/image.tex': True,
            'lib/function/title.tex': True,
            'lib/imports.tex': True,
            'lib/index.tex': True,
            'lib/initconf.tex': True,
            'lib/pageconf.tex': True,
            'lib/portrait.tex': True,
            'lib/styles.tex': True,
            'lib/environments.tex': True,
            'lib/example.tex': False,
            'main.tex': False
        },
        'CONFIGFILE': 'lib/config.tex',
        'EXAMPLECLONE': 'example.tex',
        'EXAMPLEFILE': 'lib/example.tex',
        'INITCONFFILE': 'lib/initconf.tex',
        'MAINFILE': 'main.tex',
        'SINGLEFILE': 'informe.tex',
        'STATS': {
            'FILE': 'stats/INFORME/stats.txt',
            'LCODE': 'stats/INFORME/stats-lcode.png',
            'CTIME': 'stats/INFORME/stats-ctime.png'
        },
        'ZIP': {
            'NORMAL': {
                'FILE': 'release/Template-Informe.zip',
                'EXCEPTED': ['greekenum.sty', 'auxiliar_example.tex', '.aux', 'auxiliar_main.tex', 'auxiliar.tex',
                             'auxiliar_pageconf.tex', 'auxiliar_title.tex'],
                'ADD': {
                    'FILES': ['main.tex'],
                    'FOLDER': ['images', 'lib']
                },
                'GHOST': ''
            },
            'COMPACT': {
                'FILE': 'release/Template-Informe-Single.zip',
                'EXCEPTED': [],
                'ADD': {
                    'FILES': ['main.tex'],
                    'FOLDER': ['images', 'lib']
                },
                'GHOST': ''
            }
        }
    },
    'AUXILIAR': 'subreleases/Template-Auxiliares/'
}
