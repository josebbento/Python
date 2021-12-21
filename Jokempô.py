import random
#jogador
print('''|===================================|
|          Jogo de Jokempô          |
|===================================|

''')
input('aperte enter para começar a jogar: ')
jogador = input('escolha entre Pedra, Papel e Tesoura: ').strip().lower()

#CPU
opções = ['Pedra','Papel','Tesoura']
cpu = random.choice(opções)
print('C.P.U.: {}'.format(cpu))

print('''===================
 {} X {}'''.format(jogador.title(),cpu))
#escolha do ganhador
#  jogador == pedra
if jogador == 'pedra' or jogador == '1°' or jogador == '1' or jogador == '1° opção' or jogador == 'opção 1':
  if cpu == 'Pedra':
    print('\033[37 mEMPATE')

  if cpu == 'Tesoura':
    print('\033[32 mVOCÊ GANHOU')

  if cpu == 'Papel':
    print('\033[31 mC.P.U. GANHOU')

#  jogador == papel
if jogador == 'papel' or jogador == '2°' or jogador == '2' or jogador == '2° opção' or jogador == 'opção 2':
  if cpu == 'Papel':
    print('\033[37m EMPATE')

  if cpu == 'Pedra':
    print('\033[32m VOCÊ GANHOU')

  if cpu == 'Tesoura':
    print('\033[31m C.P.U. GANHOU')

#  jogador == tesoura
if jogador == 'tesoura' or jogador == '3°' or jogador == '3' or jogador == '3° opção' or jogador == 'opção 3':
  if cpu == 'Tesoura':
    print('\033[37m EMPATE')

  if cpu == 'Papel':
    print('\033[32m VOCÊ GANHOU')

  if cpu == 'Pedra':
    print('\033[31m C.P.U. GANHOU')

print('\033[37m='*(8*2+3))