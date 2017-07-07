# coding=utf-8
"""
VFRAME
Clase para usar el frame vertical.

Autor: http://tkinter.unpythonic.net/wiki/VerticalScrolledFrame
Fecha: 2017
Licencia: MIT
"""

# noinspection PyCompatibility
from Tkinter import Frame, Scrollbar, Canvas, NW, BOTH, TRUE, LEFT, RIGHT, VERTICAL, FALSE, Y


# noinspection PyUnusedLocal
class VerticalScrolledFrame(object, Frame):
    """
    Frame Vertical con Scroll
    """

    def __init__(self, parent, *args, **kw):
        Frame.__init__(self, parent, *args, **kw)
        vscrollbar = Scrollbar(self, orient=VERTICAL)
        vscrollbar.pack(fill=Y, side=RIGHT, expand=FALSE)
        canvas = Canvas(self, bd=0, highlightthickness=0,
                        yscrollcommand=vscrollbar.set)
        canvas.pack(side=LEFT, fill=BOTH, expand=TRUE)
        vscrollbar.config(command=canvas.yview)
        canvas.xview_moveto(0)
        canvas.yview_moveto(0)
        self.interior = interior = Frame(canvas)
        interior_id = canvas.create_window(0, 0, window=interior, anchor=NW)
        self.canv = canvas  # @UndefinedVariable
        self.scroller = vscrollbar

        def _configure_interior(event):
            size = (interior.winfo_reqwidth(), interior.winfo_reqheight())
            canvas.config(scrollregion="0 0 %s %s" % size)
            if interior.winfo_reqwidth() != canvas.winfo_width():
                canvas.config(width=interior.winfo_reqwidth())

        interior.bind('<Configure>', _configure_interior)

        def _configure_canvas(event):
            if interior.winfo_reqwidth() != canvas.winfo_width():
                canvas.itemconfigure(interior_id, width=canvas.winfo_width())

        canvas.bind('<Configure>', _configure_canvas)
