# Definición de la clase base (clase Persona)
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def presentarse(self):
        return f"Me llamo {self.nombre} y tengo {self.edad} años."

# Clase derivada (clase Estudiante) que hereda de Persona
class Estudiante(Persona):
    def __init__(self, nombre, edad, escuela):
        super().__init__(nombre, edad)  # Llama al constructor de la clase base
        self.escuela = escuela

    def presentarse(self):
        return super().presentarse() + f" Soy estudiante de {self.escuela}."

# Clase derivada (clase Empleado) que hereda de Persona
class Empleado(Persona):
    def __init__(self, nombre, edad, empresa):
        super().__init__(nombre, edad)  # Llama al constructor de la clase base
        self.empresa = empresa

    def presentarse(self):
        return super().presentarse() + f" Trabajo en {self.empresa}."

# Crear instancias de las clases derivadas
estudiante = Estudiante("Alice", 20, "Universidad X")
empleado = Empleado("Bob", 30, "Empresa Y")

# Llamar al método presentarse de las instancias
print(estudiante.presentarse())  # Salida: Me llamo Alice y tengo 20 años. Soy estudiante de Universidad X.
print(empleado.presentarse())    # Salida: Me llamo Bob y tengo 30 años. Trabajo en Empresa Y.
