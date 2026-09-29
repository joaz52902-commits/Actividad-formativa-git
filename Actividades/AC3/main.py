from random import choice, randint
from clases import Auto, RegistroPatentes, OficinaEmisora, Estructura_oficinas
from generadores import generador_patentes_para_oficinas
MARCAS = (
    "Toyota",
    "Kia",
    "Hyundai",
    "Mazda",
    "Nissan",
    "Suzuki",
)

MODELOS = (
    "Yaris",
    "Rio",
    "Accent",
    "3",
    "Sentra",
    "Swift",
)



def simular_nuevo_vehiculo():
    return (
        randint(0, 49),
        choice(MARCAS),
        choice(MODELOS),
        randint(2007, 2026),
    )


if __name__ == "__main__":

    #creando estructura para guardar oficionas
    diccio_oficinas = Estructura_oficinas()

    #creando oficinas y guardandolas en la estructura de datos
    for i in range(50):
        office = OficinaEmisora(generador_patentes_para_oficinas)
        diccio_oficinas["office.id"] = office

    
    #creando el registro de patentes
    registro_patentes = RegistroPatentes()

    ### Registrar vehiculos
    for _ in range(500):
        numero_oficina, marca, modelo, anho = simular_nuevo_vehiculo()
        office = diccio_oficinas.get("numero_oficina", 0)
        try:
            auto = Auto(office, marca, modelo, anho)
        except:
            StopIteration()
            office.patente_oficina(next(generador_patentes_para_oficinas))


        registro_patentes.agregar_auto()

    print("Vehículos del año 2023:")
    print(list(registro_patentes.vehiculos_por_anho(2023)))

    print("Antigüedad de los vehículos en 2026:")
    print(list(registro_patentes.antiguedades_registros(2026)))

    print("Marcas por año:")
    print(registro_patentes.marcas_por_anho())
