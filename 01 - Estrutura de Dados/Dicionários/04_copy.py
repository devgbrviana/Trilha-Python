contatos = {"gabriel@gmail.com": {"nome": "Gabriel", "telefone": "3333-2221"}}

copia = contatos.copy()
copia["gabriel@gmail.com"] = {"nome": "biel"}

print(contatos["gabriel@gmail.com"])  # {"nome": "Gabriel", "telefone": "3333-2221"}

print(copia["gabriel@gmail.com"])  # {"nome": "biel"}