from services.scraper import scraper_info
import pytest





def test_one():
    assert scraper_info("https://sgonzalezb.github.io/Web_Scraping/client-side-js/Tinkles.html") == ["Supernova",'Locro','Asado','Dulce de Leche','De lo más profundo del Mediterráneo a tu plato','Maíz,Carne de Cerdo,Patatas,Leche,Azúcar,Vainilla','105 in stock','25$','8.8⭐','Glootie','Empanadas','Pollo al disco','Chipás','Menú típico de la dimensión C-132.','Carne picada, verduras, pollo, maíz dulce, cebolla, legumbres','89 in stock','15$','7.5⭐','Jagoff','Tacos dorados de queso y papa','Chicharron','Capiratada','Menú procedente del lejano Oeste','Masa de Hojaldre , Carne de Cerdo, Queso , Patatas , Arroz, ojo vieja','520 in stock','25$','8.9⭐']
  
def test_two():
    assert scraper_info("https://sgonzalezb.github.io/Web_Scraping/client-side-js/Flippy.html") == ["Krandor","Rollitos de primavera","Pollo con almentras","Dantá","Plato típico del planeta oriental Clasnodar.","Pollo del planeta Tierra, verduras del Amazonas, cebolla con patas, pimiento azul.","78 in stock","19.99$","6⭐",'Beaduregard','Arroz tres delicias','Sopa de aleta de tiburón','Tanghulú','Menú típico del planeta Tierra del norte de EEUU.','Ojo de hipopótamo, aleta de tiburón, excrementos de rata, la mascá de centella, pelodeorto de buey.','190 in stock','7$','5⭐','Amfiddians','Sopa Wan-ton','Fideos Chin-Chan','Pastel de Lura','Menú procedente del mar oceánico de la dimensión H-328','Pelusa del bolsillo de Doraemon, alfajoles, pimiento azul, alubias blancas, pata de conejo.','64 in stock','17.99$','7.3⭐']

def test_three():
    assert scraper_info("https://sgonzalezb.github.io/Web_Scraping/client-side-js/Cyborg.html") == ['Gromflomite','Pissotto','Lasaña','Pannacotta','De lo más exquisito de la dimensión H-49.','Laminas de lasaña, pisto,carne picada, maíz, verduras exóticas.','81 in stock','39$','6.8⭐','Meeseeks','Panini','Ravioli','Tiramisu','El plato Messianico , del planeta Kepler','Ojo de araña, pan integral, queso fundido, café','32 in stock','28$','7.3⭐','Plutoniano','Ensalada Capresse','Pizza','Cannoli','Real Hasta la muelte, brrrr','Cacho de Plutón,mostaza, masa pizza,intestino de cíclope','169 in stock','18$','7.9⭐']

def test_four():
    assert scraper_info("https://sgonzalezb.github.io/Web_Scraping/client-side-js/Nebulon.html") == ['Gazorpian','Calamares romana','Paella o Pami','Gató de almendras','La cocina del infierno, presentada envuelta en llamas','Calamares dimensión c-135, arroz cultivado en Plutón, gato terrícola','15 in stock','50$','9.5⭐','Cromulons','Gazpacho','Tortilla Española','Crema Catalana','De España, que es la caña','Verduras de la luna, huevos de avestruz, nata de alíengena, canela en rama','125 in stock','15$','6.5⭐','Garblovian','Salmorejo','Pulpo Gallega','Arroz con leche','De lo más profundo de mi corazón.','Salmón,Pulpo Gallego,arroz vegetal.','360 in stock','10$','5.9⭐']

def test_five():
    assert scraper_info("https://sgonzalezb.github.io/Web_Scraping/client-side-js/Wizard.html") == ['Flansians','Kao Suay','Brochetas de pollo satay','Mango rice','Menú típico del planeta Júpiter.','Pezuña de cabra, ojo de cíclope, pollo, arroz, espécias del planeta salvaje.','94 in stock','25$','8⭐','Smarkians','om Yam','Khao Pod Grong','Rambutén','Menú sacado de las entrañas de Plutón.','Verduras exóticas, cola de serpiente, arroz, limón, manzana.','109 in stock','27$','7⭐','Fungo','Popian','Son Tam','Hang-kut','Menú para pupilas gustativas refinadas, de procedencia Astuariana.','Pimiento naranja, tallarines, salmón y atún del planeta Tierra, alpiste.','69 in stock','30$','9⭐']

def test_six():
    assert scraper_info("https://sgonzalezb.github.io/Web_Scraping/client-side-js/Zigeriano.html") == ['Hambrosians','Choripan','Hatambe arrollado','Alfajores','Menú de las profundidades marinas del planeta C-170.','Maíz, cabeza reducida de zigeriano, tomate, pimiento azul y todo tipo de algas.','80 in stock','25$','9⭐','Klaaxzovians','Talos de Curnitas caseras','Sopa de tortilla especial','Flan de rompape','Del desierto del planeta Arena de la dimensión R-43.','Patas de grillo mutante, con mostaza fluorescente, entrañas de cerdo, verduras exóticas.','89 in stock','18$','7.2⭐','Terryfolds','Ensalada de Frijoles','Pozgde rojo','Pan de eclote','Menú picante del planeta Inferno de la dimensión L-98.','Hojas tropicales, frutos secos picantes, cayena, pimientos de padrón y pepinos rojos.','65 in stock','30$','9.5⭐']


