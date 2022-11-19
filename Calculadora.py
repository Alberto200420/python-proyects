#calculadora en python
numero1 = float(input("ingresa el primer numero: ")) 
numero2 = float(input("ingresa el segundo numero: "))


while True:
    print("""
    Dime ¿Que quieres hacer?
    1. Sumar
    2. Restar
    3. Multiplicar
    4. Dividir
    5. Cambiar los numeros 
    6. Salir
    """)

    opcion = int(input("Elije una opcion: "))
    if opcion == 1:
        print("\n El resultado de la suma es: ", numero1 + numero2)
    elif opcion == 2:
        print("\n El resultado de la resta es: ", numero1 - numero2)
    elif opcion == 3:
        print("\n El resultado de la multiplicacion es: ", numero1 * numero2)
    elif opcion ==4:
        print("\n El resultado de la divicion es: ", numero1 / numero2)
    elif opcion ==5:
        numero1 = float(input("ingresa el primer numero: "))
        numero2 = float(input("ingresa el segundo numero: "))
    elif opcion ==6:
        print("\n Adios")    
        break 
    else: 
        print("\n Opcion incorrecta") 