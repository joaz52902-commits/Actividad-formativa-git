import queue
import threading
import time
from random import randint

cola_emergencias = queue.Queue()
alerta_tormenta = threading.Event()

registro_hospital = {}
lock_registro = threading.Lock()

class EstacionMeteorologica(threading.Thread):
    def __init__(self):
        super().__init__()
        self.daemon = True

    def run(self):
        while True:
            tiempo = randint(2,4)
            print("Alerta de tormenta")
            alerta_tormenta.clear()
            time.sleep(tiempo)
            print("Tormenta a terminado")
            alerta_tormenta.set()
