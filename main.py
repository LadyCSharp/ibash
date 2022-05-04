import requests
from bs4 import BeautifulSoup
import re
import pprint
p = 1
domain = 'http://ibash.org.ru/'
keywords=['Python', 'питон', 'SQL']
rezult = list()
N = 20
while len(rezult) <= N:
    url = f'{domain}?page=' + str(p)
    p += 1
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')


    quotes = soup.find_all(class_ = 'quotbody')

    for quote in quotes:
        q=str(quote)
        for kw in keywords:
            if kw in q:
                rezult.append(quote)
                break  #без него одна цитата может попасть в список несколько раз

i=1
with open('text.txt', 'wt') as f:
    for rez in rezult:
        print(i)

        print(rez.get_text())

        f.write(str(i)+" ")
        f.write(rez.get_text())
        f.write('\n')
        i += 1