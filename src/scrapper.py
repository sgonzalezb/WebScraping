import requests

url = requests.get("https://sgonzalezb.github.io/Web_Scraping/menus2.html")
codi_fuente = url.text
#print (codi_fuente) para ver el código HTML legible 
inicio_enlace = codi_fuente.find('<a href=')
final_enlace = codi_fuente.find("</a>")
muestra = codi_fuente[codi_fuente.find('<a href='):codi_fuente.find("</a>")]