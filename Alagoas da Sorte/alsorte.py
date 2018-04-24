import requests
from bs4 import BeautifulSoup
from alst import informacao


url = 'http://site.alagoasdasorte.com.br/index.php/resultados'
	
rqt = requests.get(url)

soup = BeautifulSoup(rqt.text, 'lxml')

system = soup.find_all('select')

valor = []

for data in system:
	date = data.find_all('option')
	for dat in date:
		d = dat.get('value')
		if d != '0':
			valor.append(d)
l_g = []

arq = open('Padroes.txt', 'w')

for i in range(0, len(valor)):
	p = valor[i]
	data = {'resultado_id':p}

	r = requests.post(url, data=data)

	soup = BeautifulSoup(r.text, 'lxml')

	g = informacao(soup, l_g)

lst = []

for i in range(1, 10):
	a = '0' + str(i)
	c = 'O numero ' + a + ' = '
	t = c + str(g.count(a))
	lst.append(t)
		
for i in range(10, 61):
	a = str(i)
	c = 'O numero ' + a + ' = '
	s = c + str(g.count(a))
	lst.append(s)

arq = open('Padroes.txt', 'a')
arq.write('|-----------------------------------------------------------------------------------------------------------------------------|')
arq.write('\n|                                                                                                                             |\n|                                                  TABELA  GERAL                                                              |')
arq.write('\n|                                                                                                                             |\n|-----------------------------------------------------------------------------------------------------------------------------|\n')
arq.write('|                                                                                                                             |\n|                                                                                                                             |\n')
for i in range(0, len(lst)):
	if i == 0:
		arq.write('|')
	if i == 5 or i == 10 or i == 15 or i == 20 or i == 25 or i == 30 or i == 35 or i == 40 or i == 45 or i == 50 or i == 55 or i == 60 or i == 61:
		arq.write('|\n|                                                                                                                             |\n|')

	arq.writelines('    ' + lst[i])
	arq.write('    ')
		
arq.write('|\n|                                                                                                                             |\n|-----------------------------------------------------------------------------------------------------------------------------|')
arq.close()

arq.close()