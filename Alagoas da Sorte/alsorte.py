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

for i in range(1, 10):
	a = '0' + str(i)
	c = 'O numero ' + a + ' = '
	print(c + str(l.count(a)))

for i in range(10, 61):
	a = str(i)
	c = 'O numero ' + a + ' = '
	print(c + str(l.count(a)))