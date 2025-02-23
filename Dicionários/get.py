contatos = {"flaviom@gmail.com": {"nome": "Flavio", "telefone": "3333-2221"}}

# contatos["chave"]  # KeyError

resultado = contatos.get("chave")  # None
print(resultado)

resultado = contatos.get("chave", {})  # {}
print(resultado)

resultado = contatos.get(
    "flaviom@gmail.com", {}
)  # {"flaviom@gmail.com": {"nome": "Flavio", "telefone": "3333-2221"}
print(resultado)

# O método get é uma forma de acessar um valor de um dicionário, sem lançar uma exceção KeyError caso a chave não exista.