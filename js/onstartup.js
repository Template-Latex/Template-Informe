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

function getRandomInt(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

function shadeColor2(color, percent) {
    var f = parseInt(color.slice(1), 16),
        t = percent < 0 ? 0 : 255,
        p = percent < 0 ? percent * -1 : percent,
        R = f >> 16,
        G = f >> 8 & 0x00FF,
        B = f & 0x0000FF;
    return "#" + (0x1000000 + (Math.round((t - R) * p) + R) * 0x10000 + (Math.round((t - G) * p) + G) * 0x100 + (Math.round((t - B) * p) + B)).toString(16).slice(1);
}

// Se selecciona una imagen al azar
jQuery(document).ready(function($) {

    // Se comprueba si es navegador móvil
    var is_movile_browser = false;
    if (/Mobi/.test(navigator.userAgent)) {
        is_movile_browser = true;
        console.log('Utilizando versión móvil.')
    } else {
        console.log('Utilizando versión web.')
    }

    var images_background = [
        ['09305524.jpg', 'bottom', '#343434'], // 0
        ['67535412.jpg', 'bottom', '#C96265'], // 1
        ['93314696.jpg', 'top', '#6A6061'], // 2
        ['background.jpg', 'top', '#5E4E2A'], // 3
        ['12939392.jpg', 'bottom', '#614654'], // 4
        ['19392139.jpg', 'bottom', '#4E3E25'], // 5
        ['46140562.jpg', 'bottom', '#EF3D4D'], // 6
        ['37320735.jpg', 'bottom', '#333132'], // 7
        ['71453949.jpg', 'bottom', '#4F4F51'], // 8
        ['39581671.jpg', 'bottom', '#262C3C'], // 9
        ['99206040.jpg', 'bottom', '#5284A9'], // 10
        ['92910382.jpg', 'bottom', '#444444'], // 11
        ['04274037.jpg', 'top', '#602A13'], // 12
        ['72131838.jpg', 'center', '#896956'], // 13
        ['80718230.jpg', 'bottom', '#4C44AB'], // 14
        ['08038477.jpg', 'bottom', '#616D61'], // 15
        ['22532189.jpg', 'bottom', '#47474C'], // 16
        ['07086832.jpg', 'top', '#4F6068'], // 17
        ['11917378.jpg', 'bottom', '#393939'], // 18
        ['11944943.jpg', 'bottom', '#0A344F'], // 19
        ['15032996.jpg', 'bottom', '#304651'], // 20
        ['37994916.jpg', 'bottom', '#30307A'], // 21
        ['63330443.jpg', 'bottom', '#0C3C9A'], // 22
        ['46199258.jpg', 'bottom', '#5B4A48'], // 23
        ['39593777.jpg', 'bottom', '#014BBA'], // 24
        ['47702546.jpg', 'bottom', '#702269'], // 25
        ['51280378.jpg', 'bottom', '#174C82'], // 26
        ['80794446.jpg', 'bottom', '#6D5630'], // 27
        ['36752157.jpg', 'bottom', '#FE3060'], // 28
        ['42450256.jpg', 'bottom', '#50405B'], // 29
        ['89228305.jpg', 'bottom', '#C51A20'], // 30
        ['95243003.jpg', 'bottom', '#173966'], // 31
        ['16978868.jpg', 'bottom', '#7E5A40'], // 32
        ['22125894.jpg', 'bottom', '#272D69'], // 33
        ['77421788.jpg', 'bottom', '#4E6D44'], // 34
        ['91643340.jpg', 'bottom', '#197B30'], // 35
        ['88093858.jpg', 'bottom', '#485620'] // 36
    ];
    var images_indx_random = getRandomInt(0, images_background.length - 1);
    // images_indx_random = 36; // testeo
    var image_url = 'images/' + images_background[images_indx_random][0];
    var image_pos = images_background[images_indx_random][1];
    console.log(String.format('Estableciendo el fondo de pantalla {0} - ID {1}', image_url, images_indx_random));

    if (!is_movile_browser) {
        $('.page-header').parallax({
            imageSrc: image_url,
            speed: 0.15
        });
    } else {
        $('.page-header').css('background', '#161415 url(' + image_url + ') ' + image_pos + ' no-repeat fixed');
        $('.page-header').css('background-attachment', 'fixed');
        $('.page-header').css('-webkit-background-size', 'cover');
        $('.page-header').css('-moz-background-size', 'cover');
        $('.page-header').css('-o-background-size', 'cover');
        $('.page-header').css('background-size', 'cover');
        $('.page-header').css('max-width', '100%');
        $('.page-header').css('max-height', '100%');
        $('.page-header').css('width', $(window).width());
        // $(function() {
        //     $.stellar({
        //         horizontalScrolling: false,
        //         verticalOffset: 0
        //     });
        // });
        // $('.scrollable-home').stellar();
    }

    // var ua = navigator.userAgent.toLowerCase();
    // var isAndroid = ua.indexOf("android") > -1;
    // if (isAndroid) {
    //     $('.page-header').css('background', '#161415 ' + image_url);
    //     $('.page-header').css('background-attachment', 'fixed !important');
    //     $('.page-header').css('background-repeat', 'no-repeat !important');
    // }

    // Se cambia el color de los titulos
    var chosencolor = images_background[images_indx_random][2];
    $('.main-content h1').css('color', chosencolor);
    $('.main-content h2').css('color', chosencolor);
    $('.main-content h3').css('color', chosencolor);
    $('.main-content h4').css('color', chosencolor);
    $('.main-content h5').css('color', chosencolor);
    $('.main-content h6').css('color', chosencolor);
    $('.menu-big-entry').css('color', chosencolor);
    $('.menu-little-entry').css('color', chosencolor);
    $('.section-template').css('color', chosencolor);
    $('.que-hay-de-nuevo-blockquote h3').css('color', chosencolor);
    $('.back-to-top').css('background-color', chosencolor);

    // Se cambia el color de las cajas de código
    bgprecolor = shadeColor2(chosencolor, 0.85);
    codeprecolor = shadeColor2(chosencolor, 0.2);
    $('.main-content pre').css('border', 'solid 1px ' + codeprecolor);
    $('.main-content pre').css('background-color', bgprecolor);
    $('.main-content blockquote').css('color', codeprecolor);
    $('.main-content blockquote').css('border-left', '0.3rem solid ' + codeprecolor);
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
    // Se agregan 60 de version 2.3.7-2.4.0
    if (total_downloads == 0) {
        total_downloads = 'NaN';
    } else {
        total_downloads += 129 + 60 + 138 + 3 + 3 + 1 + 4 + 55 + 115 + 74 + 17 + 3 + 18 + 7 + 68 + 71 + 12 + 9 + 4 + 33 + 1 + 60;
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
// $('#scrolls').parallax({
//      imageSrc: 'images/background4.jpg',
//      speed: 0.15
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
                }, 700);
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
