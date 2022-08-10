from funciones_matematicas import *
from clases import Persona



variable1=int(input("Ingrese un numero: "))
variable2=int(input("Ingrese otro numero: "))

print(sumar(variable1,variable2))
print(restar(variable1,variable2))


variable=Persona("Francisco","Gonzalez",20)

variable.saludar()


