from hash import Hash
import os


class ManejoArchivos:
    def leer_archivo_texto(self, ruta_archivo):
        # Lee el contenido completo de un archivo de texto
        try:
            with open(ruta_archivo, "r", encoding="utf-8") as archivo:
                contenido = archivo.read()
                return contenido

        except Exception as e:
            raise IOError(f"Error al leer el archivo {ruta_archivo}: {str(e)}")

    def guardar_archivo_con_hash(self, contenido, directorio_destino="data/archivos"):
        # Guarda un archivo con nombre basado en su hash
        hash = Hash()

        try:
            # Crear directorio si no existe
            os.makedirs(directorio_destino, exist_ok=True)

            # Generar hash y nombre de archivo
            hash_archivo = hash.calcular_hash_fnv1(contenido)
            nombre_archivo = f"{hash_archivo}.txt"
            ruta_completa = os.path.join(directorio_destino, nombre_archivo)

            # Guardar archivo
            with open(ruta_completa, "w", encoding="utf-8") as archivo:
                archivo.write(contenido)

            return hash_archivo, ruta_completa

        except Exception as e:
            raise IOError(f"Error al guardar archivo: {str(e)}")

    def eliminar_archivo_por_hash(self, hash_archivo, directorio="data/archivos"):
        # Elimina un archivo basándose en su hash
        try:
            nombre_archivo = f"{hash_archivo}.txt"
            ruta_archivo = os.path.join(directorio, nombre_archivo)

            if os.path.exists(ruta_archivo):
                os.remove(ruta_archivo)
                return True
            else:
                return False

        except Exception as e:
            raise IOError(f"Error al eliminar archivo: {str(e)}")
