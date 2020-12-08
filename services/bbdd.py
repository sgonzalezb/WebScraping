from pymongo import MongoClient
import pymongo

def to_mongo(entrada):
    client = pymongo.MongoClient("mongodb+srv://m001-student:m001-mongodb-basics@sandbox.q0fpj.mongodb.net/<proyecto>?retryWrites=true&w=majority")
    basededatos = client.proyecto
    coleccion = basededatos.menú
    for item in entrada:
        buscar = coleccion.find_one({"Nombre":item['Nombre']})
        if buscar is None:
            x = coleccion.insert_one(item)
    return print(x.inserted_id) #Si no inserta ninún documento, dará un error con que la variable X no está definida



if __name__ == "__main__":
    assert to_mongo([{'Descripción': 'De lo más profundo d...a tu plato', 'Ingredientes': 'Maíz,Carne de Cerdo,...r,Vainilla', 'Nombre': 'Supernova', 'Postre': 'Dulce de Leche', 'Precio': '25$', 'Primero': 'Locro', 'Reviews': '8.8⭐', 'Segundo': 'Asado', 'Stock': '105 in stock'}, {'Descripción': 'Menú típico de la di...ión C-132.', 'Ingredientes': 'Carne picada, verdur... legumbres', 'Nombre': 'Glootie', 'Postre': 'Chipás', 'Precio': '15$', 'Primero': 'Empanadas', 'Reviews': '7.5⭐', 'Segundo': 'Pollo al disco', 'Stock': '89 in stock'}, {'Descripción': 'Menú procedente del ...jano Oeste', 'Ingredientes': 'Masa de Hojaldre , C... ojo vieja', 'Nombre': 'Jagoff', 'Postre': 'Capiratada', 'Precio': '25$', 'Primero': 'Tacos dorados de queso y papa', 'Reviews': '8.9⭐', 'Segundo': 'Chicharron', 'Stock': '520 in stock'}]) == ("hecho")
