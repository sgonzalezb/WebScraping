from services.scraper import scraper_info
import pytest





def test_one():
    assert scraper_info("https://sgonzalezb.github.io/Web_Scraping/client-side-js/Tinkles.html") == ["Supernova",'Locro','Asado','Dulce de Leche','De lo más profundo del Mediterráneo a tu plato','Maíz,Carne de Cerdo,Patatas,Leche,Azúcar,Vainilla','105 in stock','25$','8.8⭐','Glootie','Empanadas','Pollo al disco','Chipás','Menú típico de la dimensión C-132.','Carne picada, verduras, pollo, maíz dulce, cebolla, legumbres','89 in stock','15$','7.5⭐','Jagoff','Tacos dorados de queso y papa','Chicharron','Capiratada','Menú procedente del lejano Oeste','Masa de Hojaldre , Carne de Cerdo, Queso , Patatas , Arroz, ojo vieja','520 in stock','25$','8.9⭐']
  
def test_two():
    assert scraper_info("https://sgonzalezb.github.io/Web_Scraping/client-side-js/Flippy.html") == ["Krandor","Rollitos de primavera","Pollo con almentras","Dantá","Plato típico del planeta oriental Clasnodar.","Pollo del planeta Tierra, verduras del Amazonas, cebolla con patas, pimiento azul.","78 in stock","19.99$","6⭐",'Beaduregard','Arroz tres delicias','Sopa de aleta de tiburón','Tanghulú','Menú típico del planeta Tierra del norte de EEUU.','Ojo de hipopótamo, aleta de tiburón, excrementos de rata, la mascá de centella, pelodeorto de buey.','190 in stock','7$','5⭐','Amfiddians','Sopa Wan-ton','Fideos Chin-Chan','Pastel de Lura','Menú procedente del mar oceánico de la dimensión H-328','Pelusa del bolsillo de Doraemon, alfajoles, pimiento azul, alubias blancas, pata de conejo.','64 in stock','17.99$','7.3⭐']




