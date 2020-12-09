import requests

def scraper_info(list_url):
    assert type(list_url == list)
    list_value = []
    for url in list_url:
            code = requests.get(url).text
            end_value = 0
            cont_value = 0
            while cont_value < 27:
                cont_value += 1
                init_class = code.find('class="texto"',end_value) #inicio de la clase
                end_class = code.find('>', init_class) #posición final de la clase
                end_value = code.find('<', end_class) #posición final del valor
                value = code[end_class+1:end_value] #almacena el valor 
                list_value.append(value) # añade a la lista el valor
    assert (len(list_value) == (162))
    return list_value