import requests

url = requests.get("https://sgonzalezb.github.io/Web_Scraping/menus2.html")
codi_fuente = url.text
#print (codi_fuente) para ver el código HTML legible
def buscador_enlaces():
    position = 0
    contador = 0
    while contador < 7:
        inicio_enlace = codi_fuente.find('https://sgonzalez', position)
        final_enlace = codi_fuente.find(".html", position)
        url_scrapp = codi_fuente[inicio_enlace : final_enlace]
        contador += 1
        position += final_enlace + 1
    return url_scrapp



if __name__ == "__main__":
    assert buscador_enlaces() == ('https://sgonzalezb.github.io/Web_Scraping/index.html')
