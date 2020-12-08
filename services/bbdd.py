from pymongo import MongoClient
import pymongo

def to_mongo(list_dic):
    assert (type(list_dic == list))
    client = pymongo.MongoClient("mongodb+srv://m001-student:m001-mongodb-basics@sandbox.q0fpj.mongodb.net/<proyecto>?retryWrites=true&w=majority")
    database = client.proyecto  #indicando base de datos
    colection = database.menú   #indicando colección
    for dictionary in list_dic:
        find = colection.find_one({"Nombre":dictionary['Nombre']})   #Para no insertar documentos duplicados
        if find == None:                                              
            insert = colection.insert_one(dictionary)                
    return insert.inserted_id 