import requests
import pymongo
from pymongo import MongoClient
from crawler import url_search
from scraper import scraper_info
from dicc_creator import creator_diction
from bbdd import to_mongo

input = "https://sgonzalezb.github.io/Web_Scraping/index.html"
def launch_app(input):
    assert type(input == str)
    list_url = url_search(input)
    list_value = scraper_info(list_url)
    list_dic = creator_diction(list_value)
    mongo = to_mongo(list_dic)
    return mongo

#if __name__ == "__main__":
  # assert launch_app("https://sgonzalezb.github.io/Web_Scraping/index.html") == ("")