from hash import Hash
from datetime import datetime


class Articulo:
    # Clase que representa un artículo científco en el sistema
    def __init__(self, titulo, autores, año, contenido):
        # Inicializa un nuevo artículo
        self.hash = Hash()
        self.titulo = self.validar_titulo(titulo)
        self.autores = self.validar_autores(autores)
        self.año = self.validar_año(año)
        self.hash_contenido = self.hash.calcular_hash_fnv1(contenido)
        self.archivo = f"{self.hash_contenido}.txt"

    def validar_titulo(self, titulo):
        # Valida y limpia el título del artículo
        if not titulo or not titulo.strip():
            raise ValueError("El título no puede estar vacío.")
        return titulo.strip()

    def validar_autores(self, autores):
        # Valida y limpia la lista de autores
        if not autores or not autores.strip():
            raise ValueError("Debe especificar al menos un autor")
        return autores

    def validar_año(self, año):
        # Valida el año de publicación
        try:
            año_int = int(año)
            año_actual = datetime.now().year

            if año_int < 1800 or año_int > año_actual + 1:
                raise ValueError(f"El año debe estar entre 1800 y {año_actual + 1}")

            return año_int

        except (ValueError, TypeError):
            raise ValueError("El año debe ser un número válido")

    def actualizar_metadatos(self, titulo=None, autores=None, año=None):
        # Actualiza los datos del artículo
        if titulo is not None:
            self.titulo = self.validar_titulo(titulo)
        if autores is not None:
            self.autores = self.validar_autores(autores)
        if año is not None:
            self.año = self.validar_año(año)

    def convertir_a_string_db(self, separador="|"):
        # Convierte el artículo a string para almacenar en la base de datos
        return f"{self.hash_contenido}{separador}{self.titulo}{separador}{self.autores}{separador}{self.año}{separador}{self.archivo}"

    @classmethod
    def crear_desde_string_db(cls, linea_db, separador="|"):
        # Crea un artículo desde una línea de la base de datos
        try:
            partes = linea_db.strip().split(separador)

            articulo = cls.__new__(cls)
            articulo.hash_contenido = partes[0]
            articulo.titulo = partes[1]
            articulo.autores = partes[2]
            articulo.año = int(partes[3])
            articulo.archivo = partes[4]

            return articulo

        except Exception as e:
            raise ValueError(f"Error al parsear línea de base de datos: {str(e)}")

    def __str__(self):
        # Representación en string del artículo
        return f"Articulo: '{self.titulo}' publicado por: '{self.autores}' en el año: ({self.año})"
