import services.url_search
import requests

list_url = services.url_search.buscador_enlaces("https://sgonzalezb.github.io/Web_Scraping/index.html")

def scraper_info(list_url):
    fuente = requests.get(list_url)
    code = fuente.text
    contador_cosas = 0
    fin_valor = 0
    contador_valores = 0
    out = []
    while contador_valores < 27:
        inicio_clase = code.find('class="texto"',fin_valor) #Dentro del html nos indica la posición de las etiquetas que tienen dicha clase
        fin_clase = code.find('>', inicio_clase) 
        fin_valor = code.find('<', fin_clase) #Tanto en fin_valor como fin_clase lo que hacemos es buscar entre el inicio y el final de la etiqueta hmtl
        valor = code[fin_clase+1:fin_valor] #Aquí en la variable valor almacenamos lo que hay entre la etiqueta html con la calse "texto"
        añada_lista = out.append(valor)
        contador_cosas += 1
    return out




















