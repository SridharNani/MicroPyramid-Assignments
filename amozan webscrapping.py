import requests
from bs4 import BeautifulSoup
import sqlite3

conn = sqlite3.connect("udemy4.db")
c = conn.cursor()

c.execute("CREATE TABLE oneplus(m_name text,m_price real,m_rating text)")
# conn.close()
print("table crated")

Url='https://www.amazon.in/s?bbn=1389401031&rh=n%3A1389401031%2Cp_89%3AOnePlus&dc&qid=1628135476&rnid=3837712031&ref=lp_1389401031_nr_p_89_0'

def get_scrap(Url):
    res = requests.get(url=Url).content
    soup = BeautifulSoup(res, 'html.parser')
    names = []
    prices = []
    ratings = []
    for name in soup.find_all('a', href=True, attrs={'class':'a-link-normal a-text-normal'}):
        nm = name.find('span', attrs={'class':'a-size-base-plus a-color-base a-text-normal'})
        names.append(nm.text)

    for price in soup.find_all('a', href=True, attrs={'class':'a-size-base a-link-normal a-text-normal'}):
        pr = price.find('span', attrs={'class':'a-price-whole'})
        prices.append(pr.text)

    for rating in soup.find_all('i', attrs={'class':'a-icon a-icon-star-small a-star-small-4 aok-align-bottom'}):
        rt = rating.find('span', attrs={'class':'a-icon-alt'})
        print(rt.text)
        ratings.append(rt.text)

    for n, p, r in zip(names, prices, ratings):
        name = n
        price = p
        rating = r
        print(n)
        print(p)
        print(r)
        c.execute('''INSERT INTO oneplus VALUES (?,?,?)''', (name, price, rating))




get_scrap(Url)

conn.commit()
print('complete')
c.execute('''SELECT * FROM oneplus''')
results = c.fetchall()
print(results)
conn.close()
#