import requests

url = requests.get("https://sgonzalezb.github.io/Web_Scraping/menus2")
font_code = url.text
#print (codi_fuente) para ver el código HTML legible
def buscador_enlaces():
    init_pos = 1846
    cont = 0
    urls_scraped = []
    while cont < 6:
        cont += 1
        inicio_enlace = font_code.find('https://sgonzalez', init_pos)
        final_enlace = font_code.find(".html", init_pos)
        index_url = font_code[inicio_enlace : final_enlace]
        init_pos = final_enlace + 1
        urls_scraped.append(index_url)
    return urls_scraped











if __name__ == "__main__":
    assert buscador_enlaces() == (['https://sgonzalezb.github.io/Web_Scraping/Tinkles','https://sgonzalezb.github.io/Web_Scraping/Wizard','https://sgonzalezb.github.io/Web_Scraping/Flippy','https://sgonzalezb.github.io/Web_Scraping/Zigeriano','https://sgonzalezb.github.io/Web_Scraping/Nebulon','https://sgonzalezb.github.io/Web_Scraping/Cyborg'])
   