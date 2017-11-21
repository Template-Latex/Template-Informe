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

var last_version = '$VERSION';
var last_version_link = '$VERSION_LINK';
var new_version_entry = '';
var pdf_href_lastv = '';
var total_downloads = 0;
var version_entries = [];

jQuery(document).ready(function($) {

    // Se escriben los badges
    writeBadges();

    // Se crean colores de elementos a partir de color base wallpaper
    acolor = shadeColor2(wallpaper_db.color, 0.3);
    backgroundmaincolor = shadeColor2(wallpaper_db.color, 0.98);
    bgprecolor = shadeColor2(wallpaper_db.color, 0.9);
    codebarcolor = shadeColor2(wallpaper_db.color, 0.4);
    codeprecolor = shadeColor2(wallpaper_db.color, 0.2);
    hrcolor = shadeColor2(wallpaper_db.color, 0.7);
    pacecolor = shadeColor2(wallpaper_db.color, 0.15);

    // Se añaden las descargas del template base
    var jsonquery = $.getJSON(href_json_releases, function(json) {

        // Se cargan los datos del json
        total_downloads = 0;
        for (i = 0; i < json.length; i++) {
            try {
                for (j = 0; j < json[i].assets.length; j++) {
                    total_downloads += parseInt(json[i].assets[j].download_count);
                    version_entries.push(json[i].tag_name);
                }
            } catch (err) {
                console.log(String.format('Error al obtener la cantidad de descargas del archivo {0}', json[i].name));
            }
        }

        // Válido para los subtemplates
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
            console.log(String.format('Última versión template: {0}', last_version));
        } catch (err) {
            console.log('Error al obtener la última versión del template');
            errVersion();
        }

        // Se actualiza total de descargas
        if (total_downloads == 0) {
            total_downloads = nan_value;
        } else {
            updateDownloadCounter(total_downloads, update_download_counter);
            j = '';
            for (var i = 0; i < download_list_counter.length; i++) {
                j = download_list_counter[i][1];
                if (version_entries.indexOf(j) == -1) {
                    if (Array.isArray(download_list_counter[i][0])) {
                        total_downloads += download_list_counter[i][0][0] + download_list_counter[i][0][1];
                    } else {
                        total_downloads += download_list_counter[i][0];
                    }
                }
            }
        }
        update_download_banner(total_downloads);

        // Se añade link estadísticas a banner descargas
        $('#main-content-section #templatestats').attr('href', stats_href + stats_name);

        if (update_download_counter == 'Template-Informe') {
            // Si es Template-Informe se muestra botón otras descargas
            $('a[name*=leanModal]').leanModal({
                top: 200,
                closeButton: '.modal_close'
            });
            normal_link = String.format('{0}/download/{1}/Template-Informe.zip', href_github_project, last_version);
            $('#download-button-1file').append(String.format(' <font id="buttonfile1text">(v{0}) <img src="{1}/zip.png" class="iconbutton" /></font>', last_version, href_resources_folder));
            $('#download-button').attr('href', normal_link);
            $('#download-button').append(String.format(' <font id="buttonfilectext">(v{0}) <img src="{1}/zip.png" class="iconbutton" /></font>', last_version, href_resources_folder));
            writeOtherLinks(last_version);
        } else {
            // Se establece la versión en el botón de descargas
            $('#download-button-1file').attr('href', compact_link);
            $('#download-button-1file').append(String.format(' <font id="buttonfilectext">(v{0}) <img src="{1}/zip.png" class="iconbutton" /></font>', last_version, href_resources_folder));
            $('#download-button').attr('href', normal_link);
            $('#download-button').append(String.format(' <font id="buttonfile1text">(v{0}) <img src="{1}/zip.png" class="iconbutton" /></font>', last_version, href_resources_folder));
            $(function() {
                $('#download-button-1file').click(function() {
                    if (total_downloads != nan_value) {
                        total_downloads += 1;
                        update_download_banner(total_downloads);
                    }
                });
            });
        }

        // Se muestra descargas y botones con efecto
        fadein_css('#total-download-counter-1', '0.1s');
        fadein_css('#total-download-counter-2', '0.1s');
        $('#buttonfile1text').fadeIn('slow');
        $('#buttonfilectext').fadeIn('slow');

        // Se establece la última versión del pdf
        pdf_href_lastv = pdf_js_href + String.format(href_pdf_version, last_version);
        $('#template-preview-pdf').attr('href', pdf_href_lastv);
        $(".badgeejemplopdf").attr('href', pdf_href_lastv);

        // Se obtiene el what's new
        $('#github-button-header').attr('href', href_github_project_source);
        whats_new_html = "<div id='que-hay-de-nuevo-version-title'>{0}</div><blockquote class='que-hay-de-nuevo-blockquote'>{1}</blockquote>";
        whats_new_versions = Math.min(changelog_max, json.length);
        md_converter = new showdown.Converter();
        show_github_button = (whats_new_versions == changelog_max);
        try {
            for (i = 0; i < whats_new_versions; i++) {
                version_created_at = json[i].created_at.substring(0, 10);
                title_new_version = String.format('<b>Versión <a href="{2}"">{0}</b></a>: <i class="fecha-estilo">{1}</i>', json[i].tag_name, version_created_at, json[i].html_url);
                content_version = md_converter.makeHtml(json[i].body);
                new_version_entry += String.format(whats_new_html, title_new_version, content_version);
                if (i < whats_new_versions - 1 && changelog_show_hr) {
                    new_version_entry += '<hr class="style1">';
                }
            }
            if (show_github_button) {
                new_version_entry += String.format("Puedes ver la lista de cambios completa <a href='{0}'>en Github<img src='{1}/github.png' width='16' height='' class='iconbutton' alt='' /></a>", href_github_project, href_resources_folder);
            }
            $('#que-hay-de-nuevo').html(new_version_entry);
            $('.main-content hr').css('background-color', hrcolor);
            $('.que-hay-de-nuevo-blockquote').css('border-left', '0.25rem solid ' + codebarcolor);
        } catch (err) {
            console.log('Error al obtener los contenidos de las últimas versiones');
            hide_element_id('whatsnew');
            hide_element_id('changelog-menu');
        }

        // Se llama a afterJSON
        afterJSONLoad();
    });

    // Se activa error de json
    jsonquery.fail(function() {
        console.log('Error al obtener la última versión del template');
        errVersion();
    });

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

    // Se cambia el color de las barras hr
    $('.main-content hr').css('background-color', hrcolor);

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
    if (changepacecolor) {
        $('.pace .pace-progress').css('background', pacecolor);
        $('.pace .pace-activity').css('border-top-color', codeprecolor);
        $('.pace .pace-activity').css('border-left-color', codeprecolor);
        $('.pace .pace-progress-inner').css('box-shadow', '0 0 10px ' + bgprecolor + ', 0 0 5px ' + bgprecolor + ';');
    }

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
            if (total_downloads != nan_value) {
                total_downloads += 1;
                update_download_banner(total_downloads);
            }
        });
    });

    // Muestra un botón para subir al hacer scroll
    var amountScrolled = 600;
    $(window).scroll(function() {
        location.pathname.replace(/^\//, '');
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

    // Se añade el link a chat banner
    $('#chatgitter').attr('href', gitter_href + update_download_counter);

    // Se llama a la función de cada template después de cargar
    afterDocumentReady();
});
