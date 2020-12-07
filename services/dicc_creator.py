from scraper import scraper_info,importar

def creator_diction(importar):
    key_dic = ["Nombre","Primero","Segundo","Postre","Descripción","Ingredientes","Stock","Precio","Reviews"]
    lista = []
    lista_dic = []
    contador_valores = 0
    for item in importar:
        contador_item = 0
        while contador_item < 1:
            lista.append(item)
            contador_item += 1
            contador_valores += 1
        if contador_valores == 9: 
            primer_dict = dict(zip(key_dic,lista))
            contador_valores = 0
            lista = []
            lista_dic.append(primer_dict)
    return lista_dic
    

if __name__ == "__main__":
    assert creator_diction(["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18"]) == ("")        








































   




