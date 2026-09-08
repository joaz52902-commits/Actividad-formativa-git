import os
import collections
from clases import Producto, Tienda, Persona

if __name__ == "__main__":
    carpeta = input("Ingrese nombre de carpeta: ")
    productos_path = os.path.join(carpeta, "productos.txt")
    acciones_path = os.path.join(carpeta, "acciones.txt")

    inventario = {}
    tienda = Tienda()
    with open(productos_path, "r") as productos_file:
        for producto_line in productos_file.readlines():
            valores = producto_line.strip().split(",")
            nombre = valores[0]
            precio = int(valores[1])
            cantidad = int(valores[2])
            product = Producto(nombre, int(precio), int(cantidad))
            inventario[nombre] = product

    with open(acciones_path, "r") as acciones_file:
        for accion_line in acciones_file.readlines():
            valores = accion_line.strip().split(",")
            accion = valores[0]
            rut = valores[1]
            persona = Persona(rut)
            if accion == "Agregar al carro":
                nombre_producto = valores[2]
                persona.agregar_al_carro(tienda, rut, nombre_producto, inventario)

            elif accion == "Cerrar sesion":
                persona.cerrar_secion(tienda, rut, inventario)

            elif accion == "Sacar del carro":
                persona.sacar_del_carro(tienda, rut, inventario)
                
            elif accion ==  "Pagar":
                persona.pagar(tienda, rut, nombre, inventario)