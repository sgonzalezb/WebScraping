import requests

def buscador_enlaces(input):
    assert (type(input == str)) ##ASSERT PARA QUE EL ENLACE DE ENTRADA SEA UN STRING
    url = requests.get(input)
    font_code = url.text
    init_pos = font_code.find('</header>')
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
    




    










   