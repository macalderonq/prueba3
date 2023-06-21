
import numpy as np
import funciones as fn
import random as rd

datosVehiculo=[]
vehiculos=[]

while True:
    try:
        fn.menu()
        opcion=int(input("Seleccione un número del menú: "))
        if opcion==1:
            tipo=input("Ingrese el tipo de vehículo: ")
            datosVehiculo.append(tipo)
            patente=fn.comprobarPatente()
            datosVehiculo.append(patente)
            marca=input("Ingrese la marca del vehículo: ")
            datosVehiculo.append(marca)
            precio=input("Ingrese el precio del vehículo: ")
            datosVehiculo.append(precio)
            fechaRegistro=input("Ingrese la fecha de registro del vehículo: ")
            datosVehiculo.append(fechaRegistro)
            nombreDueno=input("Ingrese el nombre del dueño: ")
            datosVehiculo.append(nombreDueno)
            while True:
                opcionMulta=int(input("¿Desea ingresar una multa?\n1.-Sí\n2.-No\n"))
                if opcionMulta==1:
                    montoMulta=input("Ingrese el monto de la multa: ")
                    datosVehiculo.append(montoMulta)
                    fechaMulta=input("Ingrese la fecha de la multa: ")
                    datosVehiculo.append(fechaMulta)
                if opcionMulta==2:
                    datosVehiculo.append("0")
                    datosVehiculo.append("0")
                    break                
            vehiculos.append(datosVehiculo)
            # La lista "datosVehiculo" contiene los datos en orden [tipo,patente,marca,precio,fechaRegistro,nombreDueno,montoMulta,fechaMulta]
        if opcion==2:
            fn.buscarPatente(vehiculos)
        if opcion==3:
            fn.menuCertificados()
            opcionCertificado=int(input("Seleccione un número segun el certificado que desea: "))
            patenteCertificado=input("Ingrese la patente: ")
            if opcionCertificado==1:
                print("\n==CERTIFICADO DE EMISION DE CONTAMINANTES==")
            if opcionCertificado==2:
                print("\n==CERTIFICADO DE ANOTACIONES VIGENTES==")
            if opcionCertificado==3:
                print("\n==CERTIFICADO DE MULTAS==")
            print("")
            print("Valor $",rd.randint(1500,3500))
            print("Patente: ", patenteCertificado )
            print("")
        if opcion==4:
            print("=====FIN DEL PROCESO====")
            print("MARIA JOSE CALDERON")
            print("VERSION 1.0")
            break
    except:
        print("SE HA PRODUCIDO UN ERROR")


    
