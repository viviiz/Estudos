# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1QlO5voRJ1fQMVQQWveD40Eir5NNkfM-c
"""

##Este código pede dois números e imprime o maior deles

x  =  float ( input ( "Digite o primeiro número: \n " ))
y  =  float ( input ( "Digite o segundo número: \n " ))

if ( x  >  y ):
  print ( "O maior numero é: "  +  str ( x ))
elif ( y  >  x ):
  print ( "O maior numero é: "  +  str ( y ))
else :
  print ( "Os números são iguais." )

##Este código pede um número e mostra se é positivo, negativo ou neutro

x  =  float ( input ( "Digite um número: \n " ))

if ( x  >  0 ):
  print ( "O numero "  +  str ( x ) +  "é positivo." )
elif ( x  <  0 ):
  print ( "O numero "  +  str ( x ) +  "é negativo." )
else :
  print ( "O numero "  +  str ( x ) +  "é neutro." )

##Este código verifica se o caractere inserido é F ou M

x  =  str ( input ( "Qual seu gênero? Considere 'F' ou 'M' como resposta. \n " ))
if ( x  ==  'F' ):
  print ( "O gênero é feminino." )
elif ( x  ==  'M' ):
  print ( "O genero e masculino." )
else :
  print ( "Gênero inválido." )

##Este código verifica se o caractere é uma consoante ou vogal

x  =  input ( "Digite um caráter: \n " )

if ( x  ==  'a' ) ou ( x  ==  'e' ) ou ( x  ==  'i' ) ou ( x  ==  'o' ) ou ( x  ==  "u" ):
  print ( "O caráter digitado é um vogal." )
else :
  print ( "O caráter digitando é uma coincidência." )

##This code asks for 3 numbers and prints the highest of them

x = float(input("Digite o primeiro número:\n"))
y = float(input("Digite o segundo número:\n"))
z = float(input("Digite o terceiro número:\n"))

if(x > z) and (x > y):
  print("O maior número é:" + str(x))
elif(z > x) and (z > y):
  print("O maior número é:" + str(z))
else:
  print("O maior número é:" + str(y))

##Este código pede 3 números e imprime o maior e o menor deles

x  =  float ( input ( "Digite o primeiro número: \n " ))
y  =  float ( input ( "Digite o segundo número: \n " ))
z  =  float ( input ( "Digite ou terceiro número: \n " ))

if ( x  >  z ) e ( x  >  y ):
  print ( "O maior numero é:"  +  str ( x ))
elif ( z  >  x ) e ( z  >  y ):
  print ( "O maior numero é:"  +  str ( z ))
else :
  print ( "O maior numero é:"  +  str ( y ))

if ( x  <  z ) e ( x  <  y ):
  print ( "O menor numero é:"  +  str ( x ))
elif ( z  <  x ) e ( z  <  y ):
  print ( "O menor numero é:"  +  str ( z ))
else :
  print ( "O menor numero é:"  +  str ( y ))

##Este código pede três preços e imprime o menor deles

x  =  float ( input ( "Digite o primeiro preço: \n " ))
y  =  float ( input ( "Digite o segundo preço: \n " ))
z  =  float ( input ( "Digite o terceiro preço: \n " ))

if ( x  <  y ) e ( x  <  z ):
  print ( "O menor preço é: "  +  str ( x ))
elif ( y  <  x ) e ( y  <  z ):
  print ( "O menor preço é: "  +  str ( y ))
else :
  print ( "O menor preço é: "  +  str ( z ))

##Este código lê três números e os imprime em ordem decrescente

numbers  = []

for  i  int  range ( 0 , 3 ):
  addNumber  =  float ( input ( "Digite um número: \n " ))
  numbers.add( addNumber )

print ( "A ordem descrente é: "  +  str (( sorted ( numbers , reverse  =  True )))))

##Este código pergunta o horário da sua aula

shift  =  str ( input ( "Qual horário da sua aula? Digite uma das respostas válidas. \n M - Matutino \n V - Vespertino \n N - Noturno \n " ))
if ( shift  ==  'M' ) ou ( shift  ==  'm' ):
  print ( "Bom dia!" )
elif ( shift  ==  'V' ) ou ( shift  ==  'v' ):
  print ( "Boa tarde!" )
elif ( shift  ==  'N' ) ou ( shift  ==  'n' ):
  print ( "Boa noite!" )
else :
  print ( "Turno inválido." )

##Este código pede um ano e verifica se é bissexto

ano  =  int ( input ( "Digite o ano a ser selecionado: \n " ))
salto  =  ano  %  4
if ( ano  >  0 ):
  if ( salto  ==  0 ):
    print ( "O ano"  +  str ( ano ) +  "é bissexto." )
  else :
    print ( "O ano"  +  str ( ano ) +  "não é bissexto." )
else :
  print ( "Ano digitado inválido." )