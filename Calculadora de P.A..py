print('''|===========================|
| Calculadora de P.A. V 1.1 |
|===========================|

''')
sair = ''

while sair != 's' and sair != 'sim' and sair != 'com certeza' and sair != 'claro':

    contador = 0
    quantos = ''

    termo1 = float (input ('insira o primeiro termo da P.A.: '))

    razão = float (input ('insira a razão da P.A.: '))

    print('P.A. de {}: '.format(termo1),end='')

    while contador != 9:
        print('{}, '.format(termo1 + razão * contador),end = '')
        contador += 1
    print(termo1 + razão * contador)
    print()

    while quantos != 0 :
        quantos = float (input ('insira a quantidade de termos a mais que gostaria de ver: '))
        
        if quantos != 0:
          quantos += contador
          while contador < quantos-1:
            contador += 1
            print('{}, '.format(termo1 + razão * contador),end = '') 
          contador += 1
          print(termo1 + razão * contador)
          
        print()

    sair = input('deseja sair? ')
    print('\n')