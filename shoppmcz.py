# encoding: utf-8
import urllib.request
import requests
from bs4 import BeautifulSoup

url = 'http://www.maceioshopping.com/cinema/'
r = requests.get(url)

soup = BeautifulSoup(r.text, 'lxml')

lista_informacao = soup.find_all('h4', class_='heading')

for link_filmes in lista_informacao:
    links = link_filmes.find_all('a')
    for link in links:
        url_filme = link.get('href')
        print("Url: " + url_filme + "\n")
        
        s = requests.get(url_filme)
        soup = BeautifulSoup(s.text, 'lxml')
        titulo = soup.find_all('header', class_='section-title large')
        
        for titulo_filme in titulo:
            filme = titulo_filme.find('h1', {'class':'heading'})
            nome_filme = filme.text
                
            print("Filme: " + nome_filme + "\n")
            
        t = requests.get(url_filme)
        soup = BeautifulSoup(t.text, 'lxml')
        descricao = soup.find_all('div', class_='story')

        for descricao_filme in descricao:
            sinopse = descricao_filme.find('p')
            sinopse_filme = sinopse.text
            break
        print("Sinopse: " + sinopse_filme + "\n")

        f = requests.get(url_filme)
        soup = BeautifulSoup(f.text, 'lxml')
        mais = soup.find_all('span', class_='meta-item meta-ratings')

        for informacoes_extra in mais:
            extras = informacoes_extra.find('strong')
            mais_extras = extras.text
            ultra_extra = informacoes_extra.find('a')
            mega_extra = ultra_extra.text
            print(mais_extras + " " + mega_extra + "\n")

        h = requests.get(url_filme)
        soup = BeautifulSoup(h.text, 'lxml')
        duracao = soup.find_all('span', class_='meta-item meta-duration')

        for duracao_filme in duracao:
            duracao_extra = duracao_filme.find('strong')
            m_duracao = duracao_extra.text
            
            content = str(duracao_filme)
            find = 'class="meta-item meta-duration"'
            posicao = int(content.index(find) + len(find))
            cont = content[ posicao : posicao  + 75]
            p = int(content.index(cont) + len(cont))
            local = content[ p : p + 5 ]

            print(m_duracao + " " + local + "\n")

        g = requests.get(url_filme)
        soup = BeautifulSoup(g.text, 'lxml')
        genero = soup.find_all('span', class_='meta-item meta-genres')

        for genero_filme in genero:
            genero1 = genero_filme.find('strong')
            g1 = genero1.text
            print(g1, end=" ")
            break
        for g_filmes in genero:
            genero2 = g_filmes.find_all('a')
            for gen_filmes in genero2:
                url_genero = gen_filmes.get('href')

                w = requests.get(url_genero)
                soup = BeautifulSoup(w.text, 'lxml')
                gen_ero = soup.find_all('div', class_='title')

                for url_g in gen_ero:
                    url_gen = url_g.find('h1')
                    gen_film = url_gen.text
                print(gen_film, end=" ")
            print("")
        print("================================================================================================================================================\n")