contatos = {"gabriel@gmail.com": {"nome": "Gabriel", "telefone": "3333-2221"}}

# contatos["chave"]  # KeyError

resultado = contatos.get("chave")  # None
print(resultado)

resultado = contatos.get("chave", {})  # {}
print(resultado)

resultado = contatos.get(
    "gabriel@gmail.com", {}
)  # {"gabriel@gmail.com": {"nome": "Gabriel", "telefone": "3333-2221"}
print(resultado)