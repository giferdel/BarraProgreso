from progress.bar import Bar
import time

# OPCIÓN BARRA 1 CON #
def bar_proceso():
    bar1 = Bar('Procesando:', max=20)
    for num in range(20):
        time.sleep(0.2)
        bar1.next()
    bar1.finish()