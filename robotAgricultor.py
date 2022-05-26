#INSTRUCCIONES
#Sin mala hierba = 0 ; Con mala hierba = 1
#UBICACIONES
#Parcela 1 = P1, Parcela 2 = P2, Parcela 3 = P3
import random
class parcela(object):
  def __init__(self):
#crear instancias entre ubicaciones y intrucciones aleatoria entre el 0 y 2
    self.locationcondition =  {'A': random.randint(0,2), 'B': random.randint(0,2), 'C': random.randint(0,2)}
    