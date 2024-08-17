# Dicionário
perguntas = [
    {
        'Pergunta' : 'Quanto é 2 + 2?',
        'Opções' : ['1','3','4','5'],
        'Resposta' : '4',
    },
    {
        'Pergunta' : 'Quanto é 5 * 5?',
        'Opções' : ['25','55','10','51'],
        'Resposta' : '25',
    },
    {
        'Pergunta' : 'Quanto é 10/2?',
        'Opções' : ['4','5','2','1'],
        'Resposta' : '5',
    },
]

qtd_acertos = 0

# Exibindo as perguntas e as suas opções  
for pergunta in perguntas:
    print('Pergunta: ',pergunta['Pergunta'])
    print()

    opcoes = pergunta['Opções']
    for i,opcao in enumerate(opcoes): # Enumerando as opções 
        print(f'{i})', opcao)
    print()

    escolha = input('Escolha uma opção: ') # Pegando a opção selecionada 

    acertou = False
    escolha_int = None
    qtd_opcoes = len(opcoes)

    # Verificando se a opção selecionada é um valor inteiro 
    if escolha.isdigit():
        escolha_int = int(escolha)

    # Verificando se foi selecionado uma das 4 opções 
    if escolha_int is not None:
        if escolha_int >= 0 and escolha_int < qtd_opcoes:
            if opcoes[escolha_int] == pergunta['Resposta']:
                acertou = True

    if acertou:
        qtd_acertos += 1 # Contando o número de acertos 
        print('Acertou 👍')
    else:
        print(' Errou ❌')
    print()
    
    # Exibindo o resutado 
    print('Você acertou ',qtd_acertos)
    print('de', len(perguntas), 'perguntas.')
    
