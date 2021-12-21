import time
ano = float (input('insira um ano, ano 0 = ano atual do pc: '))
if ano == 0:
  ano = int (time.strftime("%Y"))
  print('atual ano: {}'.format(ano))
if ano % 100 == 0:
  if ano % 400 == 0:
      print('o ano é bixesto')
  else:
      print('o ano não é bixesto')
else:
  if ano % 4 == 0:
      print('o ano é bixesto')
  else:
      print('o ano não é bixesto')