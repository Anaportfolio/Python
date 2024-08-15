"""# Duplicando o valor
def duplicar(number):
    return number * 2

# Triplicando o valor
def triplicar(number):
    return number * 3

# Quadruplicando o valor 
def quadruplicar(number):
    return number * 4

# Recebendo o valor 
valor = int(input("Digite o valor: "))

duplicar_valor = duplicar(valor)
triplicar_valor = triplicar(valor)
quadruplicar_valor = quadruplicar(valor)

# Exibindo os resultados das multiplicações 
print(f"Duplicando: {duplicar_valor}")
print(f"Triplicando: {triplicar_valor}")
print(f"Quadruplicando: {quadruplicar_valor}")"""

# Multiplicando 
def multiplicador(numero, multiplicador):
        return numero * multiplicador

# Recebendo os valores 
valor = int(input("Digite o valor: "))
multipli= int(input("Digite o multiplicador: "))

result = multiplicador(valor, multipli)

# Exibindo o resultado da multiplicação 
print(f"O resultado é: {result}")