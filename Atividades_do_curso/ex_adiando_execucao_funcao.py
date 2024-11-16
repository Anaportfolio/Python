# Função Soma 
def soma (x,y):
    return x + y

# Função Multiplicar
def multiplica(x,y):
    return x * y 


# Executando as funções 
def executa(funcao, x):
    def interna(y):
        return funcao(x,y)
    return interna

soma_com_cinco = executa(soma,5)
multiplica_por_dez = executa(multiplica,10)

# Exibindo 
print(soma_com_cinco(10))
print(multiplica_por_dez(10))