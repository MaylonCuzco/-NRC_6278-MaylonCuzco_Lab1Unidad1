#INSTRUCCIONES
#Sin mala hierba = 0 ; Con mala hierba = 1
#UBICACIONES
#Parcela 1 = P1, Parcela 2 = P2, Parcela 3 = P3
import random
class Parcelas(object):
  def __init__(self):
#crear instancias entre ubicaciones y intrucciones aleatoria entre el 0 y 2
   self.ubicacionestado =  {'P1': random.randint(0,1), 'P2': random.randint(0,1), 'P3': random.randint(0,1)}
        

class EntornoRobot(Parcelas):
  def __init__(self, parcela):
    print("---------- ROBOT AGRICULTOR -----------")
    print("Estado: ")
    print(parcela.ubicacionestado)
    print("Estado objetivo: {[P1:0],[P2:0],[P3:0]}")
    # El robot esta en una ubicación aleatoria
    robotubicacion = random.randint(0,2)
    costo=0

