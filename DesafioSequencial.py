# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1kkycP1R4yHpinbFEfPrLnN6WoDwDSxcn
"""

print( "Alô, ETE PORTO DIGITAL" )

numero  =  int ( input ( "Digite um numero: \n " ))
print ( "Você digitou: "  +  str ( numero ))

##Este código pede 2 números e imprime a soma entre eles

x  =  int ( input ( "Digite o primeiro número da soma: \n " ))
y  =  int ( input ( "Digite o segundo número do soma: \n " ))
print ( "A soma é: "  +  str ( x  +  y ))

##Este código pede 4 números e imprime a mídia entre eles

n1  =  float ( input ( "Digite sua primeira nota: \n " ))
n2  =  float ( input ( "Digite sua segunda nota: \n " ))
n3  =  float ( input ( "Digite sua terceira nota: \n " ))
n4  =  float ( input ( "Digite sua quarta nota: \n " ))
print ( "A sua média é: "  +  str (( n1  +  n2  +  n3  +  n4 ) / 4 ))

#Este código faz a conversão de um determinado número de metros para centímetros

metros  =  float ( input ( "Digite quantos metros você deseja converter para metros: \n " ))
print ( "O valor de"  +  str ( meters ) +  "metros em metros é:"  +  str ( meters  *  100 ) +  "cm" )

##Este código pede um número de raio e usa-o para descobrir uma área de círculo

r  =  float ( input ( "Qual raio do círculo? \n " ))
a  =  3,14  * ( r  **  2 )
print ( "A área do círculo é: "  +  str ( a ))

##Este código calcula a área de um quadrado e mostra o dobro dessa área

side  =  float ( input ( "Digite o comprimento do lado do quadrado: \n " ))
a  =  lado  *  2
print ( "A area do quadrado e: "  +  str ( a ))
print ( "O perímetro do quadrado é: "  +  str ( a  *  2 ))

##Este código pergunta quanto uma pessoa recebe por hora de trabalho e quantas horas foram
##este mês para calcular o valor total

moneyPerHour  =  float ( input ( "Quanto você ganha por hora trabalhada? \n " ))
horas  =  int input ( " Quantas horas você trabalhou neste mês? \n " ))
total  =  dinheiroPor hora  *  horas
print ( "Seu salário esse mês é: "  +  str ( total ))

##Este código converte Fahrenheit defree para graus Celsius

fahrenheit  =  float ( input ( "Qual valor de temperatura você deseja converter? \n " ))
celsius  =  5  * (( fahrenheit  -  32 ) /  9 )
print ( "A temperatura em Celsius é: "  +  str ( celsius ))

##Este código converte Fahrenheit defree para graus Celsius

fahrenheit  =  float ( input ( "Qual valor de temperatura você deseja converter? \n " ))
celsius  =  5  * (( fahrenheit  -  32 ) /  9 )
print ( "A temperatura em Celsius é: "  +  str ( celsius ))

##Este código converte Celsius defree para graus Fahrenheit

celsius  =  float ( input ( "Qual valor de temperatura você deseja converter? \n " ))
fahrenheit  = ( celsius  *  1,8 ) +  32
print ( "A temperatura em Fahrenheit é: "  +  str ( fahrenheit ))

##Este código pede 2 números inteiros e 1 número real e calcula operações de múltiplos
##entre eles

n1  =  int ( input ( "Digite o primeiro número inteiro: \n " ))
n2  =  int ( input ( "Digite ou segundo número inteiro: \n " ))
n3  =  float ( input ( "Digite ou número real: \n " ))
operação1  = ( n1  *  2 ) * ( n2  /  2 )
print ( "O valor do produto do dobro do primeiro com a metade do segundo é: "  +  str ( operação1 ))
operação2  = ( n1  *  3 ) + ( n3 )
print ( "O valor da soma do triplo do primeiro com o terceiro é: "  +  str ( operação2 ))
operação3  =  n3  **  3
print ( "O valor do terceiro elevador ao cubo é: "  +  str ( operação3 ))

##Este código calcula o peso ideal usando a fórmula correta para homens e mulheres

gênero  =  int ( input ( "Qual seu gênero? \n 1 - Feminino \n 2 - Masculino \n " ))
if ( sexo  ==  1 ):
  altura  =  float ( input ( "Qual sua altura? \n " ))
  peso ideal  = ( 62,1  *  altura ) -  44,7
  print ( "O peso ideal para a altura"  +  str ( altura ) +  "é:"  +  str ( idealWeight ) +  "kgs" )

elif ( gênero  ==  2 ):
  altura  =  float ( input ( "Qual sua altura? \n " ))
  Peso ideal  = ( 72,7  *  altura ) -  58
  print ( "O peso ideal para a altura"  +  str ( altura ) +  "é:"  +  str ( idealWeight ) +  "kgs" )

else :
  print ( "Digite um código válido." )

##Este código usa uma regra de que se um pescador pescar mais de 50kg em uma corrida ele tem que pagar um preço excedente
##usando esta regra o código imprime o valor excedente e o preço a ser pago

fishingAmount  =  float ( input ( "Quantos quilos de peixe foram pescados? \n " ))
if ( pescaQuantidade  <  50 ):
  print ( "Não há multa para quantidades menores que 50kgs" )

else :
  superação  =  quantidade de pesca  -  50
  print ( "O valor em quilos excedente do permitido é:  " +  superação ) )
  priceOverrun  =  overrun  *  4
  print ( "O valor a ser pago devido a pesca excedente é: "  +  str ( priceOverrun ))

##Este código calcula a quantidade de tempo para baixar um arquivo através do tamanho e da velocidade do link

fileSize  =  float ( input ( "Qual o tamanho do arquivo a ser baixado em MB? \n " ))
linkSpeed  ​​=  float ( input ( "Qual a velocidade do seu link em Mbps? \n " ))
downloadTime  =  fileSize  / ( linkSpeed  ​​/  8 )
print ( "O tempo de download desse arquivo em minutos é: "  +  str ( downloadTime  /  60 ))