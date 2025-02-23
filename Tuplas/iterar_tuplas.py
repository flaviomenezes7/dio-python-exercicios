carros = (
    "gol",
    "celta",
    "palio",
)

for carro in carros: # Iterando sobre os elementos da tupla
    print(carro)


for indice, carro in enumerate(carros): # Iterando sobre os elementos da tupla e seus índices
#  O método enumerate() retorna uma tupla com o índice e o valor.
    print(f"{indice}: {carro}")