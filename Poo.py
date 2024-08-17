class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre  # Atributo
        self.edad = edad  # Atributo

    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")  # Método

# Crear un objeto (instancia de la clase Persona)
persona1 = Persona("Juan", 30)

# Usar un método del objeto
persona1.saludar()  # Salida: Hola, mi nombre es Juan y tengo 30 años.




class Empleado(Persona):  # Empleado hereda de Persona
    def __init__(self, nombre, edad, puesto):
        super().__init__(nombre, edad)  # Llama al constructor de la superclase
        self.puesto = puesto  # Nuevo atributo específico de Empleado


    def mostrar_informacion(self):
        print(f"Empleado: {self.nombre}, Edad: {self.edad}, Puesto: {self.puesto}")

# Crear un objeto de la clase Empleado
empleado1 = Empleado("Ana", 28, "Ingeniera de Software")
empleado1.mostrar_informacion()  # Salida: Empleado: Ana, Edad: 28, Puesto: Ingeniera de Software


try:
    x = int(input("Ingresa un número: "))
    y = int(input("Ingresa otro número: "))
    resultado = x / y
except ValueError:
    print("Error: Debes ingresar un número.")
except ZeroDivisionError:
    print("Error: No puedes dividir por cero.")
except Exception as e:  # Captura cualquier otra excepción
    print(f"Error inesperado: {e}")
else:
    print(f"El resultado es: {resultado}")
finally:
    print("Fin del cálculo.")
