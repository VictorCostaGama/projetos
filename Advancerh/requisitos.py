# -*- coding: UTF-8 -*-
import requests
import re
from bs4 import BeautifulSoup

def requisitos(lista_informacao):
    
    lista_def = []
    
    for requerir in lista_informacao:
        requerir = requerir.find_all('p')
        requerir = str(requerir)
        find = '</strong></p>, '
        posicao = int(requerir.index(find) + len(find))
        requerir = requerir[posicao : posicao + len(requerir)]
        
        cleanr = re.compile('<.*?>')
        cleantext = re.sub(cleanr, '', requerir)
        deletar = '[]'
        
        for i in range(0,len(deletar)):
            cleantext = cleantext.replace(deletar[i], "")
        
        cleantext = cleantext.replace("mD", "m D")
        cleantext = cleantext.replace(".,", ".")
        cleantext = str(cleantext)
        lista_def.append(cleantext)
    
    return lista_def