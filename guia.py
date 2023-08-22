import json
import os 

dataPaisesCiudades={}
dataPaisesCiudades["Departamentos"]=[]
with open ('PaisesCiudad.json') as miArchivo:
    departamentos=json.load(miArchivo)
    for elem in departamentos["Departamentos"]:
        departamento={}
        departamento["idDep"]=elem["idDep"]
        departamento["nomDepartamento"]=elem["nomDepartamento"]
        departamento["Ciudades"]=elem["Ciudades"]
        dataPaisesCiudades["Departamentos"].append(departamento)

def pyToJson():
    with open ('PaisesCiudad.json','w') as miArchivo:
        json.dump(dataPaisesCiudades,miArchivo,ensure_ascii=False,indent=8)

def msgError(msg):
    print(msg)
    input("Presione cualquier tecla para continuar...")

def validarInput(msg):
    while True:
        try: 
            n=input(msg)
            if n==None or n.strip()=="":
                msgError("Digite algun dato...") 
                continue
            break
        except Exception as e:
            msgError("Ha ocurrido un error ",e)
    return n

def validarEntero(msg):
    while True:
        try:
            n=int(input(msg))
            if n<1:
                msgError('El valor debe ser mayor a 0...')
                continue
            break
        except ValueError:
            msgError('Ingrese el dato de forma numerica...')
    return n

def validarFloat(msg):
    while True:
        try:
            n=float(input(msg))
            return n
        except ValueError:
            msgError('Ingrese el dato de forma numerica...') 

def IdCiudades():
    with open('PaisesCiudad.json') as miPais:
        misDatos = json.load(miPais)
        listaDepartamentos = misDatos["Departamentos"]
    listaIds=[]
    for depto in listaDepartamentos:
        for ciudad in depto['Ciudades']:
            listaIds.append(ciudad["idCiudad"])
    return(listaIds)

def IdDepartamentos():
    with open('PaisesCiudad.json') as miPais:
        misDatos = json.load(miPais)
        listaDepartamentos = misDatos["Departamentos"]
    listaIds=[]
    for depto in listaDepartamentos:
        listaIds.append(depto["idDep"])
    return(listaIds)

listaIdsDepartamentos = IdDepartamentos()
listaIdsCiudades = IdCiudades()

def listarCiudades():
    os.system('cls')
    print("-"*10,"CIUDADES","-"*10, "\n")
    listaDepartamentos=dataPaisesCiudades["Departamentos"]
    for departamento in listaDepartamentos:
        for ciudad in departamento["Ciudades"]:
            print(f"> ID de la ciudad: {ciudad['idCiudad']}")
            print(f"> Ciudad: {ciudad['nomCiudad']}")
            print(f"> Direccion a imagen de la ciudad: {ciudad['imagen']}")
            print("> Coordenadas: ")
            print(f"- Latitud: {ciudad['coordenadas']['lat']}")
            print(f"- Longitud: {ciudad['coordenadas']['lon']}")
            print()
    input("Presione cualquier tecla para volver al menu.")

def adicionarCiudad():
    os.system('cls')
    print("***ADICIONA CIUDADES**")
    print()
    idDepartamento=validarEntero("> Ingrese el ID del departamento al que desea adicionar una ciudad: ")
    cont=0
    for elem in dataPaisesCiudades["Departamentos"]:
        if elem['idDep']==idDepartamento:
            cont+=1
            cuantasCiudades=validarEntero("> Numero de ciudades que adicionara al departamento: ")
            for i in range(0,cuantasCiudades):
                crearCiudadyAgregar(idDepartamento)
    if cont==0:
        msgError("Este departamento no se encuentra registrado.")
    pyToJson()

def eliminarCiudad():
   os.system('cls')
   print("***ELIMINA UN DEPARTAMENTO***\n")
   idDepartamento=validarEntero("> Ingrese el ID del departamento: ")
   idCiudad=validarEntero("> Ingrese el ID de la ciudad: ")
   for elem in dataPaisesCiudades["Departamentos"]:
       if elem['idDep']==idDepartamento:
           for ciudad in elem["Ciudades"]:
                if ciudad["idCiudad"]==idCiudad:
                    eliminar=elem["Ciudades"].index(ciudad)
                    eliminado=elem["Ciudades"].pop(eliminar)
                    print("Se elimino a: ")
                    print(eliminado)
                    pyToJson()
   
def crearCiudadyAgregar(idDep):
    for elem in dataPaisesCiudades["Departamentos"]:
        if elem['idDep']==idDep:
            idCiu=verificarCiudad()
            nomCiudad=validarInput("> Nombre de la ciudad: ")
            imag=validarInput("> Direccion a imagen de la ciudad: ")
            lat=validarFloat("> Longitud: ")
            lon=validarFloat("> Latitud: ")
            ciudad={"idCiudad":idCiu, "nomCiudad":nomCiudad,"imagen":imag,"coordenadas":{"lat":lat,"lon":lon}}
            elem["Ciudades"].append(ciudad)


def verificarCiudad():
    while True:
        try:
            idCiu=validarEntero("> Ingrese el ID de la ciudad: ")
            cont=0
            for elem in listaIdsCiudades:
                if elem==idCiu:
                    cont+=1
            if cont>0:
                msgError("Este ID ya se encuentra registrado. Vuelva a intentarlo.")
                continue
            break
        except Exception as e:
            print("Ha ocurrido un error ",e)
    return idCiu


def verificarDep():
    while True:
        try:
            idDep=validarEntero("> Ingrese el ID del departamento: ")
            cont=0
            for elem in listaIdsDepartamentos:
                if elem==idDep:
                    cont+=1
            if cont>0:
                msgError("Este ID ya se encuentra registrado. Vuelva a intentarlo.")
                continue
            break
        except Exception as e:
            msgError("Ha ocurrido un error ",e)
    return idDep


def crearDepartamento():
    os.system('cls')
    print("***ADICIONA UN DEPARTAMENTO***\n")
    idDep=verificarDep()
    dep=validarInput("> Nombre del departamento: ")
    print("\n***CIUDADES DEL DEPARTAMENTO***\n")
    departamento={"idDep":idDep,
                  "nomDepartamento":dep,
                  "Ciudades":[]}
    dataPaisesCiudades["Departamentos"].append(departamento)
    numCiudades=validarEntero("> Numero de ciudades que ingresara: ")
    for i in range (0,numCiudades):
        crearCiudadyAgregar(idDep)
    pyToJson()

def eliminarDepartamento():
    os.system('cls')
    print("***ELIMINA UN DEPARTAMENTO***\n")
    idEliminar=validarEntero("Ingrese el ID del departamento que desea eliminar: ")
    cont=0
    for elem in dataPaisesCiudades["Departamentos"]:
        cont+=1
        if elem['idDep']==idEliminar:
            idEliminar = idEliminar-1
            depEliminado = dataPaisesCiudades["Departamentos"].pop(idEliminar)
            print(depEliminado)
    if cont==0:
        print("El ID no se encuentra registrado.")
    pyToJson()        

def listarDepartamentos():
    os.system('cls')
    print("-"*10,"DEPARTAMENTOS","-"*10)
    for elem in dataPaisesCiudades["Departamentos"]:
        print(f"\n> ID del departamento: {elem['idDep']}")
        print(f"> Departamento: {elem['nomDepartamento']}")
    input("\nPresione cualquier tecla para volver al menu.")

def menu():
     os.system('cls')
     seguir=True
     while seguir:
        print("\n***DEPARTAMENTOS Y CIUDADES***")
        print()
        print("MENU:")
        print()
        print("1. Listar todas las ciudades.")
        print("2. Adicionar una nueva ciudad en un departamento existente.")
        print("3. Eliminar una ciudad de un departamento")
        print("4. Crear un Departamento.")
        print("5. Eliminar un Departamento")
        print("6. Listar todos los Departamentos")
        print("7. Salir.")
        op=validarEntero("\nOpcion -> ")

        if op==1:
            listarCiudades()
        if op==2:
            adicionarCiudad()
        if op==3:
            eliminarCiudad()
        if op==4:
            crearDepartamento()
        if op==5:
            eliminarDepartamento()
        if op==6:
            listarDepartamentos()
        if op==7:
            print("Gracias por utilizar el programa... Suerte!")
            seguir=False

menu()