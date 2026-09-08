import os
from clases import Producto

def cargar_productos(ruta: str) -> list:
    productos = []
    with open(ruta, "r") as file:
        for line in file:
            line = line.strip().split(",")
            product = Producto(line[0], int(line[1]), int(line[2]))
            productos.append(product)
    return productos

def simular_ventas(productos: list) -> None:
    for producto in productos:
        producto.vender()


if __name__ == '__main__':
    ruta = os.path.join('data', 'menu.txt')
    productos = cargar_productos(ruta)
    print('=== DCCafeteria ===')
    for producto in productos:
        print(producto.descripcion())
    print(f'Productos registrados: {Producto.total_productos}')
    simular_ventas(productos)
    simular_ventas(productos)
