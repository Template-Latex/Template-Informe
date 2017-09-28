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
var openPhotoSwipe;

function afterDocumentReady() {
    // Muestra las portadas
    openPhotoSwipe = function() {
        var pswpElement = document.querySelectorAll('.pswp')[0];
        var items = [];
        for (var i = 1; i <= 16; i++) {
            items.push({
                src: String.format('images/portada{0}.png', i),
                w: 544,
                h: 704,
                title: String.format('<b>Portada {0}</b> (<div class="codegallerytitle">\\portraitstyle=style{0}</div>)', i)
            })
        }
        var options = {
            index: 0,
            showAnimationDuration: 400,
            hideAnimationDuration: 400,
            shareEl: false,
            counterEl: true,
            history: true
        };
        var gallery = new PhotoSwipe(pswpElement, PhotoSwipeUI_Default, items, options);
        gallery.listen('close', function() {
            $('a.back-to-top').fadeIn('slow');
        });
        gallery.init();
        $('a.back-to-top').fadeOut('slow');
    };
}

function afterJSONLoad() {}
