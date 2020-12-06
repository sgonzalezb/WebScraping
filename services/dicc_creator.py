import services.scraper

def creator_diction(out):
    key_dic = ["Nombre","Primero","Segundo","Postre","Descripción","Ingredientes","Stock","Precio","Reviews"]
    lista1 = []
    lista2 =  []
    lista3 = []
    suma_items = 0
    assert len(out) < 28
    for value in out: 
        suma_items += 1
        if suma_items <= 9:
            
            lista1.append(value)#valores del primer diccionario (el primer menú de la página)

        elif suma_items > 9 and suma_items <= 18:
            lista2.append(value)#valores del segundo diccionario (el segundo menú de la página)
            
        elif suma_items > 18:
            lista3.append(value)#valores del tercer menú (el tercero menú de la página)
    primer_dict = dict(zip(key_dic,lista1))     #
    segundo_dict = dict(zip(key_dic,lista2))    #   Intentar refactorizar este bloque de aquí
    tercer_dict = dict(zip(key_dic,lista3))     #
    lista_dev = [primer_dict,segundo_dict,tercer_dict]

    
    return lista_dev




