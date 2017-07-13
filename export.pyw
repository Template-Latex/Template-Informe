# coding=utf-8
"""
EXPORT
Exporta main.tex a informe.tex (template sin archivos externos).
Cambia versión y fecha a archivos.

Autor: PABLO PIZARRO @ github.com/ppizarror
Fecha: ABRIL-JULIO 2017
Licencia: MIT
"""

# Importación de librerías
from extlbx import *
from functools import partial
import json
import signal
import traceback

# Constantes
HELP = {
    'ESC': 'Cierra la aplicación',
    'F1': 'Muestra esta ayuda',
    'F2': 'Muestra las configuraciones',
    'F3': 'Muestra el acerca de',
    'F4': 'Limpia la ventana',
    'ENTER': 'Inicia la rutina'
}
LIMIT_MESSAGES_CONSOLE = 1000
TITLE = 'Export Template'
TITLE_LOADING = 'Export Template | Espere ...'

# Otros
__author__ = 'Pablo Pizarro R.'
__version__ = '1.1.0'


# noinspection PyCompatibility,PyBroadException,PyCallByClass,PyUnusedLocal
class CreateVersion(object):
    """
    Pide la versión al usuario y genera releases.
    """

    def __init__(self):

        def _checkver(sv):
            """
            Función auxiliar que chequea que la versión ingresada sea correcta.

            :param sv: String var de la versión
            :return:
            """
            ver = sv.get()
            try:
                mk_version(ver)
                self._startbutton.configure(state='normal', cursor='hand2')
                self._versiontxt.bind('<Return>', self._start)
            except:
                self._startbutton.configure(state='disabled', cursor='arrow')
                self._versiontxt.bind('<Return>')

        def _clear(*args):
            """
            Limpia la ventana.

            :param args: Argumentos opcionales
            :return:
            """
            self._clearconsole(-1)
            self._release.set('Seleccione template')
            self._versiontxt.delete(0, 'end')
            self._root.focus()

        def _kill(*args):
            """
            Destruye la ventana.

            :return:
            """

            # noinspection PyUnresolvedReferences
            def _oskill():
                if os.name is 'nt':
                    os.system('taskkill /PID {0} /F'.format(str(os.getpid())))
                else:
                    os.kill(os.getpid(), signal.SIGKILL)

            self._root.destroy()
            exit()

        def _printconfig(*args):
            """
            Imprime las configuraciones.

            :param args: Argumentos opcionales
            :return: None
            """
            self._clearconsole()
            self._print('CONFIGURACIONES')
            maxlen = 0
            key = self._configs.keys()
            key.sort(key=natural_keys)
            for j in key:
                if self._configs[j]['EVENT']:
                    maxlen = max(maxlen, len(j))
            for j in key:
                if self._configs[j]['EVENT']:
                    self._print('\t{0} [{1}]'.format(j.ljust(maxlen), self._getconfig(j)))

        def _scroll_console(event):
            """
            Función que atrapa el evento del scrolling y mueve los comandos.

            :param event: Evento
            :return: None
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

        def _set_config(paramname, paramvalue, *args):
            """
            Guarda la configuración.

            :param paramname: Nombre del parámetro
            :param paramvalue: Valor del parámetro
            :return:
            """
            if paramvalue is '!':
                self._configs[paramname]['VALUE'] = not self._configs[paramname]['VALUE']
            else:
                self._configs[paramname]['VALUE'] = paramvalue
            self._print('SE ESTABLECIO <{0}> EN {1}'.format(paramname, self._configs[paramname]['VALUE']))

        def _set_templatever(template_name, *args):
            """
            Establece el tipo de template en la lista.

            :param template_name: ID del template
            :return:
            """
            self._release.set(template_name)

        def _show_about(*args):
            """
            Imprime acerca de en consola.

            :param args: Argumentos opcionales
            :return: None
            """
            self._clearconsole(-1)
            self._print('ACERCA DE')
            self._print('\tExport Template v{0}'.format(__version__))
            self._print('\tAutor: {0}\n'.format(__author__))
            license = file_to_list(EXTLBX_LICENSE)
            for line in license:
                self._print(line, scrolldir=-1)

        def _show_help(*args):
            """
            Imprime la ayuda en consola.

            :param args: Argumentos opcionales
            :return: None
            """
            self._clearconsole(-1)
            self._print('AYUDA')
            keys = HELP.keys()
            keys.sort()
            for k in keys:
                self._print('\t{0}: {1}'.format(k, HELP[k]), scrolldir=-1)

        def _update_ver(*args):
            """
            Pasa el foco al campo de versión, carga versiones de cada release.

            :param args: Argumentos opcionales
            :return:
            """
            self._versiontxt.focus()
            self._versiontxt.delete(0, 'end')
            self._clearconsole()
            for j in RELEASES.keys():
                if self._release.get() == RELEASES[j]['NAME']:
                    self._versiontxt.configure(state='normal')
                    self._print('SELECCIONADO: {0}'.format(RELEASES[j]['NAME']))
                    self._print('ÚLTIMA VERSIÓN: {0}'.format(get_last_ver(RELEASES[j]['STATS']['FILE'])))
                    return

        self._root = Tk()
        self._root.protocol('WM_DELETE_WINDOW', _kill)
        self._sounds = Sound()

        # Se obtienen configuraciones
        with open(EXTLBX_CONFIGS) as json_data:
            d = json.load(json_data)
            self._configs = d

        # Ajusta tamaño ventana
        size = [self._configs['WINDOW_SIZE']['WIDTH'], self._configs['WINDOW_SIZE']['HEIGHT']]
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
        p = 1
        ky = RELEASES.keys()
        ky.sort()
        for b in ky:
            rels.append(RELEASES[b]['NAME'])
            self._root.bind('<Control-Key-{0}>'.format(p), partial(_set_templatever, RELEASES[b]['NAME']))
            p += 1
        self._release = StringVar(self._root)
        self._release.set('Seleccione template')
        w = apply(OptionMenu, (f1, self._release) + tuple(rels))
        w['width'] = 20
        w['relief'] = GROOVE
        w['anchor'] = W
        w['cursor'] = 'hand2'
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
        self._info = Label(self._info_slider.interior, text='', justify=LEFT, anchor=NW, bg='black', fg='white',
                           wraplength=self._configs['WINDOW_SIZE']['WIDTH'], font=fonts[0], relief=FLAT, border=2,
                           cursor='arrow')
        self._info.pack(anchor=NW, fill=BOTH)
        self._info_slider.scroller.pack_forget()
        self._console = []
        self._root.bind('<MouseWheel>', _scroll_console)
        self._cnextnl = False

        self._root.bind('<Escape>', _kill)

        # Eventos
        self._root.bind('<F1>', _show_help)
        self._root.bind('<F2>', _printconfig)
        self._root.bind('<F3>', _show_about)
        self._root.bind('<F4>', _clear)
        for i in self._configs.keys():
            if self._configs[i]['EVENT']:
                self._root.bind(self._configs[i]['KEY'], partial(_set_config, i, '!'))
                HELP[self._configs[i]['KEY'].replace('<', '').replace('>', '')] = 'Activa/Desactiva {0}'.format(i)

    def _clearconsole(self, scrolldir=1):
        """
        Limpia la consola.

        :param scrolldir: Dirección del scroll
        :return:
        """

        # noinspection PyShadowingNames
        def _slide(*args):
            """
            Mueve el scroll.

            :return: None
            """
            self._info_slider.canv.yview_scroll(1000 * scrolldir, 'units')

        self._console = []
        self._info.config(text='')
        self._root.after(10, _slide)

    def _getconfig(self, paramname):
        """
        Obtiene el valor de la configuración.

        :param paramname: Nombre del parámetro de la configuración
        :return:
        """
        return self._configs[paramname]['VALUE']

    def _print(self, msg, hour=False, end=None, scrolldir=1):
        """
        Imprime mensaje en consola.

        :param msg: Mensaje
        :param hour: Muestra la hora
        :param scrolldir: Dirección del scroll
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

        def _slide(*args):
            """
            Mueve el scroll.

            :return: None
            """
            self._info_slider.canv.yview_scroll(2000 * scrolldir, 'units')

        try:
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
            self._root.after(50, _slide)
        except:
            self._clearconsole()

    def execute(self):
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

        def _scroll():
            self._info_slider.canv.yview_scroll(1000, 'units')

        def _callback():
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
                        convert.export_informe(ver, versiondev, versionhash, printfun=self._print, doclean=True,
                                               dosave=self._getconfig('SAVE'), docompile=self._getconfig('COMPILE'),
                                               addstat=self._getconfig('SAVE_STAT'),
                                               plotstats=self._getconfig('PLOT_STAT'),
                                               savepdf=self._getconfig('SAVE_PDF'))
                    elif t == 2:
                        convert.export_auxiliares(ver, versiondev, versionhash, printfun=self._print,
                                                  dosave=self._getconfig('SAVE'), docompile=self._getconfig('COMPILE'),
                                                  addstat=self._getconfig('SAVE_STAT'),
                                                  plotstats=self._getconfig('PLOT_STAT'),
                                                  savepdf=self._getconfig('SAVE_PDF'))
                    elif t == 3:
                        convert.export_controles(ver, versiondev, versionhash, printfun=self._print,
                                                 dosave=self._getconfig('SAVE'), docompile=self._getconfig('COMPILE'),
                                                 addstat=self._getconfig('SAVE_STAT'),
                                                 plotstats=self._getconfig('PLOT_STAT'),
                                                 savepdf=self._getconfig('SAVE_PDF'))
                    else:
                        raise Exception('ERROR: ID INCORRECTO')
                except Exception as e:
                    tkMessageBox.showerror('Error fatal', 'Ocurrio un error inesperado al procesar la solicitud.')
                    self._print('ERROR: EXCEPCIÓN INESPERADA')
                    self._print(str(e))
                    self._print(traceback.format_exc())
                    self._sounds.alert()

                # Vuelve a cargar librerías
                reload_extlbx()

            self._root.configure(cursor='arrow')
            self._root.title(TITLE)
            self._versiontxt.delete(0, 'end')
            self._root.update()
            self._root.after(50, _scroll)
            return

        self._root.title(TITLE_LOADING)
        self._root.configure(cursor='wait')
        self._root.update()
        self._root.after(500, _callback)
        self._startbutton.configure(state='disabled')
        return


if __name__ == '__main__':
    CreateVersion().execute()
