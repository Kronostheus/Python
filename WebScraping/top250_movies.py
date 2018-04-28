import requests
import pandas as pd

from bs4 import BeautifulSoup

r = requests.get('https://www.imdb.com/chart/top?ref_=nv_mv_250_6')
soup = BeautifulSoup(r.text, 'html.parser')

results = soup.find_all('tr')[1:-2]
records = []


for entry in results:
    titleColumn = entry.find('td', {'class':'titleColumn'})
    data = titleColumn.find('a')

    rating = entry.find('strong').contents[0]
    year = titleColumn.find('span').contents[0][1:-1]
    url = 'https://www.imdb.com' + data['href']
    director, actors = data['title'].split(' (dir.),')
    title = data.contents[0]
    records.append((title, rating, year, actors.strip(), director, url))

data = pd.DataFrame(records, columns=['Title', 'Rating', 'Year', 'Actors', 'Director','URL'])
data.to_csv('top250_movies.csv', encoding='utf-8')