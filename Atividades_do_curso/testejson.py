import json
"""
pessoa = {
    'nome': 'Luiz Otávio',
    'sobrenome': 'Miranda',
    'enderecos':[
        {'rua': 'R1', 'numero': 32},
        {'rua': 'R2', 'numero':55},
    ],
    'altura':1.8,
    'numero_preferidos': (2, 4, 6, 8, 10),
    'dev': True,
    'nada': None,
}

with open('teste.json', 'w') as arquivo:
    json.dump(pessoa, arquivo, ensure_ascii=False, indent=2) 

"""

with open('teste.json', 'r') as arquivo:
    pessoa = json.load(arquivo)
    print(pessoa)