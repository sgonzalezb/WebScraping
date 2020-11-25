from src.url_search import buscador_enlaces  
import pytest


def test_test():
    assert buscador_enlaces() == (['https://sgonzalezb.github.io/Web_Scraping/Tinkles','https://sgonzalezb.github.io/Web_Scraping/Wizard','https://sgonzalezb.github.io/Web_Scraping/Flippy','https://sgonzalezb.github.io/Web_Scraping/Zigeriano','https://sgonzalezb.github.io/Web_Scraping/Nebulon','https://sgonzalezb.github.io/Web_Scraping/Cyborg'])
