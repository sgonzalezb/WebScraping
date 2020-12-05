from services import list_url
import requests



## primer enlace https://sgonzalezb.github.io/Web_Scraping/Tinkles

def scraper_info(input):
    code = requests.get(input)
    font_code = code.text
    cont_items_menus = 0
    pos_initial = font_code.find('</header>')
    item = ['class="name"','class="primero"','class="segundo"','class="postre"','class="description"','class="ingredients"','class="stock"','class="price"','class="rating"']
    while cont_items_menus <= 27 :
        cont_items_menus += 1
        inicio_element = font_code.find(item,pos_initial)
        final_element = font_code.find()


    
