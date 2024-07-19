# Enquanto for True o programa vai continuar sendo executado
while True:
    num1 = input("Digite o primeiro número: ") # Recebendo o numero 1
    num2 = input("Digite o segundo número: ") # Recebendo o numero 2
    ope = input("Digite o operador: ") # Recebendo o operador

    numeros_validos = None # Bandeira 

    # Verificando se os inputs foram preenchidos 
    try:
        num1_float = float(num1) # Convertendo o numero 1 em float 
        num2_float = float(num2) # Convertendo o numero 2 em float 
        numeros_validos = True
    except:
        numeros_validos = None

    # Exibindo que houve um erro nos inputs ao receber os valores 
    if numeros_validos is None:
        print("Um ou ambos os números digitados são invalidos")
        continue 

    if len(ope) > 1:
        print("Digite apenas um operador!")
        continue

    # Realizando o calculo e exibindo o resultado 
    if ope == "+":
        print(f"O resultado é: {num1_float + num2_float}")
    elif ope == "-":
        print(f"O resultado é: {num1_float - num2_float}")
    elif ope == "*":
        print(f"O resultado é: {num1_float * num2_float}")
    elif ope == "/":
        print(f"O resultado é: {num1_float / num2_float}")
    else:
        print("Nunca deveria chegar aqui")

    operadores_permitidos = "+-/*" # Definindo os operadores permitidos 

    # Verificando se operador digitado é um dos operadores permitidos
    if ope not in operadores_permitidos:
        print("Operador inválido!")

    sair = input("Quer sair? [s/n]: ").lower().startswith("s") # string para minúsculo e pegando a primeira letra

    # Encerrando o programa 
    if sair is True:
        break 