# coding=utf-8
"""
Administra archvos .zip, agrega directorios y carpetas.

Autor: PABLO PIZARRO @ github.com/ppizarror
Fecha: ABRIL 2017
Licencia: MIT
"""

# Importación de librerías
import zipfile
import os


# Importación de archivos
class ZipUtility(object):
    def __init__(self, filename):
        """
        Constructor, crea un archivo zipfile con un nombre
        :param filename: Nombre del archivo
        """

        if '.zip' not in filename:
            filename += '.zip'

        # Crea un objeto zipfile
        self.zip = zipfile.ZipFile(filename, 'w', zipfile.ZIP_DEFLATED)

    def save(self):
        """
        Guarda el archivo zip
        :return: 
        """
        self.zip.close()

    def add_file(self, ufile):
        """
        Añade un archivo al zip
        :param ufile: Ubicación del archivo
        :return: 
        """
        self.zip.write(ufile)

    def add_folder(self, folder):
        """
        Agrega una carpeta al archivo zip
        :param folder: Carpeta
        :return: 
        """
        for f in os.listdir(folder):
            full_path = os.path.join(folder, f)
            if os.path.isfile(full_path):
                self.add_file(full_path)
            elif os.path.isdir(full_path):
                self.add_folder(full_path)
