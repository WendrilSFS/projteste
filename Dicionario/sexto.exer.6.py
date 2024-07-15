amigos = {
    'marcos': 30,
    'jose': 25,
    'mariah': 28,
    'joao': 22
}

tuplas = [(nome, idade) for nome, idade in amigos.items()]


for amigo in tuplas:
    print(f"Nome: {amigo[0]}, Idade: {amigo[1]}")