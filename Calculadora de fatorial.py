r=1;n=int(input('insira um número inteiro: '))
print('{}! = '.format(n),end='')
for a in range (n,1,-1):
    print('{} X '.format(a),end='')
    r*=a
print('1 = {}'.format(r))