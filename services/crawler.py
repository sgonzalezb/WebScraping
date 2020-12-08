import requests

def url_search(link): 
    assert (type(input == str)) 
    url = requests.get(link).text   #código fuente pasado a str
    init_pos = url.find('</header>') # inicia la busqueda a partir de la etiqueta </header>
    cont_url = 0
    list_url = []
    num_men = 6
    while cont_url < num_men:
        cont_url += 1
        inicio_enlace = url.find('https://sgonzalez', init_pos)
        final_enlace = url.find(".html", init_pos)
        di_link = url[inicio_enlace : final_enlace]
        init_pos = final_enlace + 1
        list_url.append(di_link)
    return list_url