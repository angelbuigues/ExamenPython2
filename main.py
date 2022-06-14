
import csv
def read_data(fichero1, fichero2):
    
    with open(fichero1, 'r') as file:
        reader = csv.reader(file)
        diccionario={}
        for row in reader:
            diccionario[row[0]]=row[2]
            print(row)


    print("---Diccionario----")

    print(diccionario)
    '''
     with open(fichero2, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

    
    '''
   

if __name__ == "__main__":
    fichero1 = "stops_data.csv"
    fichero2 = "stops.csv"

    read_data(fichero1,fichero2)


