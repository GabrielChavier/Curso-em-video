#crie um programa que leia um numero real qualquer pelo teclado e mostre na tela sua porcao inteira
import math
num = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua porção inteira e {}'.format(num, math.trunc(num)))

#outro modo de fazer
from math import trunc
num = float(input('Digite um Valor: '))
print('O valor digitado foi {} e a sua poção inteira e {}'.format(num,trunc(num)))

#outro  modo de fazer
num = float(input('Digite um valor'))
print('O valor digitado foi {} e a sua poção inteira e {}'.format(num, int(num)))