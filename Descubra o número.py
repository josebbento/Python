import random
desistir = 'n'´
continuar = 's'
#cabesário-------------------------------------
while continuar == 's':
  print('''=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
| ADIVINHANDO O NÚMERO V 3.1  |
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

Tente acertar o número pensado pelo pc

''')
#menu-----------------------------------------
  print('''[1] nível fácil (0-10)
[2] nível médio (0-100)
[3] nível difícil (0-1000)
[4] nível expert (0-10), mas é pensado em outro número após o erro
[5] nível editável (x-y)''')
  opção =  str (input ('insira o nível que deseja jogar: ').lower().strip())
#variaveis com valores "fixos"---------------
  chutes = 1
  x = 0
#jogador2------------------------------------
  if opção == '1' or opção == '[1]' or opção == 'nível fácil' or opção == 'fácil':
    y = 10
  elif opção == '2' or opção == '[2]' or opção == 'nível médio' or opção == 'médio':
    y = 100
  elif opção == '3' or opção == '[3]' or opção == 'nível difícil' or opção == 'difícil':
    y = 1000
  elif opção == '4' or opção == '[4]' or opção == 'nível expert' or opção == 'expert':
    y = 10
  elif opção == '5' or opção == '[5]' or opção == 'nível editável' or opção == 'editável':
    x = int(input('insira o valor minimo(x): '))
    y = int(input('insira o valor máximo(y): '))
  j2 = int(random.randint(x,y))
#jogador1------------------------------------
  j1 = int (input ('insira um chute: ').strip())
#comparador----------------------------------
  while j1 != j2:
    print('\nvocê errou')
    if opção == '4' or opção == '[4]' or opção == 'nível expert' or opção == 'expert':
      j2 = int(random.randint(x,y))
    if chutes%10 == 0:
      desistir = input('deseja desistir? ').lower().strip()[0]
      if desistir == 's':
        break
    else:
      if j1 < j2:
        comparação = 'maior'
      else:
        comparação = 'menor'
      print('tente com um número {} que {}'.format(comparação,j1))
    j1 = int (input ('insira um chute: '))
    chutes += 1
#final---------------------------------------
  if desistir == 's':
    print()
    print('\nvocê perdeu')
    continuar = input('deseja continuar? ').lower().strip()[0]
  else:
    print('\nvocê venceu\nvocê presicou de {} tentativas'.format(chutes))
    continuar = input('deseja continuar? ').lower().strip()[0]
  if continuar == 's':
    print('--------------------------------------------------\n\n')