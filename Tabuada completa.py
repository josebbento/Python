novamente = 's'
contador = 0
a=13

n=int(input('insira um número: '))

print('-'*a)
print('{} * 0 = 0'.format(n))
print('-'*a)

while novamente == 's':
    contador = contador + 1
    print('{} * {} = {}'.format(n,contador,n*contador))
    print('-'*a)
    if contador % 10 == 0:
        novamente = input('deseja ver mais dez números? ').lower().strip()[0]       