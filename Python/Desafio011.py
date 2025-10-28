larg = float(input('Largura da parede'))
alt = float(input('Altura da parede'))
area = larg * alt

print('Sua parede tem a dimesão de {} x {} e sua area e de {}'.format(larg, alt , area))
tinta = area / 2
print('Para pintar sua parede, voce precisará de  {} de tinta.'.format(tinta))