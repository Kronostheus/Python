import requests
import time
import pandas as pd
from bs4 import BeautifulSoup

results = []

def getRequest(page):
    try:
        url = 'http://www.metacritic.com/browse/games/release-date/available/ps4/metascore?page=' + str(page)
        # defining user-agent to avoid 403 Forbidden
        request = requests.get(url, headers={'User-agent': 'Mozilla/5.0'})
        request.raise_for_status()
        return request
    except requests.exceptions.RequestException as err:
        print("OOps: Something Else",err)
    except requests.exceptions.HTTPError as errh:
        print("Http Error:",errh)
    except requests.exceptions.ConnectionError as errc:
        print("Error Connecting:",errc)
    except requests.exceptions.Timeout as errt:
        print("Timeout Error:",errt)

def getSoup(request):
    soup = BeautifulSoup(request.text, 'html.parser')
    results = soup.find_all('li', attrs={'class':'game_product'})
    return results

def getData(soup):
    for game in soup:
        nameUrl = game.find('a')
        url = 'http://www.metacritic.com' + nameUrl['href']
        name = nameUrl.text.strip()
        metascore = game.find('div', attrs={'class':'metascore_w'}).text
        score = game.find('span', attrs={'class':'textscore'}).text
        # avoid games with little or no User Reviews
        if score == 'tbd':
            continue
        userscore = int(eval(score) * 10)
        results.append((name, metascore, userscore, url))

def exportCSV(data):
    records = pd.DataFrame(data, columns=['Name', 'MetaScore', 'UserScore', 'URL'])
    records.to_csv('metacriticPS4.csv', encoding='utf-8')

for page in range(5):
    req = getRequest(page)
    soup = getSoup(req)
    getData(soup)
    # avoid overwhelming server and getting 429 Too Many Requests
    time.sleep(0.1)
exportCSV(results)
    