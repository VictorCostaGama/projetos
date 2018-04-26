import requests
from bs4 import BeautifulSoup
from arielleProd import raspagens

url = 'http://www.arielle.com.br/produtos/listar?infinite=true'

lista_url_produto = []

for i in range(1, 7):

    parm = {'pag':str(i)}

    r = requests.get(url, params=parm)

    soup = BeautifulSoup(r.text, 'lxml')

    url_prod = soup.find_all('div', class_='produto')
    
    for url_p in url_prod:
        url_produto = url_p.a.get('href')
        lista_url_produto.append(url_produto)

raspagens(lista_url_produto)