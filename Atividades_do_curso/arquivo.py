caminho_arquivo = '/home/ana-beatriz/Área de trabalho/projeto/Python/Atividades_do_curso/arquivos/'
caminho_arquivo += 'arquivo.txt'

with open(caminho_arquivo, 'w') as arquivo:
    arquivo.write("Linha 1")
    arquivo.write("Linha 2")
    arquivo.seek(0,0) 



with open(caminho_arquivo, 'r') as arquivo:
    print(arquivo.read())