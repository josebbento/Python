h=float(input('insira a altura da sua parede em metros, só o valor: '))
l=float(input('insira a largura da sua parede em metros, só o valor: '))
a=h*l
r=a%2
print('')
print('a área da sua parede é de {}m².'.format(a))
if a<=1:
  print('você precisa 1 lata de tinta')
elif r == 0.0:
  print('você precisa {} latas de tinta'.format(a/2))
elif r != 0.0:
  total = a // 2 + 1
  print('você precisa {} latas de tinta'.format(total))