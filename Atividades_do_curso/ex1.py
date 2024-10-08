import os

palavra_secreta = 'programa' # Definindo a palavra secreta
letras_acertadas = '' # Letras acertadas 
numero_tentativas = 0 # Tentativas 

while True:
    letra_digitada = input('Digite uma letra: ') # Pegando a letra digitada 
    numero_tentativas += 1

    # Verificando se foi digitado pelo menos uma letra 
    if len(letra_digitada) > 1:
        print('Digite apenas uma letra.')
        continue

    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada

    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'

    print('Palavra formada:', palavra_formada)

    # Exibindo os resultados 
    if palavra_formada == palavra_secreta:
        os.system('cls')
        print('VOCÊ GANHOU!! PARABÉNS!')
        print('A palavra era', palavra_secreta)
        print('Tentativas:', numero_tentativas)
        letras_acertadas = ''
        numero_tentativas = 0


