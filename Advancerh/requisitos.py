# -*- coding: UTF-8 -*-
import requests
import re
from bs4 import BeautifulSoup

def requisitos(lista_informacao):
    
    lista_def = []
    
    for requerir in lista_informacao:
        requerir = requerir.find_all('p')
        requerir = str(requerir)
        
        cleanr = re.compile('<.*?>')
        cleantext = re.sub(cleanr, '', requerir)
        deletar = '[]'
        
        for i in range(0,len(deletar)):
            cleantext = cleantext.replace(deletar[i], "")
        
        cleantext = cleantext.replace("mD", "m D")
        cleantext = cleantext.replace(".,", ".")
        cleantext = cleantext.replace(" ::, ", "" + "\n\n")

        for i in range(0, len(cleantext)):
            cleantext = cleantext.replace(" ::  ", "")
            cleantext = cleantext.replace(" :: ", "")

        lista_def.append(cleantext + "\n\n========================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================\n\n")
    
    return lista_def