import requests
from bs4 import BeautifulSoup
import sqlite3 as sql

conn = sql.connect('udemy.db')
cur = conn.cursor()
# cur.execute("create table python( question text ,answer text ,page text)")
# print("Table created")

url = "https://www.udemy.com/topic/python/"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

question = []
answer = []
rdata = []


questions = soup.find_all('span', {"class":"udlite-accordion-panel-title"})
for question in questions:
    question.append(question.text)


answers = soup.find_all('div', {"class":"udlite-text-sm questions-and-answers--answer--2PMFk"})
for answer in answers:
    answer.append(answer.text)

for rd in soup.find_all('div', {'class': 'udlite-heading-md questions-and-answers--link--11XUK'}):
    link = rd.find('a', href=True)
    if link is None:
        continue
    rdata.append(link['href'])


for q, a, r in zip(question, answer, rdata):
    question = q
    answer = a
    page = r

    cur.execute('''INSERT  INTO python values(?,?,?)''', (question, answer, page))
    print('complete')


conn.commit()
cur.execute('''select * from python''')
results = cur.fetchall()
print(results)
conn.close()
