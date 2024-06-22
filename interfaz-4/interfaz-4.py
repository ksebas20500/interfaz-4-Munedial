import tkinter as tk
from tkinter import Toplevel, messagebox

# Lista global de jugadores registrados y equipos registrados
jugadores_registrados = []
equipos_registrados = []

# Equipo
class Equipo:
    def __init__(self, nombre, entrenador):
        self.nombre = nombre
        self.entrenador = entrenador
        self.jugadores = []

    def mostrar_info(self):
        info = f"Equipo: {self.nombre}, Entrenador: {self.entrenador}\nJugadores:\n"
        for jugador in self.jugadores:
            info += f"  - {jugador.mostrar_info()}\n"
        return info

    def agregar_jugador(self, jugador):
        self.jugadores.append(jugador)

# Jugador
class Jugador:
    def __init__(self, nombre, edad, posicion):
        self.nombre = nombre
        self.edad = edad
        self.posicion = posicion

    def mostrar_info(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Posición: {self.posicion}"

# Partido
class Partido:
    def __init__(self, equipo_local, equipo_visitante, estadio):
        self.equipo_local = equipo_local
        self.equipo_visitante = equipo_visitante
        self.estadio = estadio
        self.resultado = None

    def jugar_partido(self, resultado):
        self.resultado = resultado

    def mostrar_resultado(self):
        return (f"Partido en {self.estadio.nombre}, {self.estadio.ciudad}\n"
                f"{self.equipo_local.nombre} vs {self.equipo_visitante.nombre}\n"
                f"Resultado: {self.resultado}")

# Grupo
class Grupo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.equipos = []

    def mostrar_info(self):
        info = f"Grupo {self.nombre}\n"
        for equipo in self.equipos:
            info += f"{equipo.mostrar_info()}\n"
        return info

    def agregar_equipo(self, equipo):
        self.equipos.append(equipo)

# Estadio
class Estadio:
    def __init__(self, nombre, ciudad, capacidad):
        self.nombre = nombre
        self.ciudad = ciudad
        self.capacidad = capacidad

    def mostrar_info(self):
        return f"Estadio: {self.nombre}, Ciudad: {self.ciudad}, Capacidad: {self.capacidad}"

# Mundial
class Mundial:
    def __init__(self):
        self.grupos = []
        self.estadios = []
        self.partidos = []

    def registrar_grupo(self, grupo):
        self.grupos.append(grupo)

    def registrar_estadio(self, estadio):
        self.estadios.append(estadio)

    def agregar_partido(self, partido):
        self.partidos.append(partido)

    def mostrar_partidos(self):
        resultados = ""
        for partido in self.partidos:
            resultados += f"{partido.mostrar_resultado()}\n"
        return resultados

# Inicialización del objeto Mundial
mundial = Mundial()

# Funciones para la interfaz gráfica
def registrar_jugador():
    ventana_registro = Toplevel(Raiz)
    ventana_registro.title("Registrar Jugador")
    ventana_registro.geometry("300x250")

    tk.Label(ventana_registro, text="Nombre").place(relx=0.1, rely=0.2)
    tk.Label(ventana_registro, text="Edad").place(relx=0.1, rely=0.35)
    tk.Label(ventana_registro, text="Posición").place(relx=0.1, rely=0.5)

    nombre_var = tk.StringVar()
    tk.Entry(ventana_registro, textvariable=nombre_var).place(relx=0.35, rely=0.2)

    edad_var = tk.StringVar()
    tk.Entry(ventana_registro, textvariable=edad_var).place(relx=0.35, rely=0.35)

    posicion_var = tk.StringVar()
    tk.Entry(ventana_registro, textvariable=posicion_var).place(relx=0.35, rely=0.5)

    def guardar_jugador():
        nombre = nombre_var.get()
        edad = edad_var.get()
        posicion = posicion_var.get()
        nuevo_jugador = Jugador(nombre, edad, posicion)
        jugadores_registrados.append(nuevo_jugador)  # Agregar a la lista global
        messagebox.showinfo("Registro exitoso", "El jugador ha sido registrado exitosamente")
        ventana_registro.destroy()

    tk.Button(ventana_registro, text="Registrar", command=guardar_jugador).place(relx=0.6, rely=0.75)

def registrar_equipo():
    ventana_registro = Toplevel(Raiz)
    ventana_registro.title("Registrar Equipo")
    ventana_registro.geometry("300x250")

    tk.Label(ventana_registro, text="Nombre del equipo").place(relx=0.1, rely=0.2)
    tk.Label(ventana_registro, text="Entrenador").place(relx=0.1, rely=0.35)

    nombre_var = tk.StringVar()
    tk.Entry(ventana_registro, textvariable=nombre_var).place(relx=0.35, rely=0.2)

    entrenador_var = tk.StringVar()
    tk.Entry(ventana_registro, textvariable=entrenador_var).place(relx=0.35, rely=0.35)

    def guardar_equipo():
        nombre = nombre_var.get()
        entrenador = entrenador_var.get()
        nuevo_equipo = Equipo(nombre, entrenador)
        equipos_registrados.append(nuevo_equipo)  # Agregar a la lista global
        messagebox.showinfo("Registro exitoso", "El equipo ha sido registrado exitosamente")
        ventana_registro.destroy()

    tk.Button(ventana_registro, text="Registrar", command=guardar_equipo).place(relx=0.6, rely=0.75)

def agregar_jugador_a_equipo():
    ventana_agregar = Toplevel(Raiz)
    ventana_agregar.title("Agregar Jugador a Equipo")
    ventana_agregar.geometry("400x300")

    tk.Label(ventana_agregar, text="Jugador").place(relx=0.1, rely=0.2)
    tk.Label(ventana_agregar, text="Equipo").place(relx=0.1, rely=0.35)

    jugador_var = tk.StringVar()
    equipo_var = tk.StringVar()

    jugadores_nombres = [jugador.nombre for jugador in jugadores_registrados]
    equipos_nombres = [equipo.nombre for equipo in equipos_registrados]

    if jugadores_nombres:
        jugador_var.set(jugadores_nombres[0])
    if equipos_nombres:
        equipo_var.set(equipos_nombres[0])

    tk.OptionMenu(ventana_agregar, jugador_var, *jugadores_nombres).place(relx=0.35, rely=0.2)
    tk.OptionMenu(ventana_agregar, equipo_var, *equipos_nombres).place(relx=0.35, rely=0.35)

    def agregar_jugador():
        jugador_nombre = jugador_var.get()
        equipo_nombre = equipo_var.get()

        jugador = next((j for j in jugadores_registrados if j.nombre == jugador_nombre), None)
        equipo = next((e for e in equipos_registrados if e.nombre == equipo_nombre), None)

        if jugador and equipo:
            equipo.agregar_jugador(jugador)
            messagebox.showinfo("Operación exitosa", "El jugador ha sido agregado al equipo exitosamente")
            ventana_agregar.destroy()
        else:
            messagebox.showerror("Error", "Jugador o equipo no encontrado")

    tk.Button(ventana_agregar, text="Agregar", command=agregar_jugador).place(relx=0.6, rely=0.75)

def agregar_partido():
    ventana_agregar_partido = Toplevel(Raiz)
    ventana_agregar_partido.title("Agregar Partido")
    ventana_agregar_partido.geometry("400x300")

    tk.Label(ventana_agregar_partido, text="Equipo Local").place(relx=0.1, rely=0.2)
    tk.Label(ventana_agregar_partido, text="Equipo Visitante").place(relx=0.1, rely=0.35)
    tk.Label(ventana_agregar_partido, text="Estadio").place(relx=0.1, rely=0.5)

    equipo_local_var = tk.StringVar()
    equipo_visitante_var = tk.StringVar()
    estadio_var = tk.StringVar()

    equipos_nombres = [equipo.nombre for equipo in equipos_registrados]
    estadios_nombres = ["Estadio1", "Estadio2", "Estadio3"]  # Reemplazar con los estadios registrados

    if equipos_nombres:
        equipo_local_var.set(equipos_nombres[0])
        equipo_visitante_var.set(equipos_nombres[0])
    if estadios_nombres:
        estadio_var.set(estadios_nombres[0])

    tk.OptionMenu(ventana_agregar_partido, equipo_local_var, *equipos_nombres).place(relx=0.35, rely=0.2)
    tk.OptionMenu(ventana_agregar_partido, equipo_visitante_var, *equipos_nombres).place(relx=0.35, rely=0.35)
    tk.OptionMenu(ventana_agregar_partido, estadio_var, *estadios_nombres).place(relx=0.35, rely=0.5)

    def guardar_partido():
        equipo_local_nombre = equipo_local_var.get()
        equipo_visitante_nombre = equipo_visitante_var.get()
        estadio_nombre = estadio_var.get()

        equipo_local = next((e for e in equipos_registrados if e.nombre == equipo_local_nombre), None)
        equipo_visitante = next((e for e in equipos_registrados if e.nombre == equipo_visitante_nombre), None)
        estadio = Estadio(estadio_nombre, "Ciudad", 50000)  # Reemplazar con la información del estadio real

        if equipo_local and equipo_visitante:
            nuevo_partido = Partido(equipo_local, equipo_visitante, estadio)
            mundial.agregar_partido(nuevo_partido)
            messagebox.showinfo("Operación exitosa", "El partido ha sido agregado exitosamente")
            ventana_agregar_partido.destroy()
        else:
            messagebox.showerror("Error", "Equipo local o visitante no encontrado")

    tk.Button(ventana_agregar_partido, text="Agregar", command=guardar_partido).place(relx=0.6, rely=0.75)

def mostrar_partidos():
    ventana_partidos = Toplevel(Raiz)
    ventana_partidos.title("Partidos")
    ventana_partidos.geometry("400x300")

    resultados = mundial.mostrar_partidos()
    tk.Label(ventana_partidos, text=resultados, justify=tk.LEFT).pack(pady=10, padx=10)
    tk.Button(ventana_partidos, text="Cerrar", command=ventana_partidos.destroy).pack(pady=10)

def marcar_resultado():
    ventana_resultado = Toplevel(Raiz)
    ventana_resultado.title("Marcar Resultado")
    ventana_resultado.geometry("400x300")

    tk.Label(ventana_resultado, text="Partido").place(relx=0.1, rely=0.2)
    tk.Label(ventana_resultado, text="Resultado").place(relx=0.1, rely=0.35)

    partido_var = tk.StringVar()
    partidos_nombres = [f"{partido.equipo_local.nombre} vs {partido.equipo_visitante.nombre}" for partido in mundial.partidos]
    if partidos_nombres:
        partido_var.set(partidos_nombres[0])
    tk.OptionMenu(ventana_resultado, partido_var, *partidos_nombres).place(relx=0.35, rely=0.2)

    resultado_var = tk.StringVar()
    tk.Entry(ventana_resultado, textvariable=resultado_var).place(relx=0.35, rely=0.35)

    def guardar_resultado():
        partido_info = partido_var.get()
        resultado = resultado_var.get()

        equipos = partido_info.split(" vs ")
        equipo_local = equipos[0]
        equipo_visitante = equipos[1]

        for partido in mundial.partidos:
            if (partido.equipo_local.nombre == equipo_local and
                partido.equipo_visitante.nombre == equipo_visitante):
                partido.jugar_partido(resultado)
                messagebox.showinfo("Resultado marcado", "El resultado ha sido registrado exitosamente")
                ventana_resultado.destroy()
                return

        messagebox.showerror("Error", "Partido no encontrado")

    tk.Button(ventana_resultado, text="Guardar", command=guardar_resultado).place(relx=0.6, rely=0.75)

# Base
Raiz = tk.Tk()
Raiz.title("MENÚ MUNDIAL")
Raiz.geometry("800x600")
Raiz.configure(bg="lightblue")

# Adding a frame for the menu
menu_frame = tk.Frame(Raiz, bg="darkgrey", width=200)
menu_frame.pack(side="left", fill="y")

# Adding a frame for the logo
logo_frame = tk.Frame(Raiz, bg="lightblue")
logo_frame.pack(side="right", expand=True, fill="both")

# Load the logo image
logo_image = tk.PhotoImage(file="Poo-2Corte/png-transparent-2014-fifa-world-cup-2018-world-cup-logo-coreldraw-world-cup-2014-removebg-preview.png")
logo_label = tk.Label(logo_frame, image=logo_image, bg="lightblue")
logo_label.pack(expand=True)

# Menu buttons
btn_registrar_jugador = tk.Button(menu_frame, text="Registrar Jugador", command=registrar_jugador, bg="lightyellow", width=20, height=2)
btn_registrar_jugador.pack(pady=10)

btn_registrar_equipo = tk.Button(menu_frame, text="Registrar Equipo", command=registrar_equipo, bg="lightyellow", width=20, height=2)
btn_registrar_equipo.pack(pady=10)

btn_agregar_jugador_a_equipo = tk.Button(menu_frame, text="Agregar Jugador a Equipo", command=agregar_jugador_a_equipo, bg="lightyellow", width=20, height=2)
btn_agregar_jugador_a_equipo.pack(pady=10)

btn_agregar_partido = tk.Button(menu_frame, text="Agregar Partido", command=agregar_partido, bg="lightyellow", width=20, height=2)
btn_agregar_partido.pack(pady=10)

btn_mostrar_partidos = tk.Button(menu_frame, text="Mostrar Partidos", command=mostrar_partidos, bg="lightyellow", width=20, height=2)
btn_mostrar_partidos.pack(pady=10)

btn_marcar_resultado = tk.Button(menu_frame, text="Marcar Resultado", command=marcar_resultado, bg="lightyellow", width=20, height=2)
btn_marcar_resultado.pack(pady=10)

# Close button
btn_cerrar = tk.Button(menu_frame, text="Cerrar", command=Raiz.quit, bg="lightyellow", fg="black", width=20, height=2)
btn_cerrar.pack(pady=10)

Raiz.mainloop()
