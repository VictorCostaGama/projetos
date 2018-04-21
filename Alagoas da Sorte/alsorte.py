import requests
from bs4 import BeautifulSoup

url = 'http://site.alagoasdasorte.com.br/index.php/resultados'

r = requests.get(url)

soup = BeautifulSoup(r.text, 'lxml')

system = soup.find_all('div', id='noshow')

l = []

for response in system:
	rts = response.find_all('td')
	for rt in rts:
		tr = rt.get_text()
		l.append(tr)
lst = []
for i in range(1, 10):
	a = '0' + str(i)
	c = 'O numero ' + a + ' = '
	t = c + str(l.count(a))
	lst.append(t)

for i in range(10, 61):
	a = str(i)
	c = 'O numero ' + a + ' = '
	s = c + str(l.count(a))
	lst.append(s)

stre = soup.find_all('div', id='resultados_edicao')

for ert in stre:
	title = ert.p.get_text()

arq = open('Padroes.txt', 'w')
arq.write('|-------------------------------------------------------------------------------------------------------------------|')
arq.write('\n|                                                                                                                   |\n|                                    LISTA '+ title + '                                            |')
arq.write('\n|                                                                                                                   |\n|-------------------------------------------------------------------------------------------------------------------|\n')
arq.write('|                                                                                                                   |\n|                                                                                                                   |\n')
for i in range(0, len(lst)):
	if i ==0:
		arq.write('|')
	if i == 5 or i == 10 or i == 15 or i == 20 or i == 25 or i == 30 or i == 35 or i == 40 or i == 45 or i == 50 or i == 55 or i == 60 or i == 61:
		arq.write('|\n|                                                                                                                   |\n|')

	arq.writelines('    ' + lst[i])
	arq.write('    ')
	
arq.write('|\n|                                                                                                                   |\n|-------------------------------------------------------------------------------------------------------------------|')
arq.close()
		
	