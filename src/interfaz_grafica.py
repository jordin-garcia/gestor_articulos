import tkinter as tk
from tkinter import filedialog, messagebox
from controlador import GestorArticulos

## Main ##
root = tk.Tk()
root.title("Aplicación Gestión de Configuración de Usuario")
root.geometry("600x400")

#Presentacion
tk.Label(root, text=f"Bienvenido al programa", 
         font=("Arial", 16, "bold")).pack(pady=10)

#Crear barra de menú
menubar = tk.Menu(root, bg=config["color_menu"], fg=config["color_letra"])
root.config(menu = menubar)

#Archivo
archivo_menu = tk.Menu(menubar, tearoff=0)
archivo_menu.add_command(label = "Abrir (default)", command = accion_abrir)
archivo_menu.add_command(label = "Cargar desde archivo", command= cargar_archivo)
archivo_menu.add_command(label = "Guardar")
archivo_menu.add_command(label = "Guardar como", command = guardar_como)
menubar.add_cascade(label = "Archivo", menu = archivo_menu)

#Edición (simulado)
edicion_menu = tk.Menu(menubar, tearoff=0)
edicion_menu.add_command(label = "Copiar")
edicion_menu.add_command(label = "Pegar")
menubar.add_cascade(label="Edición", menu = edicion_menu)

#Ver (simulado)
ver_menu = tk.Menu(menubar, tearoff=0)
ver_menu.add_command(label="Zoom")
menubar.add_cascade(label="Ver", menu = ver_menu)

#Settings
settings_menu = tk.Menu(menubar, tearoff=0)
settings_menu.add_command(label="Ajustes", command = ventana_settings)
menubar.add_cascade(label="Settings", menu = settings_menu)

#Ejecutar la aplicación
root.mainloop()