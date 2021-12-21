#variaveis
altura = input('insira sua altura em metros: ').lower()
altura = float (altura.replace('m','').replace('etro','').replace('s',''))
massa = input('insira sua massa corporal em Kg: ').lower()

#massa escrita -> massa valor
if 'kg' in massa:
  massa = float (massa.replace('kg',''))
elif 'quilos' in massa:
  massa = float (massa.replace('quilos',''))
elif 'quilogramas' in massa:
  massa = float (massa.replace('quilogramas',''))
else:
  massa = float (massa)

#imc
imc = massa/altura**2
print()
print('seu imc:',imc)

#resultados
if imc < 18.5:
  print('\033[34mvocê está abaixo do peso')
elif imc <= 25:
  print('\033[32mvocê está com o peso ideal')
elif imc <= 30:
  print('\033[33mvocê está com sobrepreso')
elif imc <= 40:
  print('\033[31mvocê está com obesidade')
else:
  print('\033[31m!!!RISCO SÉRISSIMO DE SÁUDE!!!\nOBESIDADE MÓRBIDA')

#massa ideal
if imc < 18.5 or imc > 25:
  print('\033[37mpeso ideal minimo: {:.1f}Kg'.format(18.5*altura**2))
  print('peso ideal máximo: {:.1f}Kg'.format(25*altura**2))