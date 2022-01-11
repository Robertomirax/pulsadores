from lib.rebotes import Rebotes

pres1 = 0
pres2 = 0
def bot1():
    global pres1
    print('presionaste el boton 1 ', pres1, ' veces')
    pres1 +=1

def bot2():
    global pres2
    print('presionaste el boton 2 ', pres2, ' veces')
    pres2 +=1

boton1 = Rebotes(12,rutina=bot1)
boton2 = Rebotes(14,rutina=bot2)

