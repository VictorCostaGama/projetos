# -*- coding: UTF-8 -*-
def escrever(lista, req):
    arq = open('vagas.txt', 'w', encoding="iso8859-1")
    for i in range(0, len(lista)):
        arq.writelines(lista[i])
        arq.write("\n\n")
        arq.writelines(req[i])
        arq.write("\n\n========================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================\n\n")
    arq.close()