import customtkinter as ctk
from PIL import Image, ImageTk
import tkinter as tk
import os
import sys
from main import *
from tkinter import messagebox, StringVar, DoubleVar
from tkinter import filedialog, messagebox



# Establecer el color del sistema
ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('green')


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

ventana_abierta = True


def Ventana_Principal():
    global root

    Empleado.cargar_empleados()
    Usuario.cargar_usuarios()

    root = ctk.CTk()
    root.geometry("600x440")
    root.title("Login")

    icon_path = resource_path("./imagenes\pokemon_go_play_game_cinema_film_movie_2_icon-icons.com_69159.ico")
    root.iconbitmap(icon_path)


    
    global entry1, entry2


    # Fondo
    img1_path = resource_path('imagenes/cinema-background-csjrmkuhfvvumb2q.jpg')
    img1 = ImageTk.PhotoImage(Image.open(img1_path))
    li = ctk.CTkLabel(master=root, image=img1)
    li.pack()

    
    # Cuadrado para las entradas
    frame = ctk.CTkFrame(master=li, width=320, height=360, corner_radius=15)
    frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    # Elementos de frame
    l2 = ctk.CTkLabel(master=frame, text="Iniciar Sesión", font=("Century Gothic", 20))
    l2.place(x=50, y=45)

    entry1 = ctk.CTkEntry(master=frame, width=220, placeholder_text="Usuario")
    entry1.place(x=50, y=110)

    entry2 = ctk.CTkEntry(master=frame, width=220, placeholder_text="Password", show="*")
    entry2.place(x=50, y=165)

    l2 = ctk.CTkLabel(master=frame, text="¿Olvidaste tu contraseña?", font=("Century Gothic", 10))
    l2.place(x=165, y=195)

    button1 = ctk.CTkButton(master=frame, width=220, text="Login", corner_radius=6, command=Login)
    button1.place(x=50, y=240)

    # Botón para registrarse
    button2 = ctk.CTkButton(master=frame, width=220, text="Registrar", corner_radius=6, command=Registro)
    button2.place(x=50, y=290)

    def cerrar_Ventana():
        global ventana_abierta  # Usar la variable global
        if ventana_abierta:  # Verifica si la ventana está abierta
            Empleado.guardar_empleados()
            Usuario.guardar_usuarios()
            ventana_abierta = False  # Cambia el estado de la ventana
            root.destroy()  # Cierra la ventana

    root.protocol("WM_DELETE_WINDOW", cerrar_Ventana)

    root.mainloop()



# ventana registro
def Registro():

    root.destroy()
    root4 = ctk.CTk()
    root4.geometry("600x440")
    root4.title("Registro")

    icon_path = resource_path("pokemon_go_play_game_cinema_film_movie_2_icon-icons.com_69159.ico")
    root4.iconbitmap(icon_path)

    
    global entry3, entry4, entry5

    # Fondo
    img_path = resource_path("./imagenes/77420df3f9e33db5b79ee25455d3340e.jpg" )
    img = Image.open(img_path)
    img = img.resize((2000, 1600), Image.LANCZOS)  
    img_tk = ImageTk.PhotoImage(img)

    f1 = ctk.CTkLabel(master=root4, image=img_tk)
    f1.place(relwidth=1, relheight=1)
    # Frame a la derecha
    frame2 = ctk.CTkFrame(master=f1, width=320, height=360, corner_radius=15)
    frame2.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    # Elementos de frame
    f2 = ctk.CTkLabel(master=frame2, text="Registro", font=("Century Gothic", 25))
    f2.place(x=50, y=35)

    entry3 = ctk.CTkEntry(master=frame2, width=220, placeholder_text="Nombre")
    entry3.place(x=50, y=100)

    entry4 = ctk.CTkEntry(master=frame2, width=220, placeholder_text="email")
    entry4.place(x=50, y=145)

    entry5 = ctk.CTkEntry(master=frame2, width=220, placeholder_text="password")
    entry5.place(x=50, y=190)

    button3 = ctk.CTkButton(master=frame2, width=220, text="Registrar", corner_radius=6, command=Boton_Registrar)
    button3.place(x=50, y=275)

    root4.protocol("WM_DELETE_WINDOW", lambda: (root4.destroy(), Ventana_Principal()))

    root4.mainloop()

# Agregar Funcion de Boton Registrar
def Boton_Registrar():
    nombre = entry3.get()
    email = entry4.get()
    password = entry5.get()
    Usuario.registrar(nombre, email, password)
    messagebox.showinfo("Registro", "Usuario registrado con exito")

#Funcion boton iniciar sesion
def Login():
    usuario = entry1.get()
    password = entry2.get()

    # Verificar si es empleado
    empleado_iniciar = Empleado.iniciar_sesion(usuario, password)
    print(f"Iniciando sesión como empleado: {empleado_iniciar}")  # Declaración para depuración
    if empleado_iniciar and empleado_iniciar.rol == "Empleado":
        root.destroy()
        Ventana_empleado()
        return

    # Verificar si es cliente
    cliente_iniciar = Usuario.iniciar_sesion(usuario, password)
    print(f"Iniciando sesión como cliente: {cliente_iniciar}")  # Declaración para depuración
    if cliente_iniciar and cliente_iniciar.rol == "Cliente":
        root.destroy()
        Ventana_cliente()
        return

    messagebox.showerror("Error", "Usuario o contraseña incorrecta")

# ventana empleados
def Ventana_empleado():
    global root2
    root2 = ctk.CTk()
    root2.geometry("800x600")
    root2.title("Empleado")

    icon_path = resource_path("imagenes\pokemon_go_play_game_cinema_film_movie_2_icon-icons.com_69159.ico")
    root2.iconbitmap(icon_path)


    # Cargar la imagen de fondo
    img_path = resource_path("./imagenes/fondods-de-la-ciudad-de-anime-estetica-0jgeoodxtcmwhw1z.jpg")
    img = Image.open(img_path)
    img = img.resize((800, 600), Image.LANCZOS)
    img_tk = ImageTk.PhotoImage(img)


    fondo = tk.Label(master=root2, image=img_tk)
    fondo.place(relwidth=1, relheight=1)
    fondo.lower()  # Mueve la imagen de fondo detrás de todos los demás widgets

    # Frame principal sin color de fondo para que la imagen sea visible
    main_frame = ctk.CTkFrame(master=root2, corner_radius=10)
    main_frame.place(relwidth=1, relheight=1)

    # Bienvenida
    bi = ctk.CTkLabel(master=main_frame, text="Bienvenido", font=("Century Gothic", 32, "bold"))
    bi.place(relx=0.5, rely=0.1, anchor="center")  # Centrar el texto

    # Frame para los botones
    botones_frame = ctk.CTkFrame(master=main_frame, corner_radius=10)
    botones_frame.place(relx=0.5, rely=0.5, anchor="center")

    # Botones
    btn_peliculas = ctk.CTkButton(master=botones_frame, text="Peliculas", command=lambda: abrir_ventana("Peliculas"), width=200, font=("Century Gothic", 16))
    btn_peliculas.grid(row=0, column=0, padx=10, pady=10) 

    btn_funcion = ctk.CTkButton(master=botones_frame, text="Funciones", command=lambda: abrir_ventana("Funciones"), width=200, font=("Century Gothic", 16))
    btn_funcion.grid(row=0, column=1, padx=10, pady=10)

    btn_menu = ctk.CTkButton(master=botones_frame, text="Menu", command=lambda: abrir_ventana("Menu"), width=200, font=("Century Gothic", 16))
    btn_menu.grid(row=1, column=0, padx=10, pady=10)

    btn_verUsuario = ctk.CTkButton(master=botones_frame, text="Ver Usuarios", command=lambda: abrir_ventana("Ver Usuario"), width=200, font=("Century Gothic", 16))
    btn_verUsuario.grid(row=1, column=1, padx=10, pady=10)

    btn_promo = ctk.CTkButton(master=botones_frame, text="Promociones", command=lambda: abrir_ventana("Promociones"), width=200, font=("Century Gothic", 16))
    btn_promo.grid(row=2, column=0, padx=10, pady=10)

    btn_sala = ctk.CTkButton(master=botones_frame, text="Salas", command=lambda: abrir_ventana("Salas"), width=200, font=("Century Gothic", 16))
    btn_sala.grid(row=2, column=1, padx=10, pady=10)

    btn_salir = ctk.CTkButton(master=botones_frame, text="Cerrar Sesión", command=lambda: abrir_ventana("salir"), width=200, font=("Century Gothic", 16))
    btn_salir.grid(row=3, column=0, padx=10, pady=10, columnspan=2)

    root2.image = img_tk

    root2.mainloop()


 

# selector para los botones de empleados
def abrir_ventana(opcion):
    root2.destroy()

    if opcion == "Peliculas":
        Peliculas()
    elif opcion == "Funciones":
        funciones()
    elif opcion == "Menu":
        Menu()
    elif opcion == "Ver Usuario":
        Ver_usuarios()
    elif opcion == "Promociones":
        promo()
    elif opcion == "Salas":
        sala()
    elif opcion == "salir":
        cerrar()

# ventana agregar peliculas
def Peliculas():
    root5 = ctk.CTk()
    root5.geometry("600x440")
    root5.title("Peliculas")

    icon_path = resource_path("imagenes\pokemon_go_play_game_cinema_film_movie_2_icon-icons.com_69159.ico")
    root5.iconbitmap(icon_path)

    

    # Cargar películas existentes al inicio
    Pelicula.cargar_peliculas()

    # Variables para almacenar datos de la película
    title_var = ctk.StringVar()
    duration_var = ctk.StringVar()
    rating_var = ctk.StringVar()
    image_path = ""  # Inicializar image_path

    # Función para cargar la imagen
    def load_image():
        nonlocal image_path
        image_path = filedialog.askopenfilename(title="Seleccionar Imagen", filetypes=[("Image Files", "*.jpg;*.jpeg;*.png")])
        if image_path:
            img = Image.open(image_path)
            img = img.resize((100, 100))  # Redimensionar la imagen
            img_tk = ImageTk.PhotoImage(img)
            image_label.configure(image=img_tk)
            image_label.image = img_tk  # Mantener una referencia a la imagen

    # Fondo
    fondo_path = resource_path("./imagenes/13242296.jpg")
    fondo = Image.open(fondo_path)
    fondo = fondo.resize((2000, 1900), Image.LANCZOS)
    fondo_img = ImageTk.PhotoImage(fondo)

    # Crear un Label para mostrar esta otra imagen de fondo
    fondo_label = ctk.CTkLabel(master=root5, image=fondo_img)
    fondo_label.place(relwidth=1, relheight=1)
    fondo_label.image = fondo_img 

    frame = ctk.CTkFrame(master=root5, width=320, height=440, corner_radius=15)
    frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    ti = ctk.CTkLabel(master=frame, text="Subir Pelicula", font=("Century Gothic", 14))
    ti.grid(row=0, column=0, columnspan=2, pady=(10, 20))

    # Etiquetas y Entradas
    label1 = ctk.CTkLabel(master=frame, text="Titulo")
    label1.grid(row=1, column=0, sticky="w", padx=10)
    entry6 = ctk.CTkEntry(master=frame, textvariable=title_var, width=220)
    entry6.grid(row=1, column=1, padx=10)

    label2 = ctk.CTkLabel(master=frame, text="Duración")
    label2.grid(row=2, column=0, sticky="w", padx=10)
    entry7 = ctk.CTkEntry(master=frame, textvariable=duration_var, width=220)
    entry7.grid(row=2, column=1, padx=10)

    label3 = ctk.CTkLabel(master=frame, text="Género")
    label3.grid(row=3, column=0, sticky="w", padx=10)
    entry8 = ctk.CTkEntry(master=frame, textvariable=rating_var, width=220)
    entry8.grid(row=3, column=1, padx=10)

    img_c = ctk.CTkButton(master=frame, text="Cargar Imagen", command=load_image, width=220)
    img_c.grid(row=4, column=0, columnspan=2, pady=(10, 10))

    image_label = ctk.CTkLabel(master=frame)
    image_label.grid(row=5, column=0, columnspan=2, pady=(10, 10))

    def add_movie():
        nonlocal image_path
        nombre = title_var.get()
        duracion = duration_var.get()
        genero = rating_var.get()
        
        # Validar que se haya seleccionado una imagen
        if not image_path:
            messagebox.showerror("Error", "Por favor, carga una imagen.")
            return
        
        # Crear una nueva película
        nueva_pelicula = Pelicula(nombre, duracion, genero, image_path)

        # Guardar las películas en el archivo JSON
        Pelicula.guardar_peliculas()
        
        # Mostrar mensaje de éxito
        messagebox.showinfo("Éxito", f"Pelicula '{nombre}' agregada exitosamente.")

        # Limpiar campos
        title_var.set("")
        duration_var.set("")
        rating_var.set("")
        image_path = ""  # Reiniciar image_path
        image_label.configure(image='')  # Limpiar la imagen

    ctk.CTkButton(master=frame, text="Agregar Película", command=add_movie).grid(row=6, column=0, columnspan=2, pady=(10, 10))

    fondo_label.image = fondo_img

    root5.protocol("WM_DELETE_WINDOW", lambda: (root5.destroy(), Ventana_empleado()))
    root5.mainloop()

# ventana agregar funciones 
def funciones():
    root6 = ctk.CTk()
    root6.geometry("800x600")
    root6.title("Crear y Administrar Función")


    icon_path = resource_path("imagenes\pokemon_go_play_game_cinema_film_movie_2_icon-icons.com_69159.ico")
    root6.iconbitmap(icon_path)

    # Cargar películas y salas
    Pelicula.cargar_peliculas()
    Sala.cargar_salas()
    Funcion.cargar_funciones()  # Cargar las funciones existentes
    peliculas = Pelicula.lista_peliculas
    salas = Sala.lista_salas

    # Verifica que las listas no estén vacías
    if not peliculas:
        messagebox.showerror("Error", "No se encontraron películas.")
        root6.destroy()
        return
    if not salas:
        messagebox.showerror("Error", "No se encontraron salas.")
        root6.destroy()
        return

    # Variables para almacenar datos
    horario_var = StringVar()

    # Frame para crear funciones
    create_frame = ctk.CTkFrame(master=root6, width=400, height=250, corner_radius=10)
    create_frame.pack(pady=20, padx=20, fill="both", expand=True)

    # Etiqueta y ComboBox para seleccionar película
    ctk.CTkLabel(master=create_frame, text="Seleccionar Película", font=("Arial", 16)).pack(pady=10)
    pelicula_combobox = ctk.CTkComboBox(master=create_frame, values=[pelicula.nombre for pelicula in peliculas], width=250)
    pelicula_combobox.pack(pady=10)

    # Etiqueta y ComboBox para seleccionar sala
    ctk.CTkLabel(master=create_frame, text="Seleccionar Sala", font=("Arial", 16)).pack(pady=10)
    sala_combobox = ctk.CTkComboBox(master=create_frame, values=[sala.identificador for sala in salas], width=250)
    sala_combobox.pack(pady=10)

    # Etiqueta y Entry para ingresar horario
    ctk.CTkLabel(master=create_frame, text="Ingresar Horario", font=("Arial", 16)).pack(pady=10)
    entry_horario = ctk.CTkEntry(master=create_frame, textvariable=horario_var, width=250)
    entry_horario.pack(pady=10)

    def agregar_funcion():
        pelicula_titulo = pelicula_combobox.get()  # Obtener el valor seleccionado del combo box
        sala_id = sala_combobox.get()  # Obtener el valor seleccionado del combo box
        horario = horario_var.get()

        if not pelicula_titulo or not sala_id or not horario:
            messagebox.showerror("Error", "Por favor completa todos los campos")
            return

        # Buscar la película y la sala en las listas
        pelicula = next((p for p in peliculas if p.nombre == pelicula_titulo), None)
        sala = next((s for s in salas if s.identificador == sala_id), None)
        
        if pelicula is None:
            messagebox.showerror("Error", "Película no encontrada")
            return
        if sala is None:
            messagebox.showerror("Error", "Sala no encontrada")
            return

        nueva_funcion = Funcion(pelicula, sala, horario)
        Funcion.guardar_funciones()  # Guardar funciones en el archivo JSON

        messagebox.showinfo("Éxito", f"Función para '{pelicula_titulo}' creada exitosamente")

        # Limpiar los campos después de agregar la función
        pelicula_combobox.set("")  # Limpiar el combo box
        sala_combobox.set("")  # Limpiar el combo box
        horario_var.set("")

        # Actualizar la lista de funciones
        actualizar_lista_funciones()

    def eliminar_funcion(funcion):
        Funcion.lista_funciones.remove(funcion)  # Cambiar a la lista de la clase
        Funcion.guardar_funciones()
        messagebox.showinfo("Éxito", f"Función eliminada exitosamente")
        actualizar_lista_funciones()

    def actualizar_lista_funciones():
        for widget in funciones_frame.winfo_children():
            widget.destroy()

        for funcion in Funcion.lista_funciones:  # Cambiar a la lista de la clase
            funcion_frame = ctk.CTkFrame(master=funciones_frame, corner_radius=10)
            funcion_frame.pack(pady=5, padx=5, fill="x", expand=True)

            funcion_label = ctk.CTkLabel(master=funcion_frame, text=f"Película: {funcion.pelicula.nombre}, Sala: {funcion.sala.identificador}, Horario: {funcion.horario}", anchor="w")
            funcion_label.pack(side="left", padx=10, pady=5)

            eliminar_boton = ctk.CTkButton(master=funcion_frame, text="Eliminar", command=lambda f=funcion: eliminar_funcion(f), width=80)
            eliminar_boton.pack(side="right", padx=10, pady=5)

    # Botón para crear la función
    ctk.CTkButton(master=create_frame, text="Crear Función", command=agregar_funcion).pack(pady=20)

    # Etiqueta para la lista de funciones
    ctk.CTkLabel(master=root6, text="Lista de Funciones", font=("Arial", 20)).pack(pady=10)

    # Frame para la lista de funciones
    funciones_frame = ctk.CTkFrame(master=root6, corner_radius=10)
    funciones_frame.pack(pady=10, padx=20, fill="both", expand=True)

    # Inicializar la lista de funciones
    actualizar_lista_funciones()

    root6.protocol("WM_DELETE_WINDOW", lambda: (root6.destroy(), Ventana_empleado()))

    root6.mainloop()

# ventana de menu
def Menu():
    root8 = ctk.CTk()
    root8.geometry("600x440")
    root8.title("Administrar Zona de Comida")

    icon_path = resource_path("imagenes\pokemon_go_play_game_cinema_film_movie_2_icon-icons.com_69159.ico")
    root8.iconbitmap(icon_path)
    
    # Variables para almacenar datos
    producto_var = StringVar()
    precio_var = DoubleVar()

    # Etiqueta y Entry para ingresar producto
    ctk.CTkLabel(master=root8, text="Producto").pack(pady=(10, 0))
    entry_producto = ctk.CTkEntry(master=root8, textvariable=producto_var)
    entry_producto.pack(pady=(0, 10))

    # Etiqueta y Entry para ingresar precio
    ctk.CTkLabel(master=root8, text="Precio").pack(pady=(10, 0))
    entry_precio = ctk.CTkEntry(master=root8, textvariable=precio_var)
    entry_precio.pack(pady=(0, 10))

    def agregar_producto():
        nombre = producto_var.get()
        try:
            precio = float(precio_var.get())
        except ValueError:
            messagebox.showerror("Error", "Por favor ingresa un precio válido")
            return

        if not nombre or precio <= 0:
            messagebox.showerror("Error", "Por favor ingresa un nombre válido y un precio mayor a 0")
            return

        zona_comida.agregar_producto(nombre, precio)
        messagebox.showinfo("Éxito", f"Producto '{nombre}' agregado exitosamente")

        # Limpiar los campos después de agregar el producto
        producto_var.set("")
        precio_var.set(0.0)

    def eliminar_producto():
        nombre = producto_var.get()
        if not nombre:
            messagebox.showerror("Error", "Por favor ingresa el nombre del producto")
            return

        zona_comida.eliminar_producto(nombre)
        messagebox.showinfo("Éxito", f"Producto '{nombre}' eliminado exitosamente")

        # Limpiar el campo después de eliminar el producto
        producto_var.set("")

    def mostrar_menu():
        menu = zona_comida.mostrar_menu()
        menu_str = "\n".join(menu)
        messagebox.showinfo("Menú", f"Menú actual:\n{menu_str}")

    # Botones para agregar, eliminar y mostrar productos
    ctk.CTkButton(master=root8, text="Agregar Producto", command=agregar_producto).pack(pady=(10, 0))
    ctk.CTkButton(master=root8, text="Eliminar Producto", command=eliminar_producto).pack(pady=(10, 0))
    ctk.CTkButton(master=root8, text="Mostrar Menú", command=mostrar_menu).pack(pady=(10, 0))

    root8.protocol("WM_DELETE_WINDOW", lambda: (root8.destroy(), Ventana_empleado()))

    root8.mainloop()

# ventana para ver la lista de usuarios registrados en el sistema
def Ver_usuarios():
    root9 = ctk.CTk()
    root9.geometry("600x440")
    root9.title("Lista de Usuarios")

    icon_path = resource_path("imagenes\pokemon_go_play_game_cinema_film_movie_2_icon-icons.com_69159.ico")
    root9.iconbitmap(icon_path)
    
    # Cargar usuarios
    Usuario.cargar_usuarios()

    # Frame principal
    main_frame = ctk.CTkFrame(master=root9, corner_radius=10)
    main_frame.place(relwidth=1, relheight=1)

    # Título
    titulo = ctk.CTkLabel(master=main_frame, text="Usuarios Registrados", font=("Century Gothic", 24, "bold"))
    titulo.pack(pady=20)

    # Frame para la lista de usuarios con scroll
    scroll_frame = ctk.CTkScrollableFrame(master=main_frame, width=560, height=300, corner_radius=10)
    scroll_frame.pack(pady=10)

    # Añadir usuarios a la lista
    for usuario in Usuario.lista_usuarios:
        usuario_label = ctk.CTkLabel(master=scroll_frame, text=f"Nombre: {usuario.name}, Email: {usuario.email}", font=("Century Gothic", 18))
        usuario_label.pack(pady=5)


    root9.protocol("WM_DELETE_WINDOW", lambda: (root9.destroy(), Ventana_empleado()))

    root9.mainloop()

# ventana de promociones
def promo():
    Promocion.cargar_promociones()  # Cargar promociones desde el archivo
    promociones = Promocion.promociones  # Obtener la lista de promociones cargadas

    # Ventana principal
    rootp = ctk.CTk()
    rootp.geometry("600x500")
    rootp.title("Gestión de Promociones")

    icon_path = resource_path("imagenes\pokemon_go_play_game_cinema_film_movie_2_icon-icons.com_69159.ico")
    rootp.iconbitmap(icon_path)
    
    # Frame principal
    main_frame = ctk.CTkFrame(master=rootp, corner_radius=10)
    main_frame.place(relwidth=1, relheight=1)

    # Título
    titulo_label = ctk.CTkLabel(master=main_frame, text="Gestión de Promociones", font=("Century Gothic", 24, "bold"))
    titulo_label.pack(pady=20)

    # Frame para la lista de promociones con scroll
    scroll_frame = ctk.CTkScrollableFrame(master=main_frame, width=560, height=300, corner_radius=10)
    scroll_frame.pack(pady=10)

    # Frame para agregar nueva promoción
    agregar_frame = ctk.CTkFrame(master=main_frame, corner_radius=10)
    agregar_frame.pack(pady=20, padx=10, fill="x")

    nuevo_nombre_label = ctk.CTkLabel(master=agregar_frame, text="Nombre de la Promoción", font=("Century Gothic", 16))
    nuevo_nombre_label.pack(anchor="w", padx=10, pady=5)

    nuevo_nombre_entry = ctk.CTkEntry(master=agregar_frame, width=400)
    nuevo_nombre_entry.pack(anchor="w", padx=10, pady=5)

    nuevo_descuento_label = ctk.CTkLabel(master=agregar_frame, text="Descuento (%)", font=("Century Gothic", 16))
    nuevo_descuento_label.pack(anchor="w", padx=10, pady=5)

    nuevo_descuento_entry = ctk.CTkEntry(master=agregar_frame, width=400)
    nuevo_descuento_entry.pack(anchor="w", padx=10, pady=5)

    def mostrar_promociones():
        for widget in scroll_frame.winfo_children():
            widget.destroy()
        for promo in promociones:
            promo_frame = ctk.CTkFrame(master=scroll_frame, corner_radius=10)
            promo_frame.pack(pady=5, padx=10, fill="x")

            promo_titulo_label = ctk.CTkLabel(master=promo_frame, text=promo.nombre, font=("Century Gothic", 18, "bold"))
            promo_titulo_label.pack(anchor="w", padx=10, pady=5)

            promo_descuento_label = ctk.CTkLabel(master=promo_frame, text=f"Descuento: {promo.descuento}%", font=("Century Gothic", 16))
            promo_descuento_label.pack(anchor="w", padx=10, pady=5)

            eliminar_button = ctk.CTkButton(master=promo_frame, text="Eliminar", command=lambda p=promo: eliminar_promocion(p))
            eliminar_button.pack(anchor="e", padx=10, pady=5)

    def agregar_promocion():
        nombre = nuevo_nombre_entry.get()
        descuento = nuevo_descuento_entry.get()
        if nombre and descuento:
            try:
                descuento = float(descuento)
                nueva_promo = Promocion(nombre, descuento)
                nuevo_nombre_entry.delete(0, 'end')
                nuevo_descuento_entry.delete(0, 'end')
                # Guardar promociones
                Promocion.guardar_promociones()  # Guardar promociones en el archivo
                # Actualizar la lista de promociones
                mostrar_promociones()
            except ValueError:
                print("El descuento debe ser un número válido.")

    def eliminar_promocion(promocion):
        promociones.remove(promocion)
        Promocion.guardar_promociones()  # Guardar promociones en el archivo
        mostrar_promociones()

    agregar_button = ctk.CTkButton(master=agregar_frame, text="Agregar Promoción", command=agregar_promocion)
    agregar_button.pack(pady=10)

    mostrar_promociones()

    rootp.protocol("WM_DELETE_WINDOW", lambda: (rootp.destroy(), Ventana_empleado()))
    rootp.mainloop()

# ventana crear salas
def sala():
    root7 = ctk.CTk()
    root7.geometry("600x440")
    root7.title("Salas")

    icon_path = resource_path("imagenes\pokemon_go_play_game_cinema_film_movie_2_icon-icons.com_69159.ico")
    root7.iconbitmap(icon_path)

    
    # Cargar y redimensionar la imagen
    img_path = resource_path("./imagenes/sala.jpg")
    fondo = Image.open(img_path)
    fondo = fondo.resize((2000, 1800), Image.LANCZOS)  # Ajustar el tamaño a la ventana
    imagentk = ImageTk.PhotoImage(fondo)  # Usar PhotoImage en lugar de BitmapImage

    # Crear un Label para mostrar la imagen de fondo
    fondo_label = ctk.CTkLabel(master=root7, image=imagentk)
    fondo_label.place(relwidth=1, relheight=1)
    fondo_label.image = imagentk

    tamaño = ctk.StringVar()
    identificador = ctk.StringVar()
    capacidad = ctk.StringVar()

    frame = ctk.CTkFrame(master=root7, width=320, height=360, corner_radius=15)  
    frame.place(relx=0.5, rely=0.5, anchor="center") 

    ctk.CTkLabel(master=frame, text="Agregar Sala", font=("Arial", 18)).pack(pady=(10, 0))

    ctk.CTkLabel(master=frame, text="Tamaño").pack(pady=(10, 0))
    entry_t = ctk.CTkEntry(master=frame, textvariable=tamaño)
    entry_t.pack(pady=(0, 10))

    ctk.CTkLabel(master=frame, text="Identificador").pack(pady=(10, 0))
    entry_I = ctk.CTkEntry(master=frame, textvariable=identificador)
    entry_I.pack(pady=(0, 10))

    ctk.CTkLabel(master=frame, text="Capacidad").pack(pady=(10, 0))
    entry_ta = ctk.CTkEntry(master=frame, textvariable=capacidad)
    entry_ta.pack(pady=(0, 10))

    def agregar_sala():
        Tamaño = tamaño.get()
        Identificador = identificador.get()
        Capacidad = capacidad.get()

        # Validar que los campos no estén vacíos
        if not Tamaño or not Identificador or not Capacidad:
            messagebox.showerror("Error", "Por favor completa todos los campos")
            return
        
        try:
            Capacidad = int(Capacidad)  # Convertir capacidad a entero
        except ValueError:
            messagebox.showerror("Error", "La capacidad debe ser un número entero.")
            return

        nueva_sala = Sala(Tamaño, Identificador, Capacidad)

        Sala.guardar_salas()

        messagebox.showinfo("Éxito", f"Sala {Identificador} agregada exitosamente")

        tamaño.set("")
        identificador.set("")
        capacidad.set("")

    ctk.CTkButton(master=frame, text="Guardar", command=agregar_sala).pack(pady=(20, 10))


    # Mantener una referencia a la imagen
    fondo_label.image = imagentk

    root7.protocol("WM_DELETE_WINDOW", lambda: (root7.destroy(), Ventana_empleado()))
    root7.mainloop()

# cerrar sesion
def cerrar():
    Empleado.guardar_empleados()
    Usuario.guardar_usuarios()
    # Asegúrate de que los datos se limpien o se verifiquen antes de guardar
    Ventana_Principal()
# Inicio Cliente



def Ventana_cliente():
    global root3
    root3 = ctk.CTk()
    root3.geometry("800x600")
    root3.title("Cliente")

    icon_path = resource_path("imagenes\pokemon_go_play_game_cinema_film_movie_2_icon-icons.com_69159.ico")
    root3.iconbitmap(icon_path)

    
    # Establecer un color de fondo
    root3.configure(bg='lightblue')

    img_path = resource_path("./imagenes/cliente.jpg")
    img3 = Image.open(img_path)
    img3 = img3.resize((1800, 1200), Image.LANCZOS)
    img3_tk = ImageTk.PhotoImage(img3)

    # Crear un Label para mostrar la imagen de fondo
    fondo = ctk.CTkLabel(master=root3, image=img3_tk)
    fondo.place(relwidth=1, relheight=1)
    fondo.image = img3_tk 

    # Crear un marco para la barra de navegación
    nav_frame = ctk.CTkFrame(master=root3, width=200, corner_radius=0, fg_color='gray')
    nav_frame.place(relx=0, rely=0, relheight=1)

    # Botones de navegación
    btn_cartelera = ctk.CTkButton(master=nav_frame, text="Cartelera", command=lambda: abrir_ventana_c("Cartelera"))
    btn_cartelera.pack(pady=10, padx=10, fill='x')

    btn_menu = ctk.CTkButton(master=nav_frame, text="Menu", command=lambda: abrir_ventana_c("Menu"))
    btn_menu.pack(pady=10, padx=10, fill='x')

    btn_reserva = ctk.CTkButton(master=nav_frame, text="Reserva", command=lambda: abrir_ventana_c("Reserva"))
    btn_reserva.pack(pady=10, padx=10, fill='x')

    btn_reserva_ver = ctk.CTkButton(master=nav_frame, text="Mis Reservas", command=lambda: abrir_ventana_c("Mis Reservas"))
    btn_reserva_ver.pack(pady=10, padx=10, fill='x')

    btn_cerrar_sesion = ctk.CTkButton(master=nav_frame, text="Cerrar Sesión", command=lambda: abrir_ventana_c("Cerrar"))
    btn_cerrar_sesion.pack(pady=10, padx=10, fill='x')

    # Agregar un mensaje de bienvenida
    welcome_label = ctk.CTkLabel(master=root3, text="¡Bienvenido! ¿Cómo estás hoy?", font=("Courier New", 24), fg_color='black')
    welcome_label.place(relx=0.5, rely=0.40, anchor=tk.CENTER)  # Centrar el mensaje en la parte superior

    root3.image = img3_tk

    root3.mainloop()

# Cartelera
def mostrar_peliculas():
    # Cargar películas desde el archivo JSON
    Pelicula.cargar_peliculas()

    # Crear una nueva ventana
    ventana_peliculas = ctk.CTk()
    ventana_peliculas.geometry("800x600")
    ventana_peliculas.title("Lista de Películas")

    icon_path = resource_path("imagenes\pokemon_go_play_game_cinema_film_movie_2_icon-icons.com_69159.ico")
    ventana_peliculas.iconbitmap(icon_path)

    
    # Crear un marco para mostrar las películas
    peliculas_frame = ctk.CTkFrame(master=ventana_peliculas)
    peliculas_frame.pack(pady=20, padx=20, fill='both', expand=True)

    # Crear un Label para mostrar la información de la película
    info_label = ctk.CTkLabel(master=ventana_peliculas, text="", font=("Arial", 16))
    info_label.pack(pady=10)

    # Crear un Label para mostrar la imagen de la película
    image_label = ctk.CTkLabel(master=ventana_peliculas)
    image_label.pack(pady=10)


    # Función para mostrar la información de la película seleccionada
    def mostrar_info(pelicula):
        info_text = f"Nombre: {pelicula.nombre}\nDuración: {pelicula.duracion}\nGénero: {pelicula.genero}"
        info_label.configure(text=info_text)

        # Cargar la imagen de la película
        img_path = pelicula.imagen
        if os.path.exists(img_path):
            img = Image.open(img_path)
            img = img.resize((100, 150), Image.LANCZOS)  # Ajustar el tamaño de la imagen
            img_tk = ImageTk.PhotoImage(img)
            image_label.configure(image=img_tk)
            image_label.image = img_tk  # Mantener una referencia a la imagen
        else:
            messagebox.showerror("Error", "La imagen no existe.")
         

    # Agregar botones para cada película
    for pelicula in Pelicula.lista_peliculas:
        button = ctk.CTkButton(master=peliculas_frame, text=pelicula.nombre, command=lambda p=pelicula: mostrar_info(p))
        button.pack(pady=5, fill='x')



    ventana_peliculas.protocol("WM_DELETE_WINDOW", lambda: (ventana_peliculas.destroy(), Ventana_cliente()))
    ventana_peliculas.mainloop()

# Mostrar Menu
def mostrar_menu_zona_comida():
    # Crear una nueva ventana para mostrar el menú
    ventana_menu = ctk.CTk()
    ventana_menu.geometry("400x400")
    ventana_menu.title("Menú de la Zona de Comida")

    
    icon_path = resource_path("imagenes\pokemon_go_play_game_cinema_film_movie_2_icon-icons.com_69159.ico")
    ventana_menu.iconbitmap(icon_path)


    # Crear un marco para el menú
    menu_frame = ctk.CTkFrame(master=ventana_menu)
    menu_frame.pack(pady=20, padx=20, fill='both', expand=True)

    # Título del menú
    title_label = ctk.CTkLabel(master=menu_frame, text="Menú de la Zona de Comida", font=("Arial", 18, "bold"))
    title_label.pack(pady=10)

    # Mostrar los productos del menú
    for producto in zona_comida.menu:
        producto_label = ctk.CTkLabel(master=menu_frame, text=f"{producto['nombre']} - ${producto['precio']}", font=("Arial", 14))
        producto_label.pack(pady=5)

    ventana_menu.protocol("WM_DELETE_WINDOW", lambda: (ventana_menu.destroy(), Ventana_cliente()))

    ventana_menu.mainloop()


# reservar

# Función para cargar datos desde un archivo JSON
def cargar_datos_desde_json(ruta_archivo):
    if os.path.exists(ruta_archivo):
        with open(ruta_archivo, "r") as file:
            return json.load(file)
    return []

# Función para guardar datos en un archivo JSON
def guardar_datos_en_json(ruta_archivo, datos):
    with open(ruta_archivo, "w") as file:
        json.dump(datos, file, indent=4)


class Reservar_v(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Reservas de Cine")
        self.geometry("600x600")

        icon_path = resource_path("imagenes\pokemon_go_play_game_cinema_film_movie_2_icon-icons.com_69159.ico")
        self.iconbitmap(icon_path)

        self.label_usuario = ctk.CTkLabel(self, text="Usuario")
        self.label_usuario.pack(pady=10)

        self.entry_usuario = ctk.CTkEntry(self)
        self.entry_usuario.pack(pady=10)

        self.label_funcion = ctk.CTkLabel(self, text="Función")
        self.label_funcion.pack(pady=10)

        funciones = cargar_datos_desde_json(FUNCIONES_JSON)
        self.funciones_disponibles = [f"{funcion['pelicula']} - {funcion['sala']} - {funcion['horario']}" for funcion in funciones]
        self.optionmenu_funcion = ctk.CTkOptionMenu(self, values=self.funciones_disponibles, command=self.visualizar_asientos)
        self.optionmenu_funcion.pack(pady=10)

        self.label_asientos = ctk.CTkLabel(self, text="Asientos Disponibles")
        self.label_asientos.pack(pady=10)

        self.frame_asientos = ctk.CTkFrame(self)
        self.frame_asientos.pack(pady=10)

        self.asientos_widgets = {}

        self.label_promocion = ctk.CTkLabel(self, text="Promoción")
        self.label_promocion.pack(pady=10)

        Promocion.cargar_promociones()
        self.promociones_disponibles = [promocion.nombre for promocion in Promocion.promociones]
        self.optionmenu_promocion = ctk.CTkOptionMenu(self, values=self.promociones_disponibles)
        self.optionmenu_promocion.pack(pady=10)

        self.button_reservar = ctk.CTkButton(self, text="Reservar", command=self.reservar)
        self.button_reservar.pack(pady=20)

        self.protocol("WM_DELETE_WINDOW", self.on_close)

    def visualizar_asientos(self, _=None):
        for widget in self.frame_asientos.winfo_children():
            widget.destroy()

        funcion_seleccionada = self.optionmenu_funcion.get()
        if not funcion_seleccionada:
            return

        funciones = cargar_datos_desde_json(FUNCIONES_JSON)
        for funcion in funciones:
            if f"{funcion['pelicula']} - {funcion['sala']} - {funcion['horario']}" == funcion_seleccionada:
                asientos_reservados = funcion.get("asientos_reservados", [])
                break
        else:
            asientos_reservados = []

        for row in range(5):
            for col in range(5):
                asiento = f"{row}-{col}"
                btn = ctk.CTkButton(self.frame_asientos, text=asiento, command=lambda a=asiento: self.toggle_asiento(a))
                if asiento in asientos_reservados:
                    btn.configure(state="disabled", fg_color="red")
                self.asientos_widgets[asiento] = btn
                btn.grid(row=row, column=col, padx=5, pady=5)

    def toggle_asiento(self, asiento):
        btn = self.asientos_widgets[asiento]
        if btn.cget("fg_color") == "green":
            btn.configure(fg_color="white")
        else:
            btn.configure(fg_color="green")

    def reservar(self):
        usuario_nombre = self.entry_usuario.get()
        funcion_seleccionada = self.optionmenu_funcion.get()
        promocion_seleccionada = self.optionmenu_promocion.get()
        asientos = [asiento for asiento, btn in self.asientos_widgets.items() if btn.cget("fg_color") == "green"]

        if not usuario_nombre:
            messagebox.showerror(title="Error", message="Por favor, ingrese su nombre de usuario")
            return

        if not funcion_seleccionada:
            messagebox.showerror(title="Error", message="Por favor, seleccione una función")
            return

        if not asientos:
            messagebox.showerror(title="Error", message="Por favor, seleccione los asientos")
            return

        funciones = cargar_datos_desde_json(FUNCIONES_JSON)
        for funcion in funciones:
            if f"{funcion['pelicula']} - {funcion['sala']} - {funcion['horario']}" == funcion_seleccionada:
                funcion_obj = next((f for f in Funcion.lista_funciones if f.pelicula.nombre == funcion['pelicula'] and f.sala.identificador == funcion['sala'] and f.horario == funcion['horario']), None)
                break
        else:
            messagebox.showerror(title="Error", message="Función no encontrada")
            return

        if not funcion_obj.reservar(asientos):
            messagebox.showerror(title="Error", message="Algunos asientos ya están reservados")
            return

        usuario = {"name": usuario_nombre}
        promocion = next((p for p in Promocion.promociones if p.nombre == promocion_seleccionada), None)

        reserva = Reserva(usuario, funcion_seleccionada, asientos, promocion)
        reserva.guardar_reserva()
        Funcion.guardar_funciones()

        descuento = reserva.calcular_descuento()
        messagebox.showinfo(title="Éxito", message=f"Reserva realizada con éxito. Descuento aplicado: ${descuento:.2f}")
        self.visualizar_asientos()

    def on_close(self):
        self.destroy()
        Ventana_cliente()

    

    
# ver reservas
class VentanaVerReservas:
    def __init__(self, root):
        self.root = root
        self.root.geometry("800x600")
        self.root.title("Mis Reservas")

        icon_path = resource_path("imagenes\pokemon_go_play_game_cinema_film_movie_2_icon-icons.com_69159.ico")
        self.root.iconbitmap(icon_path)

        # Frame principal
        self.main_frame = ctk.CTkFrame(master=self.root, corner_radius=10)
        self.main_frame.place(relwidth=1, relheight=1)

        # Título
        self.titulo = ctk.CTkLabel(master=self.main_frame, text="Mis Reservas", font=("Century Gothic", 32, "bold"))
        self.titulo.place(relx=0.5, rely=0.1, anchor="center")

        # Ingreso del nombre de usuario
        self.label_usuario = ctk.CTkLabel(master=self.main_frame, text="Ingresa tu nombre de usuario:")
        self.label_usuario.place(relx=0.5, rely=0.2, anchor="center")

        self.entry_usuario = ctk.CTkEntry(master=self.main_frame)
        self.entry_usuario.place(relx=0.5, rely=0.25, anchor="center")

        # Botón para mostrar reservas
        self.boton_mostrar = ctk.CTkButton(master=self.main_frame, text="Mostrar Reservas", command=self.mostrar_reservas)
        self.boton_mostrar.place(relx=0.5, rely=0.3, anchor="center")

        # Frame para las reservas
        self.reservas_frame = ctk.CTkFrame(master=self.main_frame, corner_radius=10)
        self.reservas_frame.place(relx=0.5, rely=0.5, anchor="center")

        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

    def mostrar_reservas(self):
        usuario_nombre = self.entry_usuario.get()  # Obtener el nombre del usuario ingresado
        reservas = Reserva.cargar_reservas()  # Cargar reservas usando el método de la clase

        # Limpiar el frame de reservas antes de mostrar nuevas reservas
        for widget in self.reservas_frame.winfo_children():
            widget.destroy()

        # Filtrar reservas por el nombre del usuario
        reservas_usuario = [reserva for reserva in reservas if reserva.usuario == usuario_nombre]

        # Mostrar reservas del usuario
        if reservas_usuario:
            for idx, reserva in enumerate(reservas_usuario):
                reserva_texto = (
                    f"Función: {reserva.funcion}\n"  # Mostrar la función
                    f"Asientos: {', '.join(reserva.asientos)}\n"
                    f"Fecha de Reserva: {reserva.fecha_reserva.strftime('%Y-%m-%d %H:%M:%S')}\n"
                )
                # Verificar si hay una promoción aplicada
                if reserva.promocion:
                    reserva_texto += f"Promoción: {reserva.promocion.nombre} ({reserva.promocion.descuento}% de descuento)\n"
                else:
                    reserva_texto += "Promoción: No aplica\n"
                
                reserva_label = ctk.CTkLabel(master=self.reservas_frame, text=reserva_texto, font=("Century Gothic", 16))
                reserva_label.grid(row=idx, column=0, padx=10, pady=10)
        else:
            sin_reservas_label = ctk.CTkLabel(master=self.reservas_frame, text="No tienes reservas.", font=("Century Gothic", 16))
            sin_reservas_label.grid(row=0, column=0, padx=10, pady=10)

    def on_close(self):
        self.root.destroy()


    def on_close(self):
        # Cerrar la ventana actual y abrir la ventana de cliente
        self.root.destroy()
        Ventana_cliente()





# Cargar datos iniciales
Usuario.cargar_usuarios()
Pelicula.cargar_peliculas()
Sala.cargar_salas()
Funcion.cargar_funciones()

# cerrar sesion
def cerra_sesion():
    # Destruir la ventana actual y abrir la ventana principal
    Ventana_Principal()


# selccion menu var
def abrir_ventana_c(opcion):
    root3.destroy()
    if opcion == "Cartelera":
        mostrar_peliculas()
    elif opcion == "Menu":
        mostrar_menu_zona_comida()
    elif opcion == "Reserva":
        if __name__ == "__main__":
            Reserva = Reservar_v()
            Reserva.mainloop()
    elif opcion == "Mis Reservas":
        root = ctk.CTk()  # Crear la ventana principal
        app = VentanaVerReservas(root)  # Inicializar la ventana de reservas
        root.mainloop()  
    elif opcion == "Cerrar":
        cerra_sesion()
        
   


Ventana_Principal()