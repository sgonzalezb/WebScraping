import requests



## primer enlace https://sgonzalezb.github.io/Web_Scraping/Tinkles
link = "https://sgonzalezb.github.io/Web_Scraping/client-side-js/Tinkles.html"
def scraper_info(link):
    fuente = requests.get(link)
    code = fuente.text
    clase = 'class="texto"'
    inicio_clase = code.find(clase) #dentro del html nos indica la posicion de las etiquetas que tienen dicha clase
    fin_clase = code.find('>', inicio_clase)
    fin_valor = code.find('<', fin_clase)
    valor = code[fin_clase:fin_valor]
    return valor



if __name__ == "__main__":  
    assert scraper_info("https://sgonzalezb.github.io/Web_Scraping/client-side-js/Tinkles.html")==("Supernova")

