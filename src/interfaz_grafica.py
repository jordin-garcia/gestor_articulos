import tkinter as tk
from tkinter import ttk, messagebox, filedialog, scrolledtext
from controlador import GestorArticulos


class InterfazGrafica:
    def __init__(self):
        self.gestor = GestorArticulos()
        self.ventana_principal = tk.Tk()
        self.configurar_ventana()
        self.crear_widgets()

    def configurar_ventana(self):
        # Configura la ventana principal
        self.ventana_principal.title("Gestor de Artículos Científicos")
        self.ventana_principal.geometry("800x700")
        self.ventana_principal.resizable(True, True)

    def crear_widgets(self):
        # Crea todos los widgets de la interfaz

        # Frame principal
        frame_principal = ttk.Frame(self.ventana_principal, padding="10")
        frame_principal.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Configurar grid
        self.ventana_principal.columnconfigure(0, weight=1)
        self.ventana_principal.rowconfigure(0, weight=1)
        frame_principal.columnconfigure(1, weight=1)

        # Título
        ttk.Label(
            frame_principal,
            text="Gestor de Artículos Científicos",
            font=("Arial", 16, "bold"),
        ).grid(row=0, column=0, columnspan=3, pady=(0, 20))

        # Sección de agregar artículo
        self.crear_seccion_agregar(frame_principal)

        # Separador
        ttk.Separator(frame_principal, orient="horizontal").grid(
            row=2, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=20
        )

        # Sección de búsqueda
        self.crear_seccion_busqueda(frame_principal)

        # Separador
        ttk.Separator(frame_principal, orient="horizontal").grid(
            row=4, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=20
        )

        # Sección de listado
        self.crear_seccion_listado(frame_principal)

    def crear_seccion_agregar(self, parent):
        # Frame para agregar
        frame_agregar = ttk.LabelFrame(
            parent, text="Agregar Nuevo Artículo", padding="10"
        )
        frame_agregar.grid(
            row=1, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(0, 10)
        )
        frame_agregar.columnconfigure(1, weight=1)

        # Campos de entrada
        ttk.Label(frame_agregar, text="Título:").grid(
            row=0, column=0, sticky=tk.W, pady=2
        )
        self.entry_titulo = ttk.Entry(frame_agregar, width=50)
        self.entry_titulo.grid(
            row=0, column=1, sticky=(tk.W, tk.E), padx=(5, 0), pady=2
        )

        ttk.Label(frame_agregar, text="Autor(es):").grid(
            row=1, column=0, sticky=tk.W, pady=2
        )
        self.entry_autores = ttk.Entry(frame_agregar, width=50)
        self.entry_autores.grid(
            row=1, column=1, sticky=(tk.W, tk.E), padx=(5, 0), pady=2
        )

        ttk.Label(frame_agregar, text="Año:").grid(row=2, column=0, sticky=tk.W, pady=2)
        self.entry_año = ttk.Entry(frame_agregar, width=10)
        self.entry_año.grid(row=2, column=1, sticky=tk.W, padx=(5, 0), pady=2)

        ttk.Label(frame_agregar, text="Archivo:").grid(
            row=3, column=0, sticky=tk.W, pady=2
        )
        self.label_archivo = ttk.Label(
            frame_agregar, text="Ningún archivo seleccionado", foreground="gray"
        )
        self.label_archivo.grid(row=3, column=1, sticky=tk.W, padx=(5, 0), pady=2)

        # Botones
        ttk.Button(
            frame_agregar, text="Seleccionar Archivo", command=self.seleccionar_archivo
        ).grid(row=3, column=2, padx=(5, 0), pady=2)
        ttk.Button(
            frame_agregar, text="Agregar Artículo", command=self.agregar_articulo
        ).grid(row=4, column=1, pady=(10, 0))

        self.ruta_archivo = None

    def crear_seccion_busqueda(self, parent):
        frame_busqueda = ttk.LabelFrame(parent, text="Buscar Artículos", padding="10")
        frame_busqueda.grid(
            row=3, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(0, 10)
        )
        frame_busqueda.columnconfigure(1, weight=1)

        # Búsqueda por autor
        ttk.Label(frame_busqueda, text="Buscar por autor:").grid(
            row=0, column=0, sticky=tk.W, pady=2
        )
        self.entry_buscar_autor = ttk.Entry(frame_busqueda, width=30)
        self.entry_buscar_autor.grid(
            row=0, column=1, sticky=(tk.W, tk.E), padx=(5, 0), pady=2
        )
        ttk.Button(frame_busqueda, text="Buscar", command=self.buscar_por_autor).grid(
            row=0, column=2, padx=(5, 0), pady=2
        )

        # Búsqueda por año
        ttk.Label(frame_busqueda, text="Buscar por año:").grid(
            row=1, column=0, sticky=tk.W, pady=2
        )
        self.entry_buscar_año = ttk.Entry(frame_busqueda, width=10)
        self.entry_buscar_año.grid(row=1, column=1, sticky=tk.W, padx=(5, 0), pady=2)
        ttk.Button(frame_busqueda, text="Buscar", command=self.buscar_por_año).grid(
            row=1, column=2, padx=(5, 0), pady=2
        )

    def crear_seccion_listado(self, parent):
        frame_listado = ttk.LabelFrame(
            parent, text="Artículos en el Sistema", padding="10"
        )
        frame_listado.grid(
            row=5, column=0, columnspan=3, sticky=(tk.W, tk.E, tk.N, tk.S), pady=(0, 10)
        )
        frame_listado.columnconfigure(0, weight=1)
        frame_listado.rowconfigure(1, weight=1)
        parent.rowconfigure(5, weight=1)

        # Botones de acción
        frame_botones = ttk.Frame(frame_listado)
        frame_botones.grid(row=0, column=0, sticky=(tk.W, tk.E), pady=(0, 10))

        ttk.Button(frame_botones, text="Listar Todos", command=self.listar_todos).pack(
            side=tk.LEFT, padx=(0, 5)
        )
        ttk.Button(
            frame_botones, text="Ordenar por Título", command=self.ordenar_por_titulo
        ).pack(side=tk.LEFT, padx=(0, 5))
        ttk.Button(
            frame_botones, text="Ordenar por Autor", command=self.ordenar_por_autor
        ).pack(side=tk.LEFT, padx=(0, 5))
        ttk.Button(
            frame_botones, text="Ver Contenido", command=self.ver_contenido
        ).pack(side=tk.LEFT, padx=(0, 5))
        ttk.Button(
            frame_botones, text="Modificar", command=self.modificar_articulo
        ).pack(side=tk.LEFT, padx=(0, 5))
        ttk.Button(frame_botones, text="Eliminar", command=self.eliminar_articulo).pack(
            side=tk.LEFT, padx=(0, 5)
        )

        # Lista de artículos
        self.lista_articulos = ttk.Treeview(
            frame_listado, columns=("Hash", "Título", "Autor", "Año"), show="headings"
        )
        self.lista_articulos.heading("Hash", text="Hash")
        self.lista_articulos.heading("Título", text="Título")
        self.lista_articulos.heading("Autor", text="Autor(es)")
        self.lista_articulos.heading("Año", text="Año")

        self.lista_articulos.column("Hash", width=100)
        self.lista_articulos.column("Título", width=200)
        self.lista_articulos.column("Autor", width=150)
        self.lista_articulos.column("Año", width=80)

        # Scrollbar para la lista
        scrollbar = ttk.Scrollbar(
            frame_listado, orient=tk.VERTICAL, command=self.lista_articulos.yview
        )
        self.lista_articulos.configure(yscrollcommand=scrollbar.set)

        self.lista_articulos.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        scrollbar.grid(row=1, column=1, sticky=(tk.N, tk.S))

    def seleccionar_archivo(self):
        # Abre el diálogo para seleccionar archivo
        archivo = filedialog.askopenfilename(
            title="Seleccionar archivo de texto",
            filetypes=[("Archivos de texto", "*.txt")],
        )
        if archivo:
            self.ruta_archivo = archivo
            self.label_archivo.config(text=archivo.split("/")[-1], foreground="black")

    def agregar_articulo(self):
        # Agrega un nuevo artículo
        titulo = self.entry_titulo.get().strip()
        autores = self.entry_autores.get().strip()
        año = self.entry_año.get().strip()

        if not titulo or not autores or not año or not self.ruta_archivo:
            messagebox.showerror("Error", "Todos los campos son obligatorios")
            return

        try:
            resultado = self.gestor.agregar_articulo(
                titulo, autores, año, self.ruta_archivo
            )
            messagebox.showinfo("Resultado", resultado)

            # Limpiar campos
            self.entry_titulo.delete(0, tk.END)
            self.entry_autores.delete(0, tk.END)
            self.entry_año.delete(0, tk.END)
            self.label_archivo.config(
                text="Ningún archivo seleccionado", foreground="gray"
            )
            self.ruta_archivo = None

            # Actualizar lista
            self.listar_todos()

        except Exception as e:
            messagebox.showerror("Error", f"Error al agregar artículo: {str(e)}")

    def buscar_por_autor(self):
        autor = self.entry_buscar_autor.get().strip()
        if not autor:
            messagebox.showerror("Error", "Ingrese un autor para buscar")
            return

        articulos = self.gestor.buscar_por_autor(autor)
        self.mostrar_articulos(articulos)

    def buscar_por_año(self):
        año = self.entry_buscar_año.get().strip()
        if not año:
            messagebox.showerror("Error", "Ingrese un año para buscar")
            return

        try:
            año_int = int(año)
            articulos = self.gestor.buscar_por_año(año_int)
            self.mostrar_articulos(articulos)
        except ValueError:
            messagebox.showerror("Error", "El año debe ser un número válido")

    def listar_todos(self):
        # Lista todos los artículos
        articulos = self.gestor.listar_todos_articulos()
        self.mostrar_articulos(articulos)

    def ordenar_por_titulo(self):
        articulos = self.gestor.base_datos.ordenar_por_titulo()
        self.mostrar_articulos(articulos)

    def ordenar_por_autor(self):
        articulos = self.gestor.base_datos.ordenar_por_autor()
        self.mostrar_articulos(articulos)

    def mostrar_articulos(self, articulos):
        # Muestra artículos en la lista

        # Limpiar lista
        for item in self.lista_articulos.get_children():
            self.lista_articulos.delete(item)

        # Agregar artículos
        for articulo in articulos:
            self.lista_articulos.insert(
                "",
                tk.END,
                values=(
                    articulo.hash_contenido[:8],
                    articulo.titulo,
                    articulo.autores,
                    articulo.año,
                ),
            )

    def obtener_articulo_seleccionado(self):
        # Obtiene el artículo seleccionado en la lista
        seleccion = self.lista_articulos.selection()
        if not seleccion:
            return None

        # Obtener hash completo del artículo
        item = self.lista_articulos.item(seleccion[0])
        hash_corto = item["values"][0]

        # Buscar artículo con hash completo
        articulos = self.gestor.listar_todos_articulos()
        for articulo in articulos:
            if articulo.hash_contenido.startswith(hash_corto.replace("...", "")):
                return articulo

        return None

    def modificar_articulo(self):
        # Abre la ventana para modificar un artículo
        articulo = self.obtener_articulo_seleccionado()
        if not articulo:
            messagebox.showerror("Error", "Seleccione un artículo para modificar")
            return

        # Crear ventana de modificación
        ventana_modificar = tk.Toplevel(self.ventana_principal)
        ventana_modificar.title(f"Modificar: {articulo.titulo}")
        ventana_modificar.geometry("400x300")
        ventana_modificar.resizable(False, False)
        ventana_modificar.grab_set()  # Hacer ventana modal

        # Frame principal
        frame = ttk.Frame(ventana_modificar, padding="20")
        frame.pack(fill=tk.BOTH, expand=True)

        # Título (solo lectura)
        ttk.Label(
            frame, text="Título (no modificable):", font=("Arial", 10, "bold")
        ).pack(anchor=tk.W, pady=(0, 5))
        ttk.Label(frame, text=articulo.titulo, foreground="gray").pack(
            anchor=tk.W, pady=(0, 15)
        )

        # Autor (modificable)
        ttk.Label(frame, text="Autor(es):", font=("Arial", 10, "bold")).pack(
            anchor=tk.W, pady=(0, 5)
        )
        entry_autor = ttk.Entry(frame, width=50)
        entry_autor.pack(fill=tk.X, pady=(0, 15))
        entry_autor.insert(0, articulo.autores)

        # Año (modificable)
        ttk.Label(frame, text="Año:", font=("Arial", 10, "bold")).pack(
            anchor=tk.W, pady=(0, 5)
        )
        entry_año = ttk.Entry(frame, width=10)
        entry_año.pack(anchor=tk.W, pady=(0, 20))
        entry_año.insert(0, str(articulo.año))

        # Botones
        frame_botones = ttk.Frame(frame)
        frame_botones.pack(fill=tk.X, pady=(10, 0))

        def guardar_cambios():
            # Guarda los cambios realizados
            nuevo_autor = entry_autor.get().strip()
            nuevo_año = entry_año.get().strip()

            if not nuevo_autor or not nuevo_año:
                messagebox.showerror("Error", "Los campos autor y año son obligatorios")
                return

            try:
                año_int = int(nuevo_año)
                resultado = self.gestor.actualizar_articulo(
                    articulo.hash_contenido, autores=nuevo_autor, año=año_int
                )
                messagebox.showinfo("Resultado", resultado)
                ventana_modificar.destroy()
                self.listar_todos()  # Actualizar lista

            except ValueError:
                messagebox.showerror("Error", "El año debe ser un número válido")
            except Exception as e:
                messagebox.showerror("Error", f"Error al modificar artículo: {str(e)}")

        ttk.Button(frame_botones, text="Guardar Cambios", command=guardar_cambios).pack(
            side=tk.LEFT, padx=(0, 10)
        )
        ttk.Button(
            frame_botones, text="Cancelar", command=ventana_modificar.destroy
        ).pack(side=tk.LEFT)

    def ver_contenido(self):
        # Muestra el contenido de un artículo seleccionado
        articulo = self.obtener_articulo_seleccionado()
        if not articulo:
            messagebox.showerror("Error", "Seleccione un artículo")
            return

        # Mostrar contenido en ventana separada
        self.mostrar_ventana_contenido(articulo)

    def mostrar_ventana_contenido(self, articulo):
        # Muestra el contenido del artículo en una ventana separada
        ventana_contenido = tk.Toplevel(self.ventana_principal)
        ventana_contenido.title(f"Contenido: {articulo.titulo}")
        ventana_contenido.geometry("600x400")

        # Frame principal
        frame = ttk.Frame(ventana_contenido, padding="10")
        frame.pack(fill=tk.BOTH, expand=True)

        # Información del artículo
        info_frame = ttk.LabelFrame(frame, text="Información del Artículo", padding="5")
        info_frame.pack(fill=tk.X, pady=(0, 10))

        ttk.Label(info_frame, text=f"Título: {articulo.titulo}").pack(anchor=tk.W)
        ttk.Label(info_frame, text=f"Autor(es): {articulo.autores}").pack(anchor=tk.W)
        ttk.Label(info_frame, text=f"Año: {articulo.año}").pack(anchor=tk.W)
        ttk.Label(info_frame, text=f"Hash: {articulo.hash_contenido}").pack(anchor=tk.W)

        # Contenido
        contenido_frame = ttk.LabelFrame(
            frame, text="Contenido del Archivo", padding="5"
        )
        contenido_frame.pack(fill=tk.BOTH, expand=True)

        contenido_texto = scrolledtext.ScrolledText(contenido_frame, wrap=tk.WORD)
        contenido_texto.pack(fill=tk.BOTH, expand=True)

        # Cargar contenido
        contenido = self.gestor.obtener_contenido_archivo(articulo.hash_contenido)
        if contenido:
            contenido_texto.insert(tk.END, contenido)
        else:
            contenido_texto.insert(tk.END, "No se pudo cargar el contenido del archivo")

        contenido_texto.config(state=tk.DISABLED)

    def eliminar_articulo(self):
        articulo = self.obtener_articulo_seleccionado()
        if not articulo:
            messagebox.showerror("Error", "Seleccione un artículo para eliminar")
            return

        # Confirmar eliminación
        if not messagebox.askyesno(
            "Confirmar", "¿Está seguro de que desea eliminar este artículo?"
        ):
            return

        # Eliminar artículo
        resultado = self.gestor.eliminar_articulo(articulo.hash_contenido)
        messagebox.showinfo("Resultado", resultado)

        # Actualizar lista
        self.listar_todos()

    def ejecutar(self):
        # Inicia la aplicación
        self.ventana_principal.mainloop()
