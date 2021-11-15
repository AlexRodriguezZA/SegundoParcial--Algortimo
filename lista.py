
def __criterio(dato, criterio):
    if(criterio is None):
        return dato
    else:
        return dato[criterio]

def quicksort(vector, inicio, fin, criterio):
    primero = inicio
    ultimo = fin -1
    pivote = fin
    while(primero < ultimo):
        while(__criterio(vector[primero], criterio) <= __criterio(vector[pivote], criterio) and primero <= ultimo):
            primero += 1
        while(__criterio(vector[ultimo], criterio) > __criterio(vector[pivote], criterio) and ultimo >= primero):
            ultimo -= 1
        if(primero < ultimo):
            vector[primero], vector[ultimo] = vector[ultimo], vector[primero]
    if(__criterio(vector[pivote], criterio) < __criterio(vector[primero], criterio)):
        vector[primero], vector[pivote] = vector[pivote], vector[primero]

    if(inicio < primero):
        quicksort(vector, inicio, primero -1, criterio)
    if(fin > primero):
        quicksort(vector, primero + 1, fin, criterio)

class Lista(object):
    """crea un objeto de tipo lista"""

    def __init__(self):
        self.__elementos = []
    
    def __criterio(self, dato, criterio):
        if(criterio == None):
            return dato
        else:
            return dato[criterio]

    def insertar(self, dato, criterio=None): #! tener en cuenta que la insercion es ordenada
        if(len(self.__elementos) == 0):
            self.__elementos.append(dato)
        elif(self.__criterio(dato, criterio) < self.__criterio(self.__elementos[0], criterio)):
            self.__elementos.insert(0, dato)
        else:
            pos = 0
            while(pos < len(self.__elementos) and self.__criterio(dato, criterio)>=self.__criterio(self.__elementos[pos], criterio)):
                pos +=1 
            self.__elementos.insert(pos, dato) 


    def eliminar(self, dato, criterio=None, clave=None, criterio_clave=None):
        pos = self.busqueda(dato, criterio, clave, criterio_clave)
        if(pos != -1):
            return self.__elementos.pop(pos)
        else:
            return None


    def modificar_elemento(self, pos, nuevo_valor, criterio=None):
        self.__elementos.pop(pos)
        self.insertar(nuevo_valor, criterio)

    def busqueda(self, buscado, criterio=None, clave=None, criterio_clave=None):
        pos = -1
        primero = 0
        ultimo = len(self.__elementos) -1
        while(primero <= ultimo and pos == -1):
            medio = (primero + ultimo) // 2
            if(self.__criterio(self.__elementos[medio], criterio) == buscado):
                pos = medio
            elif(self.__criterio(self.__elementos[medio], criterio) > buscado):
                ultimo = medio -1
            else:
                primero = medio + 1

        if(pos != -1 and clave is not None and self.__elementos[pos][criterio_clave] != clave):
            while(self.__criterio(self.__elementos[pos], criterio) == self.__criterio(self.__elementos[pos-1], criterio)):
                pos -= 1
            
            while(self.__elementos[pos][criterio_clave] != clave and 
                self.__criterio(self.__elementos[pos], criterio) == self.__criterio(self.__elementos[pos+1], criterio)):
                pos += 1
            
            if(self.__elementos[pos][criterio_clave] != clave):
                pos = -1

        return pos

        # [1, 2, 3, 4, 4, 4, 5, 6,7]
    
    def obtener_elemento(self, pos):
        if(pos >= 0):
            return self.__elementos[pos]
        else:
            return None

    def lista_vacia(self):
        return len(self.__elementos) == 0
    
    def tamanio(self):
        return len(self.__elementos)

    def barrido(self):
        for elemento in self.__elementos:
            print(elemento)
    
    def barrido_jedi(self):
        for elemento in self.__elementos:
            print(elemento['name'], elemento['species'])
    
    def barrido_stormtrooper(self, numero):
        for elemento in self.__elementos:
            if(elemento['codigo'] % 1000 == numero):
                print(elemento['legion'], elemento['codigo'])
    
    def barrido_stormtrooper_legion(self, legion):
        for elemento in self.__elementos:
            if(elemento['legion'] == legion):
                print(elemento['legion'], elemento['codigo'])
    
    def barrido_green(self):
        for elemento in self.__elementos:
            if('green' in elemento['lightsaber_color']):
                print(elemento['name'])
    
    def barrido_lista_autos(self):
        for elemento in self.__elementos:
            print(elemento)
            print('autos:')
            elemento['autos'].barrido()

    # def barrido(self):
    #     for elemento in self.__elementos:
    #         for valor in elemento.values():
    #             print(valor)
        
    def barrido_eliminando(self, datos_eliminar):

        for elemento in self.__elementos:
            if(elemento in datos_eliminar):
                self.__elementos.remove(elemento)
    
    def ordenar(self, criterio):
        quicksort(self.__elementos, 0, len(self.__elementos)-1, criterio)


# from random import randint
# lista_vocales = Lista()
# lista_num = Lista()
# lista_par = Lista()
# lista_impar = Lista()
# lista_personas = Lista()
# lista_uno = Lista()
# lista_dos = Lista()

# for i in range(5):
#     lista_uno.insertar(i)
#     lista_dos.insertar(randint(1,10))

# print('lista uno')
# lista_uno.barrido()
# print()
# print('lista dos')
# lista_dos.barrido()
# print()

# for i in range(lista_dos.tamanio()):
#     num = lista_dos.obtener_elemento(i)
#     if(lista_uno.busqueda(num) == -1):
#         lista_uno.insertar(num)

# lista_uno.barrido()


# for i in range(20):
#     lista_num.insertar(randint(1,999))

# # lista_num.barrido()
# # while(not lista_num.lista_vacia()):
# #     print(lista_num.eliminar(lista_num.obtener_elemento(0)))

# for i in range(lista_num.tamanio()):
#     num = lista_num.obtener_elemento(i)
#     if(num % 2 == 0):
#         lista_par.insertar(num)
#     else:
#         lista_impar.insertar(num)

# print('lista par')
# lista_par.barrido()
# print()
# print('lista impar')
# lista_impar.barrido()



# for i in range(50):
#     vocal = chr(randint(65, 90))
#     lista_vocales.insertar(vocal)

# lista_vocales.barrido()

# vocales = ['A', 'E', 'I', 'O', 'U']

# for vocal in vocales:
#     aux = lista_vocales.eliminar(vocal)
#     while(aux is not None):
#         aux = lista_vocales.eliminar(vocal)

# # lista_vocales.barrido_eliminando(vocales)
# print()
# lista_vocales.barrido()

# datos = [
#     {'name':'juan','edad': 34, 'provincia' : 'chaco', 'dni': 32, 'autos': Lista()},
#     {'name':'juan','edad': 80, 'provincia' : 'misiones', 'dni': 20, 'autos': Lista()},
#     {'name':'maria','edad': 18, 'provincia' : 'entre rios', 'dni': 28, 'autos': Lista()},
#     {'name':'julieta','edad': 18, 'provincia' : 'catamarca', 'dni': 45, 'autos': Lista()},
#     {'name':'carlos','edad': 40, 'provincia' : 'entre rios', 'dni': 38, 'autos': Lista()},

# ]

# for i in range(10):
#     persona = {}
#     persona['name'] = input('ingrese nombre ')
#     persona['edad'] = int(input('ingrese edad '))
#     # faltan campos
    # lista_personas.insertar(persona, 'name')

# for persona in datos:
#     lista_personas.insertar(persona, 'name')

# auto1 = {'modelo': 2020, 'marca': 'fiat', 'patente': 'abc123'}
# auto2 = {'modelo': 2020, 'marca': 'ford', 'patente': 'abc456'}
# auto3 = {'modelo': 2020, 'marca': 'ford', 'patente': 'abc789'}

# pos = lista_personas.busqueda('maria', 'name', 28, 'dni')
# if(pos != -1):
#     lista_personas.obtener_elemento(pos)['autos'].insertar(auto1, 'marca')
#     lista_personas.obtener_elemento(pos)['autos'].insertar(auto2, 'marca')
#     lista_personas.obtener_elemento(pos)['autos'].insertar(auto3, 'marca')

# pos_auto = lista_personas.obtener_elemento(pos)['autos'].busqueda('ford', 'marca', 'abc789', 'patente')
# if(pos_auto != -1):
#     lista_personas.obtener_elemento(pos)['autos'].obtener_elemento(pos_auto)['modelo'] = 2013

# lista_personas.barrido_lista_autos()


# print('elemento eliminado', lista_personas.eliminar('juan', 'name', 38, 'dni'))
# print()
# lista_personas.barrido()

# print()
# pos = lista_personas.busqueda(18, 'edad', 'catamarca', 'provincia')
# print(lista_personas.obtener_elemento(pos))

# for i in range(0, 10):
#     lista_num.insertar(randint(0, 100))

# lista_num.barrido()
# print()
# numero = int(input('ingrese valor a buscar '))
# print(lista_num.busqueda(numero))


# lista_num.modificar_elemento(pos, 43)
# print()
# numero = int(input('ingrese valor a eliminar '))
# print(lista_num.eliminar(numero))
# print()
# lista_num.barrido()
