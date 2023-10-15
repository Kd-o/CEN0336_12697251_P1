#!/usr/bin/env python3

#Objetivo do script: Calcular a area de um triangulo retangulo de lado 'a' e 'b', onde esses lados devem ter valor inteiro e menor que 500.

import sys #permite que valores sejam importados da linha de comando.

a = sys.argv[1] #valor do primeiro cateto.
b = sys.argv[2] #valor do segundo cateto.

if not (a.isdigit() and b.isdigit()):
    print(f'As entradas "{a}" e "{b}" deveriam ser numeros inteiros positivos, portanto, nem "floats" nem "str".') #if que verifica se um dos valores nao eh puramente numerico.
    exit() #Termina-se aqui, pois se nao a seguir ocorreriam erros.

c = int(a)
d = int(b) #Transforma 'a' e 'b' em inteiros.

if not (c < 500 and d < 500):
    print(f'Os valores de {a} ou {b} nao devem ser maior que 500.') #if que verifica se algum dos valores eh superior a 499.
else:
    print(f'A area do triangulo retangulo com lados a={a} e b={b}, eh',c*d/2) #Resultado caso tudo acima estaja de acordo.
