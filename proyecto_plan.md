# Plan de Desarrollo - Gestor de Artículos Científicos

## División del Trabajo por Integrante

---

## 🔧 **PARTE 1 - Jordin: Estructura Base y Hash**

### Responsabilidades:

- Configurar el repositorio de GitHub
- Implementar la función de hash FNV-1
- Crear la estructura base del proyecto
- Implementar carga y guardado de archivos

### Tareas específicas:

1. **Configuración inicial del proyecto**

   - Crear repositorio en GitHub
   - Estructura de carpetas: `/src`, `/data`, `/docs`
   - Archivo `requirements.txt` (si es necesario)
   - README básico
2. **Implementación del algoritmo de hash**

   ```python
   def calcular_hash_fnv1(contenido):
       # Implementar FNV-1 hash
       pass
   ```
3. **Sistema de archivos**

   - Función para leer archivos .txt
   - Función para guardar archivos con nombre hash
   - Validación de formatos de archivo
4. **Estructura de datos básica**

   - Definir clase `Articulo`
   - Crear estructura básica del archivo principal

### Entregables:

- Repositorio configurado
- Módulo `hash.py`
- Módulo `manejo_archivos.py`
- Clase `Articulo` en `articulo.py`
- Pruebas básicas del hash

---

## 📊 **PARTE 2 - Andrés: Tabla Hash y Base de Datos**

### Responsabilidades:

- Implementar tabla hash con encadenamiento
- Sistema de base de datos persistente
- Carga inicial de datos en memoria

### Tareas específicas:

1. **Implementación de tabla hash**

   ```python
   class TablaHashEncadenamiento:
       def __init__(self, tamaño=101):
           # Implementar estructura
           pass

       def insertar(self, clave, valor):
           pass

       def buscar(self, clave):
           pass

       def eliminar(self, clave):
           pass
   ```
2. **Base de datos persistente**

   - Crear/leer archivo `articulos_db.txt`
   - Formato: `hash|título|autor|año|archivo`
   - Funciones de sincronización
3. **Sistema de carga inicial**

   - Cargar todos los registros al iniciar
   - Construir tabla hash en memoria
   - Validación de integridad de datos

### Entregables:

- Módulo `tabla_hash.py`
- Módulo `base_datos.py`
- Sistema de persistencia funcionando
- Pruebas de la tabla hash

---

## 🖥️ **PARTE 3 - Elizabeth: Interfaz Gráfica**

### Responsabilidades:

- Diseñar e implementar la interfaz gráfica con Tkinter
- Formularios de entrada de datos
- Menús y navegación

### Tareas específicas:

1. **Ventana principal**

   ```python
   class VentanaPrincipal:
       def __init__(self):
           # Configurar ventana principal
           pass
   ```
2. **Formularios de entrada**

   - Campos: título, autor(es), año
   - Botón para seleccionar archivo .txt
   - Validaciones de entrada
3. **Menús y opciones**

   - Menú principal con opciones
   - Ventanas secundarias para:
     - Listar artículos
     - Modificar datos
     - Eliminar artículos
4. **Interfaz de listados**

   - Lista por autor (alfabético)
   - Lista por título (alfabético)
   - Interfaz de búsqueda

### Entregables:

- Módulo `interfaz_grafica.py`
- Todas las ventanas y formularios
- Navegación entre ventanas
- Diseño intuitivo y funcional

---

## ⚙️ **PARTE 4 - André: Integración y Funcionalidades**

### Responsabilidades:

- Integrar todos los módulos
- Implementar lógica de negocio
- Funcionalidades adicionales y optimizaciones

### Tareas específicas:

1. **Controlador principal**

   ```python
   class GestorArticulos:
       def __init__(self):
           # Integrar todos los componentes
           pass
   ```
2. **Lógica de negocio**

   - Verificación de duplicados
   - Operaciones CRUD completas
   - Sincronización de cambios
3. **Funcionalidades adicionales**

   - Índices secundarios (por autor/año)
   - Búsquedas avanzadas
   - Filtros adicionales
4. **Finalización del proyecto**

   - Pruebas integrales
   - Documentación final
   - Refinamiento de la interfaz

### Entregables:

- Módulo `controlador.py`
- Archivo principal `main.py`
- Índices secundarios implementados
- Documentación completa

---

## 📅 **Cronograma Sugerido**

### Semana 1: Jordin

- Días 1-2: Configuración de GitHub y estructura
- Días 3-4: Implementación de hash FNV-1
- Días 5-7: Sistema de archivos y pruebas

### Semana 2: Andrés

- Días 1-3: Implementación tabla hash
- Días 4-5: Base de datos persistente
- Días 6-7: Sistema de carga y pruebas

### Semana 3: Elizabeth

- Días 1-2: Ventana principal y formularios
- Días 3-4: Menús y ventanas secundarias
- Días 5-7: Interfaces de listado y refinamiento

### Semana 4: André

- Días 1-2: Integración de módulos
- Días 3-4: Lógica de negocio completa
- Días 5-6: Funcionalidades adicionales
- Día 7: Pruebas finales y documentación

---

## 🔄 **Flujo de Trabajo en GitHub**

### Estrategia de Branches:

1. **main**: Código estable y funcional
2. **feature/hash-implementation** (Jordin)
3. **feature/database-hashtable** (Andrés)
4. **feature/gui-interface** (Elizabeth)
5. **feature/integration** (André)

### Proceso:

1. Cada integrante crea su branch desde `main`
2. Realiza commits frecuentes con mensajes descriptivos
3. Al terminar, hace Pull Request a `main`
4. Revisión por el equipo antes de merge
5. André integra todo en la fase final

---

## 📋 **Estructura Final del Proyecto**

```
proyecto-articulos/
├── src/
│   ├── articulo.py           # Clase Articulo (Jordin)
│   ├── hash.py               # Hash FNV-1 (Jordin)
│   ├── manejo_archivos.py    # Manejo archivos (Jordin)
│   ├── tabla_hash.py         # Tabla hash (Andrés)
│   ├── base_datos.py         # BD persistente (Andrés)
│   ├── interfaz_grafica.py   # Interfaz gráfica (Elizabeth)
│   ├── controlador.py        # Lógica integrada (André)
│   └── main.py               # Punto entrada (André)
├── data/
│   ├── articulos_db.txt   # Base de datos
│   └── archivos/          # Archivos .txt con hash
├── tests/                 # Pruebas unitarias
├── docs/                  # Documentación
├── requirements.txt       # Dependencias
└── README.md              # Documentación principal
```

---

## ✅ **Criterios de Aceptación**

Cada parte debe cumplir:

- Código documentado y comentado
- Funciones probadas individualmente
- Integración exitosa con partes anteriores
- Seguir estándares de Python (PEP 8)
- Commits descriptivos en GitHub

---

## 🎯 **Tips para el Éxito**

1. **Comunicación constante**: Usar WhatsApp/Discord para coordinación diaria
2. **Reuniones semanales**: Al final de cada fase para integración
3. **Documentación**: Cada función debe tener docstrings
4. **Pruebas**: Probar cada módulo antes de integrar
5. **Backup**: Commits frecuentes para evitar pérdida de trabajo

¡Este plan asegura que cada integrante contribuya equitativamente y el proyecto se desarrolle de manera ordenada!
