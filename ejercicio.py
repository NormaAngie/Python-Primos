#print("Hola Alumnos")
#print("Adios mundo cruel")
#uncomentario
#ejercicio1
#a=0
#for i in range(5):
 #   a+=1
  #      print(a)


#def mensaje():
  #  print("Impime1")
   # print("implem2")

#mensaje()
#Ejercicio=6
#def sum(num1,num2):
 #   resultado=num1+num2
  #  return resultado
#almacena_resultado=sum(5,8)
#print(almacena_resultado)


#Ejercicio 11 listas(sert
#miLista=["Maria","Pepe","Marta","Antonio"]
#print(miLista[0:2])
#print(miLista[:2])
#print(miLista[2:0])
#miLista.append("Sandra")
#miLista.insert(2,"Angie")
#miLista.extend(["Ana","César"])
#print(miLista.index("César"))
#print(miLista[:])
#print("César" in miLista)
#miLista=["Maria",78.21,True,5]
#miLista.remove(5)
#print(miLista[:])
#miLista.pop() #remueve el úmo elementodela lista

#para concatenar 3 veces la misma lista
#practica Tuplas

#mitupla=("Juan",13,1,1995)
#miLista=list(mitupla)
#print(mitupla[1])
#print(miLista)

#miLista=["Juan",13,1,1995,"Juan"]
#mitupla=tuple(miLista)
#print(mitupla in mitupla)
#print(mitupla.count(13))
#print(mitupla.count("Juan"))
#print(len(mitupla))

#mitupla="Juan",13,1,1995
#print(mitupla)
#nombre,dia,mes,agno=mitupla
#print(nombre)
#print(dia)
#print(mes)
#print(agno)

#Diccionario #clave:Valor
#miDiccionario={"Alemania":"Berlin","Francia":"París","UK":"London"}
#print(miDiccionario["Francia"])
#print(miDiccionario)
#eliminar elemento
#del miDiccionario["UK"]
#print(miDiccionario)
#
#mitupla=["España","Francia","UK"]
#miDiccionario={mitupla[0]:"Madrid",mitupla[1]:"Paris",mitupla[2]:"Londres"}
#print(miDiccionario)

#miDiccionario={23:"Jordan","Nombre":"Michael","Equipo":"Chicago","anillos":{"temporadas":[1991,1992,1993,19998]}}
#print(miDiccionario)
#print(mDiccionario.keys())
#print(miDiccionario.values())
#print(len(miDiccionario))

#CONDICIONALES 1
#i
#print("Programa de avaluacion de notas de alumnos")
#nota_alumno=input()

#defevaluacion(nota):
 # valoracion="aprobado"
 # if nota<5:
  #  valoracion=r"suspenso"
 #  return valoracion
#print(evaluacion(int(nota_alumno)))4

#practica if else
#print("Verificacion de acceso")
#edad_usuario=int(input("introduce tu edad, por favor"))
#if edad_usuario<18:
 # print("No puedes pasar")
#elif edad_usuario>100:
 # print("Eres un vampiro o que?")
#else:
 # print("Puedes pasar")

#print("El programa ha finalizado")

#
#print("Verificacion de acceso")

#nota_alumno = int(input("Intoduce tu nota por favor"))

#if nota_alumno<5r:
 # print("insuficiente")
#elif nota_alumno>9:
#print("insuficiente")
#...

#practicas condicional
#edad=-7re100:
 # Print("Edad es correcta")
#else:o_
 # print("Edad incorrecta")


#salario_presi=int(input("Introduce salario prenteesid  "))
#print("salario_presi:" + str(salario_presi))    

#salario_director=int(input("introduce salario director "))
#print("salario director: " + str(salario_director))

#salario_administrativo=int(input("introduce salario administrativo "))
#print("salario administativo " + str(salario_administrativo))

#if salario_presi>salario_director>salario_administrativo:
 # print("Todo funciona correctamenteo")
#else:
 # print("Algo esta mal en esta empresa")

#print("Programa de becas al Año 2017")
#distancia_escuela=int(input("introduce la distancia a la escuela en km"))
#print(distancia_escuela)

#numero_hermanos=int(input("introduce el no. de hermanos en el centro"))
#print(numero_hermanos)

#salario_familiar=int(input("introduce salario anual bruto"))
#print(salario_familiar)

#if distancia_escuela>40 and numero_hermanos>2 and salario_familiar<=2000:
#  print("Tienes derecho a beca ")
#else:
#  print("No tienes derecho a beca")

#print("Asignaturas optativas 2017")
#print("Informatica -Pruebas de Software -Usabilidad y accesibgadilid")
#opcion=input("Escribur la asignatura escogida")
#asignatura=opcion.lower()

#if asignatura in ("informatica", "pruebas de software","usabilidad y accesibgadilid"):
 # print("Asignatura elegida " + asignaturira) 
#else:
 # print("La asignatura escogida no esta contemplada")


#bucles for,  

#for i in [1,2,3]:
#  print("Hola")

#for i in ["primavera","verano","otoño","invierno"]:
#  print("Hola")

#for i in ["primavera","verano","otoño","invierno"]:
#  print(i)
#maticas","3"]:
 # print("Hola",end="")

#for i in ["pildoras","informaticas",3]:
 # print("Hola",end="  ")

#for i in "norma_angelica@hotmail.com":
 #  print("Hola",end="  ")

#email=False
#for i in "norma_angelica@hotmail.com":
#  if (i=="@"):
#    email=True
#if email==True: 
#  print("email es correcto ")
#else:
#   print("email no es correcto ")


#"email=False
#"miEmail=input("introduce tu direccion de email:")
#"for i in miEmail:
#""  if (i=="@"):
#""    email=True
#"if email==True: 
#  print("email es correcto ")
#else:
#   print("email no es correcto ")

#email=False
#contador=0

#miEmail=input("introduce tu direccion de email:")
#for i in miEmail:
#  if (i=="@" or i=="."):
#    contador=contador+1

#if contador==2: 
#   print("email es correcto ")
#else:
#   print("email no es correcto ")

#for i in range(5):
#  print("Hola")
 
#for i in range(5):
#  print(f"valor de la variable {i}")

#for i in range(5,50,3):
#   print(f"valor de la variable {i}")
  

#valido=False
#email=input("Introduce tu email")

#for i in range(len(email)):
#  if email[i]=="@":
#    valido=True

#if  valido:
#  print("Email correcto")
#else:
#  print("Email es incorrecto")

#i=1
#while i <= 10:
 # print("Ejecucion" + str(i))
  #i=i+1  

#edad=int(input("Introduccionde la edad por favor:"))
#while edad<5 or  edad>100:
 # print("Has introducido una edad negativa. Vuelvala a intentarlo")
#edad=int(input("Introduce tu edad porfavor:"))


#print("Gracias por colaborar. Puedes pasar")
#print("Edad del aspirante " + str(edad))

#import math
#print("Programa para calculo de raiz cuadrada")
#numero=int(input("Intoduce un numero n")
#Generadores
#def generaNumeros():
#yield numeros

#def generadores(limite):
#  num=1

 # miLista=[] 
 # while num<limite:
  #  miLista.append(num*2)
   # num=num+1
  #return miLista

#print(generadores(10))


#def generaPares(limite):
#  num=1

  
 # while num<limite:
  #  yield num*2

   # num=num+1

#devuelvePares=generaPares(10)
#for i in devuelvePares:
#  print(i)

#def generaPares(limite):
#  num=1

  
 # while num<limite:
 #   yield num*2

  #  num=num+1

#devuelvePares=generaPares(10)
#print(next(devuelvePares))
#print(next(devuelvePares))
#print(next(devuelvePares))
 
#Generadores Yiedlfrom
#def miGenerador():
#  yield elementos

#*recibe uno o varios arguementos
#def devuelve_ciudades(*ciudades):
  #  for elementos in ciudades:
  #    for subElemento in elementos:
 #       yield from subElemento

#ciudades_devueltas=devuelve_ciudades("Madrid","Barcelona","Bilbao","Valencia")
#print(next(ciudades_devueltas))
#print(next(ciudades_devueltas))

#Excepciones I
#def suma(num1, num2):
#  return num1+num2

#def resta(num1,num2):
 # return num1-num2

#def multiplica(num1,num2):
 # return num1*num2

#def divide(num1,num2):
 # try:
  #  return num1/num2
  #except ZeroDivisionError:
  #  print("No se puede dividir entre 0")
  #  return "Operacion errónea"

#op1=(int(input("Introduce el primer número: ")))
#op2=(int(input("Introduce el primer número: ")))

#operacion=input("Introduce la operacion a realizar (suma, resta, multiplicacion, division):")

#if operacion=="suma":
 # print(suma(op1,op2))
#elif operacion=="resta":
 # print(resta(op1,op2))
#elif operacion=="multiplica":
#  print(multiplica(op1,op2))
#elif operacion=="divide":
 # print(divide(op1,op2))
  #control de excepcion
#else:
 # print("Operacion no completada")

#def divide(num1,num2):
 #try:
  #return num1/num2
 #except ZeroDivisionError:
  # print("No se puede dividir entre 0")
 #  return "Operacion errónea"

#while True:
  #try:
    #op1=(int(input("Introduce el primer número: ")))
   # op2=(int(input("Introduce el segundo número: ")))
  #  break
 # except ValueError:
 #   print("Los valores introducidos no son correctos, intentelo de nuevo")
  
#operacion=input("Introduce la operacion a realizar (suma, resta, multiplicacion, division):")

#if operacion=="suma":
 #print(suma(op1,op2))
#elif operacion=="resta":
 #print(resta(op1,op2))
#elif operacion=="multiplica":
 # print(multiplica(op1,op2))
#elif operacion=="divide":
 #print(divide(op1,op2))
#control de excepcion
#else:
 # print("Operacion no completada")


#def divide():
 # try:
 #   op1=(float(input("Introduce el primer número:")))
 #   op2=(float(input("Introduce el segundo número:")))
 #   print("La division es: " + str(op1/op2))
 # except ValueError:
 #   print("El valor introducido es érroneo")
 # except ZeroDivisionError:
 #   print("No se puede dividir entre 0!")
  
 # finally:
 #   print("Cálculo finalizado")

#divide()

#Excepciones 3
#def evaluaEdad(edad):
#  if edad<0:
 #   #raise TypeError("No se permiten edades negativas")
  # if edad<20:
   # return "eres muy joven"
  #elif edad<40:
   # return "Eres joven"
  #elif edad<5:
   # return "Eres maduro"
  #elif edad<100:
   # return "Cuidate..."

#print(evaluaEdad(15))

#import math
#def calculaRaiz(num1):
#  if num1<0:
#    raise ValueError ("El numero no puede ser negativo")
#  else:
#    return math.sqrt(num1)

#op1=(int(input("Introduce un numero:")))
#try:
 # print(calculaRaiz(op1))
#except ValueError as ErrorDeNumeroNegativo:
#  print(ErrorDeNumeroNegativo)
#print("Programa terminado")

#class Coche():
#  largoChasis=250
#  anchoChasis=120
#  ruedas=4
#  enmarcha=False

 # def arrancar(self): #propiedades
 #   self.enmarcha=True
    #/*miCoche.enmarcha=True
 # def estado(self):
 #   if(self.enmarcha):
 #    return"El coche está en marcha"
 #  else:
 #    return "El coche está parado"

#miCoche=Coche() #instanciar una clase
#print("El largo del coche es: ", miCoche.largoChasis)
#print("El coche tiene",miCoche.ruedas, "ruedas")
#miCoche.arrancar()

#print(miCoche.estado())

#class Coche():
  
  #largoChasis=250
  #anchoChasis=120
  #ruedas=4
  #enmarcha=False

  #def arrancar(self,arrancamos): 
    #self.enmarcha=arrancamos

    #if(self.enmarcha):
      #return "El coche está en marcha"
    #else:
     # return "El coche está parado"

  #def estado(self):
   # print("El coche tiene", self.ruedas, "ruedas. Un ancho de", self.anchoChasis, "y un largo de", self.largoChasis)

#miCoche=Coche() #instanciar una clase
#print("El largo del coche es: ", miCoche.largoChasis)
#print("El coche tiene",miCoche.ruedas, "ruedas")
#print(miCoche.arrancar(True))
#miCoche.estado()
#print("A continuacion creamos el segundo objeto----")

#miCoche2=Coche()
#print("El largo del coche es: ", miCoche2.largoChasis)
#print("El coche tiene",miCoche2.ruedas, "ruedas")
#print(miCoche2.arrancar(False))
#miCoche2.estado()

#class Coche():
  
#  def __init__(self):
#    self.__largoChasis=250
#    self.__anchoChasis=120
#    self.__ruedas=4
#    self.__enmarcha=False

#  def arrancar(self,arrancamos): 
#    self.__enmarcha=arrancamos

#    if(self.__enmarcha):
#      chequeo=self.__chequeo_interno()

#    if(self.__enmarcha and chequeo):
#        return "El coche está en marcha"

#    elif(self.__enmarcha and chequeo==False):
#      return "Algo ha ido mal en el chequeo. no podemos arrancar"
#    else:  
#      return "El coche está parado  "
   
#  def estado(self):
#    print("El coche tiene", self.__ruedas, "ruedas. Un ancho de", self.__anchoChasis, "y un largo de", self.__largoChasis)

#  def __chequeo_interno(self):
#    print("realizado chequeo interno")
#    self.gasolina="ok"
#    self.aceite="mal"
#    self.puertas="cerradas"
   
#    if(self.gasolina=="ok" and self.aceite=="ok" and self.puertas=="cerradas"):
#      return True
#    else:
#      return False


#miCoche=Coche() #instanciar una clase
#print(miCoche.arrancar(True))
#miCoche.estado()
#print("A continuacion creamos el segundo objeto----")
#miCoche2=Coche()
#print(miCoche2.arrancar(False))
#miCoche2.estado()

#class Vehiculos():
#  def __int__(self, modelo):

#    #self.marca=marca
#    self.modelo=modelo
#    self.enmarcha=False
#    self.acelera=False
#    self.frena=False
    
#  def arrancar(self):
#    self.enmarcha=True

#  def acelerar(self):
#    self.acelera=True
  
#  def frenar(self):
#    self.frena=True
  
#  def estado(self):
#    print("Marca:",  "\nModelo:",  "\nEn Marcha:", self.enmarcha, "\nAcelerando:", self.acelera,"\nFrenado:", self.frena)

#class Motox(Vehiculos):
#  hcaballito=""
#  def caballito(self):
#    hcaballito="Voy haciendo el caballito"

#miMoto1=Motox()
#miMoto1.caballito()
#miMoto1.estado()

#Ejercicio 2:

#class Transporte(): #comportamientos universales

#    def __init__(self, marca, modelo):

#        self.marca=marca

#        self.modelo=modelo
#        self.en_marcha=False
#        self.acelera=False

#        self.frena=False

#    def arrancar(self):

#        self.en_marcha=True

#    def acelerar(self):

#        self.acelera=True

#    def frenar(self):

#        self.frena=True

#    def edo(self):

        #print("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn marcha: ", self.en_marcha, #"\nAcelerando: ", self.acelera, "\nFrenando: ", self.frena)

#class Furgoneta(Transporte):
 #   def carga(self,cargar):
 #     self.cargado=cargar
 #     if(self.cargado):
 #       return "La furgoneta está cargada"
 #     else:
 #       return "La furgoneta no está cargada"

#class Moto(Transporte): #aquí le pones la super clase para que le heredes a la moto, en este caso, si no le pones a qué superclase pertenece te marca error en la consola. Es un comportamiento propio

#    hcaballito="" #aquí declaras una variable "hcaballito"  
#    def caballito(self):
#        self.hcaballito="Estás haciendo el caballito"
#    def edo(self):
         #print("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn marcha: ", self.en_marcha, #"\nAcelerando: ", self.acelera, "\nFrenando: ", self.frena,"\n", self.hcaballito)

#class VElectricos():
#    def __init__(self):
#      self.autonomia=100

#    def cargarEnergia(self):
#      self.cargando=True
      
#mi_moto=Moto("BMW", "D1800")
#mi_moto.caballito()
#mi_moto.edo()
#miFurgoneta=Furgoneta("Renault","Kangoo")
#miFurgoneta.arrancar()
#miFurgoneta.edo()
#print(miFurgoneta.carga(True))

#class BicicletaElectrica(VElectricos, Transporte):
#  pass
#miBici=BicicletaElectrica()


#Herencia Super
#class Persona():
  #def __init__(self,nombre,edad,residencia):
  #    self.nombre=nombre
  #    self.edad=edad
  #    self.residencia=residencia
#  def descripcion(self):
#    print("Nombre:", self.nombre,"Edad:",self.edad,"Residencia:",self.residencia)

#class Empleado(Persona):
#  def __init__(self,salario,antiguedad,nombre_empleado,edad_empleado,residencia_empleado):
#      super().__init__(nombre_empleado,edad_empleado,residencia_empleado)
#      self.salario=salario
#      self.antiguedad=antiguedad
#  def descripcion(self):
#    super().descripcion()
#    print("Salario:",self.salario,"Antiguedad",self.antiguedad)

#ManuelZ=Empleado(1500,15,"Manuel",55,"Colombia")
#ManuelZ.descripcion()
#principio de sustitucion, junto con la funcion isinstance.
#print(isinstance(ManuelZ,Empleado))




    
