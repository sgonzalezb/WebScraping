import requests

def url_search(entrada): ##LA URL DEBE SER LA  INDEX.HTML 
    #assert (type(input == str)) ##ASSERT PARA QUE EL ENLACE DE ENTRADA SEA UN STRING
    url = requests.get(entrada)
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





if __name__ == "__main__":
    assert url_search('https://sgonzalezb.github.io/Web_Scraping/index.html') == (['https://sgonzalezb.github.io/Web_Scraping/client-side-js/Tinkles','https://sgonzalezb.github.io/Web_Scraping/client-side-js/Wizard','https://sgonzalezb.github.io/Web_Scraping/client-side-js/Flippy','https://sgonzalezb.github.io/Web_Scraping/client-side-js/Zigeriano','https://sgonzalezb.github.io/Web_Scraping/client-side-js/Nebulon','https://sgonzalezb.github.io/Web_Scraping/client-side-js/Cyborg'])
