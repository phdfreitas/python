#
# Created by Pedro Freitas on 20/01/2020.
#

def notas(* ficha, situacao = False):
	"""->Função para analisar notas e situações de vários alunos.
		:param ficha: uma ou mais notas dos alunos (aceira mais de uma)
		:param situacao: valor opcional, por padrão False, se for True vai mostrar a situação do aluno 
		:return: dicionário com várias informações sobre a situação da turma.
	"""
	boletim = {}
	media = 0
	boletim['Total'] = len(ficha)
	boletim['Maior'] = max(ficha)
	boletim['Menor'] = min(ficha)
	for n in ficha:
		media += n
	media = media / len(ficha)
	boletim['Media'] = media

	if situacao == False:
		return boletim
	else:
		if media >= 7:
			boletim['Situacao'] = 'BOA'
		elif (media >= 5 and media < 7):
			boletim['Situacao'] = 'RAZOÁVEL'
		else:
			boletim['Situacao'] = 'RUIM'
		return boletim


print(notas(3.5, 10, 6.5, situacao = True))
#print(help(notas))