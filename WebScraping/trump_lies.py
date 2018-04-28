import requests
import pandas as pd

from bs4 import BeautifulSoup

r = requests.get('https://www.nytimes.com/interactive/2017/06/23/opinion/trumps-lies.html')
soup = BeautifulSoup(r.text, 'html.parser')

# <span class="short-desc">
#   <strong> DATE </strong> LIE
#   <span class="short-truth">
#       <a href="URL"> EXPLANATION </a>
#   </span>
# </span>

results = soup.find_all('span', attrs={'class':'short-desc'})

records = []

for result in results:
    date = result.find('strong').text[0:-1] + ', 2017'
    # contents extracts a list with everything separated
    lie = result.contents[1][1:-2]
    explanation = result.find('a').text[1:-1]
    url = result.find('a')['href']
    records.append((date, lie, explanation, url))

data = pd.DataFrame(records, columns=['Date', 'Lie', 'Explanation', 'URL'])
data['Date'] = pd.to_datetime(data['Date'])
data.to_csv('trump_lies.csv', index=False, encoding='utf-8')