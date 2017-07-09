# coding=utf-8
"""
RELEASES
Contiene archivos de cada release.

Autor: PABLO PIZARRO @ github.com/ppizarror
Fecha: 2017
Licencia: MIT
"""

RELEASES = {
    '_INFORME': {
        'NAME': 'Template-Informe',
        'ID': 1,
        'ROOT': '',
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
            'FILE': 'stats/Informe/stats.txt',
            'LCODE': 'stats/Informe/stats-lcode.png',
            'CTIME': 'stats/Informe/stats-ctime.png'
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
                    'FILES': ['informe.tex', 'example.tex'],
                    'FOLDER': ['images']
                },
                'GHOST': ''
            }
        },
        'MESSAGE': '\nCREANDO TEMPLATE-INFORME v{0}',
        'VERLINE': 'Template-Informe v{0} | (Pablo Pizarro R.) ppizarror.com'
    },
    'AUXILIAR': {
        'NAME': 'Template-Auxiliares',
        'ID': 2,
        'ROOT': 'subreleases/Template-Auxiliares/',
        'FILES': {
            'main.tex': [],
            'lib/function/core.tex': [],
            'lib/function/elements.tex': [],
            'lib/function/equation.tex': [],
            'lib/function/image.tex': [],
            'lib/function/title.tex': [],
            'lib/function/auxiliar.tex': [],
            'lib/example.tex': [],
            'lib/initconf.tex': [],
            'lib/config.tex': [],
            'lib/pageconf.tex': [],
            'lib/styles.tex': [],
            'lib/imports.tex': [],
        },
        'FILEDELCOMENTS': {
            'main.tex': False,
            'lib/function/core.tex': True,
            'lib/function/elements.tex': True,
            'lib/function/equation.tex': True,
            'lib/function/image.tex': True,
            'lib/function/title.tex': True,
            'lib/function/auxiliar.tex': True,
            'lib/example.tex': False,
            'lib/initconf.tex': True,
            'lib/config.tex': False,
            'lib/pageconf.tex': True,
            'lib/styles.tex': True,
            'lib/imports.tex': True
        },
        'FILESTRIP': {
            'main.tex': False,
            'lib/function/core.tex': True,
            'lib/function/elements.tex': True,
            'lib/function/equation.tex': True,
            'lib/function/image.tex': True,
            'lib/function/title.tex': True,
            'lib/function/auxiliar.tex': True,
            'lib/example.tex': False,
            'lib/initconf.tex': True,
            'lib/config.tex': False,
            'lib/pageconf.tex': True,
            'lib/styles.tex': True,
            'lib/imports.tex': True
        },
        'SUBRELFILES': {
            'MAIN': 'auxiliar_main.tex',
            'PAGECONF': 'lib/auxiliar_pageconf.tex',
            'IMPORTS': 'lib/auxiliar_imports.tex',
            'ENVFUN': 'lib/environments.tex'
        },
        'CONFIGFILE': 'lib/config.tex',
        'EXAMPLECLONE': 'example.tex',
        'EXAMPLEFILE': 'lib/example.tex',
        'FUNCTIONS': 'lib/function/auxiliar.tex',
        'IMPORTSFILE': 'lib/imports.tex',
        'INITCONFFILE': 'lib/initconf.tex',
        'MAINFILE': 'main.tex',
        'PAGECONFFILE': 'lib/pageconf.tex',
        'SINGLEFILE': 'auxiliar.tex',
        'STATS': {
            'FILE': 'stats/Auxiliares/stats.txt',
            'LCODE': 'stats/Auxiliares/stats-lcode.png',
            'CTIME': 'stats/Auxiliares/stats-ctime.png'
        },
        'ZIP': {
            'NORMAL': {
                'FILE': 'release/Template-Auxiliares.zip',
                'EXCEPTED': ['.aux'],
                'ADD': {
                    'FILES': ['subreleases/Template-Auxiliares/main.tex'],
                    'FOLDER': ['subreleases/Template-Auxiliares/images', 'subreleases/Template-Auxiliares/lib']
                },
                'GHOST': 'subreleases/Template-Auxiliares/'
            },
            'COMPACT': {
                'FILE': 'release/Template-Auxiliares-Single.zip',
                'EXCEPTED': [],
                'ADD': {
                    'FILES': ['main.tex'],
                    'FOLDER': ['images', 'lib']
                },
                'GHOST': 'subreleases/Template-Auxiliares/'
            }
        },
        'MESSAGE': '\nCREANDO TEMPLATE-AUXILIARES v{0}',
        'VERLINE': 'Template-Auxiliares v{0} | (Pablo Pizarro R.) ppizarror.com'
    }
}
