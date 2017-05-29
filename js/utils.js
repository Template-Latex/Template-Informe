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

// Actualizador de descargas
function updateDownloadCounter(downloads) {
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
    // Se agregan 3 descargas de version 2.4.1
    // Se agregan 20 descargas de version 2.4.2-2.4.5
    download_list_counter = [129, 60, 138, 3, 3, 1, 4, 55, 115, 74, 17, 3, 18, 7, 68, 71, 12, 9, 4, 33, 1, 60, 3, 20];

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
    for (i=0; i<download_list_counter.length; i++){
        downloads += download_list_counter[i];
    }
    return downloads;
}
