contatos = {"flaviom@gmail.com": {"nome": "Flavio", "telefone": "3333-2221"}}

copia = contatos.copy()
copia["guilherme@gmail.com"] = {"nome": "Flavin"}

print(contatos["flaviom@gmail.com"])  # {"nome": "Flavio", "telefone": "3333-2221"}

print(copia["flaviom@gmail.com"])  # {"nome": "Flavin"}



# Copy é uma forma de criar uma cópia de um dicionário.