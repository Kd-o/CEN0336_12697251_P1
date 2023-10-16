#!/usr/bin/env python3

import sys #Permite importar da linha de codigo.

w = sys.argv[1]
a = sys.argv[2]
b = sys.argv[3]
c = sys.argv[4]
d = sys.argv[5]
e = sys.argv[6]
f = sys.argv[7] #Importamos os 7 elementos conforme definido

s = w.upper() #Por precaucao, fazem-se todas as letras da sequencia maiusculas

if not (s.isalpha and s.count('A') > 0 and s.count('G') > 0 and s.count('T') > 0):
    print('O primeiro elemento deve ser uma sequencia contendo pelo menos "A", "G" e "T".') #Testa se a sequencia eh formada de letras e tem pelo menos 'A', 'G' e 'T' que serao necessarios futuramente. Nao achei que valia o esforco testar, por exemplo, se a sequencia nao contem "P" ou alguma outra letra invalida.
    exit() #Caso ocorra da sequencia estar incorreta, nao faz sentido continuar

if not (a.isdigit() and b.isdigit() and c.isdigit() and d.isdigit() and e.isdigit() and f.isdigit()):
    print('O elemento segundo ate o setimo devem ser numeros inteiros diferentes e positivos.') #Testa se todos os valores dos elementos 2 ao 7 sao numericos.
    exit() #Caso nao sejam numericos, nao faz sentido continuar

A = int(a)
B = int(b)
C = int(c)
D = int(d)
E = int(e)
F = int(f) #O sys.argv sempre importa 'str', portanto transformei os valores em numeros inteiros.

nums = [A,B,C,D,E,F]
i = sorted(nums) #Fiz uma lista com os numeros importados para poder ordena-la, assim os numeros poderiam vir em qualquer ordem.

if (max(i) > len(s)):
    print('O maior elemento dever ser menor que o tamanho da sequencia.') #O ultimo teste verifica se o limite do exon nao esta alem da sequencia
    exit() #Caso esteja, nao faz sentido continuar

CDS1_CDS2 = s[i[1]:i[2]-1]
CDS2_CDS3 = s[i[3]:i[4]-1] # Para fins de organizacao, criei 2 variaveis dos introns de interesse entre os intervalos. Usei da lista "i" pois os valores poderiam estar em qualquer ordem

#A partir de agora, basta imprimir as informacoes desejadas

print('A sequencia entre CDS1 e CDS2 eh', CDS1_CDS2)
if s[i[1]:i[1]+2] == 'GT':
    print('(3) A sequencia entre CDS1 e CDS2 inicia-se com "GT".')
if s[i[2]-3:i[2]-1] == 'AG':
    print('(3) A sequencia entre CDS1 e CDS2 termina-se com "AG".') #Para a questao 3.

print('A sequencia entre CDS2 e CDS3 eh', CDS2_CDS3)
if s[i[3]:i[3]+2] == 'GT':
    print('(4) A sequencia entre CDS2 e CDS3 inicia-se com "GT".')
if s[i[4]-3:i[4]-1] == 'AG':
    print('(4) A sequencia entre CDS2 e CDS3 termina-se com "AG".') #Para questao 4.

if (s[i[1]:i[1]+2] == 'GT' and s[i[2]-3:i[2]-1] == 'AG' and s[i[3]:i[3]+2] == 'GT' and s[i[4]-3:i[4]-1] == 'AG'): #Pelo jeito que estava escrito na questao, todos deveriam ser verdadeiros ao mesmo tempo.
    print('As condicoes (3) e (4) sao verdadeiras, portanto a sequencia de concatenada de exons eh:')
    print(s[i[0]-1:i[1]]+s[i[2]-1:i[3]]+s[i[4]-1:i[5]]) #Para a questao 5.
