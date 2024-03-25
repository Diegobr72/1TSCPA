agenda_amigos = [
  {
      "nome": "Yasmin",
      "endereco": "Rua dos Peixes 342",
      "telefone": "123456789",
      "idade": 29
   },

  {   "nome": "Mariazinha",
      "endereco": "Avenida Mar 788",
      "telefone": "987654321",
      "idade": 26
   },

  {
      "nome": "Pedro",
      "endereco": "Rua da Quaresma",
      "telefone": "456789123",
      "idade": 23
   },

  {
      "nome": "Lucas",
      "endereco": "Rua das Palmeiras 321",
      "telefone": "654321987",
      "idade": 27
  },

  {
      "nome": "Juliana",
      "endereco": "Avenida das Fadas 888",
      "telefone": "789123456",
      "idade": 24
  }
]

for amigo in agenda_amigos[:]:
    amigo["estado_civil"] = ""

print(agenda_amigos)

# Itere sobre uma cópia da lista para evitar problemas com a remoção
for amigo in agenda_amigos[:]:
    if amigo['nome'] == "Mariazinha":
        agenda_amigos.remove(amigo)  # Remova da lista
        print(f"Amigo {amigo['nome']} removido da agenda.")

print(agenda_amigos)
