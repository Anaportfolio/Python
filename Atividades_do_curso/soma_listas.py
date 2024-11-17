from itertools import zip_longest


# Listas
list_a = [1,2,3,4,5,6,7]
list_b = [1,2,3,4]

# Realizando a soma dos valores das listas
list_sun = [x + y for x,y in zip_longest(list_a,list_b, fillvalue=0)]

# Exibindo o resultado 
print(list_sun)

