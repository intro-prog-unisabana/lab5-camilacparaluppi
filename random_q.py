import random
random.seed(123)
inicio_rango = int(input("Enter the start value:\n"))
final_rango = int(input("Enter the end value:\n"))
numero_aleatorio = random.randint(inicio_rango, final_rango)
print(f"Generated random number: {numero_aleatorio}")