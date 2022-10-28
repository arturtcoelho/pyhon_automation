import requests
from bs4 import BeautifulSoup

import traceback

def get_pratos():

    pratos = []
    count = -1

    url = "https://pra.ufpr.br/ru/ru-centro-politecnico/"
    page = requests.get(url)

    soup = BeautifulSoup(page.content, "html.parser")
        
    cardapios = soup.find_all('figure', 'wp-block-table')
    hoje = cardapios[0]
    linhas = hoje.find('table').find('tbody').find_all('td')
    for prato in linhas:
        if prato.find('strong'):
            count+=1
            pratos.append([])
        pratos[count].append(str(prato.text))

    return pratos

if __name__ == '__main__':
    try:
        get_pratos()

    except Exception:
        traceback.print_exc()
