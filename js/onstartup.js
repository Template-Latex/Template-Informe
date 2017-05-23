// Se instancia el convertidor de md
var md_converter = new showdown.Converter();

// Función String.format(...)
if (!String.format) {
    String.format = function(format) {
        var args = Array.prototype.slice.call(arguments, 1);
        return format.replace(/{(\d+)}/g, function(match, number) {
            return typeof args[number] != 'undefined' ?
                args[number] :
                match;
        });
    };
}

// Se selecciona una imagen al azar

jQuery(document).ready(function($) {
var images_background = [
    'url(images/09305524.jpg) bottom',
    'url(images/67535412.jpg) bottom',
    'url(images/93314696.jpg) center',
    'url(images/background.jpg) top',
    'url(images/background4.jpg) bottom',
    'url(images/background6.jpg) bottom',
    'url(images/46140562.jpg) bottom',
    'url(images/37320735.jpg) bottom',
    'url(images/71453949.jpg) bottom',
    'url(images/39581671.jpg) bottom',
    'url(images/99206040.jpg) bottom',
    'url(images/92910382.jpg) bottom',
    'url(images/04274037.jpg) top',
    'url(images/72131838.jpg) center',
    'url(images/80718230.jpg) bottom',
    'url(images/08038477.jpg) bottom',
    'url(images/22532189.jpg) bottom',
    'url(images/07086832.jpg) top',
    'url(images/11917378.jpg) bottom',
    'url(images/11944943.jpg) bottom',
    'url(images/15032996.jpg) bottom',
    'url(images/37994916.jpg) bottom',
    'url(images/63330443.jpg) bottom',

    'url(images/46199258.jpg) bottom',
    'url(images/39593777.jpg) bottom',
    'url(images/47702546.jpg) bottom',
    'url(images/51280378.jpg) bottom'
];
var images_indx_random = Math.floor(Math.random() * images_background.length);
// images_indx_random = 26; // testeo
var image_url = images_background[images_indx_random];
console.log('Estableciendo el fondo de pantalla ' + image_url);
console.log($('#scrolld'))
$('.page-header').css('background', '#161415 ' + image_url + ' no-repeat fixed');
$('.page-header').css('background-attachment', 'fixed');
$('.page-header').css('-webkit-background-size', 'cover !important');
$('.page-header').css('-moz-background-size', 'cover !important');
$('.page-header').css('-o-background-size', 'cover !important');
$('.page-header').css('background-size', 'cover !important');

var ua = navigator.userAgent.toLowerCase();
var isAndroid = ua.indexOf("android") > -1;
if(isAndroid) {
  $('.page-header').css('background-attachment', 'fixed !important');
}

});

// Se definen las líneas de cada sección en la página web
var linea_info_documento = 21;
var linea_tabla = 39;
var linea_configuraciones = 75;
var linea_importaciones = 122;
var linea_inicio = 562;

// Descargas totales
var total_downloads = 0;

// Se añaden las descargas de template-informe-cursos
// $.getJSON("https://api.github.com/repos/ppizarror/Template-Informe-cursos/releases", function(json) {
//     for (i = 0; i < json.length; i++) {
//         try {
//             total_downloads += parseInt(json[i].assets[0].download_count);
//
//         } catch (err) {
//             console.log(String.format('Error al obtener la cantidad de descargas del archivo {0}', json[i].name));
//         }
//     }
// });

// Se añaden las descargas del template base
$.getJSON("https://api.github.com/repos/ppizarror/Template-Informe/releases", function(json) {
    for (i = 0; i < json.length; i++) {
        try {
            for (j = 0; j < json[i].assets.length; j++) {
                total_downloads += parseInt(json[i].assets[j].download_count);
            }
        } catch (err) {
            console.log(String.format('Error al obtener la cantidad de descargas del archivo {0}', json[i].name));
        }
    }
    var last_version = "$VERSION";
    var last_version_link = "$VERSION_LINK";
    try {
        last_version = json[0].tag_name;
        last_version_link = json[0].assets[0].browser_download_url;
        last_version_link_1 = json[0].assets[1].browser_download_url;
        if (last_version_link.includes('-Single')) {
            normal_link = last_version_link_1;
            compact_link = last_version_link;
        } else {
            normal_link = last_version_link;
            compact_link = last_version_link_1;
        }
    } catch (err) {
        console.log('Error al obtener la última versión del software');
    }

    //Se imprimen estados en consola
    console.log(String.format('Cantidad de descargas totales: {0}', total_downloads));
    console.log(String.format('Última versión: {0}', last_version));
    console.log(String.format('Última versión - enlace descarga: {0}', last_version_link));

    // Se añaden las 129 descargas de https://api.github.com/repos/ppizarror/Template-Informe-cursos/releases
    // Se añaden 60 descargas entre 1.8.5 y 1.9.6
    // Se añaden 138 descargas entre 1.9.6 y 2.0.6
    // Se añaden 3 descargas de versión 2.0.7
    // Se añaden 3 descargas de versión 2.0.8
    // Se agrega 1 descarga de versión 2.0.9
    // Se agrega 4 descara de versión 2.1.1
    // Se agregan 55 descargas de version 2.1.2-2.1.5
    // Se agregan 115 descargas entre version 2.1.5 y 2.2.1
    // Se agregan 74 descargas de version 2.2.2
    // Se agregan 17 descargas de versión 2.2.3
    // Se agregan 3 descargas de version 2.2.4
    // Se agregan 18 descargas de version 2.2.5
    // Se agregan 7 descargas de version 2.2.6
    // Se agregan 68 descargas entre version 2.2.6 y 2.3.0
    // Se agregan 71 descargas de version 2.3.1
    // Se agregan 12 descargas de version 2.3.2
    // Se agregan 9 descargas de version 2.3.3
    // Se agregan 4 descargas de version 2.3.4
    // Se agregan 33 descargas de version 2.3.5
    // Se agrega 1 descarga de version 2.3.6
    if (total_downloads == 0) {
        total_downloads = 'NaN';
    } else {
        total_downloads += 129+60+138+3+3+1+4+55+115+74+17+3+18+7+68+71+12+9+4+33+1;
    }

    // Se establece la versión en el contador de descargas totales
    document.getElementById('total-download-counter-1').innerHTML = total_downloads;
    document.getElementById('total-download-counter-2').innerHTML = total_downloads;

    // Se establece la versión en el botón de descargas
    msg_download_normal = '{1} <font style="color: #333333;">({0})</font> <img src="resources/zip.png" width="16px" height="16px" class="iconbutton" />'
    msg_download_compact = '{1} <font style="color: #ffffff;">({0})</font>  <img src="resources/zip.png" width="16px" height="16px" class="iconbutton" />'
    document.getElementById("download-button").href = normal_link;
    document.getElementById("download-button").innerHTML = String.format(msg_download_normal, last_version, document.getElementById("download-button").innerHTML);
    document.getElementById("download-button-1file").innerHTML = String.format(msg_download_compact, last_version, document.getElementById("download-button-1file").innerHTML);
    document.getElementById("download-button-1file").href = compact_link;

    // Se establece la última versión del pdf
    console.log(String.format('Archivo pdf a mostrar: versions/Template v{0}.pdf', last_version))
    document.getElementById("template-preview-pdf").href = String.format('versions/Template v{0}.pdf', last_version);
    $(".badgeejemplopdf").prop("href", String.format('versions/Template v{0}.pdf', last_version));

    // Se obtiene el what's new
    var whats_new_html = "<div id='que-hay-de-nuevo-version-title'>{0}</div><blockquote id='que-hay-de-nuevo-blockquote'>{1}</blockquote>";
    var whats_new_versions = 7;
    try {
        var new_version_entry = "";
        for (i = 0; i < whats_new_versions; i++) {
            version_created_at = json[i].created_at.substring(0, 10);
            title_new_version = String.format('<b>Versión <a href="{2}"">{0}</b></a>: <i class="fecha-estilo">{1}</i>', json[i].tag_name, version_created_at, json[i].html_url);
            content_version = md_converter.makeHtml(json[i].body);
            new_version_entry += String.format(whats_new_html, title_new_version, content_version);
            new_version_entry += '<hr class="style1">';
        }
        new_version_entry += "Puedes ver la lista de cambios completa <a href='https://github.com/ppizarror/Template-Informe/releases'>en Github</a>.";
        document.getElementById("que-hay-de-nuevo").innerHTML = new_version_entry;
    } catch (err) {
        console.log('Error al obtener los contenidos de las últimas versiones');
        document.getElementById('whatsnew').style = 'display:none';
        document.getElementById('changelog-menu').style = 'display:none';
    }
});

// // Paralaje en el fondo
// $('#scrolld').parallax({
//     imageSrc: 'images/background4.jpg',
//     speed: 0.15
// });

$('total-download-counter').each(function() {
    this.id.innerHTML = total_downloads;
});

// Smooth scrolling al clickear un anchor
$(function() {
    $('a[href*="#"]:not([href="#"])').click(function() {
        if (location.pathname.replace(/^\//, '') == this.pathname.replace(/^\//, '') && location.hostname == this.hostname) {
            var target = $(this.hash);
            target = target.length ? target : $('[name=' + this.hash.slice(1) + ']');
            if (target.length) {
                $('html, body').animate({
                    scrollTop: target.offset().top
                }, 1000);
                return false;
            }
        }
    });
});

// Se actualiza la cantidad de descargas al hacer click
$(function() {
    $('#download-button').click(function() {
        total_downloads += 1;
        document.getElementById('total-download-counter-1').innerHTML = total_downloads;
        document.getElementById('total-download-counter-2').innerHTML = total_downloads;
    });
});
$(function() {
    $('#download-button-1file').click(function() {
        total_downloads += 1;
        document.getElementById('total-download-counter-1').innerHTML = total_downloads;
        document.getElementById('total-download-counter-2').innerHTML = total_downloads;
    });
});

var amountScrolled = 600;
$(window).scroll(function() {
    location.pathname.replace(/^\//, '')
    if ($(window).scrollTop() > amountScrolled) {
        $('a.back-to-top').fadeIn('slow');
    } else {
        $('a.back-to-top').fadeOut('slow');
    }
});
