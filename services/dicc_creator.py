
def creator_diction(list_value):
    assert type(list_value == list)
    key_dic = ["Nombre","Primero","Segundo","Postre","Descripción","Ingredientes","Stock","Precio","Reviews"] 
    value_dic = []         #almacena los valores y luego creará los diccionarios a partir de esta lista             
    list_dic = []          # almacena todos los diccionarios
    cont_values = 0
    for value in list_value:
        contador_item = 0
        while contador_item < 1:
            value_dic.append(value)
            contador_item += 1
            cont_values += 1
        if cont_values == 9: 
            dictionary = dict(zip(key_dic,value_dic)) #crea el diccionario a partir de dos listas
            assert(len(dictionary) == 9)
            cont_values = 0
            value_dic = []
            list_dic.append(dictionary)
    return list_dic