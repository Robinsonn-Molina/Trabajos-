while True:
    print("\nMenú de Operaciones Aritméticas:")
    print("1. Suma (+)")
    print("2. Resta (-)")
    print("3. Multiplicación (*)")
    print("4. División (/)")
    print("5. Salir")
    
    opcion = input("Seleccione una opción (1-5): ") 
    
    if opcion == 5:
        print("Saliendo del programa...") 
        break
    
    num1 = int(input("Ingrese el primer número: ")) #por acá debe estar
    num2 = int(input("Ingrese el segundo número: "))
    
    if opcion == "1":
        resultado = num1 + num2
        print("Resultado:", resultado)
    elif opcion == "2":
        resultado = num1 - num2
        print("Resultado:", resultado)
    elif opcion == "3":
        resultado = num1 * num2
        print("Resultado:", resultado)
    elif opcion == "4":
        if num2 == 0:
            print("Error: No se puede dividir entre 0.")
        else:
            resultado = num1 / num2
            print("Resultado:", resultado)
#algo falla