
from cola import Cola


class Arbol(object):

    def __init__(self, info=None, datos=None):
        self.info = info
        self.datos = datos
        self.der = None
        self.izq = None
        self._altura = 0

    def arbol_vacio(self):
        return self.info is None
    
    def altura(self, arbol):
        if(arbol is None):
            return -1
        else:
            return arbol._altura

    def actualizar_altura(self):
        if(self is not None):
            altura_izq = self.altura(self.izq)
            altura_der = self.altura(self.der)
            self._altura = (altura_izq if altura_izq > altura_der else altura_der) + 1
    
    def rotacion_simple(self, control):
        if(control):
            aux = self.izq
            self.izq = aux.der
            aux.der = self
        else:
            aux = self.der
            self.der = aux.izq
            aux.izq = self
        self.actualizar_altura()
        aux.actualizar_altura()
        return aux

    def rotacion_doble(self, control):
        if(control):
            self.izq = self.izq.rotacion_simple(False)
            self = self.rotacion_simple(True)
        else:
            self. der = self.der.rotacion_simple(True)
            self = self.rotacion_simple(False)
        return self

    def balancear(self):
        if(self is not None):
            if(self.altura(self.izq)-self.altura(self.der) == 2):
                if(self.altura(self.izq.izq) >= self.altura(self.izq.der)):
                    self = self.rotacion_simple(True)
                else:
                    self = self.rotacion_doble(True)
            elif(self.altura(self.der)-self.altura(self.izq) == 2):
                if(self.altura(self.der.der) >= self.altura(self.der.izq)):
                    self = self.rotacion_simple(False)
                else:
                    self = self.rotacion_doble(False)
        return self

    def insertar_nodo(self, dato, datos=None):
        if(self.info is None):
            self.info = dato
            self.datos = datos
        elif(dato < self.info):
            if(self.izq is None):
                self.izq = Arbol(dato, datos)
            else:
                self.izq = self.izq.insertar_nodo(dato, datos)
        else:
            if(self.der is None):
                self.der = Arbol(dato, datos)
            else:
                self.der = self.der.insertar_nodo(dato, datos)
        self = self.balancear()
        self.actualizar_altura()
        return self

    def inorden(self):
        if(self.info is not None):
            if(self.izq is not None):
                self.izq.inorden()
            print(self.info, self.datos)
            if(self.der is not None):
                self.der.inorden()

    def postorden(self):
        if(self.info is not None):
            if(self.der is not None):
                self.der.postorden()
            print(self.info)
            if(self.izq is not None):
                self.izq.postorden()

    def preorden(self):
        if(self.info is not None):
            print(self.info, self._altura)
            if(self.izq is not None):
                self.izq.preorden()
            if(self.der is not None):
                self.der.preorden()

    def busqueda(self, clave):
        pos = None
        if(self.info is not None):
            if(self.info == clave):
                pos = self
            elif(clave < self.info and self.izq is not None):
                pos = self.izq.busqueda(clave)
            elif(self.der is not None):
                pos = self.der.busqueda(clave)
        return pos
    
    def busqueda_proximidad(self, clave):
        if(self.info is not None):
            if(self.izq is not None):
                self.izq.busqueda_proximidad(clave)
            if(self.info[0:len(clave)] == clave):
                print(self.info)
            if(self.der is not None):
                self.der.busqueda_proximidad(clave)
    def remplazar(self):
        """Determina el nodo que remplazará al que se elimina."""
        info, datos = None, None
        if(self.der is None):
            info = self.info
            datos = self.datos
            if(self.izq is not None):
                self.info = self.izq.info
                self.der = self.izq.der
                self.izq = self.izq.izq
                self.datos = self.izq.datos
            else:
                self.info = None
                self.datos = None
        else:
            info, datos = self.der.remplazar()
        return info, datos

    def eliminar_nodo(self, clave):
        """Elimina un elemento del árbol y lo devuelve si lo encuentra."""
        info, datos = None, None
        if(self.info is not None):
            if(clave < self.info):
                if(self.izq is not None):
                    info, datos = self.izq.eliminar_nodo(clave)
            elif(clave > self.info):
                if(self.der is not None):
                    info, datos = self.der.eliminar_nodo(clave)
            else:
                info = self.info
                datos = self.datos
                if(self.der is None and self.izq is None):
                    self.info = None
                    self.datos = None
                elif(self.izq is None):
                    self.info = self.der.info
                    self.izq = self.der.izq
                    self.der = self.der.der
                    self.datos = self.datos
                elif(self.der is None):
                    self.info = self.izq.info
                    self.der = self.izq.der
                    self.izq = self.izq.izq
                    self.datos = self.datos
                else:
                    info_aux, datos_aux = self.izq.remplazar()
                    self.info = info_aux
                    self.datos = datos_aux
                    # raiz.info, raiz.nrr = aux.info, aux.nrr
        # self = self.balancear()
        self.actualizar_altura()
        return info, datos
    
    def contar_ocurrencias(self, buscado):
        cantidad = 0
        if(self.info is not None):
            if(self.info == buscado):
                cantidad += 1
            if(self.izq is not None):
                cantidad += self.izq.contar_ocurrencias(buscado)
            if(self.der is not None):
                cantidad += self.der.contar_ocurrencias(buscado)
        return cantidad
    
    def contar_pares_impares(self):
        pares, impares = 0, 0
        if(self.info is not None):
            if(self.info % 2 == 0):
                pares += 1
            else:
                impares += 1
            if(self.izq is not None):
                par, impar = self.izq.contar_pares_impares()
                pares += par
                impares += impar
            if(self.der is not None):
                par, impar = self.der.contar_pares_impares()
                pares += par
                impares += impar
        return pares, impares

    def barrido_por_nivel(self):
        pendientes = Cola()
        pendientes.arribo(self)
        while(not pendientes.cola_vacia()):
            nodo = pendientes.atencion()
            print(nodo.info)
            if(nodo.izq is not None):
                pendientes.arribo(nodo.izq)
            if(nodo.der is not None):
                pendientes.arribo(nodo.der)    

    def barrido_por_nivel_huff(self):
        pendientes = Cola()
        pendientes.arribo(self)
        while(not pendientes.cola_vacia()):
            nodo = pendientes.atencion()
            print(nodo.info, nodo.datos)
            if(nodo.izq is not None):
                pendientes.arribo(nodo.izq)
            if(nodo.der is not None):
                pendientes.arribo(nodo.der)

    def conta_criaturas_derrotadas(self, dic):
        if(self.info is not None):
            if(self.izq is not None):
                self.izq.conta_criaturas_derrotadas(dic)
            if (self.datos["derrotado"] != "-"):
                if(self.datos['derrotado'] in dic):
                    dic[self.datos['derrotado']] += 1
                else:
                    dic[self.datos['derrotado']] = 1
            if(self.der is not None):
                self.der.conta_criaturas_derrotadas(dic)
    
    def listar_villanos(self):
        if(self.info is not None):
            if(self.izq is not None):
                self.izq.listar_villanos()
            if (self.datos["SuperHeroe"]==False):
                print(self.info, self.datos)
            if(self.der is not None):
                self.der.listar_villanos()

    def listarSuperHeoresCon_c(self):
        if(self.info is not None):
            if(self.izq is not None):
                self.izq.listarSuperHeoresCon_c()
            if ((self.datos["Nombre"][0]=="C") or (self.datos["Nombre"][0]=="c")):
                print(self.info, self.datos)
            if(self.der is not None):
                self.der.listarSuperHeoresCon_c()

    def contadorSuperHeroes(self):
        ContadorSuper = 0;
        if(self.info is not None):
                if(self.datos["SuperHeroe"] == True):
                    ContadorSuper += 1
                if(self.izq is not None):
                    ContadorSuper += self.izq.contadorSuperHeroes()
                if(self.der is not None):
                    ContadorSuper += self.der.contadorSuperHeroes()
        return ContadorSuper;

    def superHeroesDescendentes(self):
        if(self.info is not None):
            if(self.der is not None):
                self.der.superHeroesDescendentes()
            if(self.datos["SuperHeroe"] == True):
                print(self.datos)
            if(self.izq is not None):
                self.izq.superHeroesDescendentes()
    
    def bosqueheroe(self,arbolHeroe):
        if(self.info is not None):
            if(self.datos["SuperHeroe"] != False):
                arbolHeroe = arbolHeroe.insertar_nodo(self.info,self.datos)
            if(self.izq is not None):
                self.izq.bosqueheroe(arbolHeroe)
            if(self.der is not None):
                self.der.bosqueheroe(arbolHeroe)
    
    def bosquevillanos(self,arbolSupervillano):
        if(self.info is not None):
            if(self.datos["SuperHeroe"] == False):
                arbolSupervillano = arbolSupervillano.insertar_nodo(self.info,self.datos)
            if(self.izq is not None):
               self.izq.bosquevillanos(arbolSupervillano) 
            if(self.der is not None):
               self.der.bosquevillanos(arbolSupervillano)
        return arbolSupervillano
    
    def tamanioArbol(self):
        Contador = 0;
        if(self.info is not None):
                if(self.datos is not None):
                    Contador += 1
                if(self.izq is not None):
                    Contador += self.izq.tamanioArbol()
                if(self.der is not None):
                    Contador += self.der.tamanioArbol()
        return Contador;
    
    def CriaturasYvencedores(self):
        if(self.info is not None):
            if(self.izq is not None):
                self.izq.CriaturasYvencedores()
            print(self.info, self.datos["derrotado"])
            if(self.der is not None):
                self.der.CriaturasYvencedores()

    def criaturasDerrotadaHeracles(self):
        if(self.info is not None):
            if(self.izq is not None):
                self.izq.criaturasDerrotadaHeracles()
            if (self.datos["derrotado"] == "Heracles"):
                print(self.info)
            if(self.der is not None):
                self.der.criaturasDerrotadaHeracles()
    
    def criaturasCapturadasHeracles(self):
        if(self.info is not None):
            if(self.izq is not None):
                self.izq.criaturasCapturadasHeracles()
            if (self.datos["Capturada"] == "Heracles"):
                print(self.info)
            if(self.der is not None):
                self.der.criaturasCapturadasHeracles()
    def CriaturasNoDerrotadas(self):
        if(self.info is not None):
            if(self.izq is not None):
                self.izq.CriaturasNoDerrotadas()
            if (self.datos["derrotado"] == "-"):
                print(self.info)
            if(self.der is not None):
                self.der.CriaturasNoDerrotadas()
    
    def alturaSubArbolIzq(self):
        if(self.info is not None):
                print(self.info, self._altura)
                if(self.izq is not None):
                    self.izq.alturaSubArbolIzq()
                if(self.der is not None):
                    self.der.alturaSubArbolIzq()
    

    def personajesMasUnMetro(self):
        if(self.info is not None):
            if(self.izq is not None):
                self.izq.personajesMasUnMetro()
            if (self.datos["Altura"] > 100):
                print(self.info)
            if(self.der is not None):
                self.der.personajesMasUnMetro()
    def personajesMenos75kg(self):
        if(self.info is not None):
            if(self.izq is not None):
                self.izq.personajesMenos75kg()
            if (self.datos["peso"] < 75):
                print(self.info)
            if(self.der is not None):
                self.der.personajesMenos75kg()

    def mostrarLibrosDemasDe873Pag(self):
        if(self.info is not None):
            if(self.izq is not None):
                self.izq.mostrarLibrosDemasDe873Pag()
            if (self.datos["paginas"] > 873):
                print(self.info)
            if(self.der is not None):
                self.der.mostrarLibrosDemasDe873Pag()

    def mostrarTRex(self):
        if(self.info is not None):
            if(self.izq is not None):
                self.izq.mostrarTRex()
            if (self.info == "T-Rex"):
                print(self.datos)
            if(self.der is not None):
                self.der.mostrarTRex() 

    def ubicacionRaptores(self):
        if(self.info is not None):
            if(self.izq is not None):
                self.izq.ubicacionRaptores()
            if (self.info == "Raptores"):
                print("Raptor")
                print(self.datos["zona"])
            if(self.der is not None):
                self.der.ubicacionRaptores() 
    
    def contadordiplo(self):
        Contadordino = 0;
        if(self.info is not None):
                if(self.datos["nombre"] == "Diplodocus"):
                    Contadordino += 1
                if(self.izq is not None):
                    Contadordino += self.izq.contadordiplo()
                if(self.der is not None):
                    Contadordino += self.der.contadordiplo()
        return Contadordino;
# arbol = Arbol()

# dic = {} #? derrotado_por : cantidad
# arbol.conta_criaturas_derrotadas(dic)

# dato = 'Cronos'

# if(arbol.arbol_vacio()):
#     arbol.info = dato

# hijo = 'Cronos'
# padre = 'Cronos'

# pos = arbol.busqueda(padre)
# if pos:
#     if(not pos.izq):
#         pos.izq = Arbol(hijo)
#     else:
#         if not pos.izq.der:
#             pos.izq.der = Arbol(hijo)
#         else:
#             aux = pos.izq.der
#             while not aux.der:
#                 aux = aux.der
#             aux = Arbol(hijo)


# superheroe = {'name': 'Doctor Strnge', 'villano': False, 'aparicion': 1942}
# arbol = arbol.insertar_nodo(superheroe['name'], superheroe)
# superheroe = {'name': 'Capitan America', 'villano': False, 'aparicion': 1942}
# arbol = arbol.insertar_nodo(superheroe['name'], superheroe)
# superheroe = {'name': 'Capitana Marvel', 'villano': False, 'aparicion': 1942}
# arbol = arbol.insertar_nodo(superheroe['name'], superheroe)
# superheroe = {'name': 'Docasdasdas', 'villano': False, 'aparicion': 1942}
# arbol = arbol.insertar_nodo(superheroe['name'], superheroe)
# superheroe = {'name': 'Iron Man', 'villano': False, 'aparicion': 1942}
# arbol = arbol.insertar_nodo(superheroe['name'], superheroe)
# superheroe = {'name': 'Iron Hulk', 'villano': False, 'aparicion': 1942}
# arbol = arbol.insertar_nodo(superheroe['name'], superheroe)


# from random import randint
# for i in range(12):
#     arbol = arbol.insertar_nodo(randint(1, 100))
# print('ok')
# arbol.preorden()
# print()
# arbol = arbol.balancear()
# arbol.inorden()
# buscado = input('ingrese lo que desa buscar ')
# arbol.busqueda_proximidad(buscado)
# print()
# buscado = input('ingrese el nombre que desea modificar ')
# pos = arbol.busqueda(buscado)
# if(pos):
#     new_year = int(input('ingrese el nuevo año '))
#     pos.datos['aparicion'] = new_year
#     # nuevo_nombre = input('ingrese el nuevo nombre ')
#     # nombre, superheroe = arbol.eliminar_nodo(buscado)
#     # superheroe['name'] = nuevo_nombre
#     # arbol = arbol.insertar_nodo(nuevo_nombre, superheroe)
#     print()

# arbol.inorden()

# pos = arbol.busqueda('Hulk')
# if pos:
#     print(pos.datos['aparicion'])
#     pos.datos['aparicion'] = 2001
#     print(pos.datos['aparicion'])


# arbol = arbol.insertar_nodo('F')
# arbol = arbol.insertar_nodo('B')
# arbol = arbol.insertar_nodo('E')
# arbol = arbol.insertar_nodo('C')
# arbol = arbol.insertar_nodo('K')
# arbol = arbol.insertar_nodo('R')
# arbol = arbol.insertar_nodo('H')
# arbol = arbol.insertar_nodo('J')
# arbol = arbol.insertar_nodo('A')

# arbol.barrido_por_nivel()

# arbol.inorden()
# # print(arbol.izq.info, arbol.izq.izq, arbol.izq.der)
# # print(arbol.arbol_vacio())
# # arbol.preorden()

# # x = arbol.eliminar_nodo('F')
# pos = arbol.busqueda('K')
# if pos:
#     print('elemento encontrado', pos.info)

# print()
# print('barrido')
# arbol.inorden()