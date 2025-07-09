contatos = {"gabriel@gmail.com": {"nome": "Gabriel", "telefone": "3333-2221"}}

resultado = contatos.pop("gabriel@gmail.com")  # {'nome': 'Gabriel', 'telefone': '3333-2221'}
print(resultado)

resultado = contatos.pop("gabriel@gmail.com", {})  # {}
print(resultado)