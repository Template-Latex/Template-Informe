# coding=utf-8
"""
SOUND
Módulo que maneja eventos de sonidos.

Autor: PABLO PIZARRO @ github.com/ppizarror
Fecha: 2017
Licencia: MIT
"""

# Importación de librerías
import math
import winsound

# Constantes
DO = 65.406
DO_ = 69.296
RE = 73.416
RE_ = 77.782
MI = 82.407
FA = 87.307
FA_ = 92.499
SOL = 97.999
SOL_ = 103.826
LA = 110
LA_ = 116.541
SI = 123.471


# Sonidos
class Sound(object):
    """
    Crea y ejecuta sonidos.
    """

    def __init__(self):
        pass

    @staticmethod
    def _make(n, e):
        """
        Crea una nota musical <n> con un exponente <e>.

        :param n: Nota
        :param e: Exponente
        :return:
        """
        return int(math.ceil(n * pow(2, e)))

    def _play(self, n, e, t):
        """
        Reproduce una nota musical <n> en escala <e> y tiempo <t>.

        :param n: Nota
        :param e: Escala
        :param t: Tiempo
        :return:
        """
        self._triggersound(self._make(n, e), t)

    @staticmethod
    def alert():
        """
        Sonido de alerta
        :return:
        """
        winsound.MessageBeep(winsound.MB_OK)

    @staticmethod
    def _triggersound(freq, time):
        """
        Crea un sonido.

        :param freq: Frecuencia
        :param time: Tiempo
        :return:
        """
        winsound.Beep(freq, time)


if __name__ == '__main__':
    Sound().alert()
