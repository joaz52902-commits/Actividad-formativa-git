from typing import Generator

def generador_patentes_para_oficinas() -> Generator:
    for letra in "BCDFGHJKLPRSTVWXYZ":
        for letra_2 in "BCDFGHJKLPRSTVWXYZ":
            yield letra + letra_2



    