import requests
from bs4 import BeautifulSoup


domain = 'http://ibash.org.ru/'
def pibash(keywords):
    #keywords=['Python', 'питон', 'SQL']
    rezult = list()
    N = 3
    p = 1
    while len(rezult) <= N:
        url = f'{domain}?page=' + str(p)
        p += 1
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')


        quotes = soup.find_all(class_ = 'quotbody')

        for quote in quotes:
            q=str(quote).lower()
            for kw in keywords:
                if kw in q:
                    rezult.append(quote)
                    break  #без него одна цитата может попасть в список несколько раз


    mess=""
    for rez in rezult[N]:
        mess += rez.get_text() + '\n'
    return mess
