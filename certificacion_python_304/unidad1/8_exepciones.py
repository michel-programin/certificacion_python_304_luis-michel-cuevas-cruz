#nhola
numero1=float(input("ingresa el primer numero "))
numero2=float(input("ingresa el segundo numero "))
try:
    numero1=10
    numero2=2
    resultado=numero1/numero2
    print(resultado)
except ZeroDivisionError:
    print("Error:No se puede dividir un numero entre cero")
except ValueError:
    print("Error:No se puede ingrear un numero entre cero")
    

