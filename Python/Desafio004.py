from curses.ascii import islower

a = input('Digite algo:')
print('O tipo primitivo desse valor', type(a))
print('So tem espaços?', a.isspace())
print('E um numero?', a.isnumeric())
print('E alfabetico?', a.isalpha())
print('Esta em maisculas?', a.isupper())
print('Esta em minusculas?', islower())

