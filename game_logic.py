from secret_number import seed_secret_numbers, generate_secret_number
from response import input_response
seed = int(input("Enter a seed number:"))
seed_secret_numbers(seed)
generated_value = generate_secret_number()
correcto = False
tries = 0
while correcto != True:
    user_input = int(input("What is your guess:"))
    mensaje, correcto = input_response(generated_value, user_input)
    print(mensaje)
    tries += 1
print(f"It took you {tries} tries")