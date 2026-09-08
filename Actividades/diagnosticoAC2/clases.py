class Producto:
    def __init__(self, nombre: str, precio: int, stock: int) -> None:
        self.nombre = nombre
        self.precio = precio
        self._stock = stock

class Tienda:
    def __init__(self) -> None:
        self.clientes = {}

    def esta_registrado_en_tienda(self, persona: object) -> None:
        rut_persona = persona._rut
        true_or_false = rut_persona in self.clientes

        if true_or_false == False:
            self.clientes.clientes[rut_persona] = persona

class Persona:
    def __init__(self, rut: str) -> None:
        self._rut = rut
        self.carrito = []
        self.cuenta = 0

    def agregar_al_carro(self, tienda: object, rut: str, nombre: str, inventario: dict) -> None:
        #vemos si esta registrado en la tienda
        persona = tienda.clientes[rut]
        tienda.esta_registrado_en_tienda(persona)
    
        obtener_producto = inventario.get(nombre, "no encontrado")

        if obtener_producto == "no encontrado":
            print(f"No se ha encontrado el producto")

        else:
            if producto._stock > 0:
                producto = inventario[nombre]
                self.carrito.append(producto)
                self.cuenta += producto.precio
                producto._stock -= 1

            else:
                print("No hay stock del producto")

    def sacar_del_carro(self, tienda: object, rut: str, inventario: dict) -> str:
        persona = tienda.clientes[rut]
        tienda.esta_registrado_en_tienda(persona)

        if len(self.carrito) == 0:
            return "El carro esta vacio"

        #sacamos el ultimo agregado al carro 
        ultimo_agregado = self.carrito[-1]
        #eliminamos el ultimo producto agregado
        self.carrito.pop()
        self.cuenta -= ultimo_agregado.precio
        #buscamos el producto y le sumamos el que le habiamos quitado ya que lo devolvemos
        ultimo_agregado._stock += 1
        return f"{ultimo_agregado} eliminado del carrito con exito"

    def cerrar_secion(self, tienda: object, rut: str, inventario: dict) -> str:
        persona = tienda.clientes[rut]
        tienda.esta_registrado_en_tienda(persona)
        if self.carrito == []:
            return "El carro esta vacio"

        print("Productos Liberados:")
        self.cuenta = 0
        for product in self.carrito:
            print(f"{product.nombre}")
            product._stock += 1
        self.carrito = []

    def pagar(self, tienda: object, rut: str, inventario: dict) -> str:
        persona = tienda.clientes[rut]
        tienda.esta_registrado_en_tienda(persona) 

        if len(self.carrito) == []:
            return "El carro esta vacio"

        monto_a_pagar = self.cuenta
        self.cuenta = 0
        self.carrito = []
        return f"Monto a pagar: {monto_a_pagar}"
            




        



        




        

        

        

