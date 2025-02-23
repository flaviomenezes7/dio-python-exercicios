resultado = dict.fromkeys(["nome", "telefone"])  # {"nome": None, "telefone": None}
print(resultado)

resultado = dict.fromkeys(["nome", "telefone"], "vazio")  # {"nome": "vazio", "telefone": "vazio"}
print(resultado)


# Fromkeys é um método de classe que cria um novo dicionário a partir de uma lista de chaves. 
# O primeiro argumento é a lista de chaves e o segundo argumento é o valor inicial de cada chave.
# Se o segundo argumento não for passado, o valor inicial será None.