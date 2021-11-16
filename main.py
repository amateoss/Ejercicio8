import persistencia_json
lista_coches = list()
Nombre_files = input("insertar nombre de archivo: ")

while True:
    marca = input("Marca de coche:")
    if marca == "fin":
        break
    modelo = input("Modelo: ")
    combustible = input("Combustible: ")
    cilindrada = input("Cilindrada: ")
    linea = {}
    linea["Marca coche"] = marca
    linea["Modelo"] = modelo
    linea["Combustible"] = combustible
    linea["Cilindrada"] = cilindrada
    lista_coches.append(linea)
persistencia_json.store(lista_coches, Nombre_files)
lista_coches = list()
print("Lista coches:\n", lista_coches)
lista_coches = persistencia_json.retrieve(Nombre_files)
print("Lista coches:\n", lista_coches)