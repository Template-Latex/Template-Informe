# coding=utf-8
"""
ZIP UTILS
Herramientas para el uso de archivos Zip.

Autor: PABLO PIZARRO @ github.com/ppizarror
Fecha: 2017
Licencia: MIT
"""

# Importación de librerías
import os
import zipfile


class Zip(object):
    """
    Clase para administrar archivos zip
    """

    def __init__(self, filename):
        """
        Constructor, crea un archivo zipfile con un nombre
        :param filename: Nombre del archivo
        """

        if '.zip' not in filename:
            filename += '.zip'

        # Crea un objeto zipfile
        self._zip = zipfile.ZipFile(filename, 'w', zipfile.ZIP_DEFLATED)

        # Lista de excepciones
        self._excptfiles = []

    def add_excepted_file(self, filename):
        """
        Agrega un archivo a la lista de excepciones

        :param filename: Nombre del archivo
        :type filename: str
        :return: None
        """
        self._excptfiles.append(filename)

    def _check_excepted_file(self, filename):
        """
        Indica si el archivo está dentro de la lista de excepciones

        :param filename: Nombre del archivo
        :type filename: str
        :return: Booleano
        :rtype: bool
        """
        filebasename = os.path.basename(filename)
        for f in self._excptfiles:
            if filebasename == f:
                return True
        return False

    def save(self):
        """
        Guarda el archivo zip

        :return: None
        """
        self._zip.close()

    def add_file(self, ufile):
        """
        Añade un archivo al zip

        :param ufile: Ubicación del archivo
        :type ufile: str
        :return: None
        """
        self._zip.write(ufile)

    def add_folder(self, folder):
        """
        Agrega una carpeta al archivo zip

        :param folder: Carpeta
        :type folder: str
        :return: None
        """
        for f in os.listdir(folder):
            full_path = os.path.join(folder, f)
            if os.path.isfile(full_path):
                if not self._check_excepted_file(full_path):
                    self.add_file(full_path)
            elif os.path.isdir(full_path):
                self.add_folder(full_path)
