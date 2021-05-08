from pymongo import MongoClient

MONGO_URI = 'mongodb://localhost'

client = MongoClient(MONGO_URI)
db= client ['teststore']
collection =db['products']




MENU= "-Presione 1 para usar la funcion 1 \n-Presione 2 para usar la funcion 2 \n-Presione 3 para usar la funcion 3 \n-Presione 4 para usar la funcion 4 \n-Presione 5 para ver el catalogo \n-Presione 6 para salir \n"
menuopcion="null"

def funcion1() :
	print("Ejecutando funcion " + menuopcion +" ... \n")
                    
        
def funcion2 ():
	print("Ejecutando funcion " + menuopcion +" ... \n")


def funcion3 ():
	print("Ejecutando funcion " + menuopcion +" ... \n")


def funcion4 ():
	print("Ejecutando funcion " + menuopcion +" ... \n")


def funcion5 ():
    results = collection.find ()
    for r in results:
        print (r)





while menuopcion != "6" :
    if menuopcion == "1":
    	funcion1()
    if menuopcion == "2" :
        funcion2()

    if menuopcion == "3" :
        funcion3()

    if menuopcion == "4" :
        funcion4()
    if menuopcion == "5" :
        funcion5()

    
    menuopcion = input (MENU)
print ("ADIOS")

con.close()
print(menuopcion)


