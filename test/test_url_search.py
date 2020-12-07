from services.url_search import buscador_enlaces  
import pytest

@pytest.mark.buscador_enlaces
def test_buscador_enlaces():
    assert buscador_enlaces("https://sgonzalezb.github.io/Web_Scraping/index.html") == (['https://sgonzalezb.github.io/Web_Scraping/client-side-js/Tinkles','https://sgonzalezb.github.io/Web_Scraping/client-side-js/Wizard','https://sgonzalezb.github.io/Web_Scraping/client-side-js/Flippy','https://sgonzalezb.github.io/Web_Scraping/client-side-js/Zigeriano','https://sgonzalezb.github.io/Web_Scraping/client-side-js/Nebulon','https://sgonzalezb.github.io/Web_Scraping/client-side-js/Cyborg'])