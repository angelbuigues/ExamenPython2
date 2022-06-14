
import csv
def read_data(fichero1, fichero2):
    diccionario={}

    with open(fichero1, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
              with open(fichero2, 'r') as file2:
                reader2 = csv.reader(file2)
                for row2 in reader2:
                    if(row[0]==row2[0]):
                        diccionario[row[0]]={
                            'description':row2[3],
                            'id':row2[1],
                            'lat':float(row[4]),
                            'lon':float(row[5]),
                            'name':row2[2]}

    print("---Diccionario----")
    print(diccionario)
    return diccionario

def get_name_description(clave, diccionario):
    existe = False
    
    for element in diccionario:
        if(element == clave):
            existe = True
    
    if(existe):
        print("Para la clave 1080: ")
        print("------------------------")
        print(diccionario[clave]['name'])
        print(diccionario[clave]['description'])
    else:
        print("Para una clave que no existe: ")
        print("------------------------")
        print(str(err))

def search_by_lon(lon_a_buscar,diccionario):
    existe = False
    id = -1
    if(not isinstance(lon_a_buscar, float)):
        raise ValueError("No es de tipo float")
    else:
        for element in diccionario:
            if(diccionario[element]['lon'] == lon_a_buscar):
                existe = True
                id = element
    
        if(existe):
            print("Para la clave 728257.03: ")
            print("------------------------")
            print(diccionario[id]['name'])
            print(diccionario[id]['description'])

            return id
        else:
            raise ValueError("No se ha encontrado la clave")
    

   

if __name__ == "__main__":
    fichero1 = "stops_data.csv"
    fichero2 = "stops.csv"

    diccionario = read_data(fichero1,fichero2)
    try:
        #get_name_description('1080', diccionario)
        #get_name_description('10800', diccionario)

        lon = 725915.428
        #id = search_by_lon("725915.428", diccionario)
        id = search_by_lon(lon, diccionario)
        

        print("Id encontrada: "+id)
    except ValueError as err:
        print("Se ha producido un error:"+str(err))




