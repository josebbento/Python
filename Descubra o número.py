from random import randint
continuar = 's'

while continuar == 's':
   print('''=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
| ADIVINHANDO O NÚMERO V 2.0  |
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

Tente acertar o número pensado pelo pc

''')

  chutes = 1

  j2 = str(randint(0,10))

  j1 = input ('insira um chute entre 0 e 10: ')

  while j1 != j2:
    if j1 < j2:
      j1 = input ('é maior que {}, tente de novo: '.format(j1))
    else:
      j1 = input ('é menor que {}, tente de novo: '.format(j1))
    chutes += 1
  
  print('Você acertou. Parabéns\nVocê precisou de {} tentativas'.format(chutes))
  continuar = input ('deseja jogar de novo? ').lower().strip()[0]
  if continuar == 's':
    print('\n---------------------------------\n')