sair = 'n'

print('''=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
|  Calculadora de fatoriais   |
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

''')

while sair != 's' and sair != 'sim' and sair != 'com certeza' and sair != 'claro':

  r = 1

  n = int(input('insira um número: '))
  
  print('{}! = '.format(n),end='')

  if n == 1:
    print(' 1')

  else:
    while n != 1:
      print('{} X '.format(n),end='')
      r *= n
      n -= 1
    
    print('1 = {}'.format(r))
  
  sair = input('deseja sair? ')
  print()