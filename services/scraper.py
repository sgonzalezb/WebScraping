from crawler import buscador_enlaces , list_url
import requests


def contador_clases(#lista salida del crawler):
    for link in list_url:
        code = requests.get(link).text
        x = 0
        contador = 0
        posicion_inicio = 0
        while x != -1:
            x = code.find('class="texto"', posicion_inicio)
            posicion_inicio = x
            contador = +1
    return contador 

var = contador_clases(list_url)

def scraper_info(#lista salida crawler):
    out = []
    for link in list_url:
        code = requests.get(link).text
        fin_valor = 0
        contador_valores = 0
        while contador_valores < var:
            inicio_clase = code.find('class="texto"',fin_valor) #Dentro del html nos indica la posición de las etiquetas que tienen dicha clase
            fin_clase = code.find('>', inicio_clase) 
            fin_valor = code.find('<', fin_clase) #Tanto en fin_valor como fin_clase lo que hacemos es buscar entre el inicio y el final de la etiqueta hmtl
            valor = code[fin_clase+1:fin_valor] #Aquí en la variable valor almacenamos lo que hay entre la etiqueta html con la clase "texto"
            out.append(valor)
            contador_valores += 1
    return out



#importar = scraper_info(salida)


#def scraper_info(salida):
#    valores = [] #es la lista con todos los valores con class='texto' de todos los links de la página (los 6 de menús)
#    for link in salida:
#        fuente = requests.get(link).text
#        inicio_clase = fuente.find('class="texto"','fin_valor') #Dentro del html nos indica la posición de las etiquetas que tienen dicha clase
#        fin_clase = fuente.find('>', inicio_clase) 
#        fin_valor = fuente.find('<', fin_clase) #Tanto en fin_valor como fin_clase lo que hacemos es buscar entre el inicio y el final de la etiqueta hmtl
#        valor = fuente[fin_clase + 1 : fin_valor] #Aquí en la variable valor almacenamos lo que hay entre la etiqueta html con la clase "texto"
#        while valor != -1:
#        valores.append(valor)
#    return valores  


if __name__ == "__main__":
    assert scraper_info(['https://sgonzalezb.github.io/Web_Scraping/client-side-js/Tinkles','https://sgonzalezb.github.io/Web_Scraping/client-side-js/Wizard','https://sgonzalezb.github.io/Web_Scraping/client-side-js/Flippy','https://sgonzalezb.github.io/Web_Scraping/client-side-js/Zigeriano','https://sgonzalezb.github.io/Web_Scraping/client-side-js/Nebulon','https://sgonzalezb.github.io/Web_Scraping/client-side-js/Cyborg']) == ["Supernova",'Locro','Asado','Dulce de Leche','De lo más profundo del Mediterráneo a tu plato','Maíz,Carne de Cerdo,Patatas,Leche,Azúcar,Vainilla','105 in stock','25$','8.8⭐','Glootie','Empanadas','Pollo al disco','Chipás','Menú típico de la dimensión C-132.','Carne picada, verduras, pollo, maíz dulce, cebolla, legumbres','89 in stock','15$','7.5⭐','Jagoff','Tacos dorados de queso y papa','Chicharron','Capiratada','Menú procedente del lejano Oeste','Masa de Hojaldre , Carne de Cerdo, Queso , Patatas , Arroz, ojo vieja','520 in stock','25$','8.9⭐']