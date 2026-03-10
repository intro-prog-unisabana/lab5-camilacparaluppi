def list_shift(elementos, valor):
    for i in range(len(elementos)):
        valor += elementos[i]
def calc_avg(elementos):
    return sum(elementos) / len(elementos)
def print_normalized(elementos):
    print(elementos)