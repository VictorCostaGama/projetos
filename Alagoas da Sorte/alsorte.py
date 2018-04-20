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

arq = open('padroes.txt', 'w')
for i in range(0, len(lst)):
	if i == 6 or i == 12 or i == 18 or i == 24 or i == 30 or i == 36 or i == 42 or i == 48 or i == 54:
		arq.write('\n\n')

	arq.writelines(lst[i])
	arq.write('     ')
arq.close()
		
	