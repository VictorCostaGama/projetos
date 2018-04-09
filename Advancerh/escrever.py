# -*- coding: UTF-8 -*-
def escrever(req):
    arq = open('vagas.txt', 'w', encoding="iso8859-1")
    arq.writelines(req)
    arq.close()