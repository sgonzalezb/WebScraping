import services.url_search
import requests

list_url = services.url_search.buscador_enlaces("https://sgonzalezb.github.io/Web_Scraping/index.html")
def scraper_info(list_url):
    fuente = requests.get(list_url)
    code = fuente.text
    contador_cosas = 0
    fin_valor = 0
    contador_cosas = 0
    out = []
    while contador_cosas < 27:
        inicio_clase = code.find('class="texto"',fin_valor) #dentro del html nos indica la posicion de las etiquetas que tienen dicha clase
        fin_clase = code.find('>', inicio_clase)
        fin_valor = code.find('<', fin_clase)
        valor = code[fin_clase+1:fin_valor]
        añada_lista = out.append(valor)
        contador_cosas += 1
    #print(out)
    return out




















