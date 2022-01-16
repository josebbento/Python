print('=-='*16)
print('|               TENTE ACERTAR      1.0         |')
print('=-='*16)
print('|-Tente acertar o número que a CPU pensa       |')
print('|-Os números possiveis: 0, 1, 2, 3, 4, 5       |')
print('=-='*16)
print()
import random
n = float (input('insira um número: '))
gerador = random.randint(0,5)
print('número pensado:',gerador)
print()
print('=-='*16)
if gerador == n:
  print('|                 Você ganhou                  |')
else:
  print('|                C.P.U. ganhou                 |')
print('=-='*16)