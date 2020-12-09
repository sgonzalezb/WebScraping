from services.crawler import url_search  
import pytest


def test_one():
    assert url_search('https://sgonzalezb.github.io/Web_Scraping/index.html') == (['https://sgonzalezb.github.io/Web_Scraping/client-side-js/Tinkles','https://sgonzalezb.github.io/Web_Scraping/client-side-js/Wizard','https://sgonzalezb.github.io/Web_Scraping/client-side-js/Flippy','https://sgonzalezb.github.io/Web_Scraping/client-side-js/Zigeriano','https://sgonzalezb.github.io/Web_Scraping/client-side-js/Nebulon','https://sgonzalezb.github.io/Web_Scraping/client-side-js/Cyborg'])