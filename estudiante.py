# Clase Estudiante

class Estudiante:
    def __init__(self, nombre, edad, carrera):
        self.nombre = nombre
        self.edad = edad
        self.carrera = carrera

    # Método 1
    def mostrar_datos(self):
        print("Nombre:", self.nombre)
        print("Edad:", self.edad)
        print("Carrera:", self.carrera)

    # Método 2
    def estudiar(self):
        print(self.nombre, "está estudiando Programación Orientada a Objetos.")


# Creación de objetos
estudiante1 = Estudiante("Ana", 20, "Ingeniería en Sistemas")
estudiante2 = Estudiante("Carlos", 22, "Tecnologías de la Información")

# Uso de los objetos
print("=== Estudiante 1 ===")
estudiante1.mostrar_datos()
estudiante1.estudiar()

print("\n=== Estudiante 2 ===")
estudiante2.mostrar_datos()
estudiante2.estudiar()
