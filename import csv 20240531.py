import csv
import json
import time
listaempresas = []
def contribucion(ventas):
    if ventas > 200000000:
        return 'Gran Contribuyente'
    elif ventas < 200000000 and ventas >100000000:
        return 'Mediano Contribuyente'
    else:
        return 'Pequenho Contribuyente'
with open('listadoRutEmpresa.csv', 'r', newline='') as archivo_csv:
    lectorcsv = csv.DictReader(archivo_csv)
    for fila in lectorcsv:
        dictempresa = {
            'rut' : fila['rut'],
            'nombre': fila['nombre'],
            'ventas': int(fila['ventas']),
            'clasificacionEmpresas': contribucion(int(fila['ventas']))
        }
        listaempresas.append(dictempresa)
with open('contribuyentes.json', 'w') as archivo:
    json.dump(listaempresas, archivo, indent=4)
with open('contribuyentes.json', 'r') as archivo1:
    datos_leidos = json.load(archivo1)
    for datos in datos_leidos:
        print(datos)
        time.sleep(1)
