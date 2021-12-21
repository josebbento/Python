import random
lista = []
for p in range (1,5):
  a = input('o nome do {}° aluno: '.format(p))
  lista += a
escolhido=random.choice(lista)
print('aluno escolhido:',escolhido)