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

// Escribe los badges
function writeBadges() {
    $('#badgeslistdiv').html(String.format('<a href="http://ppizarror.com" id="aimg" class="tooltip"><img src="{0}autor2.svg" class="bannerimg"><span class="tooltiptext_autor"><img src="https://avatars0.githubusercontent.com/u/12925256" /><div class="autor_name">Pablo Pizarro R.</div><div class="autor_location"><svg aria-hidden="true" height="16" class="tooltiptext_autor_svg" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M6 0C2.69 0 0 2.5 0 5.5 0 10.02 6 16 6 16s6-5.98 6-10.5C12 2.5 9.31 0 6 0zm0 14.55C4.14 12.52 1 8.44 1 5.5 1 3.02 3.25 1 6 1c1.34 0 2.61.48 3.56 1.36.92.86 1.44 1.97 1.44 3.14 0 2.94-3.14 7.02-5 9.05zM8 5.5c0 1.11-.89 2-2 2-1.11 0-2-.89-2-2 0-1.11.89-2 2-2 1.11 0 2 .89 2 2z"></path></svg>Chile</div></span></a>', href_resources_folder));
    $('#badgeslistdiv').append(String.format('<a href="https://opensource.org/licenses/MIT/" id="aimg"><img src="resources/Licencia-MIT-blue.svg" /></a>', href_resources_folder));
    $('#badgeslistdiv').append(String.format('<a href="" id="aimg" class="badgeejemplopdf"><img src="{0}badge-pdf.svg" /></a>', href_resources_folder));
    $('#badgeslistdiv').append('<a href="" id="templatestats"><svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="104" height="20" id="downloadcounter-banner"><linearGradient id="b" x2="0" y2="100%"><stop offset="0" stop-color="#bbb" stop-opacity=".1"/><stop offset="1" stop-opacity=".1"/></linearGradient><clipPath id="a"><rect width="104" height="20" rx="3" fill="#fff"/></clipPath><g clip-path="url(#a)"><path fill="#555" d="M0 0h67v20H0z"/><path fill="#4c1" d="M67 0h37v20H67z"/><path fill="url(#b)" d="M0 0h104v20H0z"/></g><g fill="#fff" text-anchor="middle" font-family="DejaVu Sans,Verdana,Geneva,sans-serif" font-size="11"><text x="33.5" y="15" fill="#010101" fill-opacity=".3">Descargas</text><text x="33.5" y="14">Descargas</text><text x="84.5" y="15" fill="#010101" fill-opacity=".3" id="total-download-counter-1" style="opacity: 0"></text><text x="84.5" y="14" id="total-download-counter-2" style="opacity: 0"></text></g></svg></a><br>');
    $('#badgeslistdiv').append(String.format('<a href="http://latex.ppizarror.com/Template-Tesis/" id="aimg"><img src="{0}templates/tesis.svg" style="display: none" /></a>', href_resources_folder));
    $('#badgeslistdiv').append(String.format('<a href="http://latex.ppizarror.com/Template-Apunte/" id="aimg"><img src="{0}templates/apunte.svg" style="display: none" /></a>', href_resources_folder));
    $('#badgeslistdiv').append(String.format('<a href="http://latex.ppizarror.com/Template-Tareas/" id="aimg"><img src={0}templates/tareas.svg" style="display: none" /></a>', href_resources_folder));
    $('#badgeslistdiv').append(String.format('<a href="http://latex.ppizarror.com/Template-Auxiliares/" id="aimg"><img src="{0}templates/auxiliares.svg" /></a>', href_resources_folder));
    $('#badgeslistdiv').append(String.format('<a href="http://latex.ppizarror.com/Template-Controles/" id="aimg"><img src="{0}templates/controles.svg" /></a>', href_resources_folder));
    $('#badgeslistdiv').append(String.format('<a href="http://latex.ppizarror.com/Template-Pautas/" id="aimg"><img src="{0}templates/pauta.svg" style="display: none" /></a>', href_resources_folder));
    $('#badgeslistdiv').append(String.format('<a href="http://latex.ppizarror.com/Template-Informe/" id="aimg"><img src="{0}templates/informe.svg" /></a>', href_resources_folder));
}
