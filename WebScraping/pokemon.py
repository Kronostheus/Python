import requests
import pandas as pd

from bs4 import BeautifulSoup

def getRequest(url):
    try:
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

def getTable(request):
    soup = BeautifulSoup(request.text, 'html.parser')
    results = soup.find_all('tr')[1:]
    return results

def getRealName(link_name, small_name, namelst):
    if link_name == namelst[-1] or namelst[0] == 'Mega':
        name = small_name
    else:
        name = link_name + ' (' + small_name + ')'
    return name

def processName(row):
    mb_name = row.find('small')
    mega = False
    if mb_name != None:
        name = mb_name.text.strip()
        namelst = name.split(" ")
        # process Mega Pokemons
        if namelst[0] == 'Mega':
            mega = True
        # process Alolan Pokemons
        if namelst[0] == 'Alolan':
            name = "".join(namelst[1:]) + ' (Alolan)'
        # process other names (usually pokemon with multiple formes)
        if len(namelst) > 1:
            temp = row.find('a').text.strip()
            name = getRealName(temp, name, namelst)
        # Meowstic has only Male/Female
        else:
            name = row.find('a').text.strip() + " (" + "".join(namelst) + ")"
    else:
        name = row.find('a').text.strip()
    return [mega, name]

def processType(row):
    contents = row.find_all('a')
    type_1 = contents[1].text.strip()
    type_2 = "None"
    if len(contents) == 3:
        type_2 = contents[2].text.strip()
    return [type_1, type_2]

def getLegendNums(rows):
    res = []
    for row in rows:
        res.append(row.text.strip()[1:4])
    return res

def getLegends():
    url = 'https://bulbapedia.bulbagarden.net/wiki/User:Focus58/List_of_Legendary_Pok%C3%A9mon'
    request = getRequest(url)
    soup = BeautifulSoup(request.text, 'html.parser')
    legend_rows = soup.find_all('td', attrs={'style':'font-family:Monospace;'})
    legends_nums = getLegendNums(legend_rows)
    return legends_nums

def processNum(row):
    poke_num = row.find('td').text.strip()
    is_legend = False
    if poke_num in legends:
        is_legend = True
    return [poke_num, is_legend]

def processSkills(row):
    res = []
    skills = row.find_all('td')[-7:]
    for x in range(7):
        skill = skills[x].text.strip()
        res.append(skill)
    return res

def processGeneration(num, name):
    dex = {'1': '151', '2': '251', '3': '386', '4': '493', '5': '649', '6': '721', '7': '807'}
    namelst = name.split(" ")
    temp_gen = ""
    for gen, total in dex.items():
        if num <= total:
            temp_gen = gen
            break
    if namelst[0] == 'Mega':
        temp_gen = '6'
    if namelst[-1] == '(Alolan)':
        temp_gen = '7'
    return [temp_gen]

def buildPokemon(row):
    pokemon = []
    poke_num = processNum(row)
    poke_name = processName(row)
    pokemon = pokemon + poke_num + poke_name + processType(row) + processSkills(row) + processGeneration(poke_num[0], poke_name[1])
    return pokemon

def getData(table):
    for row in table:
        pokemon = buildPokemon(row)
        data.append(pokemon)

def exportCSV(data):
    records = pd.DataFrame(data, columns=['#', 'Legend', 'Mega', 'Name', 'Type 1', 'Type 2', 'Total', 'HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed', 'Generation'])
    records.to_csv('pokemon.csv', encoding='utf-8')

if __name__ == "__main__":
    data = []
    url = 'https://pokemondb.net/pokedex/all'
    # set() to remove duplicates, list() to return back to normal 
    legends = list(set(getLegends()))
    req = getRequest(url)
    table = getTable(req)
    getData(table)
    exportCSV(data)
    
    

