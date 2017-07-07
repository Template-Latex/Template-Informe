# coding=utf-8
"""
Exporta main.tex a informe.tex (template sin archivos externos).
Cambia versión y fecha a archivos.

Autor: PABLO PIZARRO @ github.com/ppizarror
Fecha: ABRIL 2017
Licencia: MIT
"""

# Importación de librerías
from extlbx import *
import traceback

# Constantes
TITLE = 'Export Template'
TITLE_LOADING = 'Export Template | Espere ...'
LIMIT_MESSAGES_CONSOLE = 1000


# noinspection PyCompatibility,PyUnusedLocal,PyBroadException,PyCallByClass
class CreateVersion(object):
    """
    Pide la versión al usuario.
    """

    def __init__(self):
        def _kill(*args):
            """
            Destruye la ventana.

            :return:
            """
            self._root.destroy()

        def _update_ver(*args):
            """
            Pasa el foco al campo de versión, carga versiones de cada release.

            :return:
            """
            self._versiontxt.focus()
            self._versiontxt.delete(0, 'end')
            for j in RELEASES.keys():
                if self._release.get() == RELEASES[j]['NAME']:
                    self._versiontxt.configure(state='normal')
                    self._console = []
                    self._info_slider.canv.yview_scroll(-1000, 'units')
                    self._print('SELECCIONADO: {0}'.format(RELEASES[j]['NAME']))
                    self._print('ÚLTIMA VERSIÓN: {0}'.format(get_last_ver(RELEASES[j]['STATS']['FILE'])))
                    return

        def _checkver(sv):
            """
            Función auxiliar que chequea que la versión ingresada sea correcta.

            :param sv: String var de la versión
            :return:
            """
            ver = sv.get()
            try:
                mk_version(ver)
                self._startbutton.configure(state='normal')
                self._versiontxt.bind('<Return>', self._start)
            except:
                self._startbutton.configure(state='disabled')
                self._versiontxt.bind('<Return>')

        def _scroll_console(event):
            """
            Función que atrapa el evento del scrolling y mueve los comandos.

            :param event: Evento
            :return: void
            """
            if -175 < event.x < 240 and 38 < event.y < 136:
                if is_windows():
                    if -1 * (event.delta / 100) < 0:
                        move = -1
                    else:
                        move = 2
                elif is_osx():
                    if -1 * event.delta < 0:
                        move = -2
                    else:
                        move = 2
                else:
                    if -1 * (event.delta / 100) < 0:
                        move = -1
                    else:
                        move = 2
                if len(self._console) < 5 and move < 0:
                    return
                self._info_slider.canv.yview_scroll(move, 'units')

        self._root = Tk()
        self._root.protocol('WM_DELETE_WINDOW', _kill)

        # Ajusta tamaño ventana
        size = [420, 150]
        self._root.minsize(width=size[0], height=size[1])
        self._root.geometry('%dx%d+%d+%d' % (size[0], size[1], (self._root.winfo_screenwidth() - size[0]) / 2,
                                             (self._root.winfo_screenheight() - size[1]) / 2))
        self._root.resizable(width=False, height=False)
        self._root.focus_force()

        # Estilo ventana
        self._root.title(TITLE)
        self._root.iconbitmap('extlbx/icon.ico')
        fonts = [tkFont.Font(family='Courier', size=8),
                 tkFont.Font(family='Verdana', size=6),
                 tkFont.Font(family='Times', size=10),
                 tkFont.Font(family='Times', size=10, weight=tkFont.BOLD),
                 tkFont.Font(family='Verdana', size=6, weight=tkFont.BOLD),
                 tkFont.Font(family='Verdana', size=10),
                 tkFont.Font(family='Verdana', size=7)]

        f1 = Frame(self._root, border=5)
        f1.pack(fill=X)
        f2 = Frame(self._root)
        f2.pack(fill=BOTH)

        # Selección versión a compilar
        rels = []
        for b in RELEASES.keys():
            rels.append(RELEASES[b]['NAME'])
        self._release = StringVar(self._root)
        self._release.set('Seleccione template')
        w = apply(OptionMenu, (f1, self._release) + tuple(rels))
        w['width'] = 20
        w['relief'] = GROOVE
        w['anchor'] = W
        w.pack(side=LEFT)
        self._release.trace('w', _update_ver)

        # Campo de texto para versión
        Label(f1, text='Nueva versión:').pack(side=LEFT, padx=5)
        self._versionstr = StringVar()
        self._versionstr.trace('w', lambda name, index, mode, sv=self._versionstr: _checkver(sv))
        self._versiontxt = Entry(f1, relief=GROOVE, width=10, font=fonts[5], textvariable=self._versionstr)
        self._versiontxt.configure(state='disabled')
        self._versiontxt.pack(side=LEFT, padx=5)
        self._versiontxt.focus()

        # Botón iniciar
        self._startbutton = Button(f1, text='Iniciar', state='disabled', relief=GROOVE, command=self._start)
        self._startbutton.pack(side=RIGHT, padx=0, anchor=E)

        # Consola
        self._info_slider = VerticalScrolledFrame(f2)
        self._info_slider.canv.config(bg='#000000')
        self._info_slider.pack(pady=2, anchor=NE, fill=BOTH, padx=1)
        self._info = Label(self._info_slider.interior, text='', justify=LEFT,
                           wraplength=380, anchor=NW, bg='black', fg='white', font=fonts[0],
                           relief=FLAT, border=2, cursor='xterm')
        self._info.pack(anchor=NW, fill=BOTH)
        self._info_slider.scroller.pack_forget()
        self._console = []
        self._root.bind('<MouseWheel>', _scroll_console)
        self._cnextnl = False

        # Otros eventos
        self._root.bind('<Escape>', _kill)

    def _print(self, msg, hour=False, end=None):
        """
        Imprime mensaje en consola.

        :param msg: Mensaje
        :param hour: Muestra la hora
        :return: None
        """

        def _consoled(c):
            """
            Función que genera un string con una lista.

            :param c: Lista
            :return: Texto
            """
            text = ''
            for i in c:
                text = text + i + '\n'
            return text

        def _get_hour():
            """
            Función que retorna la hora de sistema.

            :return: String
            """
            return time.ctime(time.time())[11:20]

        msg = str(msg)
        if hour:
            msg = _get_hour() + ' ' + msg
        if len(self._console) == 0 or self._console[len(self._console) - 1] != msg:
            if self._cnextnl:
                self._console[len(self._console) - 1] += msg
            else:
                self._console.append(msg)
            if end == '':
                self._cnextnl = True
            else:
                self._cnextnl = False

        if len(self._console) > LIMIT_MESSAGES_CONSOLE:
            self._console.pop()

        self._info.config(text=_consoled(self._console))
        self._info_slider.canv.yview_scroll(1000, 'units')

    def getroot(self):
        """
        Retorna el root.

        :return:
        """
        return self._root

    def open(self):
        """
        Inicia la ventana.

        :return:
        """
        self._root.mainloop()

    def _start(self, *args):
        """
        Retorna el valor ingresado
        :return:
        """

        def _callback():

            # Se obtiene la id
            t = 0
            lastv = ''
            msg = ''
            for j in RELEASES.keys():
                if self._release.get() == RELEASES[j]['NAME']:
                    t = RELEASES[j]['ID']
                    lastv = get_last_ver(RELEASES[j]['STATS']['FILE']).split(' ')[0]
                    msg = RELEASES[j]['MESSAGE']

            # Se crea la versión
            ver, versiondev, versionhash = mk_version(self._versionstr.get())

            # Se comprueba versiones
            if not validate_ver(versiondev, lastv):
                tkMessageBox.showerror('Error', 'La versión nueva debe ser superior a la actual ({0}).'.format(lastv))
                self._print('ERROR: VERSIÓN INCORRECTA')
            else:
                try:
                    self._print(msg.format(versiondev))
                    if t == 1:
                        export_informe(ver, versiondev, versionhash, printfun=self._print, doclean=True)
                    elif t == 2:
                        export_auxiliares(ver, versiondev, versionhash, printfun=self._print)
                    else:
                        self._print('ERROR: ID INCORRECTO')
                except Exception as e:
                    tkMessageBox.showerror('Error fatal', 'Ocurrio un error inesperado al procesar la solicitud.')
                    self._print('ERROR: EXCEPCIÓN INESPERADA')
                    self._print(str(e))
                    self._print(traceback.format_exc())

            self._root.configure(cursor='arrow')
            self._root.title(TITLE)
            self._versiontxt.delete(0, 'end')
            self._info_slider.canv.yview_scroll(1000, 'units')
            self._root.update()

        self._root.title(TITLE_LOADING)
        self._root.configure(cursor='wait')
        self._root.update()
        self._root.after(400, _callback)


if __name__ == '__main__':
    CreateVersion().open()
