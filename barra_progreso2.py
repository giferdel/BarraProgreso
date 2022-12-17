from progress.bar import ChargingBar
import time, random

# OPCIÓN BARRA 2 COMPLETA
def bar_instalación():
    bar2 = ChargingBar('Instalando:', max=100)
    for num in range(100):
        time.sleep(random.uniform(0, 0.2))
        bar2.next()
    bar2.finish