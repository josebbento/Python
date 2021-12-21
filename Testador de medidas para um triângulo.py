a = float (input('insira a medida de um dos lados: '))
b = float (input('insira a medida do outro lados: '))
c = float (input('insira a medida do outro lados: '))

if a+b>c and a+c>b and b+c>a:
  print('é possivel formar um triangulo')
  if a == b == c:
    tipo = 'equilatero'
  elif a == b or a==c or b==c:
    tipo = 'isoceles'
  else:
    tipo = 'escaleno'
  print('tipo de triangulo: '+tipo)

else:
  if a + b <= c and a + c <= b:
    print('''não é possivel formar um triangulo
 motivo: 
 a + b > c    |    {} + {} > {} F
 a + c > b    |    {} + {} > {} F
 b + c > a    |    {} + {} > {} V
 '''.format(a,b,c,a,c,b,b,c,a))
    
  elif a + b <= c and b + c <= a:
    print('''não é possivel formar um triangulo
 motivo: 
 a + b > c    |    {} + {} > {} F
 a + c > b    |    {} + {} > {} V
 b + c > a    |    {} + {} > {} F
 '''.format(a,b,c,a,c,b,b,c,a))
    
  elif a + c <= b and b + c <= a:
    print('''não é possivel formar um triangulo
motivo: 
a + b > c    |    {} + {} > {} V
a + c > b    |    {} + {} > {} F
b + c > a    |    {} + {} > {} F
'''.format(a,b,c,a,c,b,b,c,a))
    
  else:
    if a + b <= c:
      print('''não é possivel formar um triangulo
motivo: 
a + b > c    |    {} + {} > {} F
a + c > b    |    {} + {} > {} V
b + c > a    |    {} + {} > {} V
'''.format(a,b,c,a,c,b,b,c,a))
    
    elif a + c <= b:
      print('''não é possivel formar um triangulo
motivo: 
a + b > c    |    {} + {} > {} V
a + c > b    |    {} + {} > {} F
b + c > a    |    {} + {} > {} V
'''.format(a,b,c,a,c,b,b,c,a))
    
    else:
      print('''não é possivel formar um triangulo
motivo: 
a + b > c    |    {} + {} > {} V
a + c > b    |    {} + {} > {} V
b + c > a    |    {} + {} > {} F
'''.format(a,b,c,a,c,b,b,c,a))