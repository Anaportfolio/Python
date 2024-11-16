import copy
from dados import produtos

# Gerando novos preços dos prdutos
novos_produtos = [
    {
        **p, 'preco': round(p['preco'] * 1.1, 2)
    }
    for p in copy.deepcopy(produtos)
]

# Ordenado os produtos por nome 
produtos_ordenados_por_nome = sorted(
    copy.deepcopy(produtos),
    key=lambda p : p['nome'],
    reverse=True
)

# Ordenando os produtos por preço 
produtos_ordenados_por_preco = sorted(
    copy.deepcopy(produtos),
    key=lambda p : p['preco']
)

# Exibido
print("Dados originais")
print(*produtos, sep='\n')
print()
print("Novos preços")
print(*novos_produtos, sep='\n')
print()
print("Lista ordenada por nome")
print(*produtos_ordenados_por_nome, sep='\n')
print()
print("Lista ordenada por preço")
print(*produtos_ordenados_por_preco, sep='\n')