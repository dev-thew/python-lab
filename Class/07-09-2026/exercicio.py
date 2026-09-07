'''
Exercício 1
'''
nome = '    Ju ve n a l d o    Flo ren tin o   '
nome = "".join(nome.split()) 

print(nome)

# As aspas simples mostram que é uma string.
# Ao ir para as aspas duplas, o Python entende que é uma string também, mas a função é tirar os espaços vazios da string. A função split() divide a string em uma lista de palavras, e o join() junta essas palavras sem espaços.
# A função do "." antes do join, é para dar acesso ao join, que é um método da string.
# A função do join, é unificar as palavras da lista em uma unica string.
# O split serve para transformar a string em uma lista de palavras, separando-as pelos espaços.

#O split separa tudo em uma lista, e o join vai lá e unifica tudo em uma única string, sem espaços vazios.
# Por fim, a variável nome agora contém a string 'JuvenaldoFlorentino' sem espaços vazios.

'''
Exercício 2
'''
import re
partes = re.findall(r' [A-Z][a-z]*', nome)
nome_corrigido = " ".join(partes)

print(nome_corrigido)

# A função do import é importar uma biblioteca.
# O re é a biblioteca que está sendo importada, que é usada para trabalhar com expressões regulares.
# findall é uma função da biblioteca re que encontra todas as ocorrências de um padrão em uma string.
# o r antes da string indica que é uma string bruta, ou seja, que não vai interpretar caracteres especiais.
# Os colchetes indicam o conjunto de caracteres que queremos encontrar, no caso, letras maiúsculas e minúsculas.
# O "*" indica que queremos encontrar por exemplo letras isoladas ou palavras completas.
# O join novamente unifica as partes encontradas em uma única string, sem espaços vazios.

'''
Exercicio 3
'''
exemplo = "maTheuS Brasil"
print(exemplo.capitalize()) # Faz a primeira letra da string maiúscula ser Maiuscula e o restante minúsculo.
print(exemplo.lower()) # Faz todas as letras da string ficarem minúsculas.
print(exemplo.upper()) # Faz todas as letras da string ficarem maiúsculas.
print(exemplo.title()) # Faz a primeira letra de cada palavra ser maiúscula.
print(exemplo.strip()) # Remove espaços em branco no início e no final da string.
print(exemplo.replace("a", "o")) # Substitui todas as ocorrências de "a" por "o".
print(exemplo.split("a")) # Divide a string em uma lista de substrings, separando por "a".
print(exemplo.join(["Olá ", " tudo bem?"])) # Junta elementos de uma lista em uma única string, separando por "exemplo".



'''
Exercicio 4
''' 
'''
# As aspas triplas podem ser usadas para criar string de várias linhas, ou servi de comentário.
'''
'''
Exercício 5
'''
nome = "Heitor"
print(len(nome)) # Retorna o tamanho da string, no caso 6.

# nome é a variavel
# len() é a função que retorna o tamanho da string.

'''
Exercício 6
'''

alfabetos = "abcdefghijklmnopqrstuvwxyz"
print(alfabetos[0]) # Retorna a primeira letra da string, no caso "a".

# Alfabetos dentro do parenteses é a string que queremos acessar.
# Os colchetes indica o indicie da letra que quero acessar
# O 0 qual quero acessarm no caso a primeira posição da string, que é a letra "a".

'''
Exercício 7
'''

letras = "ABDE"
print(letras + "FGH")

# ABDE é a nossa string
# Letras dentro do () é a string que queremos acessar.
# O "+" é o operador de concatenação, que junta duas strings em uma única string.
# o FGH é a string que queremos concatenar com a string "ABDE", resultando em "ABDEFGH".

'''
Exercício 8
'''

print(letras + "F" * 5)

# O "*" é o operador de repetição, que repete a string "F" 5 vezes, resultando em "FFFFF".

'''
Exercício 9
'''

print("X" + "-" * 10 + "X")

# A dunção do + é concatenar as strings

'''
Exercício 10
'''

cidade = "Fortaleza"
fateada = cidade[0:3] 
print(fateada)

#cidade é a variavel que contém a string "Fortaleza"
# o 0 é a posição inicial da fatia, que é a letra "F"
# o 3 é a posição final da fatia, que é a letra "t"
# O print(fateada) vai imprimir a fatia da string, que é "For"