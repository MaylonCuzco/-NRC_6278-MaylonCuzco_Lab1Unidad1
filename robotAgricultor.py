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

######################################################################################################################
    #El robot agricultor comienza por la parcela 1
    if robotubicacion == 0:
            print("1: El robot agricultor se ubica en la Parcela 1")
            
            if parcela.ubicacionestado['P1'] == 1:
                print("2. La Parcela 1 está con mala hierba")
                parcela.ubicacionestado['P1'] == 0
                costo = costo + 1
                print("3. Se eliminó la mala hierba de la Parcela 1, el robot se mueve a la Parcela 2")

                if parcela.ubicacionestado['P2'] == 1:
                    print("4. La Parcela 2 está con mala hierba")
                    parcela.ubicacionestado['P2'] == 0
                    costo = costo + 1
                    print("5. Se eliminó la mala hierba de la Parcela 2, el robot se mueve a la Parcela 3")
                    
                else:
                   print("4. NO hay mala hierba en la Parcela 2, el robot se mueve a la Parcela 3")

                if parcela.ubicacionestado['P3'] == 1:
                         print("6. La Parcela 3 está con mala hierba")
                         parcela.ubicacionestado['P3'] == 0
                         costo = costo + 1
                         print("7. Se eliminó la mala hierba de la Parcela 3")
                         print("------ finaliza ------")
                         print("costo:", costo)
                else:
                     print("6. NO hay mala hierba en la Parcela 3")
                     print("------ finaliza ------")
                     print("costo:", costo)               
                     
            # Si la parcela 1 esta sin mala hierba, el robot se mueve hacia la Parcela 2 y despues a la Parcela 3
            else:
                print("2. NO hay mala hierba en la Parcela 1, el robot se mueve a la Parcela 2")
                
                if parcela.ubicacionestado['P2'] == 1:
                    print("3. La Parcela 2 está con mala hierba")
                    parcela.ubicacionestado['P2'] == 0
                    costo = costo + 1
                    print("4. Se eliminó la mala hierba de la Parcela 2, el robot se mueve a la Parcela 3")
                else: 
                    print("3. NO hay mala hierba en la Parcela 2, el robot se mueve a la Parcela 3")

                if parcela.ubicacionestado['P3'] == 1:
                     print("5. La Parcela 3 está con mala hierba")
                     parcela.ubicacionestado['C'] == 0
                     costo = costo + 1
                     print("6. Se eliminó la mala hierba de la Parcela 3")
                     print("------ finaliza -----")
                     print("costo:", costo)

                else:
                      print("5. NO hay mala hierba en la Parcela 3")
                      print("------ finaliza -------")
                      print("costo:", costo)

######################################################################################################################

        #El robot agricultor comienza por la Parcela 2
    elif robotubicacion == 1:
            print("1. El robot agricultor se ubica en la Parcela 2")
            
            if parcela.ubicacionestado['P2'] == 1:
                print("2. La Parcela 2 está con mala hierba")
                parcela.ubicacionestado['P2'] == 0
                costo = costo + 1
                print("3. Se eliminó la mala hierba de la Parcela 2, el robot se mueve a la Parcela 3")

                if parcela.ubicacionestado['P3'] == 1:
                    print("4. La Parcela 3 está con mala hierba")
                    parcela.ubicacionestado['P3'] == 0
                    costo = costo + 1
                    print("5. Se eliminó la mala hierba de la Parcela 3, el robot se mueve a la Parcela 1")
                    
                else:
                   print("4. NO hay mala hierba en la Parcela 3, el robot de mueve a la Parcela 1")

                if parcela.ubicacionestado['P1'] == 1:
                         print("6. La Parcela 1 está con mala hierba")
                         parcela.ubicacionestado['P1'] == 0
                         costo = costo + 1
                         print("7. Se eliminó la mala hierba de la Parcela 1")
                         print("------finalizar------")
                         print("costo:", costo)
                else:
                     print("6. NO hay mala hierba en la Parcela 1")
                     print("------finalizar------")
                     print("costo:", costo)  
            
            # Si la parcela 2 esta sin mala hierba, el robot se mueve hacia la Parcela 3 y despues a la Parcela 1
            else:
               
                print("2. NO hay mala hierba en la Parcela 2, el robot se mueve a la Parcela 3")
               
                if parcela.ubicacionestado['P3'] == 1:
                    print("3. La Parcela 3 está con mala hierba")
                    parcela.ubicacionestado['P3'] == 0
                    costo = costo + 1
                    print("4. Se eliminó la mala hierba de la Parcela 3, el robot se mueve a la Parcela 1")
                else:
                    print("3. NO hay mala hierba en la Parcela 3, el robot se mueve a la Parcela 1")

                if parcela.ubicacionestado['P1'] == 1:
                     print("5. La Parcela 1 está con mala hierba")
                     parcela.ubicacionestado['P1'] == 0
                     costo = costo + 1
                     print("6. Se eliminó la mala hierba de la Parcela 1")
                     print("------finalizar------")
                     print("costo:", costo)

                else:
                      print("5. NO hay mala hierba en la Parcela 1")
                      print("------finalizar------")
                      print("costo:", costo)

######################################################################################################################