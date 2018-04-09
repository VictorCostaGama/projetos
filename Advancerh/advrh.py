# -*- coding: UTF-8 -*-
import urllib.request
import requests
from bs4 import BeautifulSoup
from escrever import escrever
from requisitos import requisitos

url = 'http://www.advancerh.com.br/vagas-de-emprego.php'
r = requests.get(url)

soup = BeautifulSoup(r.text, 'lxml')

lista_informacao = soup.find_all('section', align='left')

lista = []

for vagas in lista_informacao:
    nome_vaga = vagas.find('p')
    nome_vaga = nome_vaga.text
    deletar = '::'

    for i in range(0, len(deletar)):
        nome_vaga = nome_vaga.replace(deletar[i], "")
    lista.append(nome_vaga)
req = requisitos(lista_informacao)
escrever(lista, req)