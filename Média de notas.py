n1=float(input('insira a 1° nota: '))
n2=float(input('insira a 2° nota: '))
p=input('quantas casas depois da virgula é usado? ')
print('a média das notas, {:.{}f} e {:.{}f}, é {:.{}f}'.format(n1,p,n2,p,(n1+n2)/2,p))