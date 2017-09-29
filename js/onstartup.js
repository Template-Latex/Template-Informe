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

var github_changelog = false;
var last_version = "$VERSION";
var last_version_link = "$VERSION_LINK";
var new_version_entry = "";
var pdf_href_lastv;
var total_downloads = 0;

jQuery(document).ready(function($) {

    // Se añaden las descargas del template base
    $.getJSON(href_json_releases, function(json) {

        // Se cargan los datos del json
        for (i = 0; i < json.length; i++) {
            try {
                for (j = 0; j < json[i].assets.length; j++) {
                    total_downloads += parseInt(json[i].assets[j].download_count);
                }
            } catch (err) {
                console.log(String.format('Error al obtener la cantidad de descargas del archivo {0}', json[i].name));
            }
        }
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

        // Se imprimen estados en consola
        console.log(String.format('Última versión template: {0}', last_version));

        if (total_downloads == 0) {
            total_downloads = 'NaN';
        } else {
            total_downloads = updateDownloadCounter(total_downloads, update_download_counter);
        }

        // Se establece la versión en el contador de descargas totales
        document.getElementById('total-download-counter-1').innerHTML = total_downloads;
        document.getElementById('total-download-counter-2').innerHTML = total_downloads;

        // Se añade link estadísticas a banner descargas
        $('#main-content-section #templatestats').attr('href', 'http://latex.ppizarror.com/stats/index.html?template=' + stats_name);

        // Se establece la versión en el botón de descargas
        msg_download_normal = '{1} <font id="buttonfile1text">({0}) <img src="{2}/zip.png" class="iconbutton" /></font>';
        msg_download_compact = '{1} <font id="buttonfilectext">({0}) <img src="{2}/zip.png" class="iconbutton" /></font>';
        document.getElementById("download-button").href = normal_link;
        document.getElementById("download-button").innerHTML = String.format(msg_download_normal, last_version, document.getElementById("download-button").innerHTML, href_resources_folder);
        document.getElementById("download-button-1file").innerHTML = String.format(msg_download_compact, last_version, document.getElementById("download-button-1file").innerHTML, href_resources_folder);
        document.getElementById("download-button-1file").href = compact_link;

        // Se muestra descargas y botones con efecto
        fadein_css('#total-download-counter-1', '0.1s');
        fadein_css('#total-download-counter-2', '0.1s');
        $('#buttonfile1text').fadeIn('slow');
        $('#buttonfilectext').fadeIn('slow');

        // Se establece la última versión del pdf
        pdf_href_lastv = pdf_js_href + String.format(href_pdf_version, last_version);
        document.getElementById("template-preview-pdf").href = pdf_href_lastv;
        $(".badgeejemplopdf").prop("href", pdf_href_lastv);

        // Se obtiene el what's new
        document.getElementById("github-button-header").href = href_github_project_source;
        whats_new_html = "<div id='que-hay-de-nuevo-version-title'>{0}</div><blockquote id='que-hay-de-nuevo-blockquote'>{1}</blockquote>";
        whats_new_versions = Math.min(7, json.length);
        md_converter = new showdown.Converter();
        try {
            for (i = 0; i < whats_new_versions; i++) {
                version_created_at = json[i].created_at.substring(0, 10);
                title_new_version = String.format('<b>Versión <a href="{2}"">{0}</b></a>: <i class="fecha-estilo">{1}</i>', json[i].tag_name, version_created_at, json[i].html_url);
                content_version = md_converter.makeHtml(json[i].body);
                new_version_entry += String.format(whats_new_html, title_new_version, content_version);
                new_version_entry += '<hr class="style1">';
            }
            new_version_entry += String.format("Puedes ver la lista de cambios completa <a href='{0}'>en Github<img src='{1}/github.png' width='16px' height='16px' class='iconbutton' /></a>", href_github_project, href_resources_folder);
            document.getElementById("que-hay-de-nuevo").innerHTML = new_version_entry;
            github_changelog = true;
        } catch (err) {
            console.log('Error al obtener los contenidos de las últimas versiones');
            hide_element_id('whatsnew');
            hide_element_id('changelog-menu');
        }

        // Se llama a afterJSON
        afterJSONLoad();
    });

    // Se escriben los badges
    writeBadges();

    // Se eligen colores al azar
    acolor = shadeColor2(wallpaper_db.color, 0.3);
    backgroundmaincolor = shadeColor2(wallpaper_db.color, 0.98);
    bgprecolor = shadeColor2(wallpaper_db.color, 0.9);
    codebarcolor = shadeColor2(wallpaper_db.color, 0.4);
    codeprecolor = shadeColor2(wallpaper_db.color, 0.2);
    pacecolor = shadeColor2(wallpaper_db.color, 0.15);

    // Se define color de fondo principal antes de carga imagen
    $('#background-page-header-colored').css('background-color', wallpaper_db.color);
    $('#background-page-header-colored').fadeIn('slow');

    // Se cambia el color de los titulos
    $('.back-to-top').css('background-color', wallpaper_db.color);
    $('.main-content h1').css('color', wallpaper_db.color);
    $('.main-content h2').css('color', wallpaper_db.color);
    $('.main-content h3').css('color', wallpaper_db.color);
    $('.main-content h4').css('color', wallpaper_db.color);
    $('.main-content h5').css('color', wallpaper_db.color);
    $('.main-content h6').css('color', wallpaper_db.color);
    $('.menu-big-entry').css('color', wallpaper_db.color);
    $('.menu-little-entry').css('color', wallpaper_db.color);
    $('.que-hay-de-nuevo-blockquote h3').css('color', wallpaper_db.color);
    $('.section-template').css('color', wallpaper_db.color);

    // Se cambia el color de los enlaces
    // $('a').css('color', acolor);

    // Se cambia el color de las cajas de código
    $('.main-content blockquote').css('border-left', '0.25rem solid ' + codebarcolor);
    $('.main-content blockquote').css('color', codeprecolor);
    $('.main-content pre').css('background-color', bgprecolor);
    $('.main-content pre').css('border', 'solid 1px ' + codeprecolor);

    // Se cambia el color del fondo de la página web
    $('.main-content').css('background-color', backgroundmaincolor);
    $('#contentBackground').css('background-color', backgroundmaincolor);
    $('body').css('background-color', backgroundmaincolor);

    // Se actualizan los colores del whatsnew
    $('#que-hay-de-nuevo blockquote').css('border-left', '0.25rem solid ' + codebarcolor);

    // Si no se encontraron descargas
    if (enable_error_window && total_downloads == 0 && last_version == '$VERSION' && github_changelog == false) {
        console.log('ERROR: No se detectó una versión, desactivando paneles.');
        document.getElementById('whatsnew').style = 'display:none';
        hide_element_id('download-button');
        hide_element_id('download-button-1file');
        hide_element_id('whatsnew');
        hide_element_id('downloadcounter-banner');
        document.getElementById('main-content-section').innerHTML = "<div class='error_msg_1'>Error: No se pudo obtener la última versión disponible :(</div>";
        $('.error_msg_1').css('background-image', 'url("' + href_resources_folder + 'alert_background.png")');
    } else {}

    // Se comprueba si es navegador móvil
    var is_movile_browser = false;
    if (/Mobi/.test(navigator.userAgent)) {
        is_movile_browser = true;
        console.log('Utilizando versión móvil');
    } else {
        console.log('Utilizando versión web');
    }
    console.log(String.format('Estableciendo el fondo de pantalla {0} - ID {1}', wallpaper_db.image, wallpaper_db.index));

    if (!is_movile_browser && enableparallax) {
        $('#background-page-header').parallax({
            imageSrc: wallpaper_db.image,
            speed: 0.15,
            positionY: wallpaper_db.position,
            positionX: 'center',
            zIndex: 1
        });
        console.log('Se activo el parallax');
    } else {
        var back_img = new Image();
        back_img.onload = function() {
            $('#background-page-header').css({
                'background': wallpaper_db.color + ' url(' + wallpaper_db.image + ') ' + wallpaper_db.position + ' no-repeat fixed',
                'background-attachment': 'fixed',
            });
            $('#background-page-header').css('-webkit-background-size', 'cover');
            $('#background-page-header').css('-moz-background-size', 'cover');
            $('#background-page-header').css('-o-background-size', 'cover');
            $('#background-page-header').css('background-size', 'cover');
            $('#background-page-header').css('max-width', '100%');
            $('#background-page-header').css('width', $(window).width());
            fadein_css('#background-page-header', '0.5s');
            wallpaper_db_random_blur('#background-page-header', blurprobability, blurlimits);
        }
        back_img.src = wallpaper_db.image;
    }

    // Se cambia el color de pace
    // $('.pace .pace-progress').css('background', pacecolor);
    // $('.pace .pace-activity').css('border-top-color', codeprecolor);
    // $('.pace .pace-activity').css('border-left-color', codeprecolor);
    // $('.pace .pace-progress-inner').css('box-shadow', '0 0 10px '+bgprecolor+', 0 0 5px '+bgprecolor+';');

    // Se añade un evento al cambiar tamaño página web
    $(window).resize(function() {
        $('#background-page-header').css('width', $(window).width());
    });

    // Se actualiza la cantidad de descargas al hacer click
    $('total-download-counter').each(function() {
        this.id.innerHTML = total_downloads;
    });
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

    // Muestra un botón para subir al hacer scroll
    var amountScrolled = 600;
    $(window).scroll(function() {
        location.pathname.replace(/^\//, '')
        if ($(window).scrollTop() > amountScrolled) {
            $('a.back-to-top').fadeIn('slow');
        } else {
            $('a.back-to-top').fadeOut('slow');
        }
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

    // Se llama a la función de cada template después de cargar
    afterDocumentReady();
});
