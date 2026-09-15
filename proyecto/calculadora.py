print("===== CALCULADORA =====")

numero1 = float(input("Digite el primer número: "))
numero2 = float(input("Digite el segundo número: "))

print("\nSeleccione una operación:")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")

opcion = input("Digite el número de la operación: ")

if opcion == "1":
    resultado = numero1 + numero2
    print("Resultado:", resultado)

elif opcion == "2":
    resultado = numero1 - numero2
    print("Resultado:", resultado)

elif opcion == "3":
    resultado = numero1 * numero2
    print("Resultado:", resultado)

elif opcion == "4":
    if numero2 != 0:
        resultado = numero1 / numero2
        print("Resultado:", resultado)
    else:
        print("No se puede dividir entre cero.")

else:
    print("Opción no válida.")
# Calculadora básica
