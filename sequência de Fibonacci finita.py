sair = ''

while sair != 's' and sair != 'sim':
  n1 = 0
  n2 = 0
  n3 = 0

  c1 = 0
  c2 = float(input('insira quantos números da sequência de Fibonacci: '))

  while c1 < c2:
    
    n2 = n3 + n1
    print(n2)

    c1 += 1

    if n1 == 0 :
      n1=1

    if c1 < c2:   
      n3 = n1 + n2
      print(n3)
      c1 += 1

    if c1 < c2:
      n1 = n2 + n3
      print(n1)
      c1 += 1

  sair = input('deseja sair do programa? ').lower()
  print()