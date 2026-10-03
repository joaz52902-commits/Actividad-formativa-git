from utilidades import imprimir_reporte
from clases import Cocina


if __name__ == "__main__":
    cocina = Cocina()
    resultado = cocina.simular_servicio

    if resultado is None:
        print("\nsimular_servicio() no retornó nada: debe retornar la tupla "
              "(tiempos, no_entregados).")
    else:
        tiempos, no_entregados = resultado
        imprimir_reporte(cocina.pedidos, tiempos, no_entregados)
