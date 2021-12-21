#--------------------------------inputs-----------------------------
média = input('qual é a média minima? ')
teste1 = float (input('quanto vale a primeira avaliação? '))
nota1 = float (input('insira a primeira nota: '))
teste2 = float (input('quanto vale a segunda avaliação? '))
nota2 = float (input('insira a segunda nota: '))
#-----------------------------média com porcentagem---------------
if '%' in média:
  média1 = float (média.replace('%',''))
  média1 = float (média1/100)
  médiaaluno = (nota1+nota2)/(teste1+teste2)
#-----------------------média sem porcentagem-----------------------
else:
  médiaaluno = float (teste1 + teste2)
#------------------------------resultados------------------------------
if médiaaluno < média1 * 60/100:
  resultado = '\033[31mREPROVADO'
elif médiaaluno < média1:
  resultado = '\033[33mRECUPERAÇÃO'
else:
  resultado = '\033[32mAPROVADO'
#-----------------------mostrar a média do aluno-----------------------
if '%' in média:
  print('média do aluno: {:.1f}%'.format(médiaaluno*100))
else:
  print('média do aluno: {:.1f}'.format(nota1+nota2))
#-----------------------mostrar a cituação do aluno-----------------------
print('aluno:',resultado)