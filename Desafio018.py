#faça um programa que leia o um Ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse Ângulo
from math import radians, sin, cos, tan
ângulo = float(input('Digite o ângulo que voce deseja: '))
seno = sin(radians(ângulo))
print('O ângulo de {} tem SENO de {:.2f}'.format(ângulo, seno))
cosseno = cos(radians(ângulo))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(ângulo, cosseno))
tangente = tan(radians(ângulo))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(ângulo, tangente))

# outra forma
from math import radians,cos,sin,tan
angulo = float(input('Digite o angulo: '))
c = radians(angulo)
print(f'O seno é igual {sin(c):.2f} o coseno é igual {cos(c):.2f} e a tangente é igual a {tan(c):.2f}')