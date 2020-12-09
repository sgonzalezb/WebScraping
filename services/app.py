import requests
import pymongo
from pymongo import MongoClient
from crawler import url_search
from scraper import scraper_info
from dicc_creator import creator_diction
from bbdd import to_mongo

link = "https://sgonzalezb.github.io/Web_Scraping/index.html"
def launch_app(entrada):
    list_url = url_search(entrada)
    list_value = scraper_info(list_url)
    list_dic = creator_diction(list_value)
    up_mongo = to_mongo(list_dic)
    print("Completado!")
    return up_mongo
    
launch_app(link)

  