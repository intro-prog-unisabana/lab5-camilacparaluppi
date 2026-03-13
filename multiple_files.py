from utils import greet, flip, count_letters
mensaje = input("Please type your message\n")
invertido = flip(mensaje)
cantidad_a = count_letters(mensaje, 'a')
mensaje_codificado = invertido + str(cantidad_a)
print(f"Your encoded message is: {mensaje_codificado}")