import json
import os
from datetime import datetime

# Carpeta de destino
CARPETA_DESTINO = "PROYECTO"
os.makedirs(CARPETA_DESTINO, exist_ok=True)

# Rutas completas de los archivos
EMPLEADOS_JSON = os.path.join(CARPETA_DESTINO, "empleados.json")
USUARIOS_JSON = os.path.join(CARPETA_DESTINO, "usuarios.json")
PELICULAS_JSON = os.path.join(CARPETA_DESTINO, "peliculas.json")
SALAS_JSON = os.path.join(CARPETA_DESTINO, "salas.json")
RESERVAS_JSON = os.path.join(CARPETA_DESTINO, "reservas.json")
PROMOCIONES_JSON = os.path.join(CARPETA_DESTINO, "promociones.json")
FUNCIONES_JSON = os.path.join(CARPETA_DESTINO, "funciones.json")
MENU_JSON = os.path.join(CARPETA_DESTINO, "menu.json")



class Persona:
    lista_persona = []

    def __init__(self, name, email, rol, password):
        self.name = name
        self.email = email
        self.rol = rol
        self.__password = password
        Persona.lista_persona.append(self)

    @classmethod
    def iniciar_sesion(cls, name, password):
        for persona in cls.lista_persona:
            if persona.name == name and persona._Persona__password == password:
                print(f"Bienvenido {persona.name}, acaba de iniciar sesión")
                return persona
        print("Datos incorrectos :(")
        return None

    @classmethod
    def guardar_personas(cls):
        data = []
        for persona in cls.lista_persona:
            data.append({
                "name": persona.name,
                "email": persona.email,
                "rol": persona.rol,
                "password": persona._Persona__password  # Acceder al atributo privado
            })
        try:
            with open(EMPLEADOS_JSON, "w") as file:
                json.dump(data, file, indent=4)
            print("Personas guardadas correctamente.")
        except Exception as e:
            print(f"Error al guardar personas: {e}")


class Usuario(Persona):
    lista_usuarios = []

    def __init__(self, name, email, password):
        super().__init__(name, email, "Cliente", password)  # Establecer rol como "Cliente"
        Usuario.lista_usuarios.append(self)

    @classmethod
    def cargar_usuarios(cls):
        cls.lista_usuarios.clear()  # Vaciar la lista antes de cargar los usuarios
        if os.path.exists(USUARIOS_JSON):
            with open(USUARIOS_JSON, "r") as file:
                data = json.load(file)
                for usuario_data in data:
                    cls(usuario_data["name"], usuario_data["email"], usuario_data["password"])
        else:
            print("El archivo de usuarios no existe.")
        return cls.lista_usuarios

    @classmethod
    def guardar_usuarios(cls):
        data = []
        for usuario in cls.lista_usuarios:
            data.append({
                "name": usuario.name,
                "email": usuario.email,
                "rol": usuario.rol,
                "password": usuario._Persona__password  # Acceder al atributo privado
            })
        try:
            with open(USUARIOS_JSON, "w") as file:
                json.dump(data, file, indent=4)
            print("Usuarios guardados correctamente.")
        except Exception as e:
            print(f"Error al guardar usuarios: {e}")

    @classmethod
    def registrar(cls, name, email, password):
        nuevo_usuario = cls(name, email, password)  # Crear un nuevo objeto Usuario
        cls.guardar_usuarios()  # Guardar el nuevo usuario en el archivo JSON
        print(f"Usuario {nuevo_usuario.name} registrado exitosamente.")



class Reserva:
    def __init__(self, usuario, funcion, asientos, promocion=None):
        self.usuario = usuario["name"]
        self.funcion = funcion
        self.asientos = asientos
        self.fecha_reserva = datetime.now()
        self.promocion = promocion

    def to_dict(self):
        return {
            "usuario": {"name": self.usuario},
            "funcion": self.funcion,
            "asientos": self.asientos,
            "fecha_reserva": self.fecha_reserva.isoformat(),
            "promocion": self.promocion.to_dict() if self.promocion else None
        }

    @staticmethod
    def from_dict(data):
        usuario = data["usuario"]
        funcion = data["funcion"]
        asientos = data["asientos"]
        promocion_data = data.get("promocion")
        promocion = Promocion(promocion_data["nombre"], promocion_data["descuento"]) if promocion_data else None
        reserva = Reserva(usuario, funcion, asientos, promocion)
        reserva.fecha_reserva = datetime.fromisoformat(data["fecha_reserva"])
        return reserva


    def guardar_reserva(self):
        try:
            if os.path.exists(RESERVAS_JSON):
                with open(RESERVAS_JSON, "r") as file:
                    try:
                        data = json.load(file)
                    except json.JSONDecodeError:
                        data = {"reservas": []}
            else:
                data = {"reservas": []}
            
            data["reservas"].append(self.to_dict())
            
            with open(RESERVAS_JSON, "w") as file:
                json.dump(data, file, indent=4)
            print("Reserva guardada con éxito.")
        except Exception as e:
            print(f"Error al guardar la reserva: {e}")

    @staticmethod
    def cargar_reservas():
        if os.path.exists(RESERVAS_JSON):
            with open(RESERVAS_JSON, "r") as file:
                try:
                    data = json.load(file)
                    reservas = [Reserva.from_dict(reserva) for reserva in data["reservas"]]
                    return reservas
                except json.JSONDecodeError:
                    return []
        return []





class Empleado(Persona):
    lista_empleados = []

    def __init__(self, name, email, rol, password):
        super().__init__(name, email, rol, password)
        Empleado.lista_empleados.append(self)

    @classmethod
    def cargar_empleados(cls):
        cls.lista_empleados = []  # Limpiar la lista antes de cargar
        if os.path.exists(EMPLEADOS_JSON):
            with open(EMPLEADOS_JSON, "r") as file:
                data = json.load(file)
                for empleado_data in data:
                    cls(empleado_data["name"], empleado_data["email"], empleado_data["rol"], empleado_data["password"])

    @classmethod
    def guardar_empleados(cls):
        data = []
        for empleado in cls.lista_empleados:
            data.append({
                "name": empleado.name,
                "email": empleado.email,
                "rol": empleado.rol,
                "password": empleado._Persona__password
            })
        try:
            with open(EMPLEADOS_JSON, "w") as file:
                json.dump(data, file, indent=4)
            print("Empleados guardados correctamente.")
        except Exception as e:
            print(f"Error al guardar empleados: {e}")

    @classmethod
    def registrar(cls, name, email, rol, password):
        # Verificar si el empleado ya existe
        if any(emp.email == email for emp in cls.lista_empleados):
            print(f"Error: Ya existe un empleado con el email {email}.")
            return
        
        nuevo_empleado = cls(name, email, rol, password)  # Crear un nuevo objeto Empleado
        cls.guardar_empleados()  # Guardar el nuevo empleado en el archivo JSON
        print(f"Empleado {nuevo_empleado.name} registrado exitosamente.")


class Espacio:
    def __init__(self, tamaño, identificador):
        self.tamaño = tamaño
        self.identificador = identificador

    def descripcion(self):
        return f"El espacio es de tamaño {self.tamaño} y tiene el identificador {self.identificador}"


class Sala:
    lista_salas = []

    def __init__(self, tamaño, identificador, capacidad):
        self.tamaño = tamaño
        self.identificador = identificador
        self.capacidad = capacidad
        Sala.lista_salas.append(self)

    def to_dict(self):
        """Convierte la instancia de Sala a un diccionario."""
        return {
            "tamaño": self.tamaño,
            "identificador": self.identificador,
            "capacidad": self.capacidad
        }

    @classmethod
    def cargar_salas(cls):
        """Carga las salas desde un archivo JSON."""
        cls.lista_salas.clear()  # Limpiar la lista antes de cargar
        if os.path.exists(SALAS_JSON):
            try:
                with open(SALAS_JSON, "r") as file:
                    data = json.load(file)
                    for sala_data in data:
                        cls(
                            sala_data.get("tamaño"),
                            sala_data.get("identificador"),
                            sala_data.get("capacidad")
                        )
                print(f"{len(cls.lista_salas)} salas cargadas.")
            except json.JSONDecodeError:
                print("Error al decodificar el archivo JSON.")
            except Exception as e:
                print(f"Error al cargar salas: {e}")
        else:
            print("El archivo de salas no existe.")

    @classmethod
    def guardar_salas(cls):
        """Guarda las salas en un archivo JSON."""
        data = [sala.to_dict() for sala in cls.lista_salas]  # Usar to_dict para convertir a diccionario
        try:
            with open(SALAS_JSON, "w") as file:
                json.dump(data, file, indent=4)
            print("Salas guardadas correctamente.")
        except Exception as e:
            print(f"Error al guardar salas: {e}")

class ZonaComida(Espacio):
    def __init__(self, tamaño, identificador):
        super().__init__(tamaño, identificador)
        self.menu = []

    def agregar_producto(self, nombre, precio):
        self.menu.append({"nombre": nombre, "precio": precio})
        self.guardar_menu()

    def eliminar_producto(self, nombre):
        self.menu = [producto for producto in self.menu if producto["nombre"] != nombre]
        self.guardar_menu()

    def mostrar_menu(self):
        return [f'{producto["nombre"]} - ${producto["precio"]}' for producto in self.menu]

    def cargar_menu(self):
        if os.path.exists(MENU_JSON):
            try:
                with open(MENU_JSON, "r") as file:
                    self.menu = json.load(file)
                print(f"{len(self.menu)} productos cargados.")
            except json.JSONDecodeError:
                print("Error al decodificar el archivo JSON.")
            except Exception as e:
                print(f"Error al cargar el menú: {e}")
        else:
            print("El archivo de menú no existe.")

    def guardar_menu(self):
        try:
            with open(MENU_JSON, "w") as file:
                json.dump(self.menu, file, indent=4)
            print("Menú guardado correctamente.")
        except Exception as e:
            print(f"Error al guardar el menú: {e}")

# Creo la zona
zona_comida = ZonaComida("Grande", "Zona 1")
zona_comida.cargar_menu()



class Pelicula:
    lista_peliculas = []

    def __init__(self, nombre, duracion, genero, imagen):
        self.nombre = nombre
        self.duracion = duracion
        self.genero = genero
        self.imagen = imagen
        Pelicula.lista_peliculas.append(self)

    def to_dict(self):
        """Convierte la instancia de Pelicula a un diccionario."""
        return {
            "nombre": self.nombre,
            "duracion": self.duracion,
            "genero": self.genero,
            "imagen": self.imagen
        }

    @classmethod
    def cargar_peliculas(cls):
        cls.lista_peliculas = []  # Limpiar la lista antes de cargar
        if os.path.exists(PELICULAS_JSON):
            try:
                with open(PELICULAS_JSON, "r", encoding="utf-8") as file:
                    data = json.load(file)
                    for pelicula_data in data:
                        cls(
                            pelicula_data.get("nombre"),
                            pelicula_data.get("duracion"),
                            pelicula_data.get("genero"),
                            pelicula_data.get("imagen")
                        )
                print(f"{len(cls.lista_peliculas)} películas cargadas.")
            except json.JSONDecodeError as e:
                print(f"Error al decodificar el archivo JSON: {e}")
            except Exception as e:
                print(f"Error al cargar películas: {e}")
        else:
            print("El archivo de películas no existe.")

    @classmethod
    def guardar_peliculas(cls):
        """Guarda las películas en un archivo JSON."""
        data = []
        for pelicula in cls.lista_peliculas:
            data.append(pelicula.to_dict())  # Usa to_dict para convertir a diccionario
        try:
            with open(PELICULAS_JSON, "w", encoding="utf-8") as file:
                json.dump(data, file, indent=4)
            print("Películas guardadas correctamente.")
        except Exception as e:
            print(f"Error al guardar películas: {e}")




class Funcion:
    lista_funciones = []

    def __init__(self, pelicula, sala, horario):
        self.pelicula = pelicula
        self.sala = sala
        self.horario = horario
        self.asientos_disponibles = [f"{row}-{col}" for row in range(5) for col in range(5)]  # 5x5 asientos
        self.asientos_reservados = []
        Funcion.lista_funciones.append(self)

    def to_dict(self):
        """Convierte la instancia de Funcion a un diccionario."""
        return {
            "pelicula": self.pelicula.nombre,
            "sala": self.sala.identificador,
            "horario": self.horario
        }

    @classmethod
    def cargar_funciones(cls):
        cls.lista_funciones.clear()  # Limpiar la lista antes de cargar
        if os.path.exists(FUNCIONES_JSON):
            with open(FUNCIONES_JSON, "r") as file:
                data = json.load(file)
                for funcion_data in data:
                    pelicula_obj = next((p for p in Pelicula.lista_peliculas if p.nombre == funcion_data["pelicula"]), None)
                    sala_obj = next((s for s in Sala.lista_salas if s.identificador == funcion_data["sala"]), None)
                    if pelicula_obj and sala_obj:
                        cls(pelicula_obj, sala_obj, funcion_data["horario"])
        return cls.lista_funciones

    @classmethod
    def guardar_funciones(cls):
        data = [funcion.to_dict() for funcion in cls.lista_funciones]  # Usar to_dict para convertir a diccionario

        with open(FUNCIONES_JSON, "w") as file:
            json.dump(data, file, indent=4)
        print("Funciones guardadas con éxito.")

    def reservar(self, asientos):
        for asiento in asientos:
            if asiento in self.asientos_reservados:
                print(f"Asiento {asiento} ya está reservado.")
                return False
        self.asientos_reservados.extend(asientos)
        return True
 
class Promocion:
    promociones = []

    def __init__(self, nombre, descuento):
        self.nombre = nombre
        self.descuento = descuento
        Promocion.promociones.append(self)

    def to_dict(self):
        return {"nombre": self.nombre, "descuento": self.descuento}

    @classmethod
    def cargar_promociones(cls):
        if os.path.exists(PROMOCIONES_JSON):
            with open(PROMOCIONES_JSON, "r") as file:
                data = json.load(file)
            cls.promociones = [cls(p["nombre"], p["descuento"]) for p in data]
        else:
            cls.promociones = []

    @classmethod
    def guardar_promociones(cls):
        with open(PROMOCIONES_JSON, "w") as file:
            json.dump([p.to_dict() for p in cls.promociones], file, indent=4)


em = Empleado.registrar("Admin", "admin@gmail.com", "Empleado", "admin123")
Empleado.guardar_empleados()