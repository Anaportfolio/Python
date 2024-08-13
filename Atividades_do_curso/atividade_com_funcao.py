
# Realizando a multiplicação dos valores
def multiplicar(*args):
    total = 1
    for numero in args:
        total *= numero
    return total

mutiplicacao = multiplicar(10,2,3,4,5) 
print(mutiplicacao)

# Verificando se o número é par o Impar
def par_impar(numero):
    multiplo_de_dois = numero % 2 == 0
    if multiplo_de_dois:
        return "Par"
    else:
        return "Impar"

print(par_impar(2))
print(par_impar(5))