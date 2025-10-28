#O mesmo professor do desafio anterior quer sortear a ordem de apresentacao de trabalho dos alunos. faça um programa  que leia o nome dos quatro alunos e mostre a ordem sorteada
import random
n1 = str(input('Digite o primeiro nome: '))
n2 = str(input('Digite o segundo nome: '))
n3 = str(input('Digite o terceiro nome: '))
n4 = str(input('Digite o quarto nome: '))
lista = [n1, n2, n3, n4]
random.shuffle(lista)
print('A ordem de apresentação será')
print(lista)

#outro metodo
from random import shuffle
n1 = str(input('Primeiro nome: '))
n2 = str(input('Segundo nome: '))
n3 = str(input('Terceiro nome: '))
n4 = str(input('Quarto nome: '))
lista = [n1, n2, n3, n4]
shuffle(lista)
print('A ordem de apresentação será')
print(lista)