import os

lista = [] # Criando uma lista vazia

while True:
    print('Selecione uma opção')
    opcao = input('[i]nserir [a]pagar [l]istar: ') # Pegando uma das opções

    # Inserindo um item
    if opcao == 'i':
        os.system('cls')
        valor = input('Valor: ')
        lista.append(valor)
    
    # Apagando um item 
    elif opcao == 'a':
        indice_str = input('Escolha o índice para apagar: ') # Pegando o índice do item 

        try:
            indice = int(indice_str)
            del lista[indice]
        except ValueError:
            print('Por favor digite número int.')
        except IndexError:
            print('Índice não existe na lista')
        except Exception:
            print('Erro desconhecido')

    # Exibindo a lista 
    elif opcao == 'l':
        os.system('cls')

        if len(lista) == 0: # Verificando se a lista está vazia 
            print('Nada para listar')

        for i, valor in enumerate(lista):
            print(i, valor)
    else:
        print('Por favor, escolha i, a ou l.')