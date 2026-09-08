PRECIO_MAXIMO = 500000

class Regalo:       
    def __init__(self, nombre: str, categoria: str, precio: int) -> None:
        self.nombre = nombre
        self.categoria = categoria
        self._precio = precio

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, valor):
        if 0 <= valor <= 50000:
            self._precio = valor

        else:
                print(f"[Aviso] {valor} no es un precio valido"
                    f" (0 a {PRECIO_MAXIMO}). Se mantiene {self._precio}")
            

    def __str__(self):
        return f"{self.nombre} ({self._precio})"

    def __repr__(self):
        return f"Regalo(nombre={self.nombre}, categoria={self.categoria}, precio={self._precio})"

    
    
