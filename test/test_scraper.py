from services.scraper import scraper_info
import pytest



def test_test():
    assert scraper_info ("https://sgonzalezb.github.io/Web_Scraping/") == ([ ["Supernova","Locro","Asado","Dulce de Leche","De lo más profundo del Mediterráneo a tu plato","Maíz,Carne de Cerdo,Patatas,Leche,Azúcar,Vainilla","105 in stock","25$","8.8⭐"],["Glootie","Empanadas","Pollo al disco","Chipás","Menú típico de la dimensión C-132.","Carne picada, verduras, pollo, maíz dulce, cebolla, legumbres","89 in stock","15$","7.5⭐"],["Jagoff","Tacos dorados de queso y papa","Chicharron","Capiratada","Menú procedente del lejano Oeste","Masa de Hojaldre , Carne de Cerdo, Queso , Patatas , Arroz, ojo vieja","520 in stock","25$","8.9⭐"] ])