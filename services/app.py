import requests
import pymongo
from pymongo import MongoClient
from crawler import url_search
from scraper import scraper_info
from dicc_creator import creator_diction
from bbdd import to_mongo

entrada = "https://sgonzalezb.github.io/Web_Scraping/index.html"
def llamador (entrada):
    lista_enlaces = url_search(entrada)
    scrapeao = scraper_info(lista_enlaces)
    diccionario = creator_diction(scrapeao)
    mongo = to_mongo(diccionario)
    return print(mongo)



#if __name__ == "__main__":
#    assert llamador("https://sgonzalezb.github.io/Web_Scraping/index.html") == ("")