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

    while f != 'n' and f != 'nao' and f != 'não' and f != 's' and f != 'sim':
        f = input('diseja continuar: ').lower()
        if f != 'n' and f != 'nao' and f != 'não' and f != 's' and f != 'sim':
            print('comando não entendido', end=', ')

m = s/c
print('''
Quantidade de números digitados: {}
Média: {}
Maior valor: {}
Menor valor: {}'''.format(c, m, maior, menor))
