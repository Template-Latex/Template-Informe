/*
The MIT License (MIT)

Copyright 2017 Pablo Pizarro R.

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the Software
is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
*/

// Configuraciones
var href_github_project = 'https://github.com/Template-Latex/Template-Informe/releases/';
var href_github_project_source = 'https://github.com/Template-Latex/Template-Informe/';
var href_json_releases = 'https://api.github.com/repos/Template-Latex/Template-Informe/releases';
var href_pdf_version = '../Informe/Template-Informe v{0}.pdf';
var href_resources_folder = 'http://latex.ppizarror.com/resources/';
var stats_name = 'Informe';
var update_download_counter = 'Template-Informe';

// Declaración de funciones propias de cada template
var bounceStyleReferences; // Efecto en entrada de configuración
var downloadOtherBackgroundBlur = 1; // Blur del fondo al mostrar cajón de descargas
var hfGallery; // Muestra la galería de header-footer
var line_abstract = [95, 216]; // Número de línea de abstract/resumen
var line_authortable = [33, 34]; // Número de línea tabla de integrantes
var line_configimport = [64, 65]; // Número línea importación de configuraciones
var line_docinit = [106, 227]; // Número de línea inicio del documento
var line_infodocument = [18, 19]; // Número de línea información del documento
var portraitGallery; // Muestra la galería de portadas

function afterDocumentReady() {
    $('.intro-line-abstract').each(
        function() {
            $(this).attr('style', 'cursor:pointer;');
            $(this).attr('title', String.format('Línea {0} en versión compacta', line_abstract[1]));
            $(this).html(String.format('(línea {0})', line_abstract[0]));
        }
    );
    $('.intro-line-authortable').each(function() {
        $(this).attr('style', 'cursor:pointer;');
        $(this).attr('title', String.format('Línea {0} en versión compacta', line_authortable[1]));
        $(this).html(String.format('(línea {0})', line_authortable[0]));
    });
    $('.intro-line-configimport').each(
        function() {
            $(this).attr('style', 'cursor:pointer;');
            $(this).attr('title', String.format('Línea {0} en versión compacta', line_configimport[1]));
            $(this).html(String.format('(línea {0})', line_configimport[0]));
        }
    );
    $('.intro-line-docinit').each(
        function() {
            $(this).attr('style', 'cursor:pointer;');
            $(this).attr('title', String.format('Línea {0} en versión compacta', line_docinit[1]));
            $(this).html(String.format('(línea {0})', line_docinit[0]));
        }
    );
    $('.intro-line-infodocument').each(function() {
        $(this).attr('style', 'cursor:pointer;');
        $(this).attr('title', String.format('Línea {0} en versión compacta', line_infodocument[1]));
        $(this).html(String.format('(línea {0})', line_infodocument[0]));
    });
    hfGallery = function() {
        var pswpElement = document.querySelectorAll('.pswp')[0];
        var items = [];
        for (var i = 1; i <= 8; i++) {
            items.push({
                src: String.format('images/hf{0}.png', i),
                w: 544,
                h: 704,
                title: String.format('<b>Header-Footer estilo {0}</b> (<div class="codegallerytitle">\\hfstyle=\{style{0}\}</div>)', i)
            })
        }
        var options = {
            index: 0,
            showAnimationDuration: 400,
            hideAnimationDuration: 400,
            shareEl: false,
            counterEl: true,
            history: true,
            fullscreenEl: false,
            zoomEl: false
        };
        var gallery = new PhotoSwipe(pswpElement, PhotoSwipeUI_Default, items, options);
        gallery.listen('close', function() {
            $('a.back-to-top').fadeIn('slow');
        });
        gallery.init();
        $('a.back-to-top').fadeOut('slow');
    };
    portraitGallery = function() {
        var pswpElement = document.querySelectorAll('.pswp')[0];
        var items = [];
        for (var i = 1; i <= 16; i++) {
            items.push({
                src: String.format('images/portada{0}.png', i),
                w: 544,
                h: 704,
                title: String.format('<b>Portada estilo {0}</b> (<div class="codegallerytitle">\\portraitstyle=\{style{0}\}</div>)', i)
            })
        }
        var options = {
            index: 0,
            showAnimationDuration: 400,
            hideAnimationDuration: 400,
            shareEl: false,
            counterEl: true,
            history: true,
            fullscreenEl: false,
            zoomEl: false
        };
        var gallery = new PhotoSwipe(pswpElement, PhotoSwipeUI_Default, items, options);
        gallery.listen('close', function() {
            $('a.back-to-top').fadeIn('slow');
        });
        gallery.init();
        $('a.back-to-top').fadeOut('slow');
    };
    bounceStyleReferences = function() {
        $('#config-ref').ScrollTo();
        setTimeout(function() {
            doBounce($('#stylecitereferences'), 3, '6px', 100);
        }, 1000);
    }
    // Se lee una acción desde url cuando json está cargado
    initAction = $.urlParam('action');
    if (initAction != null) {
        switch (initAction) {
            case 'portraitGallery':
                portraitGallery();
                break;
            case 'hfGallery':
                hfGallery();
                break;
        }
    }
}

function afterJSONLoad() {
    initAction = $.urlParam('action');
    if (initAction != null) {
        switch (initAction) {
            case 'download':
                $('a[name*=leanModal]').leanModal({
                    closeButton: '.modal_close'
                }).click();
                break;
            case 'download-normal':
                $('#download-button')[0].click();
                break;
        }
    }
}

function writeOtherLinks(verid) {
    var deptos = [
        ['Área de Humanidades', 'adh'],
        ['Departamento de Astronomía', 'das'],
        ['Departamento de Ciencias de la Computación', 'dcc'],
        ['Departamento de Física', 'dfi'],
        ['Departamento de Geofísica', 'dgf'],
        ['Departamento de Geología', 'geo'],
        ['Departamento de Ingeniería Civil', 'dic'],
        ['Departamento de Ingeniería Eléctrica', 'die'],
        ['Departamento de Ingeniería Industrial', 'dii'],
        ['Departamento de Ingeniería Matemática', 'dim'],
        ['Departamento de Ingeniería Mecánica', 'dimec'],
        ['Departamento de Ingeniería en Minas', 'minas'],
        ['Departamento de Ingeniería Química y Biotecnología', 'diqbt'],
        ['Facultad de Ciencias Físicas y Matemáticas', 'fcfm'],
        ['Universidad de Chile', 'uchile']
    ];
    $('#downloadtitle-title').html(String.format('Descargas v{0}', verid));
    $('#downloadother-contents').append(String.format('<div class="downloadother-entry downloadother-compact"><div class="downloadother-name">Versión compacta</div><div class="downloadother-link"><a href="{0}download/{1}/Template-Informe-Single.zip">Descargar</a></div></div>', href_github_project, verid));
    for (var i = 0; i < deptos.length; i++) {
        $('#downloadother-contents').append(String.format('<div id="downloadentry-{1}" class="downloadother-entry"><div class="downloadother-name">{0}</div><div class="downloadother-link-double"><a href="{3}download/{2}/Template-Informe-{1}.zip" class="otherdownloadclickeable">Normal</a></div><div class="downloadother-link-double"><a href="{3}download/{2}/Template-Informe-{1}-Single.zip" class="otherdownloadclickeable">Compacta</a></div></div>', deptos[i][0], deptos[i][1], verid, href_github_project));
        $(String.format('#downloadentry-{0} .otherdownloadclickeable', deptos[i][1])).click(function() {
            if (total_downloads != nan_value) {
                total_downloads += 1;
                total_downloads_l30 += 1;
                update_download_banner(total_downloads);
            }
        });
    }
}
