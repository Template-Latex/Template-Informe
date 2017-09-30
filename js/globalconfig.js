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

// Configuraciones de toda la suite Template-Latex
var blurlimits = [3, 10];
var blurprobability = 50;
var changelog_max = 7;
var enable_error_window = false;
var enableparallax = false;
var pdf_js_href = 'http://latex.ppizarror.com/pdf-version/web/viewer.html?file=';

// Escribe los badges de la suite Template-Latex
function writeBadges() {
    $('#badgeslistdiv').html('');
    $('#badgeslistdiv').append('<a href="http://latex.ppizarror.com/Template-Tesis/" id="aimg"><img src="http://latex.ppizarror.com/badges/tesis.svg" style="display: none" /></a> ');
    $('#badgeslistdiv').append('<a href="http://latex.ppizarror.com/Template-Apunte/" id="aimg"><img src="http://latex.ppizarror.com/badges/apunte.svg" style="display: none" /></a> ');
    $('#badgeslistdiv').append('<a href="http://latex.ppizarror.com/Template-Tareas/" id="aimg"><img src="http://latex.ppizarror.com/badges/tareas.svg" style="display: none" /></a> ');
    $('#badgeslistdiv').append('<a href="http://latex.ppizarror.com/Template-Auxiliares/" id="aimg"><img src="http://latex.ppizarror.com/badges/auxiliares.svg" /></a> ');
    $('#badgeslistdiv').append('<a href="http://latex.ppizarror.com/Template-Controles/" id="aimg"><img src="http://latex.ppizarror.com/badges/controles.svg" /></a> ');
    $('#badgeslistdiv').append('<a href="http://latex.ppizarror.com/Template-Pautas/" id="aimg"><img src="http://latex.ppizarror.com/badges/pauta.svg" style="display: none" /></a> ');
    $('#badgeslistdiv').append('<a href="http://latex.ppizarror.com/Template-Informe/" id="aimg"><img src="http://latex.ppizarror.com/badges/informe.svg" /></a> ');
    $('#badgeslistdiv').append('<a href="http://latex.ppizarror.com/Professional-CV/" id="aimg"><img src="http://latex.ppizarror.com/badges/professionalcv.svg" /></a> ');

    $('#badgeslistdiv').fadeIn('slow');
}
