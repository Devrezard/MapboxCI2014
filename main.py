from Getgeojson import MergingData
import sys
from streamlit.web import cli as stcli
from streamlit import runtime
import streamlit
import plotly.express as px
from aboutme import Devfolio
import hydralit_components as hc





def main():
    menu_data = [
    {'label':"Project"},
    {'label':"About Me"},
    ]
    streamlit.set_page_config(
            page_title="MapBox",
            page_icon='🌍',
            layout="wide")
    page = hc.nav_bar(menu_definition=menu_data,hide_streamlit_markers=False,sticky_nav=True,)

    if page == "Project":
        geo_df = MergingData()
        year = 2014

        fig = px.choropleth_mapbox(geo_df,
                               geojson=geo_df.geometry,
                               locations=geo_df.index,
                               color="Population",
                               center={"lat": 7.539989, "lon": -5.547080},
                               mapbox_style="carto-positron",
                               zoom=5.5, opacity=1)
        fig.update_layout(
            margin={"r": 0, "t": 35, "l": 0, "b": 0})
        with open('style.css') as f:
            streamlit.markdown(
                f'<style>{f.read()}</style>', unsafe_allow_html=True)
        streamlit.title("Mapbox Choropleth Côte d'ivoire")
        presentation, plotting = streamlit.columns(2)
        with presentation:
            streamlit.markdown("## Description ")
            streamlit.write()
            streamlit.markdown('''
            Ce projet a été developpé dans le cadre de mon apprentissage. En bref ce projet résume l'ensemble de mes compétences 
            dans le domaine du webscrapping, de l'exploration de données et de la data-vizualisation.
            Pour sa mise en place j'ai utilisé des librairies telque *BeautifulSoup* pour le web scrapping , *pandas* et *geopandas* 
            pour l'exploration des données, puis pour terminé l'utilisation de *plotly* pour la visualisation avec interaction de 
            la carte de mon pays (choropleth) fonction des habitants par region. Et enfin enbarqué dans Streamlit pour la creation d'une 
            app web.


            ### Bibliographie explorer :
            - [Plotly](https://plotly.com/python/)
            - [BeautiFulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
            - [Geopandas](https://geopandas.org/) 
            - [Pandas](https://pandas.pydata.org/)
            - [Streamlit & Hydralit](https://docs.streamlit.io/)

            <p class="autor"><span> By : </span><span>S. Christian-Renaud </span> </p>
            ''', unsafe_allow_html=True)

        with plotting:
            streamlit.write(f'Année : {year}')
            streamlit.plotly_chart(fig)
    if page == "About Me":
        Devfolio()

    
        



# Your streamlit code

if __name__ == '__main__':
    if runtime.exists():
        main()
    else:
        sys.argv = ["streamlit", "run", sys.argv[0]]
        sys.exit(stcli.main())
