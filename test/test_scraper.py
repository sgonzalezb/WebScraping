from services.scraper import scraper_info
import pytest



def test_test():
    assert scraper_info("https://sgonzalezb.github.io/Web_Scraping/client-side-js/Tinkles.html") == ("Supernova")