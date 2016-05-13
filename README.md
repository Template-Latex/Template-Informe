## Template de informe en latex
Este corresponde a un template para confeccionar informes en latex, contiene funciones básicas para agregar imágenes, fórmulas, etc.

## Configurando el documento
Para modificar el documento (Título, nombre de la universidad, curso, etc.) se deben modificar las variables definidas en el bloque de *%INFORMACIÓN DEL DOCUMENTO* al principio del documento, estas son del estilo _\newcommand{_**\nombreVariable**_}{_ **Valor**}, entre las cuales se encuentran:
+ **\nombreDelInformeTitulo**: Título del informe.
+ **\temaATratar**: Tema a tratar.
+ **\nombreDelCurso**: Curso - Ramo referido al informe.
+ **\codigoDelCurso**: Código del curso.
+ **\nombreUniversidad**: Universidad, Instituto, etc.
+ **\nombreFacultad**: Facultad relacionada a la Universidad, Instituto, etc.
+ **\departamentoUniversidad**: Departamento de la Universidad.
+ **\imagenDelDepartamento**: Imagen del departamento o universidad a usar en la portada.
+ **\imagenDelDepartamentoEscala**: Escala de la imagen a usar.

## Configurando otros elementos del documento
También se pueden modificar los márgenes de los títulos de tablas y figuras _(caption)_, el tamaño de los títulos de las secciones, etc. Estas se encuentran en el bloque de *%INFORMACIÓN DEL DOCUMENTO*, entre las cuales se encuentran:
+ **\tipofuentetitulo**: Tamaño por defecto de los títulos.
+ **\tipofuentesubtitulo**: Tamaño por defecto de los subtítulos.
+ **\tiporeferencias}{apa}**: Tipo de referencias.
+ **\nombreltformulas**: Nombre de la lista de fórmulas.
+ **\nombrelttablas**: Nombre de la lista de tablas.
+ **\nombreltfiguras**: Nombre de la lista de figuras.
+ **\nombreltcontend**: Nombre del índice de contenidos.
+ **\nombreltwtablas**: Nombre de las tablas.
+ **\nombreltwfigura**: Nombre de las figuras.
+ **\defaultcaptionmargin**: Márgenes de las leyendas por defecto.
+ **\defaultpagemarginleft**: Márgen izquierdo de las páginas en centímetros.
+ **\defaultpagemarginright**: Márgen derecho de las páginas en centímetros.
+ **\defaultpagemargintop**: Márgen superior de las páginas en centímetros.
+ **\defaultpagemarginbottom**: Márgen inferior de las páginas en centímetros.
+ **\defaultfirstpagemargintop**: Márgen superior de la portada en centímetros.

## Añadiendo librerías
Las librerías se cargan en la sección *%LIBRERÍAS INDEPENDIENTES* y *%LIBRERÍAS DEPENDIENTES*, en librerías independientes se cargan las librerías que, como bien dice su nombre, no dependen de la previa importación de otras, o que su importación no genera algún error. Las librerías utilizadas son:
+ **amsmath**: Fórmulas matemáticas.
+ **amssymb**: Símbolos matemáticos.
+ **amsthm**: Teoremas matemáticos.
+ **cancel**: Cancelar términos en fórmulas.
+ **caption**: Leyendas (o títulos de objetos).
+ **color**: Colores.
+ **easylist**: Listas.
+ **epstopdf**: Convierte archivos .eps a pdf [dependiente].
+ **fancyhdr**: Encabezados y pié de páginas.
+ **float**: Administrador de posiciones de objetos.
+ **geometry**: Dimensiones y geometría del documento.
+ **graphicx**: Propiedades extra para los gráficos.
+ **hyperref**: Permite añadir enlaces y referencias.
+ **mhchem**:	Fórmulas químicas [versión 4].
+ **multicol**: Múltiples columnas.
+ **multirow**: Añade nuevas opciones a las tablas [dependiente].
+ **lipsum**: Permite crear textos dummy.
+ **longtable**: Permite utilizar tablas en varias hojas.
+ **listings**: Permite añadir código fuente.
+ **setspace**: Cambia el espacio entre líneas.
+ **subfig**: Permite agrupar imágenes.
+ **titlesec}**: Cambia el estilo de los títulos.
+ **url**: Permite añadir enlaces.
+ **wrapfig**: Permite comprimir imágenes.

## Insertando figuras, fórmulas, citas y otros
También es posible añadir fórmulas, citas, figuras y otros elementos de forma sencilla, para ello existen las siguientes funciones:
+ __underline__: **Añadir una imagen**: Existen dos funciones para añadir imágenes:

## Autor
Pablo Pizarro, 2016.

Si tienes alguna sugerencia envíame un correo a: [pablopizarro9@gmail.com](mailto:pablopizarro9@gmail.com).
