import requests


url = requests.get("https://sgonzalezb.github.io/Web_Scraping/menus2")
font_code = url.text
#print (codi_fuente) para ver el código HTML legible
def buscador_enlaces():
    init_pos = 1846
    cont_url = 0
    list_url = []
    num_men = 6
    while cont_url < num_men:
        cont_url += 1
        inicio_enlace = font_code.find('https://sgonzalez', init_pos)
        final_enlace = font_code.find(".html", init_pos)
        index_url = font_code[inicio_enlace : final_enlace]
        init_pos = final_enlace + 1
        list_url.append(index_url)
    return list_url










   