from itertools import combinations, permutations, product

def print_iter(iterator):
    print(*list(iterator), sep = '\n')

pessoas = [
    'João', 'Maria', 'Luiz', 'Ian',
]

camisetas = [
    ['preta', 'branca'],
    ['P', 'M'],
    ['Masculino', 'Femenino']
]

print_iter(combinations(pessoas, 2))
print_iter(permutations(pessoas, 2))
print_iter(product(*camisetas))