import url_search 
import requests

url_search.buscador_enlaces ("https://sgonzalezb.github.io/Web_Scraping/index.html")

## primer enlace https://sgonzalezb.github.io/Web_Scraping/Tinkles
link = "https://sgonzalezb.github.io/Web_Scraping/client-side-js/Tinkles.html"
def scraper_info(list_url):
    fuente = requests.get(list_url)
    code = fuente.text
    contador_cosas = 0
    lista = []
    fin_valor = 0
    for link in list_url:
        contador_cosas = 0
        while contador_cosas <= 27:
            inicio_clase = code.find('class="texto"',fin_valor) #dentro del html nos indica la posicion de las etiquetas que tienen dicha clase
            fin_clase = code.find('>', inicio_clase)
            fin_valor = code.find('<', fin_clase)
            valor = code[fin_clase+1:fin_valor]
            añada_lista = lista.append(valor)
            contador_cosas += 1
    return lista












