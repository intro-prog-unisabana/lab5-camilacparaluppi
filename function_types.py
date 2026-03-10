def list_shift(elementos, valor):
    for i in range(len(elementos)):
        elementos[i] = elementos[i] + valor
def calc_avg(elementos):
    return sum(elementos) / len(elementos)
def print_normalized(elementos):
    print(elementos)