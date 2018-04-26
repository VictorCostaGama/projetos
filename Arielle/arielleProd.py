import requests
from bs4 import BeautifulSoup

def raspagens (lista_url_produto):
    
    for i in range(0, len(lista_url_produto)):

        url_prod = lista_url_produto[i]

        r = requests.get(url_prod)

        soup = BeautifulSoup(r.text, 'lxml')

        nome_produto = soup.h2.get_text()

        print(nome_produto)