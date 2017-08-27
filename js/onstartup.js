 // Se selecciona una imagen al azar
var images_background = [
    ['09305524.jpg', 'center', '#343434'], // 0
    ['67535412.jpg', 'bottom', '#C96265'], // 1
    ['93314696.jpg', 'center', '#6A6061'], // 2
    ['background.jpg', 'center', '#5E4E2A'], // 3
    ['12939392.jpg', 'center', '#614654'], // 4
    ['19392139.jpg', 'center', '#4E3E25'], // 5
    ['46140562.jpg', 'center', '#EF3D4D'], // 6
    ['37320735.jpg', 'bottom', '#333132'], // 7
    ['71453949.jpg', 'top', '#4F4F51'], // 8
    ['39581671.jpg', 'bottom', '#262C3C'], // 9
    ['99206040.jpg', 'bottom', '#5284A9'], // 10
    ['92910382.jpg', 'bottom', '#444444'], // 11
    ['04274037.jpg', 'top', '#602A13'], // 12
    ['72131838.jpg', 'center', '#896956'], // 13
    ['80718230.jpg', 'bottom', '#4C44AB'], // 14
    ['08038477.jpg', 'center', '#616D61'], // 15
    ['22532189.jpg', 'bottom', '#47474C'], // 16
    ['07086832.jpg', 'top', '#4F6068'], // 17
    ['11917378.jpg', 'bottom', '#393939'], // 18
    ['11944943.jpg', 'bottom', '#0A344F'], // 19
    ['15032996.jpg', 'bottom', '#304651'], // 20
    ['37994916.jpg', 'center', '#30307A'], // 21
    ['63330443.jpg', 'top', '#0C3C9A'], // 22
    ['46199258.jpg', 'bottom', '#5B4A48'], // 23
    ['39593777.jpg', 'bottom', '#014BBA'], // 24
    ['47702546.jpg', 'bottom', '#702269'], // 25
    ['51280378.jpg', 'center', '#174C82'], // 26
    ['80794446.jpg', 'center', '#6D5630'], // 27
    ['36752157.jpg', 'center', '#FE3060'], // 28
    ['42450256.jpg', 'bottom', '#50405B'], // 29
    ['89228305.jpg', 'bottom', '#C51A20'], // 30
    ['95243003.jpg', 'bottom', '#173966'], // 31
    ['16978868.jpg', 'center', '#7E5A40'], // 32
    ['22125894.jpg', 'bottom', '#272D69'], // 33
    ['77421788.jpg', 'center', '#4E6D44'], // 34
    ['91643340.jpg', 'bottom', '#197B30'], // 35
    ['88093858.jpg', 'bottom', '#485620'], // 36
    ['00939591.jpg', 'center', '#35455B'], // 37
    ['13838368.jpg', 'center', '#6C5640'], // 38
    ['14269512.jpg', 'center', '#4F63D5'], // 39
    ['37882132.jpg', 'bottom', '#223836'], // 40
    ['38920979.jpg', 'bottom', '#357789'], // 41
    ['39850828.jpg', 'center', '#435273'], // 42
    ['50989454.jpg', 'top', '#3e6f8f'], // 43
    ['57231197.jpg', 'bottom', '#4d3945'], // 44
    ['91853601.jpg', 'bottom', '#a32ab5'], // 45
    ['03081592.jpg', 'bottom', '#3c412a'], // 46
    ['15877230.jpg', 'center', '#3c5086'], // 47
    ['25528122.jpg', 'bottom', '#f94021'], // 48
    ['29656367.jpg', 'center', '#3b81fa'], // 49
    ['38184232.jpg', 'bottom', '#6c70a6'], // 50
    ['44532443.jpg', 'center', '#282828'], // 51
    ['45325963.jpg', 'bottom', '#2c5362'], // 52
    ['60192994.jpg', 'bottom', '#562554'], // 53
    ['62639926.jpg', 'bottom', '#54585b'], // 54
    ['65354463.jpg', 'bottom', '#3a3e3f'], // 55
    ['65737758.jpg', 'center', '#80688a'], // 56
    ['66539241.jpg', 'center', '#a62400'], // 57
    ['71516908.jpg', 'center', '#483f44'], // 58
    ['73822546.jpg', 'bottom', '#382952'], // 59
    ['80768085.jpg', 'bottom', '#323e58'], // 60
    ['93568387.jpg', 'bottom', '#354a5a'], // 61
    ['97469752.jpg', 'center', '#ba4234'], // 62
    ['02530621.jpg', 'center', '#313131'], // 63
    ['02534697.jpg', 'top', '#314200'], // 64
    ['02642756.jpg', 'center', '#5b1943'], // 65
    ['03625208.jpg', 'center', '#484f55'], // 66
    ['05378902.jpg', 'bottom', '#141b27'], // 67
    ['09553028.jpg', 'center', '#51363c'], // 68
    ['16845918.jpg', 'center', '#520031'], // 69
    ['18027342.jpg', 'center', '#123473'], // 70
    ['26185627.jpg', 'bottom', '#5142a3'], // 71
    ['30915665.jpg', 'bottom', '#7c2e46'], // 72
    ['31865394.jpg', 'bottom', '#782958'], // 73
    ['32064937.jpg', 'top', '#212224'], // 74
    ['39295944.jpg', 'center', '#a02426'], // 75
    ['45515453.jpg', 'center', '#6a2d1b'], // 76
    ['58763802.jpg', 'center', '#2d2c2a'], // 77
    ['64402687.jpg', 'center', '#1c234f'], // 78
    ['64597743.jpg', 'bottom', '#64202b'], // 79
    ['65086685.jpg', 'bottom', '#4a4e50'], // 80
    ['71169273.jpg', 'center', '#0472af'], // 81
    ['79989977.jpg', 'top', '#09182d'], // 82
    ['82956328.jpg', 'bottom', '#354b72'], // 83
    ['83984226.jpg', 'top', '#721f3f'], // 84
    ['86588736.jpg', 'center', '#5a5a5a'], // 85
    ['94052111.jpg', 'center', '#484e4e'], // 86
    ['94936130.jpg', 'center', '#561111'], // 87
    ['97039416.jpg', 'bottom', '#362d2e'], // 88
    ['07949312.jpg', 'bottom', '#4b6270'], // 89
    ['08760783.jpg', 'bottom', '#096e6a'], // 90
    ['33459034.jpg', 'center', '#544a34'], // 91
    ['42501581.jpg', 'bottom', '#0c2747'], // 92
    ['50861756.jpg', 'center', '#47411a'], // 93
    ['68963144.jpg', 'center', '#462314'], // 94
    ['70290917.jpg', 'center', '#710304'], // 95
    ['91686162.jpg', 'bottom', '#644c3a'], // 96
    ['99917062.jpg', 'bottom', '#504e4c'], // 97
    ['05327721.jpg', 'top', '#3c3c56'], // 98
    ['19489238.jpg', 'bottom', '#4c4847'], // 99
    ['27241217.jpg', 'center', '#6e513f'], // 100
    ['31534692.jpg', 'bottom', '#403c30'], // 101
    ['45125712.jpg', 'center', '#1e4a0a'], // 102
    ['59272533.jpg', 'center', '#580f25'], // 103
    ['82884717.jpg', 'bottom', '#1c0031'], // 104
    ['88649909.jpg', 'center', '#513954'], // 105
    ['95686782.jpg', 'bottom', '#2f1143'] // 106
];
var images_indx_random = getRandomInt(0, images_background.length - 1);
// images_indx_random = 106; // testeo
var image_url = href_images_parent + images_background[images_indx_random][0];
var image_pos = images_background[images_indx_random][1];

// Se eligen colores al azar
var chosencolor = images_background[images_indx_random][2];
bgprecolor = shadeColor2(chosencolor, 0.9);
codeprecolor = shadeColor2(chosencolor, 0.2);
codebarcolor = shadeColor2(chosencolor, 0.4);
pacecolor = shadeColor2(chosencolor, 0.15);
backgroundmaincolor = shadeColor2(chosencolor, 0.98);

// Descargas totales y última versión
var total_downloads = 0;
var last_version = "$VERSION";
var last_version_link = "$VERSION_LINK";
var github_changelog = false;

// Se añaden las descargas del template base
$.getJSON(href_json_releases, function(json) {
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
    // console.log(String.format('Cantidad de descargas totales: {0}', total_downloads));
    console.log(String.format('Última versión: {0}', last_version));
    console.log(String.format('Última versión - enlace descarga: {0}', last_version_link));

    if (total_downloads == 0) {
        total_downloads = 'NaN';
    } else {
        total_downloads = updateDownloadCounter(total_downloads, update_download_counter);
    }

    // Se establece la versión en el contador de descargas totales
    document.getElementById('total-download-counter-1').innerHTML = total_downloads;
    document.getElementById('total-download-counter-2').innerHTML = total_downloads;

    // Se establece la versión en el botón de descargas
    msg_download_normal = '{1} <font style="color: #333333;">({0})</font> <img src="{2}/zip.png" class="iconbutton" />';
    msg_download_compact = '{1} <font style="color: #ffffff;">({0})</font>  <img src="{2}/zip.png" class="iconbutton" />';
    document.getElementById("download-button").href = normal_link;
    document.getElementById("download-button").innerHTML = String.format(msg_download_normal, last_version, document.getElementById("download-button").innerHTML, href_resources_folder);
    document.getElementById("download-button-1file").innerHTML = String.format(msg_download_compact, last_version, document.getElementById("download-button-1file").innerHTML, href_resources_folder);
    document.getElementById("download-button-1file").href = compact_link;

    // Se establece la última versión del pdf
    var pdf_href_lastv = pdf_js_href + String.format(href_pdf_version, last_version);
    document.getElementById("template-preview-pdf").href = pdf_href_lastv;
    $(".badgeejemplopdf").prop("href", pdf_href_lastv);

    // Se obtiene el what's new
    document.getElementById("github-button-header").href = href_github_project_source;
    whats_new_html = "<div id='que-hay-de-nuevo-version-title'>{0}</div><blockquote id='que-hay-de-nuevo-blockquote'>{1}</blockquote>";
    whats_new_versions = 7;
    md_converter = new showdown.Converter();
    try {
        var new_version_entry = "";
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

    // Se actualizan los colores del whatsnew
    $('#que-hay-de-nuevo blockquote').css('border-left', '0.25rem solid ' + codebarcolor);
});

// FINAL
jQuery(document).ready(function($) {

    // Si no se encontraron descargas
    if (enable_error_window && total_downloads == 0 && last_version == '$VERSION' && github_changelog == false) {
        console.log('ERROR: No se detectó una versión, desactivando paneles.');
        document.getElementById('whatsnew').style = 'display:none';
        hide_element_id('download-button');
        hide_element_id('download-button-1file');
        hide_element_id('whatsnew');
        hide_element_id('downloadcounter-banner');
        document.getElementById('main-content-section').innerHTML = "<div class='error_msg_1'>Error: No se pudo obtener la última versión disponible :(</div>";
        $('.error_msg_1').css('background-image', 'url("' + href_resources_folder + 'alert_background.png")')
    } else {
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
    }

    // Se comprueba si es navegador móvil
    var is_movile_browser = false;
    if (/Mobi/.test(navigator.userAgent)) {
        is_movile_browser = true;
        console.log('Utilizando versión móvil.')
    } else {
        console.log('Utilizando versión web.')
    }
    console.log(String.format('Estableciendo el fondo de pantalla {0} - ID {1}', image_url, images_indx_random));

    if (!is_movile_browser && enableparallax) {
        $('.page-header').parallax({
            imageSrc: image_url,
            speed: 0.15,
            positionY: image_pos,
            positionX: 'center',
            zIndex: 1
        });
    } else {
        var back_img = new Image();
        back_img.onload = function() {
            $('.page-header').css({
                'background': chosencolor + ' url(' + image_url + ') ' + image_pos + ' no-repeat fixed',
                'background-attachment': 'fixed',
            });
            $('.page-header').css('-webkit-background-size', 'cover');
            $('.page-header').css('-moz-background-size', 'cover');
            $('.page-header').css('-o-background-size', 'cover');
            $('.page-header').css('background-size', 'cover');
            $('.page-header').css('max-width', '100%');
            $('.page-header').css('width', $(window).width());
            fadein_css('.page-header', '0.5s');
            fadein_css('#total-download-counter-1', '0.1s');
            fadein_css('#total-download-counter-2', '0.1s');
        }
        back_img.src = image_url;
    }

    // Se cambia el color de pace
    // $('.pace .pace-progress').css('background', pacecolor);
    // $('.pace .pace-activity').css('border-top-color', codeprecolor);
    // $('.pace .pace-activity').css('border-left-color', codeprecolor);
    // $('.pace .pace-progress-inner').css('box-shadow', '0 0 10px '+bgprecolor+', 0 0 5px '+bgprecolor+';');

    // Se cambia el color de los titulos
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
    $('.main-content pre').css('border', 'solid 1px ' + codeprecolor);
    $('.main-content pre').css('background-color', bgprecolor);
    $('.main-content blockquote').css('color', codeprecolor);
    $('.main-content blockquote').css('border-left', '0.25rem solid ' + codebarcolor);

    // Se cambia el color del fondo de la página web
    $('.main-content').css('background-color', backgroundmaincolor);
    $('body').css('background-color', backgroundmaincolor);

});
