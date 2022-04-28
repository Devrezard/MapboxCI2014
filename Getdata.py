import requests
from bs4 import BeautifulSoup
import pandas as pd


def DataPopulation() -> pd.DataFrame:

    # obtention des donnnées de la population ivoirienne
    urlDataPopulation = 'https://www.populationdata.net/pays/cote-divoire/divisions'
    page = requests.get(urlDataPopulation)
    # obtention des information de la page
    soup = BeautifulSoup(page.text, 'lxml')
    # dans la page il existe une table contenant les données de la
    # populatioin ivoirienne
    soup.find_all('table')
    # nous avons besooin d'une table avec l'attribut de classe
    # data
    table = soup.find('table',class_='data')
    # creation d'une liste pour la recuperation des entêtes de table
    header = []
    for i in table.find_all('th'):
        title = i.text
        header.append(title)
    # creation de notre dataframe
    dataPoPulation = pd.DataFrame(columns=header)
    # ajout des données dans le dataframe
    for j in table.find_all('tr')[1:]:
        row_data = j.find_all('td')
        row = [i.text for i in row_data]
        length = len(dataPoPulation)
        dataPoPulation.loc[length] = row
    
    # convertissons des données de la polution en entier
    getPopulation = dataPoPulation['Population']
    newdata = []
    for element in getPopulation:
        newdata.append(int(str(element).replace('habitants','').replace(' ','')))

    dataPoPulation['Population'] = newdata


    return dataPoPulation