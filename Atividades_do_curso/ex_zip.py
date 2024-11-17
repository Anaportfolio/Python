from itertools import zip_longest

# Listas 
l1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
l2 = ['BA', 'SP', 'MG', 'RJ']

# Juntando as duas listas
print(list(zip(l1,l2)))

# Juntando as duas listas e mostrando o estado que está sem cidade
# zip_longest: Combina os elementos dos iteráveis de entrada 
print(list(zip_longest(l1,l2, fillvalue='SEM CIDADE')))