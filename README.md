# gestor_articulos
Gestor de Artículos Científicos con Interfaz Gráfica y Tablas Hash

Integrantes

Andre Velasco — 1546124
Andres Mazariegos — 1535724
Jordin Garcia — 2427124
Rocio Caxaj — 2016523

Descripción (breve)
Desarrollar un gestor de artículos científicos que permita almacenar, buscar, listar y gestionar archivos asociados a artículos usando estructuras de datos (tabla hash) y una interfaz gráfica sencilla.

Objetivo general
Crear una aplicación en Python que integre tablas hash para el almacenamiento y recuperación rápida de metadatos de artículos, junto con una GUI para operaciones CRUD y manejo básico de archivos.

Objetivos específicos
Fomentar trabajo en equipo.
Reforzar conceptos de estructuras de datos (hash, índices secundarios).
Implementar hashing (FNV-1) y persistencia en texto plano.
Desarrollar una interfaz gráfica con tkinter para CRUD.
Sincronizar memoria y almacenamiento persistente.

Herramientas

Lenguaje: Python
Control de versiones: GitHub
Librerías: tkinter, os, hashlib (y librerías estándar)
Distribución del trabajo (resumida)

Jordin García — Estructura base y hash (src/hash.py, src/manejo_archivos.py, src/articulo.py).
Andrés — Tabla hash y persistencia (src/tabla_hash.py, src/base_datos.py).
Elizabeth (Rocio) — Interfaz gráfica (src/interfaz_grafica.py).
André — Integración, controlador y main (src/controlador.py, src/main.py).

Especificaciones técnicas (por archivo — resumen)

src/hash.py: Implementa FNV-1 (o FNV-1a). Función: calcular_hash_fnv1(contenido: bytes) -> int.
src/articulo.py: Clase Articulo con atributos hash, titulo, autores, anio, ruta_archivo. Métodos to_line() / from_line() para serializar.
src/manejo_archivos.py: Funciones para validar, guardar, eliminar y actualizar archivos físicos en data/archivos/ usando el hash como nombre.
src/tabla_hash.py: TablaHashEncadenamiento con operaciones insertar, buscar, eliminar y tamaño configurable (por defecto 101). Manejo simple de colisiones por encadenamiento.
src/base_datos.py: Lectura/escritura de articulos_db.txt, funciones cargar_db() y sincronizar() con backups y validaciones.
src/interfaz_grafica.py: GUI con tkinter: menú (Agregar, Listar, Buscar, Editar, Eliminar), formularios y listados. Validaciones de entrada.
src/controlador.py: Clase GestorArticulos que coordina tabla hash, base de datos y GUI. Implementa CRUD, índices secundarios (por autor / año) y manejo de duplicados.
src/main.py: Punto de entrada. Inicializa GestorArticulos, carga la DB y lanza la GUI. Parámetros configurables: tamaño de tabla y rutas de datos.
