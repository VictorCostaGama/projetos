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
  
req = requisitos(lista_informacao)

escrever(req)