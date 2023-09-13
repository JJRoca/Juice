import csv
#script para pasar datos json a categoria.csv
# def categoria():
#     data=[
#     {
#         "model": "Producto.categoriaproducto",
#         "pk": 1,
#         "fields": {
#             "categoria": "Bebidas Naturales"
#             }
#     },
#     {
#         "model": "Producto.categoriaproducto",
#         "pk": 2,
#         "fields": {
#             "categoria": "Jugos Verdes"
#             }
#     },
#     {
#         "model": "Producto.categoriaproducto",
#         "pk": 3,
#         "fields": {
#             "categoria": "Tropicales"
#             }
#     },
#     {
#         "model": "Producto.categoriaproducto",
#         "pk": 4,
#         "fields": {
#             "categoria": "Mas Tropicales"
#             }
#     },
#     {
#         "model": "Producto.categoriaproducto",
#         "pk": 5,
#         "fields": {
#             "categoria": "Poderosos"
#             }
#     },
#     {
#         "model": "Producto.categoriaproducto",
#         "pk": 6,
#         "fields": {
#             "categoria": "Desintoxicantes"
#             }
#     },
#     {
#         "model": "Producto.categoriaproducto",
#         "pk": 7,
#         "fields": {
#             "categoria": "Diureticos"
#             }
#     },
#     {
#         "model": "Producto.categoriaproducto",
#         "pk": 8,
#         "fields": {
#             "categoria": "Aliviar Malestares"
#             }
#     },
#     {
#         "model": "Producto.categoriaproducto",
#         "pk": 9,
#         "fields": {
#             "categoria": "Bebidas Calientes"
#             }
#     },
#     {
#         "model": "Producto.categoriaproducto",
#         "pk": 10,
#         "fields": {
#             "categoria": "Bebidas Frias"
#             }
#     },
#     {
#         "model": "Producto.categoriaproducto",
#         "pk": 11,
#         "fields": {
#             "categoria": "Desayunos"
#             }
#     },
#     {
#         "model": "Producto.categoriaproducto",
#         "pk": 12,
#         "fields": {
#             "categoria": "Muy Saludable"
#             }
#     },
#     {
#         "model": "Producto.categoriaproducto",
#         "pk": 13,
#         "fields": {
#             "categoria": "Pizzas"
#             }
#     },
#     {
#         "model": "Producto.categoriaproducto",
#         "pk": 14,
#         "fields": {
#             "categoria": "Paninis"
#             }
#     },
#     {
#         "model": "Producto.categoriaproducto",
#         "pk": 15,
#         "fields": {
#             "categoria": "Hamburguesas"
#             }
#     },
#     {
#         "model": "Producto.categoriaproducto",
#         "pk": 16,
#         "fields": {
#             "categoria": "Ensaladas"
#             }
#     },
#     {
#         "model": "Producto.categoriaproducto",
#         "pk": 17,
#         "fields": {
#             "categoria": "Sandwiches"
#             }
#     },
#     {
#         "model": "Producto.categoriaproducto",
#         "pk": 18,
#         "fields": {
#             "categoria": "Reposteria"
#             }
#     },
#     {
#         "model": "Producto.categoriaproducto",
#         "pk": 19,
#         "fields": {
#             "categoria": "otros."
#             }
#     },]
#     # Nombre del archivo CSV de destino
#     nombre_archivo = "categorias.csv"

#     # Abrir el archivo CSV en modo de escritura
#     with open(nombre_archivo, mode="w", newline="") as archivo_csv:
#         # Definir el encabezado del archivo CSV
#         encabezado = ["id", "categoria"]

#         # Crear el escritor CSV
#         escritor_csv = csv.DictWriter(archivo_csv, fieldnames=encabezado)

#         # Escribir el encabezado
#         escritor_csv.writeheader()

#         # Escribir los datos
#         for d in data:
#             pk = d['pk']
#             categoria = d['fields']['categoria']
#             escritor_csv.writerow({"id": pk, "categoria": categoria})

#     return(f"Los datos se han exportado correctamente a '{nombre_archivo}'.")
# a=categoria()
# print(a)

#script para pasar datos json a Producto.csv
def producto():   
    data_producto=[
        {
        "model": "Producto.productointerno",
        "pk": 1,
        "fields": {
            "producto": "Jugo",
            "ingredientes": "Frutilla + Agua / Durazno + Agua / Maracuyá + Agua / Piña + Agua / Limón + Agua / Copoazu + Agua / Mango + Agua / Tumbo + Agua / Sandia + Agua / Papaya + Agua",
            "proveedor": 4,
            "cat_producto": 1,
            "precio_p": "10.00",
            "precio_m": "12.00",
            "precio_g": "14.00",
            "existencia": 60,
            "date_add": "2022-08-28T11:02:50Z",
        
            "foto": "img_e93a0834fa013633e6aec039216fc1b9.jpg"
        }
    },
    {
        "model": "Producto.productointerno",
        "pk": 2,
        "fields": {
            "producto": "Licuado de leche ",
            "ingredientes": "Frutilla + Leche / Durazno + Leche / Maracuyá + Leche / Papaya + Leche / Piña + Leche / Plátano + Leche / Limón + Leche / Copoazu + Leche / Mango + Leche / Arándano + Leche / Manzana + Leche / Mora + Leche",
            "proveedor": 4,
            "cat_producto": 1,
            "precio_p": "12.00",
            "precio_m": "14.00",
            "precio_g": "16.00",
            "existencia": 10,
            "date_add": "2022-08-28T12:27:24Z",
        
            "foto": "img_ab2fb849f39d6a4b4072b9bb8146024f.jpg"
        }
    },
    {
        "model": "Producto.productointerno",
        "pk": 3,
        "fields": {
            "producto": "Frappe",
            "ingredientes": "Frutilla + Hielo Frappe / Durazno + Hielo Frappe / Maracuyá + Hielo Frappe / Piña + Hielo Frappe / Limón + Hielo Frappe / Copoazu + Hielo Frappe / Mango + Hielo Frappe / Tumbo + Hielo Frappe / Sandia + Hielo Frappe / Papaya + Hielo Frappe",
            "proveedor": 4,
            "cat_producto": 1,
            "precio_p": "10.00",
            "precio_m": "12.00",
            "precio_g": "14.00",
            "existencia": 7,
            "date_add": "2022-09-01T10:53:53Z",
        
            "foto": "img_producto.png"
        }
    },
    {
        "model": "Producto.productointerno",
        "pk": 4,
        "fields": {
            "producto": "Milkshake",
            "ingredientes": "Frutilla + Leche + H. Frappe / Durazno + Leche + H. Frappe / Maracuyá + Leche + H.Frappe / Piña + Leche + H. Frappe / Limón + Leche + H. Frappe / Copoazu + Leche + H. Frappe / Mango + Leche + H. Frappe / Tumbo + Leche + H. Frappe / Papaya + Leche + H. Frappe / Mora + Leche + H. Frappe",
            "proveedor": 4,
            "cat_producto": 1,
            "precio_p": "12.00",
            "precio_m": "14.00",
            "precio_g": "16.00",
            "existencia": 28,
            "date_add": "2022-09-01T10:54:26Z",
        
            "foto": "img_producto.png"
        }
    },
    {
        "model": "Producto.productointerno",
        "pk": 5,
        "fields": {
            "producto": "Smoothie ",
            "ingredientes": "Frutilla + Yogurt + H. Frappe / Durazno + Yogurt + H. Frappe / Piña + Yogurt + H. Frappe / Copoazu + Yogurt + H. Frappe / Mango + Yogurt + H. Frappe / Mora + Yogurt + H. Frappe",
            "proveedor": 4,
            "cat_producto": 1,
            "precio_p": "13.00",
            "precio_m": "15.00",
            "precio_g": "17.00",
            "existencia": 34,
            "date_add": "2022-09-01T10:54:43Z",
        
            "foto": "img_producto.png"
        }
    },
    {
        "model": "Producto.productointerno",
        "pk": 6,
        "fields": {
            "producto": "Quema Grasa",
            "ingredientes": "Piña / Limón / Apio / Espinaca",
            "proveedor": 4,
            "cat_producto": 2,
            "precio_p": "10.00",
            "precio_m": "12.00",
            "precio_g": "14.00",
            "existencia": 30,
            "date_add": "2022-09-01T10:55:26Z",
        
            "foto": "img_producto.png"
        }
    },
    {
        "model": "Producto.productointerno",
        "pk": 7,
        "fields": {
            "producto": "Refrescante Verde",
            "ingredientes": "Piña / Limón / Espinaca / Manzana",
            "proveedor": 4,
            "cat_producto": 2,
            "precio_p": "10.00",
            "precio_m": "12.00",
            "precio_g": "14.00",
            "existencia": 44,
            "date_add": "2022-09-01T10:56:18Z",
        
            "foto": "img_producto.png"
        }
    },
    {
        "model": "Producto.productointerno",
        "pk": 8,
        "fields": {
            "producto": "Aplana Abdomen",
            "ingredientes": "Pepino / Perejil / Manzana / Piña / Zanahória",
            "proveedor": 4,
            "cat_producto": 2,
            "precio_p": "10.00",
            "precio_m": "12.00",
            "precio_g": "14.00",
            "existencia": 45,
            "date_add": "2022-09-01T10:56:47Z",
        
            "foto": "img_producto.png"
        }
    },
    {
        "model": "Producto.productointerno",
        "pk": 9,
        "fields": {
            "producto": "Antioxidante",
            "ingredientes": "Pera / Acelga / Manzana verde",
            "proveedor": 4,
            "cat_producto": 2,
            "precio_p": "10.00",
            "precio_m": "12.00",
            "precio_g": "14.00",
            "existencia": 42,
            "date_add": "2022-09-01T10:57:07Z",
        
            "foto": "img_producto.png"
        }
    },
    {
        "model": "Producto.productointerno",
        "pk": 10,
        "fields": {
            "producto": "Chau Celulitis",
            "ingredientes": "Piña / Achojcha / Espinaca / Limón",
            "proveedor": 4,
            "cat_producto": 2,
            "precio_p": "10.00",
            "precio_m": "12.00",
            "precio_g": "14.00",
            "existencia": 47,
            "date_add": "2022-09-01T10:57:21Z",
        
            "foto": "img_producto.png"
        }
    },
    {
        "model": "Producto.productointerno",
        "pk": 11,
        "fields": {
            "producto": "Ultra Inmune",
            "ingredientes": "Apio / Pera / Linaza / Acelga",
            "proveedor": 4,
            "cat_producto": 2,
            "precio_p": "10.00",
            "precio_m": "12.00",
            "precio_g": "14.00",
            "existencia": 7,
            "date_add": "2022-09-04T08:38:29Z",
        
            "foto": "img_producto.png"
        }
    },
    {
        "model": "Producto.productointerno",
        "pk": 12,
        "fields": {
            "producto": "Muy divertido",
            "ingredientes": "Menta / Manzana / Limón / Achojcha / Pepino",
            "proveedor": 4,
            "cat_producto": 2,
            "precio_p": "10.00",
            "precio_m": "12.00",
            "precio_g": "14.00",
            "existencia": 15,
            "date_add": "2022-09-04T08:38:53Z",
        
            "foto": "img_producto.png"
        }
    },
    {
        "model": "Producto.productointerno",
        "pk": 13,
        "fields": {
            "producto": "Adios Colesterol",
            "ingredientes": "Linaza / Espinaca / Piña / Perejil",
            "proveedor": 4,
            "cat_producto": 2,
            "precio_p": "10.00",
            "precio_m": "12.00",
            "precio_g": "14.00",
            "existencia": 20,
            "date_add": "2022-09-04T08:39:16Z",
        
            "foto": "img_producto.png"
        }
    },
    {
        "model": "Producto.productointerno",
        "pk": 14,
        "fields": {
            "producto": "Piña o Limón H. Buena",
            "ingredientes": "Piña con Hierba buena / Limón con Hierba buena",
            "proveedor": 4,
            "cat_producto": 3,
            "precio_p": "10.00",
            "precio_m": "12.00",
            "precio_g": "14.00",
            "existencia": 7,
            "date_add": "2022-09-04T08:38:29Z",
        
            "foto": "img_producto.png"
        }
    },
    {
        "model": "Producto.productointerno",
        "pk": 15,
        "fields": {
            "producto": "Naranja con Sandia",
            "ingredientes": "Naranja / Sandia",
            "proveedor": 4,
            "cat_producto": 3,
            "precio_p": "10.00",
            "precio_m": "12.00",
            "precio_g": "14.00",
            "existencia": 15,
            "date_add": "2022-09-04T08:38:53Z",
        
            "foto": "img_producto.png"
        }
    },
    {
        "model": "Producto.productointerno",
        "pk": 16,
        "fields": {
            "producto": "Naranja Zanahoria",
            "ingredientes": "Naranja / Zanahoria",
            "proveedor": 4,
            "cat_producto": 3,
            "precio_p": "10.00",
            "precio_m": "12.00",
            "precio_g": "14.00",
            "existencia": 20,
            "date_add": "2022-09-04T08:39:16Z",
        
            "foto": "img_producto.png"
        }
    },
    {
        "model": "Producto.productointerno",
        "pk": 17,
        "fields": {
            "producto": "Zumo",
            "ingredientes": "Naranja / Mandarina",
            "proveedor": 4,
            "cat_producto": 3,
            "precio_p": "10.00",
            "precio_m": "12.00",
            "precio_g": "14.00",
            "existencia": 30,
            "date_add": "2022-09-01T10:55:26Z",
        
            "foto": "img_producto.png"
        }
    },
    {
        "model": "Producto.productointerno",
        "pk": 18,
        "fields": {
            "producto": "Piña Tropical",
            "ingredientes": "Yogurt de coc / Piña y hielo frape",
            "proveedor": 4,
            "cat_producto": 3,
            "precio_p": "15.00",
            "precio_m": "17.00",
            "precio_g": "0.00",
            "existencia": 44,
            "date_add": "2022-09-01T10:56:18Z",
        
            "foto": "img_producto.png"
        }
    },
    {
        "model": "Producto.productointerno",
        "pk": 19,
        "fields": {
            "producto": "Mango Tropical",
            "ingredientes": "Yogurt de coco / Mango y hielo frape",
            "proveedor": 4,
            "cat_producto": 3,
            "precio_p": "15.00",
            "precio_m": "17.00",
            "precio_g": "0.00",
            "existencia": 45,
            "date_add": "2022-09-01T10:56:47Z",
        
            "foto": "img_producto.png"
        }
    },
    {
        "model": "Producto.productointerno",
        "pk": 20,
        "fields": {
            "producto": "Frutos rojos",
            "ingredientes": "Frutilla / Frambuesa / Mora",
            "proveedor": 4,
            "cat_producto": 3,
            "precio_p": "15.00",
            "precio_m": "18.00",
            "precio_g": "0.00",
            "existencia": 42,
            "date_add": "2022-09-01T10:57:07Z",
        
            "foto": "img_producto.png"
        }
    },
    {
        "model": "Producto.productointerno",
        "pk": 21,
        "fields": {
            "producto": "Naranja Exotica",
            "ingredientes": "Zumo de naranja con leche",
            "proveedor": 4,
            "cat_producto": 3,
            "precio_p": "14.00",
            "precio_m": "16.00",
            "precio_g": "0.00",
            "existencia": 47,
            "date_add": "2022-09-01T10:57:21Z",
        
            "foto": "img_producto.png"
        }
    },
    {
        "model": "Producto.productointerno",
        "pk": 22,
        "fields": {
            "producto": "Mango Hawaiano",
            "ingredientes": "Mango / Piña",
            "proveedor": 4,
            "cat_producto": 4,
            "precio_p": "10.00",
            "precio_m": "12.00",
            "precio_g": "14.00",
            "existencia": 12,
            "date_add": "2022-09-04T09:03:47Z",
        
            "foto": "img_producto.png"
        }
    },
    {
        "model": "Producto.productointerno",
        "pk": 23,
        "fields": {
            "producto": "Mango Cítrico",
            "ingredientes": "Mango / Maracuya",
            "proveedor": 4,
            "cat_producto": 4,
            "precio_p": "10.00",
            "precio_m": "12.00",
            "precio_g": "14.00",
            "existencia": 18,
            "date_add": "2022-09-04T09:04:10Z",
        
            "foto": "img_producto.png"
        }
    },
    {
        "model": "Producto.productointerno",
        "pk": 24,
        "fields": {
            "producto": "Rojo y cítrico",
            "ingredientes": "Sandia / Limón y Menta",
            "proveedor": 4,
            "cat_producto": 4,
            "precio_p": "10.00",
            "precio_m": "12.00",
            "precio_g": "14.00",
            "existencia": 16,
            "date_add": "2022-09-04T09:04:31Z",
        
            "foto": "img_producto.png"
        }
    },
    {
        "model": "Producto.productointerno",
        "pk": 25,
        "fields": {
            "producto": "Vitamina C+",
            "ingredientes": "Piña / Naranja y gengibre",
            "proveedor": 4,
            "cat_producto": 4,
            "precio_p": "10.00",
            "precio_m": "12.00",
            "precio_g": "14.00",
            "existencia": 20,
            "date_add": "2022-09-04T09:04:46Z",
        
            "foto": "img_producto.png"
        }
    },
    {
        "model": "Producto.productointerno",
        "pk": 26,
        "fields": {
            "producto": "Piña de colores",
            "ingredientes": "Piña frutilla con Hierba buena",
            "proveedor": 4,
            "cat_producto": 4,
            "precio_p": "10.00",
            "precio_m": "12.00",
            "precio_g": "14.00",
            "existencia": 20,
            "date_add": "2022-09-04T09:05:54Z",
        
            "foto": "img_producto.png"
        }
    },
    {
        "model": "Producto.productointerno",
        "pk": 27,
        "fields": {
            "producto": "Limonada de fresas",
            "ingredientes": "Limón / Frutilla y Hierba buena",
            "proveedor": 4,
            "cat_producto": 4,
            "precio_p": "10.00",
            "precio_m": "12.00",
            "precio_g": "14.00",
            "existencia": 24,
            "date_add": "2022-09-04T09:06:13Z",
        
            "foto": "img_producto.png"
        }
    },
    {
        "model": "Producto.productointerno",
        "pk": 28,
        "fields": {
            "producto": "Energético",
            "ingredientes": "Leche descremada / Nuez / Salvado",
            "proveedor": 4,
            "cat_producto": 5,
            "precio_p": "12.00",
            "precio_m": "14.00",
            "precio_g": "16.00",
            "existencia": 49,
            "date_add": "2022-09-10T11:26:08Z",
        
            "foto": "img_producto.png"
        }
    },
    {
        "model": "Producto.productointerno",
        "pk": 29,
        "fields": {
            "producto": "Goliat",
            "ingredientes": "Leche descremada / Avena / Plátano",
            "proveedor": 4,
            "cat_producto": 5,
            "precio_p": "12.00",
            "precio_m": "14.00",
            "precio_g": "16.00",
            "existencia": 18,
            "date_add": "2022-09-04T09:04:10Z",
        
            "foto": "img_producto.png"
        }
    },
    {
        "model": "Producto.productointerno",
        "pk": 30,
        "fields": {
            "producto": "Musculoso",
            "ingredientes": "Leche / Plátano / Frutilla / Semillas de chia",
            "proveedor": 4,
            "cat_producto": 5,
            "precio_p": "12.00",
            "precio_m": "14.00",
            "precio_g": "16.00",
            "existencia": 16,
            "date_add": "2022-09-04T09:04:31Z",
        
            "foto": "img_producto.png"
        }
    },
    {
        "model": "Producto.productointerno",
        "pk": 31,
        "fields": {
            "producto": "Mango poderoso",
            "ingredientes": "Leche / Mango / Plátano",
            "proveedor": 4,
            "cat_producto": 5,
            "precio_p": "12.00",
            "precio_m": "14.00",
            "precio_g": "16.00",
            "existencia": 20,
            "date_add": "2022-09-04T09:04:46Z",
        
            "foto": "img_producto.png"
        }
    },
    {
        "model": "Producto.productointerno",
        "pk": 32,
        "fields": {
            "producto": "Full defensas",
            "ingredientes": "Leche / Plátano / Espinaca / Frutilla",
            "proveedor": 4,
            "cat_producto": 5,
            "precio_p": "12.00",
            "precio_m": "14.00",
            "precio_g": "16.00",
            "existencia": 20,
            "date_add": "2022-09-04T09:05:54Z",
        
            "foto": "img_producto.png"
        }
    },
    {
        "model": "Producto.productointerno",
        "pk": 33,
        "fields": {
            "producto": "Saciante",
            "ingredientes": "Leche / Piña / Plátano y papaya",
            "proveedor": 4,
            "cat_producto": 5,
            "precio_p": "12.00",
            "precio_m": "14.00",
            "precio_g": "16.00",
            "existencia": 49,
            "date_add": "2022-09-10T11:26:38Z",
        
            "foto": "img_producto.png"
        }
    },
    {
        "model": "Producto.productointerno",
        "pk": 34,
        "fields": {
            "producto": "Manzana Espumosa",
            "ingredientes": "Manzana y agua mineral / Naranja y agua mineral",
            "proveedor": 4,
            "cat_producto": 6,
            "precio_p": "10.00",
            "precio_m": "12.00",
            "precio_g": "14.00",
            "existencia": 12,
            "date_add": "2022-09-04T09:03:47Z",
        
            "foto": "img_producto.png"
        }
    },
    {
        "model": "Producto.productointerno",
        "pk": 35,
        "fields": {
            "producto": "Delicia Sin Culpa",
            "ingredientes": "Manzana / Kiwi",
            "proveedor": 4,
            "cat_producto": 6,
            "precio_p": "10.00",
            "precio_m": "12.00",
            "precio_g": "14.00",
            "existencia": 18,
            "date_add": "2022-09-04T09:04:10Z",
        
            "foto": "img_producto.png"
        }
    },
    {
        "model": "Producto.productointerno",
        "pk": 36,
        "fields": {
            "producto": "Detox Guapo",
            "ingredientes": "Pera / Apio / Jengibre",
            "proveedor": 4,
            "cat_producto": 6,
            "precio_p": "10.00",
            "precio_m": "12.00",
            "precio_g": "14.00",
            "existencia": 16,
            "date_add": "2022-09-04T09:04:31Z",
        
            "foto": "img_producto.png"
        }
    },
    {
        "model": "Producto.productointerno",
        "pk": 37,
        "fields": {
            "producto": "Detox Top",
            "ingredientes": "Brocoli / Pepino / Zanahoria / Limón",
            "proveedor": 4,
            "cat_producto": 6,
            "precio_p": "10.00",
            "precio_m": "12.00",
            "precio_g": "14.00",
            "existencia": 20,
            "date_add": "2022-09-04T09:04:46Z",
        
            "foto": "img_producto.png"
        }
    },
    {
        "model": "Producto.productointerno",
        "pk": 38,
        "fields": {
            "producto": "Naranja Verde",
            "ingredientes": "Naranja / Kiwi",
            "proveedor": 4,
            "cat_producto": 7,
            "precio_p": "10.00",
            "precio_m": "12.00",
            "precio_g": "14.00",
            "existencia": 20,
            "date_add": "2022-09-04T09:05:54Z",
        
            "foto": "img_producto.png"
        }
    },
    {
        "model": "Producto.productointerno",
        "pk": 39,
        "fields": {
            "producto": "Fresa Acelerada",
            "ingredientes": "Fresa / Naranja / Perejil",
            "proveedor": 4,
            "cat_producto": 7,
            "precio_p": "10.00",
            "precio_m": "12.00",
            "precio_g": "14.00",
            "existencia": 24,
            "date_add": "2022-09-04T09:06:13Z",
        
            "foto": "img_producto.png"
        }
    },
    {
        "model": "Producto.productointerno",
        "pk": 40,
        "fields": {
            "producto": "Sin Migraña",
            "ingredientes": "Piña / Limón / Espinaca / Manzana",
            "proveedor": 4,
            "cat_producto": 8,
            "precio_p": "10.00",
            "precio_m": "12.00",
            "precio_g": "14.00",
            "existencia": 50,
            "date_add": "2022-09-10T10:58:36Z",
        
            "foto": "img_producto.png"
        }
    },
    {
        "model": "Producto.productointerno",
        "pk": 41,
        "fields": {
            "producto": "Sin Estreñimiento",
            "ingredientes": "Pepino / Perejil / Manzana / Piña / Zanahoria",
            "proveedor": 4,
            "cat_producto": 8,
            "precio_p": "10.00",
            "precio_m": "12.00",
            "precio_g": "14.00",
            "existencia": 50,
            "date_add": "2022-09-10T10:59:38Z",
        
            "foto": "img_producto.png"
        }
    },
    {
        "model": "Producto.productointerno",
        "pk": 42,
        "fields": {
            "producto": "Sin Acidez",
            "ingredientes": "Piña / Achojcha / Apio",
            "proveedor": 4,
            "cat_producto": 8,
            "precio_p": "10.00",
            "precio_m": "12.00",
            "precio_g": "14.00",
            "existencia": 50,
            "date_add": "2022-09-10T11:05:32Z",
        
            "foto": "img_producto.png"
        }
    },
    {
        "model": "Producto.productointerno",
        "pk": 43,
        "fields": {
            "producto": "Muy Cítrico",
            "ingredientes": "Naranja / Toronja / Papaya",
            "proveedor": 4,
            "cat_producto": 8,
            "precio_p": "10.00",
            "precio_m": "12.00",
            "precio_g": "14.00",
            "existencia": 48,
            "date_add": "2022-09-10T11:11:41Z",
        
            "foto": "img_producto.png"
        }
    },
    {
        "model": "Producto.productointerno",
        "pk": 44,
        "fields": {
            "producto": "Sin Acné",
            "ingredientes": "Papaya / Salvado / Canela",
            "proveedor": 4,
            "cat_producto": 8,
            "precio_p": "10.00",
            "precio_m": "12.00",
            "precio_g": "14.00",
            "existencia": 50,
            "date_add": "2022-09-10T11:12:25Z",
        
            "foto": "img_producto.png"
        }
    },
    {
        "model": "Producto.productointerno",
        "pk": 45,
        "fields": {
            "producto": "Regula la Presión Baja",
            "ingredientes": "Naranja / Zanahoria / Jengibre",
            "proveedor": 4,
            "cat_producto": 8,
            "precio_p": "10.00",
            "precio_m": "12.00",
            "precio_g": "14.00",
            "existencia": 50,
            "date_add": "2022-09-10T11:14:17Z",
        
            "foto": "img_producto.png"
        }
    },
    {
        "model": "Producto.productointerno",
        "pk": 46,
        "fields": {
            "producto": "Protector Estomacal",
            "ingredientes": "Plátano y Papaya",
            "proveedor": 4,
            "cat_producto": 8,
            "precio_p": "10.00",
            "precio_m": "12.00",
            "precio_g": "14.00",
            "existencia": 50,
            "date_add": "2022-09-10T11:14:54Z",
        
            "foto": "img_producto.png"
        }
    },
    {
        "model": "Producto.productointerno",
        "pk": 47,
        "fields": {
            "producto": "Tónico Cerebral",
            "ingredientes": "Naranja / Almendras",
            "proveedor": 4,
            "cat_producto": 8,
            "precio_p": "10.00",
            "precio_m": "12.00",
            "precio_g": "14.00",
            "existencia": 50,
            "date_add": "2022-09-10T11:16:04Z",
        
            "foto": "img_producto.png"
        }
    },
    {
        "model": "Producto.productointerno",
        "pk": 48,
        "fields": {
            "producto": "Alivia indigestión",
            "ingredientes": "Piña / Papaya",
            "proveedor": 4,
            "cat_producto": 8,
            "precio_p": "10.00",
            "precio_m": "12.00",
            "precio_g": "14.00",
            "existencia": 50,
            "date_add": "2022-09-10T11:16:04Z",
        
            "foto": "img_producto.png"
        }
    },
    {
        "model": "Producto.productointerno",
        "pk": 49,
        "fields": {
            "producto": "Ensalada de Frutas",
            "ingredientes": "",
            "proveedor": 4,
            "cat_producto": 8,
            "precio_p": "15.00",
            "precio_m": "0.00",
            "precio_g": "0.00",
            "existencia": 44,
            "date_add": "2022-09-01T10:56:18Z",
        
            "foto": "img_producto.png"
        }
    },
    {
        "model": "Producto.productointerno",
        "pk": 50,
        "fields": {
            "producto": "Musli",
            "ingredientes": "",
            "proveedor": 4,
            "cat_producto": 8,
            "precio_p": "2.00",
            "precio_m": "0.00",
            "precio_g": "0.00",
            "existencia": 45,
            "date_add": "2022-09-01T10:56:47Z",
        
            "foto": "img_producto.png"
        }
    },
    {
        "model": "Producto.productointerno",
        "pk": 51,
        "fields": {
            "producto": "Miel Extra",
            "ingredientes": "",
            "proveedor": 4,
            "cat_producto": 8,
            "precio_p": "2.00",
            "precio_m": "0.00",
            "precio_g": "0.00",
            "existencia": 42,
            "date_add": "2022-09-01T10:57:07Z",
        
            "foto": "img_producto.png"
        }
    },
    {
        "model": "Producto.productointerno",
        "pk": 52,
        "fields": {
            "producto": "Yogurt Extra ",
            "ingredientes": "",
            "proveedor": 4,
            "cat_producto": 8,
            "precio_p": "2.00",
            "precio_m": "0.00",
            "precio_g": "0.00",
            "existencia": 47,
            "date_add": "2022-09-01T10:57:21Z",
        
            "foto": "img_producto.png"
        }
    },
    {
        "model": "Producto.productointerno",
        "pk": 53,
        "fields": {
            "producto": "Café Capuccino",
            "ingredientes": "Café + Leche espumosa",
            "proveedor": 4,
            "cat_producto": 9,
            "precio_p": "12.00",
            "precio_m": "0.00",
            "precio_g": "0.00",
            "existencia": 50,
            "date_add": "2022-09-10T11:32:07Z",
        
            "foto": "img_producto.png"
        }
    },
    {
        "model": "Producto.productointerno",
        "pk": 54,
        "fields": {
            "producto": "Café Destilado",
            "ingredientes": "Café Especial Destilado",
            "proveedor": 4,
            "cat_producto": 9,
            "precio_p": "8.00",
            "precio_m": "0.00",
            "precio_g": "0.00",
            "existencia": 50,
            "date_add": "2022-09-10T11:32:07Z",
        
            "foto": "img_producto.png"
        }
    },
    {
        "model": "Producto.productointerno",
        "pk": 55,
        "fields": {
            "producto": "Café Expreso",
            "ingredientes": "Café Especial Expreso",
            "proveedor": 4,
            "cat_producto": 9,
            "precio_p": "8.00",
            "precio_m": "0.00",
            "precio_g": "0.00",
            "existencia": 50,
            "date_add": "2022-09-10T11:34:00Z",
        
            "foto": "img_producto.png"
        }
    },
    {
        "model": "Producto.productointerno",
        "pk": 56,
        "fields": {
            "producto": "Café Americano",
            "ingredientes": "Café Especial Expreso",
            "proveedor": 4,
            "cat_producto": 9,
            "precio_p": "8.00",
            "precio_m": "0.00",
            "precio_g": "0.00",
            "existencia": 50,
            "date_add": "2022-09-10T11:41:32Z",
        
            "foto": "img_producto.png"
        }
    },
    {
        "model": "Producto.productointerno",
        "pk": 57,
        "fields": {
            "producto": "Leche Caliente",
            "ingredientes": "Leche Entera Caliente",
            "proveedor": 4,
            "cat_producto": 9,
            "precio_p": "10.00",
            "precio_m": "0.00",
            "precio_g": "0.00",
            "existencia": 49,
            "date_add": "2022-09-10T11:41:59Z",
        
            "foto": "img_producto.png"
        }
    },
    {
        "model": "Producto.productointerno",
        "pk": 58,
        "fields": {
            "producto": "Leche con Café",
            "ingredientes": "Leche Entera / Café Especial",
            "proveedor": 4,
            "cat_producto": 9,
            "precio_p": "10.00",
            "precio_m": "0.00",
            "precio_g": "0.00",
            "existencia": 50,
            "date_add": "2022-09-10T11:42:41Z",
        
            "foto": "img_producto.png"
        }
    },
    {
        "model": "Producto.productointerno",
        "pk": 59,
        "fields": {
            "producto": "Mokaccino",
            "ingredientes": "Café / Chocolate Negro / Leche Espumada",
            "proveedor": 4,
            "cat_producto": 9,
            "precio_p": "12.00",
            "precio_m": "12.00",
            "precio_g": "0.00",
            "existencia": 50,
            "date_add": "2022-09-10T11:43:28Z",
        
            "foto": "img_producto.png"
        }
    },
    {
        "model": "Producto.productointerno",
        "pk": 60,
        "fields": {
            "producto": "Chocolate Espumoso",
            "ingredientes": "Chocolate + leche espumoza",
            "proveedor": 4,
            "cat_producto": 9,
            "precio_p": "12.00",
            "precio_m": "0.00",
            "precio_g": "0.00",
            "existencia": 50,
            "date_add": "2022-09-10T11:32:07Z",
        
            "foto": "img_producto.png"
        }
    },
    {
        "model": "Producto.productointerno",
        "pk": 61,
        "fields": {
            "producto": "Café cortado",
            "ingredientes": "Expresso + una pizaca de leche",
            "proveedor": 4,
            "cat_producto": 9,
            "precio_p": "10.00",
            "precio_m": "0.00",
            "precio_g": "0.00",
            "existencia": 50,
            "date_add": "2022-09-10T11:32:07Z",
        
            "foto": "img_producto.png"
        }
    },
    {
        "model": "Producto.productointerno",
        "pk": 62,
        "fields": {
            "producto": "Expresso Dulce",
            "ingredientes": "Café Expresso + leche + leche condensada",
            "proveedor": 4,
            "cat_producto": 9,
            "precio_p": "14.00",
            "precio_m": "0.00",
            "precio_g": "0.00",
            "existencia": 50,
            "date_add": "2022-09-10T11:32:07Z",
        
            "foto": "img_producto.png"
        }
    },
    {
        "model": "Producto.productointerno",
        "pk": 63,
        "fields": {
            "producto": "Caramel Machiato",
            "ingredientes": "Expresso + caramelo + leche + texturada",
            "proveedor": 4,
            "cat_producto": 9,
            "precio_p": "14.00",
            "precio_m": "0.00",
            "precio_g": "0.00",
            "existencia": 50,
            "date_add": "2022-09-10T11:32:07Z",
        
            "foto": "img_producto.png"
        }
    },
    {
        "model": "Producto.productointerno",
        "pk": 64,
        "fields": {
            "producto": "Té",
            "ingredientes": "Variedad de Té",
            "proveedor": 4,
            "cat_producto": 9,
            "precio_p": "8.00",
            "precio_m": "0.00",
            "precio_g": "0.00",
            "existencia": 50,
            "date_add": "2022-09-10T11:43:50Z",
        
            "foto": "img_producto.png"
        }
    },
    {
        "model": "Producto.productointerno",
        "pk": 65,
        "fields": {
            "producto": "Té Frutal",
            "ingredientes": "Variedad de Té",
            "proveedor": 4,
            "cat_producto": 9,
            "precio_p": "8.00",
            "precio_m": "0.00",
            "precio_g": "0.00",
            "existencia": 50,
            "date_add": "2022-09-10T11:44:15Z",
        
            "foto": "img_producto.png"
        }
    },
    {
        "model": "Producto.productointerno",
        "pk": 66,
        "fields": {
            "producto": "Mate",
            "ingredientes": "Variedad de mates",
            "proveedor": 4,
            "cat_producto": 9,
            "precio_p": "8.00",
            "precio_m": "0.00",
            "precio_g": "0.00",
            "existencia": 49,
            "date_add": "2022-09-10T11:44:44Z",
        
            "foto": "img_producto.png"
        }
    },
    {
        "model": "Producto.productointerno",
        "pk": 67,
        "fields": {
            "producto": "Té Liberador",
            "ingredientes": "Hinojo / Comino / Anís",
            "proveedor": 4,
            "cat_producto": 9,
            "precio_p": "8.00",
            "precio_m": "0.00",
            "precio_g": "0.00",
            "existencia": 50,
            "date_add": "2022-09-10T11:45:59Z",
        
            "foto": "img_producto.png"
        }
    },
    {
        "model": "Producto.productointerno",
        "pk": 68,
        "fields": {
            "producto": "Té Antiestrés",
            "ingredientes": "Manzanilla / Jazmín",
            "proveedor": 4,
            "cat_producto": 9,
            "precio_p": "8.00",
            "precio_m": "0.00",
            "precio_g": "0.00",
            "existencia": 50,
            "date_add": "2022-09-10T11:46:30Z",
        
            "foto": "img_producto.png"
        }
    },
    {
        "model": "Producto.productointerno",
        "pk": 69,
        "fields": {
            "producto": "Té Diurético",
            "ingredientes": "Laurel",
            "proveedor": 4,
            "cat_producto": 9,
            "precio_p": "8.00",
            "precio_m": "0.00",
            "precio_g": "0.00",
            "existencia": 50,
            "date_add": "2022-09-10T11:46:53Z",
        
            "foto": "img_producto.png"
        }
    },
    {
        "model": "Producto.productointerno",
        "pk": 70,
        "fields": {
            "producto": "Té Helado",
            "ingredientes": "Variedad de tés a elegir",
            "proveedor": 4,
            "cat_producto": 10,
            "precio_p": "10.00",
            "precio_m": "0.00",
            "precio_g": "0.00",
            "existencia": 49,
            "date_add": "2022-09-10T11:55:13Z",
        
            "foto": "img_producto.png"
        }
    },
    {
        "model": "Producto.productointerno",
        "pk": 71,
        "fields": {
            "producto": "Té y Hierba buena",
            "ingredientes": "Té Verde Helado con Hierba buena",
            "proveedor": 4,
            "cat_producto": 10,
            "precio_p": "10.00",
            "precio_m": "0.00",
            "precio_g": "0.00",
            "existencia": 48,
            "date_add": "2022-09-10T11:56:05Z",
        
            "foto": "img_producto.png"
        }
    },
    {
        "model": "Producto.productointerno",
        "pk": 72,
        "fields": {
            "producto": "Té Frappé",
            "ingredientes": "Variedad de tes a elegir / Hielo",
            "proveedor": 4,
            "cat_producto": 10,
            "precio_p": "12.00",
            "precio_m": "14.00",
            "precio_g": "0.00",
            "existencia": 48,
            "date_add": "2022-09-10T11:56:59Z",
        
            "foto": "img_producto.png"
        }
    },
    {
        "model": "Producto.productointerno",
        "pk": 73,
        "fields": {
            "producto": "Frappé Light",
            "ingredientes": "Té Helado con Hierba buena / Hielo",
            "proveedor": 4,
            "cat_producto": 10,
            "precio_p": "12.00",
            "precio_m": "14.00",
            "precio_g": "0.00",
            "existencia": 48,
            "date_add": "2022-09-10T11:57:37Z",
        
            "foto": "img_producto.png"
        }
    },
    {
        "model": "Producto.productointerno",
        "pk": 74,
        "fields": {
            "producto": "Americano",
            "ingredientes": "Café / Tostadas / Huevos revueltos con jamón",
            "proveedor": 4,
            "cat_producto": 11,
            "precio_p": "20.00",
            "precio_m": "0.00",
            "precio_g": "0.00",
            "existencia": 50,
            "date_add": "2022-09-10T11:23:48Z",
        
            "foto": "img_producto.png"
        }
    },
    {
        "model": "Producto.productointerno",
        "pk": 75,
        "fields": {
            "producto": "Continental",
            "ingredientes": "Café / Tostadas /Mermeladas light / Mantequilla",
            "proveedor": 4,
            "cat_producto": 11,
            "precio_p": "15.00",
            "precio_m": "0.00",
            "precio_g": "0.00",
            "existencia": 50,
            "date_add": "2022-09-10T11:24:35Z",
        
            "foto": "img_producto.png"
        }
    },
    {
        "model": "Producto.productointerno",
        "pk": 76,
        "fields": {
            "producto": "Omelette",
            "ingredientes": "Huevos revueltos con tomate / Pimenton y Orégano",
            "proveedor": 4,
            "cat_producto": 11,
            "precio_p": "12.00",
            "precio_m": "0.00",
            "precio_g": "0.00",
            "existencia": 50,
            "date_add": "2022-09-10T11:25:32Z",
        
            "foto": "img_producto.png"
        }
    },
    {
        "model": "Producto.productointerno",
        "pk": 77,
        "fields": {
            "producto": "Panqueque Light",
            "ingredientes": "Panqueque con dulce de leche / Mermelada light / Cirup Light",
            "proveedor": 4,
            "cat_producto": 11,
            "precio_p": "10.00",
            "precio_m": "0.00",
            "precio_g": "0.00",
            "existencia": 49,
            "date_add": "2022-09-10T11:26:08Z",
        
            "foto": "img_producto.png"
        }
    },
    {
        "model": "Producto.productointerno",
        "pk": 78,
        "fields": {
            "producto": "Tostadas con Palta",
            "ingredientes": "Tostadas integrales acompañadas con crema de palta",
            "proveedor": 4,
            "cat_producto": 11,
            "precio_p": "10.00",
            "precio_m": "0.00",
            "precio_g": "0.00",
            "existencia": 49,
            "date_add": "2022-09-10T11:26:38Z",
        
            "foto": "img_producto.png"
        }
    },
    {
        "model": "Producto.productointerno",
        "pk": 79,
        "fields": {
            "producto": "Quesadillas Clásicas",
            "ingredientes": "Tortilla integral acompañadas de jamón y queso",
            "proveedor": 4,
            "cat_producto": 11,
            "precio_p": "10.00",
            "precio_m": "0.00",
            "precio_g": "0.00",
            "existencia": 50,
            "date_add": "2022-09-10T11:32:07Z",
        
            "foto": "img_producto.png"
        }
    },
    {
        "model": "Producto.productointerno",
        "pk": 80,
        "fields": {
            "producto": "Quesadilla Verde",
            "ingredientes": "Tortilla integral acompañada con crema de palta",
            "proveedor": 4,
            "cat_producto": 11,
            "precio_p": "10.00",
            "precio_m": "0.00",
            "precio_g": "0.00",
            "existencia": 50,
            "date_add": "2022-09-10T11:32:07Z",
        
            "foto": "img_producto.png"
        }
    },
    {
        "model": "Producto.productointerno",
        "pk": 81,
        "fields": {
            "producto": "Berenjena estilo pizza",
            "ingredientes": "Berenjena / Queso muzzarella / Tomate y orégano",
            "proveedor": 4,
            "cat_producto": 12,
            "precio_p": "12.00",
            "precio_m": "0.00",
            "precio_g": "0.00",
            "existencia": 50,
            "date_add": "2022-09-10T11:23:48Z",
        
            "foto": "img_producto.png"
        }
    },
    {
        "model": "Producto.productointerno",
        "pk": 82,
        "fields": {
            "producto": "Panqueque Zanahoria",
            "ingredientes": "Tajada de Queso / Tajada de mermelada",
            "proveedor": 4,
            "cat_producto": 12,
            "precio_p": "10.00",
            "precio_m": "0.00",
            "precio_g": "0.00",
            "existencia": 50,
            "date_add": "2022-09-10T11:24:35Z",
        
            "foto": "img_producto.png"
        }
    },
    {
        "model": "Producto.productointerno",
        "pk": 83,
        "fields": {
            "producto": "Tostada estilo pizza",
            "ingredientes": "2 tostadas, queso muzarella y salsa de tomate especial",
            "proveedor": 4,
            "cat_producto": 12,
            "precio_p": "10.00",
            "precio_m": "0.00",
            "precio_g": "0.00",
            "existencia": 50,
            "date_add": "2022-09-10T11:25:32Z",
        
            "foto": "img_producto.png"
        }
    },
    {
        "model": "Producto.productointerno",
        "pk": 84,
        "fields": {
            "producto": "Wafles light",
            "ingredientes": "Wafles acompañados con cyrup light",
            "proveedor": 4,
            "cat_producto": 12,
            "precio_p": "12.00",
            "precio_m": "0.00",
            "precio_g": "0.00",
            "existencia": 49,
            "date_add": "2022-09-10T11:26:08Z",
        
            "foto": "img_producto.png"
        }
    },
    {
        "model": "Producto.productointerno",
        "pk": 85,
        "fields": {
            "producto": "Omelette Verde",
            "ingredientes": "Omelette con espinaca y queso muzarella",
            "proveedor": 4,
            "cat_producto": 12,
            "precio_p": "12.00",
            "precio_m": "0.00",
            "precio_g": "0.00",
            "existencia": 49,
            "date_add": "2022-09-10T11:26:38Z",
        
            "foto": "img_producto.png"
        }
    },
    {
        "model": "Producto.productointerno",
        "pk": 86,
        "fields": {
            "producto": "Panqueque Brócoli",
            "ingredientes": "Panqueque de brocoli / Queso",
            "proveedor": 4,
            "cat_producto": 12,
            "precio_p": "12.00",
            "precio_m": "0.00",
            "precio_g": "0.00",
            "existencia": 50,
            "date_add": "2022-09-10T11:32:07Z",
        
            "foto": "img_producto.png"
        }
    },
    {
        "model": "Producto.productointerno",
        "pk": 87,
        "fields": {
            "producto": "Jamón",
            "ingredientes": "Queso Muzarella / Jamón",
            "proveedor": 4,
            "cat_producto": 13,
            "precio_p": "15.00",
            "precio_m": "0.00",
            "precio_g": "0.00",
            "existencia": 50,
            "date_add": "2022-11-26T18:34:08Z",
        
            "foto": "img_producto.png"
        }
    },
    {
        "model": "Producto.productointerno",
        "pk": 88,
        "fields": {
            "producto": "Hawaiana",
            "ingredientes": "Queso Muzarella / Jamón / Piña",
            "proveedor": 4,
            "cat_producto": 13,
            "precio_p": "16.00",
            "precio_m": "0.00",
            "precio_g": "0.00",
            "existencia": 50,
            "date_add": "2022-11-26T18:34:45Z",
        
            "foto": "img_producto.png"
        }
    },
    {
        "model": "Producto.productointerno",
        "pk": 89,
        "fields": {
            "producto": "Margarita",
            "ingredientes": "Queso Muzarella / Tomate / Albahaca",
            "proveedor": 4,
            "cat_producto": 13,
            "precio_p": "15.00",
            "precio_m": "0.00",
            "precio_g": "0.00",
            "existencia": 50,
            "date_add": "2022-11-26T18:35:41Z",
        
            "foto": "img_producto.png"
        }
    },
    {
        "model": "Producto.productointerno",
        "pk": 90,
        "fields": {
            "producto": "Dr. E. Good",
            "ingredientes": "Queso Muzarella / Jamón / Maíz / Tomate",
            "proveedor": 4,
            "cat_producto": 13,
            "precio_p": "16.00",
            "precio_m": "0.00",
            "precio_g": "0.00",
            "existencia": 50,
            "date_add": "2022-11-26T18:36:35Z",
        
            "foto": "img_producto.png"
        }
    },
    {
        "model": "Producto.productointerno",
        "pk": 91,
        "fields": {
            "producto": "Italiana",
            "ingredientes": "Queso Muzarella / Jamón / aceituna / tomate",
            "proveedor": 4,
            "cat_producto": 13,
            "precio_p": "16.00",
            "precio_m": "0.00",
            "precio_g": "0.00",
            "existencia": 50,
            "date_add": "2022-11-26T18:38:42Z",
        
            "foto": "img_producto.png"
        }
    },
    {
        "model": "Producto.productointerno",
        "pk": 92,
        "fields": {
            "producto": "Laretiña",
            "ingredientes": "Queso Muzarella / Jamón / Champiñones",
            "proveedor": 4,
            "cat_producto": 13,
            "precio_p": "16.00",
            "precio_m": "0.00",
            "precio_g": "0.00",
            "existencia": 50,
            "date_add": "2022-11-26T18:39:18Z",
        
            "foto": "img_producto.png"
        }
    },
    {
        "model": "Producto.productointerno",
        "pk": 93,
        "fields": {
            "producto": "Griega",
            "ingredientes": "Queso Muzarella / Pollo / aceituna / Tomate ",
            "proveedor": 4,
            "cat_producto": 13,
            "precio_p": "16.00",
            "precio_m": "0.00",
            "precio_g": "0.00",
            "existencia": 50,
            "date_add": "2022-11-26T18:37:10Z",
        
            "foto": "img_producto.png"
        }
    },
    {
        "model": "Producto.productointerno",
        "pk": 94,
        "fields": {
            "producto": "Española",
            "ingredientes": "Queso Muzarella / Chorizo Viena / Pimentón / Tomate",
            "proveedor": 4,
            "cat_producto": 13,
            "precio_p": "16.00",
            "precio_m": "0.00",
            "precio_g": "0.00",
            "existencia": 50,
            "date_add": "2022-11-26T18:38:00Z",
        
            "foto": "img_producto.png"
        }
    },
    {
        "model": "Producto.productointerno",
        "pk": 95,
        "fields": {
            "producto": "Clásico",
            "ingredientes": "Queso Mozzarella / Jamón / Orégano en Pan especial",
            "proveedor": 4,
            "cat_producto": 14,
            "precio_p": "15.00",
            "precio_m": "0.00",
            "precio_g": "0.00",
            "existencia": 50,
            "date_add": "2022-09-10T12:03:50Z",
        
            "foto": "img_producto.png"
        }
    },
    {
        "model": "Producto.productointerno",
        "pk": 96,
        "fields": {
            "producto": "Mozzarella",
            "ingredientes": "Queso Mozzarella / Salsa de Tomate / Orégano en Pan especial",
            "proveedor": 4,
            "cat_producto": 14,
            "precio_p": "15.00",
            "precio_m": "0.00",
            "precio_g": "0.00",
            "existencia": 50,
            "date_add": "2022-09-10T12:04:58Z",
        
            "foto": "img_producto.png"
        }
    },
    {
        "model": "Producto.productointerno",
        "pk": 97,
        "fields": {
            "producto": "Italiano",
            "ingredientes": "Salame / Queso Mozzarella / Salsa de Tomate / Orégano en Pan especial",
            "proveedor": 4,
            "cat_producto": 14,
            "precio_p": "15.00",
            "precio_m": "0.00",
            "precio_g": "0.00",
            "existencia": 50,
            "date_add": "2022-09-10T12:06:33Z",
        
            "foto": "img_producto.png"
        }
    },
    {
        "model": "Producto.productointerno",
        "pk": 98,
        "fields": {
            "producto": "Cubano",
            "ingredientes": "Queso Mozzarella / Pollo / Mostaza / Pepinillo en Pan especial",
            "proveedor": 4,
            "cat_producto": 14,
            "precio_p": "15.00",
            "precio_m": "0.00",
            "precio_g": "0.00",
            "existencia": 50,
            "date_add": "2022-09-10T12:07:42Z",
        
            "foto": "img_producto.png"
        }
    },
    {
        "model": "Producto.productointerno",
        "pk": 99,
        "fields": {
            "producto": "Pollo",
            "ingredientes": "Queso Mozzarella / Tiras de pollo a la Mostaza en Pan especial",
            "proveedor": 4,
            "cat_producto": 14,
            "precio_p": "15.00",
            "precio_m": "0.00",
            "precio_g": "0.00",
            "existencia": 50,
            "date_add": "2022-09-10T12:08:34Z",
        
            "foto": "img_producto.png"
        }
    },
    {
        "model": "Producto.productointerno",
        "pk": 100,
        "fields": {
            "producto": "Pollo Waldorf",
            "ingredientes": "Queso Mozzarella + pollo + Manzana verde + apio + salsa de la casa",
            "proveedor": 4,
            "cat_producto": 14,
            "precio_p": "15.00",
            "precio_m": "0.00",
            "precio_g": "0.00",
            "existencia": 50,
            "date_add": "2022-09-10T12:08:34Z",
        
            "foto": "img_producto.png"
        }
    },
    {
        "model": "Producto.productointerno",
        "pk": 101,
        "fields": {
            "producto": "Hamburgueza de pollo",
            "ingredientes": "Mezcla especial de filete de pollo / queso / lechuga / pimentón / tomate y papas de la casa",
            "proveedor": 4,
            "cat_producto": 15,
            "precio_p": "12.00",
            "precio_m": "0.00",
            "precio_g": "0.00",
            "existencia": 50,
            "date_add": "2022-11-26T18:40:58Z",
        
            "foto": "img_producto.png"
        }
    },
    {
        "model": "Producto.productointerno",
        "pk": 102,
        "fields": {
            "producto": "Hamburguesa de Res ",
            "ingredientes": "Mezcla especial de carne de res / queso / lechuga / pimentón / tomate y papas de la casa",
            "proveedor": 4,
            "cat_producto": 15,
            "precio_p": "14.00",
            "precio_m": "0.00",
            "precio_g": "0.00",
            "existencia": 50,
            "date_add": "2022-11-26T18:41:57Z",
        
            "foto": "img_producto.png"
        }
    },
    {
        "model": "Producto.productointerno",
        "pk": 103,
        "fields": {
            "producto": "Hamburguesa vegetariana",
            "ingredientes": "Hamburguesa de lenteja / queso / lechuga / pimentón / tomate y papas de la casa",
            "proveedor": 4,
            "cat_producto": 15,
            "precio_p": "12.00",
            "precio_m": "0.00",
            "precio_g": "0.00",
            "existencia": 50,
            "date_add": "2022-11-26T18:42:49Z",
        
            "foto": "img_producto.png"
        }
    },
    {
        "model": "Producto.productointerno",
        "pk": 104,
        "fields": {
            "producto": "Cesar ",
            "ingredientes": "Tiras de filete de pollo / lechuga / Tomate / Queso rallado / pan tostado en cubitos / salsa blanca especial",
            "proveedor": 4,
            "cat_producto": 16,
            "precio_p": "16.00",
            "precio_m": "0.00",
            "precio_g": "0.00",
            "existencia": 50,
            "date_add": "2022-11-26T17:59:48Z",
        
            "foto": "img_producto.png"
        }
    },
    {
        "model": "Producto.productointerno",
        "pk": 105,
        "fields": {
            "producto": "Griega",
            "ingredientes": "Tiras de filete de pollo a la plancha / lechuga / tomate / pepino / aceituna negra / queso en cubos / con vinagreta especial",
            "proveedor": 4,
            "cat_producto": 16,
            "precio_p": "16.00",
            "precio_m": "0.00",
            "precio_g": "0.00",
            "existencia": 50,
            "date_add": "2022-11-26T18:05:55Z",
        
            "foto": "img_producto.png"
        }
    },
    {
        "model": "Producto.productointerno",
        "pk": 106,
        "fields": {
            "producto": "Waldort",
            "ingredientes": "Tiras de file de pollo a la plancha / lechuga / tomate / queso en cubos / porción de pan integral tostado / llajua de maní",
            "proveedor": 4,
            "cat_producto": 16,
            "precio_p": "16.00",
            "precio_m": "0.00",
            "precio_g": "0.00",
            "existencia": 50,
            "date_add": "2022-11-26T18:07:42Z",
        
            "foto": "img_producto.png"
        }
    },
    {
        "model": "Producto.productointerno",
        "pk": 107,
        "fields": {
            "producto": "Salpicón",
            "ingredientes": "Tiras de filete de pollo / Tiras de filete de jamon / lechuga / tomate / queso en cubos / poción de pan integral tostado / llajua de maní",
            "proveedor": 4,
            "cat_producto": 16,
            "precio_p": "16.00",
            "precio_m": "0.00",
            "precio_g": "0.00",
            "existencia": 50,
            "date_add": "2022-11-26T18:09:58Z",
        
            "foto": "img_producto.png"
        }
    },
    {
        "model": "Producto.productointerno",
        "pk": 108,
        "fields": {
            "producto": "Primavera",
            "ingredientes": "Lomito de atún / lechuga / tomate / palta / sésamo / pan tostado en cubos y vinagreta especial",
            "proveedor": 4,
            "cat_producto": 16,
            "precio_p": "18.00",
            "precio_m": "0.00",
            "precio_g": "0.00",
            "existencia": 50,
            "date_add": "2022-11-26T18:12:06Z",
        
            "foto": "img_producto.png"
        }
    },
    {
        "model": "Producto.productointerno",
        "pk": 109,
        "fields": {
            "producto": "Mexicana",
            "ingredientes": "Tiras de filete de pollo / lechuga / palta / pico de gallo / maíz queso / nachitos",
            "proveedor": 4,
            "cat_producto": 16,
            "precio_p": "16.00",
            "precio_m": "0.00",
            "precio_g": "0.00",
            "existencia": 50,
            "date_add": "2022-11-26T18:13:17Z",
        
            "foto": "img_producto.png"
        }
    },
    {
        "model": "Producto.productointerno",
        "pk": 110,
        "fields": {
            "producto": "Tropical",
            "ingredientes": "Tiras de filete de pollo a la plancha / repollo / manzana / tomate / cilantro / pan tostado en cubos y vinagreta especial",
            "proveedor": 4,
            "cat_producto": 16,
            "precio_p": "16.00",
            "precio_m": "0.00",
            "precio_g": "0.00",
            "existencia": 50,
            "date_add": "2022-11-26T18:15:27Z",
        
            "foto": "img_producto.png"
        }
    },
    {
        "model": "Producto.productointerno",
        "pk": 111,
        "fields": {
            "producto": "Pavita clásica",
            "ingredientes": "Pollo + salsa golf + rodajas de tomate",
            "proveedor": 4,
            "cat_producto": 17,
            "precio_p": "10.00",
            "precio_m": "0.00",
            "precio_g": "0.00",
            "existencia": 50,
            "date_add": "2022-11-26T18:17:01Z",
        
            "foto": "img_producto.png"
        }
    },
    {
        "model": "Producto.productointerno",
        "pk": 112,
        "fields": {
            "producto": "Pavita especial",
            "ingredientes": "Pollo + manzana verde + apio + salsa especial",
            "proveedor": 4,
            "cat_producto": 17,
            "precio_p": "10.00",
            "precio_m": "0.00",
            "precio_g": "0.00",
            "existencia": 50,
            "date_add": "2022-11-26T18:18:17Z",
        
            "foto": "img_producto.png"
        }
    },
    {
        "model": "Producto.productointerno",
        "pk": 113,
        "fields": {
            "producto": "Pavita escabechada",
            "ingredientes": "Pollo + salsa especial + escabeche de verduras",
            "proveedor": 4,
            "cat_producto": 17,
            "precio_p": "10.00",
            "precio_m": "0.00",
            "precio_g": "0.00",
            "existencia": 50,
            "date_add": "2022-11-26T18:19:34Z",
        
            "foto": "img_producto.png"
        }
    },
    {
        "model": "Producto.productointerno",
        "pk": 114,
        "fields": {
            "producto": "Sandwich jamón y queso",
            "ingredientes": "Queso muzzarella + jamon especial de pollo",
            "proveedor": 4,
            "cat_producto": 17,
            "precio_p": "10.00",
            "precio_m": "0.00",
            "precio_g": "0.00",
            "existencia": 50,
            "date_add": "2022-11-26T18:20:42Z",
        
            "foto": "img_producto.png"
        }
    },
    {
        "model": "Producto.productointerno",
        "pk": 115,
        "fields": {
            "producto": "Pollo con escabeche de verduras",
            "ingredientes": "Tiras de filete de pollo a la plancha / cebolla / zanahoria y vainita en escabeche / en pan blanco",
            "proveedor": 4,
            "cat_producto": 17,
            "precio_p": "12.00",
            "precio_m": "0.00",
            "precio_g": "0.00",
            "existencia": 50,
            "date_add": "2022-11-26T18:22:27Z",
        
            "foto": "img_producto.png"
        }
    },
    {
        "model": "Producto.productointerno",
        "pk": 116,
        "fields": {
            "producto": "Pollo con verduras frescas ",
            "ingredientes": "Filete de pollo a la plancha / lechuga / tomate / pepino / láminas de queso en pan blanco / láminas de queso en pan integral ",
            "proveedor": 4,
            "cat_producto": 17,
            "precio_p": "12.00",
            "precio_m": "0.00",
            "precio_g": "0.00",
            "existencia": 50,
            "date_add": "2022-11-26T18:24:39Z",
        
            "foto": "img_producto.png"
        }
    },
    {
        "model": "Producto.productointerno",
        "pk": 117,
        "fields": {
            "producto": "Pollo con choclito",
            "ingredientes": "Tiras de filete de pollo / maíz / pimentón / tomate / mayonesagano en Pan Especial ",
            "proveedor": 4,
            "cat_producto": 17,
            "precio_p": "12.00",
            "precio_m": "0.00",
            "precio_g": "0.00",
            "existencia": 50,
            "date_add": "2022-11-26T18:26:02Z",
        
            "foto": "img_producto.png"
        }
    },
    {
        "model": "Producto.productointerno",
        "pk": 118,
        "fields": {
            "producto": "Atun alegre",
            "ingredientes": "Lomitos de Atún / mayonesa / tomate en pan integral",
            "proveedor": 4,
            "cat_producto": 17,
            "precio_p": "12.00",
            "precio_m": "0.00",
            "precio_g": "0.00",
            "existencia": 50,
            "date_add": "2022-11-26T18:26:53Z",
        
            "foto": "img_producto.png"
        }
    },
    {
        "model": "Producto.productointerno",
        "pk": 119,
        "fields": {
            "producto": "Lomito ensalada mix",
            "ingredientes": "Lomito de res a la plancha / ensalada de pollo / zanahoria y tomate ",
            "proveedor": 4,
            "cat_producto": 17,
            "precio_p": "12.00",
            "precio_m": "0.00",
            "precio_g": "0.00",
            "existencia": 50,
            "date_add": "2022-11-26T18:28:27Z",
        
            "foto": "img_producto.png"
        }
    },
    {
        "model": "Producto.productointerno",
        "pk": 120,
        "fields": {
            "producto": "Lomito queso",
            "ingredientes": "Lomito de res a la plancha / queso / lechuga / pimentón / tomate",
            "proveedor": 4,
            "cat_producto": 17,
            "precio_p": "14.00",
            "precio_m": "0.00",
            "precio_g": "0.00",
            "existencia": 50,
            "date_add": "2022-11-26T18:29:58Z",
        
            "foto": "img_producto.png"
        }
    },
    {
        "model": "Producto.productointerno",
        "pk": 121,
        "fields": {
            "producto": "Lomito de huevo",
            "ingredientes": "Lomito de res a la plancha / huevo / lechuga / pimentón / tomate",
            "proveedor": 4,
            "cat_producto": 17,
            "precio_p": "14.00",
            "precio_m": "0.00",
            "precio_g": "0.00",
            "existencia": 50,
            "date_add": "2022-11-26T18:30:51Z",
        
            "foto": "img_producto.png"
        }
    },
    {
        "model": "Producto.productointerno",
        "pk": 122,
        "fields": {
            "producto": "Lomito completo",
            "ingredientes": "Lomito de res a la plancha / queso / huevo / lechuga / pimentón / tomate en Pan especial y papas de la casa",
            "proveedor": 4,
            "cat_producto": 17,
            "precio_p": "16.00",
            "precio_m": "0.00",
            "precio_g": "0.00",
            "existencia": 50,
            "date_add": "2022-11-26T18:31:54Z",
        
            "foto": "img_producto.png"
        }
    },
    {
        "model": "Producto.productointerno",
        "pk": 123,
        "fields": {
            "producto": "Galletas de Avena",
            "ingredientes": "Paquete de tres galletas",
            "proveedor": 4,
            "cat_producto": 18,
            "precio_p": "2.00",
            "precio_m": "0.00",
            "precio_g": "0.00",
            "existencia": 50,
            "date_add": "2022-09-10T11:59:44Z",
        
            "foto": "img_producto.png"
        }
    },
    {
        "model": "Producto.productointerno",
        "pk": 124,
        "fields": {
            "producto": "Galletas de Coco",
            "ingredientes": "Paquetes de tres galletas",
            "proveedor": 4,
            "cat_producto": 18,
            "precio_p": "2.00",
            "precio_m": "0.00",
            "precio_g": "0.00",
            "existencia": 50,
            "date_add": "2022-09-10T12:00:15Z",
        
            "foto": "img_producto.png"
        }
    },
    {
        "model": "Producto.productointerno",
        "pk": 125,
        "fields": {
            "producto": "Queque de Almendras",
            "ingredientes": "Una rodaja de queque de almendras",
            "proveedor": 4,
            "cat_producto": 18,
            "precio_p": "8.00",
            "precio_m": "0.00",
            "precio_g": "0.00",
            "existencia": 48,
            "date_add": "2022-09-10T12:01:10Z",
        
            "foto": "img_producto.png"
        }
    },
    {
        "model": "Producto.productointerno",
        "pk": 126,
        "fields": {
            "producto": "Empanada Integral",
            "ingredientes": "Empanada Integral de Queso",
            "proveedor": 4,
            "cat_producto": 18,
            "precio_p": "7.00",
            "precio_m": "0.00",
            "precio_g": "0.00",
            "existencia": 50,
            "date_add": "2022-09-10T12:01:42Z",
        
            "foto": "img_producto.png"
        }
    },
    {
        "model": "Producto.productointerno",
        "pk": 127,
        "fields": {
            "producto": "otros..",
            "ingredientes": "' '",
            "proveedor": 1,
            "cat_producto": 19,
            "precio_p": "0.00",
            "precio_m": "0.00",
            "precio_g": "0.00",
            "existencia": 50,
            "date_add": "2022-11-28T19:35:40Z",
        
            "foto": ""
        }
    }]
    categoriaProducto="Producto.csv"
    with open(categoriaProducto,mode='w',newline="")as archivo_csv:
        encabezado=["id","producto","ingredientes","proveedor","cat_producto","precio_p","precio_m","precio_g","existencia","date_add","foto"]

        archivoPro=csv.DictWriter(archivo_csv,fieldnames=encabezado)

        archivoPro.writeheader()
        for da in data_producto:
            pk=da["pk"]
            producto=da["fields"]["producto"]
            ingredientes=da["fields"]["ingredientes"]
            proveedor=da["fields"]["proveedor"]
            cat_producto=da["fields"]["cat_producto"]
            precio_p=da["fields"]["precio_p"]
            precio_m=da["fields"]["precio_m"]
            precio_g=da["fields"]["precio_g"]
            existencia=da["fields"]["existencia"]
            date_add=da["fields"]["date_add"]
            foto=da["fields"]["foto"]
            archivoPro.writerow({"id":pk,"producto":producto,"ingredientes":ingredientes,"proveedor":proveedor,"cat_producto":cat_producto,"precio_p":precio_p,
            "precio_m":precio_m,"precio_g":precio_g,"existencia":existencia,"date_add":date_add,"foto":foto})
    return(f"Los datos se han exportado correctamente a '{categoriaProducto}'.")    
pro=producto()
print(pro)
