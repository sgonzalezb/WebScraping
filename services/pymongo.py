from pymongo import MongoClient


def subir_base(lista):
    db = MongoClient().aggregation_example
    result = db.menú.insert_many(lista) 
    print(result)
    return "hecho"



if __name__ == "__main__":
    assert subir_base([{'Descripción': 'De lo más profundo d...a tu plato', 'Ingredientes': 'Maíz,Carne de Cerdo,...r,Vainilla', 'Nombre': 'Supernova', 'Postre': 'Dulce de Leche', 'Precio': '25$', 'Primero': 'Locro', 'Reviews': '8.8⭐', 'Segundo': 'Asado', 'Stock': '105 in stock'}, {'Descripción': 'Menú típico de la di...ión C-132.', 'Ingredientes': 'Carne picada, verdur... legumbres', 'Nombre': 'Glootie', 'Postre': 'Chipás', 'Precio': '15$', 'Primero': 'Empanadas', 'Reviews': '7.5⭐', 'Segundo': 'Pollo al disco', 'Stock': '89 in stock'}, {'Descripción': 'Menú procedente del ...jano Oeste', 'Ingredientes': 'Masa de Hojaldre , C... ojo vieja', 'Nombre': 'Jagoff', 'Postre': 'Capiratada', 'Precio': '25$', 'Primero': 'Tacos dorados de queso y papa', 'Reviews': '8.9⭐', 'Segundo': 'Chicharron', 'Stock': '520 in stock'}]) == ("hecho")


