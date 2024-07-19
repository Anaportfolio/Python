
frase = "O Python é uma linguagem de programação "\
        "multiparadigma. "\
        "Python foi criado por Guido van Rossuem." # Váriavel rececebendo a frase/valor

i = 0
qtd_apareceu_mais_vezes = 0 # Quantidade de letras que apareceu mais vezes 
letra_apareceu_mais_vezes = " " # Letra que apareceu mais vezes

# Identificando qual letra aparece mais vezes 
while i < len(frase):
    letra_atual = frase[i]
    qtd_vezes_letra_apareceu_atual = frase.count(letra_atual)

    if qtd_apareceu_mais_vezes < qtd_vezes_letra_apareceu_atual:
        qtd_apareceu_mais_vezes = qtd_vezes_letra_apareceu_atual
        letra_apareceu_mais_vezes = letra_atual

    i+= 1

print(f"A letra que apareceu mais vezes é: {letra_apareceu_mais_vezes}, 
      quantidade de vezes que apareceu: {qtd_apareceu_mais_vezes}")
