from abc import ABC, abstractmethod



class Aldeano(ABC):

    def __init__(self, nombre: str, especie: str, **kwargs) -> None:

        super().__init__(**kwargs)
        self.nombre = nombre
        self.especie = especie
        self.amistad = 0

    def sumar_amistad(self, puntos: int) -> None:

        self.amistad = max(0, min(100, self.amistad + puntos))

    @abstractmethod
    def __add__(self, regalo):
        pass

    def __str__(self) -> str:
        return f"{self.nombre} ({self.especie}) - amistad: {self.amistad}"

    def __repr__(self) -> str:
        return (f"{type(self).__name__}(nombre='{self.nombre}', "
                f"especie='{self.especie}', amistad={self.amistad})")



class Interaccion:
    def __init__(self, aldeano: Aldeano, regalo, puntos: int) -> None:
        self.aldeano = aldeano
        self.regalo = regalo
        self.puntos = puntos

    def __str__(self) -> str:
        return (f"{self.aldeano.nombre} recibio {self.regalo.nombre} "
                f"({self.puntos:+d} de amistad)")

    def __repr__(self) -> str:
        return (f"Interaccion(aldeano='{self.aldeano.nombre}', "
                f"regalo='{self.regalo.nombre}', puntos={self.puntos})")
