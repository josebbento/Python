idades = 0
maioridade= 0
menosdevinte = 0

for a in range(1,5):
  print('------dados da {}ª pessoa------'.format(a))
  nome = input('seu nome: ')
  idade = float(input('sua idade: '))
  sexo = input('seu sexo (M/F): ').lower()
  print('')

  idades += idade

  if sexo == 'm' or sexo == 'masculino':
    if maioridade < idade:
      maioridade = idade
      maisvelhor = nome

  if sexo == 'f' or sexo == 'feminino':
    if idade < 20:
      menosdevinte += 1 
  

print('média das idades: {} anos'.format(idades/4))
print('o homem mais velhor: {}'.format(maisvelhor))
print('quantidade de mulheres menos de 20 anos: {}'.format(menosdevinte))