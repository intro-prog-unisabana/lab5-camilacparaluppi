import os
directorio_actual = os.getcwd()
print(f"Current working directory: {directorio_actual}")
import math
num = int(input("Enter an integer:"))
resultado = math.log2(num)
print(f"Log base 2 of {num} is: {resultado}")
piso = math.floor (resultado)
print(f"Floor: {piso}")
techo = math.ceil(resultado)
print(f"Ceiling: {techo}")