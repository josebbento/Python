print('''==========| maquina de somar |==========)

(use ponto no lugar da virgula)')

''')

n1 = float (input('insira um número: '))
n2 = float (input('insira um número: '))

n4 = n1 + n2

maisum = input('deseja inserir mais um número (s/n)? ').lower()[0]

while maisum == 's':
    n3 = float (input ('insira um número: '))
    n4 += n3
    maisum = input('deseja inserir mais um número (s/n)? ').lower()[0]

print ('Resultado:',n4)