

#Calculadora básica 

def calculadora(operacion,num1,num2):
    if operacion == "suma":
        return num1 + num2
    elif operacion == "resta":
        return num1 - num2
    elif operacion == "division":
        if num2 != 0:
            return num1 / num2
    elif operacion == "multiplicacion":
        return num1 * num2
        
    else:
        return "Operacion no valida"

num1 = 4
num2 = 6

opcion = "multiplicacion"

resultado = calculadora(opcion,num1,num2)

print (resultado)