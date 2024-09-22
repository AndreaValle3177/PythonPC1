menu="""
     Hola, eliga una opción
     1.Sumar números
     2.Restar números
     3.Multiplicar
     4.Salir
"""
print(menu)
opcion= int(input("Elije tu opcion:"))

if opcion==1:
    numberOne=float(input("ingrese numero 1"))
    numberTwo=float(input("ingrese numero 2"))
    resultado=numberOne+numberTwo
    print(f"La suma es{resultado}")
if opcion==2:
    numberOne=float(input("ingrese numero 1"))
    numberTwo=float(input("ingrese numero 2"))
    resultado=numberOne-numberTwo
    print(f"La resta es{resultado}")
if opcion==3:
    numberOne=float(input("ingrese numero 1"))
    numberTwo=float(input("ingrese numero 2"))
    resultado=numberOne*numberTwo
    print(f"La multiplicacion2 es{resultado}")
if opcion==4:
    print("Hasta luego")
else:
    print("opcion no valida")