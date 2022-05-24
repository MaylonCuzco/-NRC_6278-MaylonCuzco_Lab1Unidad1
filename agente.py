#INSTRUCCIONES
#Sin mala hierba = 0 ; Con mala hierba = 1
#UBICACIONES
#Parcela 1 = P1, Parcela 2 = P2, Parcela 3 = P3
import random
class parcela(object):
  def __init__(self):
#crear instancias entre ubicaciones y intrucciones
    self.ubicacionintruccion={'P1':'0','P2':'0','P3':'0'}
#aleatorizar las ubicaciones P1, P2 y P3
    self. ubicacionintruccion['P1']=random.choice(0,1)
    self. ubicacionintruccion['P2']=random.choice(0,1)
    self. ubicacionintruccion['P3']=random.choice(0,1)
