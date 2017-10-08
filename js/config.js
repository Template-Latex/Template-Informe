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
}

function afterJSONLoad() {}
