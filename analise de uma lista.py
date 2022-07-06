s = c = maior = menor = 0
f = ''

while f != 'n' and f != 'nao' and f != 'não':
    f = ''
    n = float(input('insira um número: '))
    s += n
    c += 1
    l = n

    if maior < n:
        maior = n
    if c == 1 or menor > n:
        menor = n

    while f != 'n' and f != 's':
        f = input('diseja continuar: ').lower().strip()[0]
        if f != 'n' and f != 's':
            print('comando não entendido', end=', ')

m = s/c
print('''
Quantidade de números digitados: {}
Média: {}
Maior valor: {}
Menor valor: {}'''.format(c, m, maior, menor))
