from typing import Generator
from copy import deepcopy

class Estructura_oficinas:
    def __init__(self)-> None:
        self.oficinas = {}

    def agregar_oficina(self, oficina_emisora):
        id = oficina_emisora.id
        self.oficinas["id"] = oficina_emisora



class OficinaEmisora:
    contador_oficinas = 0 
    def __init__(self, generador_patente_oficina: Generator) -> None:
        self.id = self.contador_oficinas
        self._patente_oficina = next(generador_patente_oficina)
        self.patente_autos = self.generador_patente_autos()
        contador_oficinas += 1
        
    def generador_patente_autos(self) -> Generator:
        for letra in "BCDFGHJKLPRSTVWXYZ":
            for letra_2 in "BCDFGHJKLPRSTVWXYZ":
                for numero in "0123456789":
                    for numero_2 in "0123456789":
                       yield f"{self.patente_oficina}-{letra + letra_2}-{numero + numero_2}"
    @property
    def patente_oficina(self) -> None:
        return self.patente_oficina

    @patente_oficina.setter
    def patente_oficina(self, generador_patente_oficina: Generator) -> None:
        self._patente_oficina = generador_patente_oficina()
        return self.patente_oficina


class RegistroPatentes:
    def __init__(self) -> None:
        self.vehiculos = []

    def agregar_auto(self, id_oficina_emisora: int, auto: object) -> None:
        agregar = {
            ["oficina"]: id_oficina_emisora,
            ["marca"]: auto.marca,
            ["modelo"]: auto.modelo,
            ["anho"]: auto.anho,
            ["patente"]: auto.patente
        }
        self.vehiculos.append(agregar)

    def vehiculos_por_anho(self, anho: int) -> Generator:
        yield list(filter(lambda diccio: diccio.get(anho) == anho, self.vehiculos))

    def antiguedades_registros(self, anho_actual: int) -> Generator: 
        yield list(map(lambda diccio: anho_actual - diccio.get("anho"), self.vehiculos))

    def marcas_por_anho(self) -> Generator:
        result = {}

        for diccio in self.vehiculos:
            anho = diccio["anho"]
            marca = diccio["marca"]
            
            marcas_set = result.get(anho, set())
            marcas_set.add(marca)
            
            
            result[anho] = marcas_set
            
        return result



class Auto:
    def __init__(self, oficina_emisora: object, marca_auto: str, modelo_auto: str, anho_auto: int) -> None:
        self.marca = marca_auto
        self.modelo = modelo_auto
        self.anho = anho_auto
        self.patente = next(oficina_emisora.generador_patente_autos)