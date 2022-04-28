import geopandas as gpd
from Getdata import DataPopulation
import pandas as pd
import os
import requests







def MergingData() -> pd.DataFrame:

    '''
    return un dataframe contenant la fusion des données de population 
    et du fichiers geojson* sans les duplicats.

    geojson : fichiers contenant des blocs de districts

    '''
    url = "https://development-data-hub-s3-public.s3.amazonaws.com/ddhfiles/144981/civadmbndaadm1cntig20160527.geojson"

    filegeojson = "District.geojson"
    if os.path.exists(filegeojson) == False:
        r = requests.get(url, allow_redirects=True)
        open(filegeojson, 'wb').write(r.content)
          
    df = DataPopulation()
    Map = gpd.GeoDataFrame.from_file("District.geojson")
    liste1 = df['Districts']
    liste2 = Map['admin1Name']
    listerename = set(liste1).difference(set(liste2))
    if len(list(listerename)) !=0:
        liste1 = liste1.replace('Abidjan (district autonome)', "District Autonome D'Abidjan")
        liste1 = liste1.replace('Gôh-Djiboua', 'Goh-Djiboua')
        liste1 = liste1.replace('Sassandra-Marahoué', 'Sassandra-Marahoue')
        liste1 = liste1.replace('Vallée du Bandama', 'Valle Du Bandama')
        liste1 = liste1.replace('Comoé', 'Comoe')
        liste1 = liste1.replace('Yamoussoukro (district autonome)', 'District Autonome De Yamoussoukro')
        liste1 = liste1.replace('Denguélé', 'Denguele')
    df['Districts'] = liste1
    Map.rename(columns={'admin1Name': 'Districts'}, inplace=True)
    geo_df = gpd.GeoDataFrame.from_features(Map).merge(
        pd.DataFrame(df), on="Districts").set_index("Districts")

    return geo_df
