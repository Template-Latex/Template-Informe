 // Genera un número aleatorio entero entre min y max
function getRandomInt(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

// Función para transformar colores, oscurece y aclarece
function shadeColor2(color, percent) {
    var f = parseInt(color.slice(1), 16),
        t = percent < 0 ? 0 : 255,
        p = percent < 0 ? percent * -1 : percent,
        R = f >> 16,
        G = f >> 8 & 0x00FF,
        B = f & 0x0000FF;
    return "#" + (0x1000000 + (Math.round((t - R) * p) + R) * 0x10000 + (Math.round((t - G) * p) + G) * 0x100 + (Math.round((t - B) * p) + B)).toString(16).slice(1);
}

// Función que transforma colores y los mezcla
function blendColors(c0, c1, p) {
    var f = parseInt(c0.slice(1), 16),
        t = parseInt(c1.slice(1), 16),
        R1 = f >> 16,
        G1 = f >> 8 & 0x00FF,
        B1 = f & 0x0000FF,
        R2 = t >> 16,
        G2 = t >> 8 & 0x00FF,
        B2 = t & 0x0000FF;
    return "#" + (0x1000000 + (Math.round((R2 - R1) * p) + R1) * 0x10000 + (Math.round((G2 - G1) * p) + G1) * 0x100 + (Math.round((B2 - B1) * p) + B1)).toString(16).slice(1);
}

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

// Desactiva cualquier elemento por id
function hide_element_id(idelem) {
    try {
        document.getElementById(idelem).style = 'display:none';
    } catch (err) {
        console.log('Error al ocultar id: ' + idelem)
    }
}

// Actualizador de descargas
function updateDownloadCounter(downloads, source) {

    switch (source) {
        case 'Template-Informe':
            // Se añaden las 129 descargas de https://api.github.com/repos/ppizarror/Template-Informe-cursos/releases
            // Se añaden 60 descargas entre versiones 1.8.5 y 1.9.6
            // Se añaden 138 descargas entre versiones 1.9.6 y 2.0.6
            // Se añaden 3 descargas de versión 2.0.7
            // Se añaden 3 descargas de versión 2.0.8
            // Se agrega 1 descarga de versión 2.0.9
            // Se agrega 4 descara de versión 2.1.1
            // Se agregan 55 descargas de versión 2.1.2-2.1.5
            // Se agregan 115 descargas entre versiones 2.1.5 y 2.2.1
            // Se agregan 74 descargas de versión 2.2.2
            // Se agregan 17 descargas de versión 2.2.3
            // Se agregan 3 descargas de versión 2.2.4
            // Se agregan 18 descargas de versión 2.2.5
            // Se agregan 7 descargas de versión 2.2.6
            // Se agregan 68 descargas entre versiones 2.2.6 y 2.3.0
            // Se agregan 71 descargas de versión 2.3.1
            // Se agregan 12 descargas de versión 2.3.2
            // Se agregan 9 descargas de versión 2.3.3
            // Se agregan 4 descargas de versión 2.3.4
            // Se agregan 33 descargas de versión 2.3.5
            // Se agrega 1 descarga de versión 2.3.6
            // Se agregan 60 de versión 2.3.7-2.4.0
            // Se agregan 3 descargas de versión 2.4.1
            // Se agregan 20 descargas entre versiones 2.4.2-2.4.5
            // Se agregan 38 descargas de versión 2.4.6
            // Se agregan 6 descargas de versión 2.4.7
            // Se agregan 146 descargas de versión 3.0.0
            // Se agregan 62 descargas de versión 3.0.1
            // Se agregan 28 descargas de versión 3.0.2
            // Se agregan 28 descargas de versión 3.0.3
            // Se agregan 84 descargas entre versiones 3.0.4-3.1.0
            // Se agregan 3 descargas de versión 3.1.2
            // Se agregan 12 descargas de versión 3.1.3
            // Se agregan 110 descargas entre versiones 3.1.4-3.2.0
            // Se agregan 31 descargas de versión 3.2.1
            // Se agregan 2 descargas de versión 3.2.2
            // Se agregan 8 descargas de versión 3.2.3
            // Se agregan 110 descargas de versión 3.2.4-3.3.0
            // Se agregan 55 descargas entre versiones 3.3.0-3.4.5
            // Se agregan 6 descargas entre versión 3.4.5-4.6.0
            // Se agregan 8 descargas de versión 3.6.0
            download_list_counter = [129, 60, 138, 3, 3, 1, 4, 55, 115, 74, 17, 3, 18, 7, 68, 71, 12, 9, 4, 33, 1, 60, 3, 20, 38, 6, 146, 62, 28, 28, 84, 3, 12, 110, 31, 2, 8, 110, 55, 6, 8];
            break;
        case 'Template-Auxiliares':
            download_list_counter = [];
            break;
        case 'Template-Tareas':
            download_list_counter = [];
            break;
        case 'Template-Apunte':
            download_list_counter = [];
            break;
        case 'Template-Pautas':
            download_list_counter = [];
            break;
        case 'Template-Controles':
            download_list_counter = [];
            break;
        case 'Template-Tesis':
            download_list_counter = [];
            break;
    }

    for (i = 0; i < download_list_counter.length; i++) {
        downloads += download_list_counter[i];
    }

    return downloads;
}
