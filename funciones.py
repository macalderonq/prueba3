def menu():
    print("======= MENÚ ======")
    print("")
    print("1.- Grabar")
    print("2.- Buscar")
    print("3.- Imprimir Certificados")
    print("4.- Salir")
    print("")


def comprobarPatente():  
    patenteCorrecta=False
    letra1=False
    letra2=False
    letra3=False
    letra4=False
    letrasCorrectas=False
    numero1Correcto=False
    numero2Correcto=False  
    while patenteCorrecta==False:
        patente=input("Ingrese la patente del vehículo: ")
        for i in range(1,10):
            if str(i)!=patente[0]:
                letra1=True
        for i in range(1,10):
            if str(i)!=patente[1]:
                letra2=True
        for i in range(1,10):
            if str(i)!=patente[2]:
                letra3=True
        for i in range(1,10):
            if str(i)!=patente[3]:
                letra4=True
        if letra1==True and letra2==True and letra3==True and letra4==True:
            letrasCorrectas=True
        for i in range(1,10):
            if str(i)==patente[4]:
                numero1Correcto=True
        for i in range(1,10):
            if str(i)==patente[5]:
                numero2Correcto=True
        if letrasCorrectas==True and numero1Correcto==True and numero2Correcto==True:
            patenteCorrecta==True
            break
        else:
            print("La patente es incorrecta.")
    return patente

def buscarPatente(vehiculos):
    patenteBuscar=input("Ingrese la patente que desea buscar:")
    for vehiculo in vehiculos:
        if vehiculo[1]==patenteBuscar:
            print("=====INFORMACION=========")
            print("")
            print("Tipo: ",vehiculo[0])
            print("Patente: ",vehiculo[1])
            print("Marca: ",vehiculo[2])
            print("Precio: ",vehiculo[3])
            print("Fecha registro: ",vehiculo[4])
            print("Nombre dueño: ",vehiculo[5])
            print("Monto multa: ",vehiculo[6])
            print("Fecha multa: ",vehiculo[7])
            print("")

def menuCertificados():
    print("======= CERTIFICADOS ======")
    print("")
    print("1.- Emision de contaminantes")
    print("2.- Anotaciones vigentes")
    print("3.- Multas")
    print("4.- Salir")
    print("")