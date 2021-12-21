print('=-='*15)

salário = float (input('insira seu salário (mensal): R$'))
produto = float (input('insira o valor da casa: R$'))
tempo = float (input('insira o por quanto tempo pagará (anos): '))

prestação = produto / (tempo * 12)
n = salário * 30 / 100

print('valor da prestação: R${:.2f}'.format(prestação))

if prestação > n:
  print('\033[31mEMPRÉSTIMO NEGADO')
else:
  print('\033[32mEMPRÉSTIMO APROVADO\033[37m')
  
print('=-='*15)