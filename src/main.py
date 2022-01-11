import utime
from machine import Pin
import micropython
micropython.alloc_emergency_exception_buf(100)

class Rebotes():
    """Elimina los rebotes al pulsar una tecla
    (pin=pin gpio, pull=PULL_UP o PULL_DOWN,
    rutina=mombre de la rutina que atiende la interrupcion,
    flanco=IRQ_FALLING o IRQ_RISING, retardo=tiempo de retardo en ms)
    """
    def __init__(self, pin=None, pull='PULL_UP', rutina=None, flanco='IRQ_FALLING', retardo=200):
        self.pin = pin
        self.pull = pull
        self.rutina = rutina
        self.flanco = flanco
        self.retardo = retardo
        self.veces = 0
        self.momento = 0.00
        self.nivel = 0
        self.tiempo = 0.00
        self.pasaron = 0.00

        if pull == 'PULL_UP':
            self.sw1 = Pin(self.pin, Pin.IN, Pin.PULL_UP)
        else:
            self.sw1 = Pin(self.pin, Pin.IN, Pin.PULL_DOWN)
        
        if self.flanco == 'IRQ_FALLING':
            self.sw1.irq(handler = self.inte, trigger=Pin.IRQ_FALLING)
            self.flanco = 0
        else:
            self.sw1.irq(handler = self.inte, trigger=Pin.IRQ_RISING)
            self.flanco = 1

    def inte(self,p):
        self.nivel = self.sw1.value()
        if self.nivel == self.flanco:
            self.tiempo = utime.ticks_ms()
            self.pasaron = self.tiempo - self.momento
            self.momento = self.tiempo
            if self.pasaron > 200:
                self.veces +=1
                print('se presiono el boton ', self.veces, ' veces         nivel ', self.nivel, '          ms ', self.pasaron)
                self.rutina()
    
    
        

def boton1():
    print('se llamó a boton1')

boto = Rebotes(12, rutina=boton1, flanco='IRQ_FALLING')
