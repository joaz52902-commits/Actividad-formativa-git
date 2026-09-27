from typing import Generator
from copy import deepcopy

class OficinaEmisora:
    contador_oficinas = 0 
    def __init__(self, generador_patente_oficina: Generator, )
        self.id = self.contador_oficinas
        self.patente_oficina = generador_patente_oficina()

        self.contador_oficinas += 1

    def generador_patente_autos(self, id_oficina: str) -> Generator:
        for letra in "BCDFGHJKLPRSTVWXYZ":
            for letra_2 in "BCDFGHJKLPRSTVWXYZ":
                for numero in "0123456789":
                    for numero_2 in "0123456789":
                       yield f"{self._id}-{letra + letra_2}-{numero + numero_2}"


class RegistroPatentes:
    def __init__(self):
        self.vehiculos = []

    def agregar_auto(self, oficina_emisora: object, auto: object):
        agregar = {
            ["oficina"] = oficina_emisora.id,
            ["marca"] = auto.marca
            ["modelo"] = auto.modelo
            ["año"] = auto.año
        }
        self.vehiculos.append

class Auto:
    def __init__(self, marca_auto: str, modelo_auto: str, año_auto: int):
        self.marca = marca_auto
        self.modelo = modelo_auto
        self.año = año_auto
        self.patente