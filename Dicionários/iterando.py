contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}



for chave in contatos: 
  print(chave, contatos[chave])  # Vai imprimir as chaves e os valores dos contatos.

print("=" * 100)

# Forma correta:
for chave, valor in contatos.items(): # O método items() retorna uma lista de tuplas com chave e valor.
    print(chave, valor)
    
    
    # As duas formas de iterar sobre um dicionário são válidas, mas a segunda é mais eficiente.
    
    
contatos = {"flaviom@gmail.com": {"nome": "flaviom", "telefone": "3333-2221"}}

resultado = contatos.items()  # dict_items([('flaviom@gmail.com', {'nome': 'Flavio', 'telefone': '3333-2221'})])
print(resultado)