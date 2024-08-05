cpf = "74682489070"
nove_digitos = cpf[:9] # Os primeiros 9 digitos 
contador_1 = 10 

# PEGANDO O PRIMEIRO DIGITO
resultado_1 = 0 
for digito in nove_digitos:
    resultado_1 += int(digito) * contador_1 # Realizando a multiplicação e a soma 
    contador_1 -= 1 
digito_1 = (resultado_1 * 10) % 11 # Multiplicando o resultado por 10 e pagando o resto

# Verificando se o último digito é 9 ou 0
digito_1 = digito_1 if digito_1 <= 9 else 0 

# PEGANDO O SEGUNDO DIGITO
dez_digitos = nove_digitos + str(digito_1) # Os primeiros 10 digitos 
contador_2 = 11 

resultado_2 = 0
for digito in dez_digitos:
    resultado_2 += int(digito) * contador_2
    contador_2 -= 1
digito_2 = (resultado_2 * 10) % 11
digito_2 = digito_2 if digito_2 <= 9 else 0

novo_cpf = f"{nove_digitos}{digito_1}{digito_2}"

# Verificando se o CPF é válido
if cpf == novo_cpf:
    print(f"{novo_cpf} é válido")
else:
    print("CPF inválido")