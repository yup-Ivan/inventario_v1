class Producto(object):

    def __init__(self, id, nombre, precio, descripcion, unidades):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.descripcion = descripcion
        self.unidades = unidades

class Almacen(object):

    def __init__(self, ubicacion):
        self.lista_prod = []
        self.lista_mov = []
        self.ubic = ubicacion
        self.precio = None #cambiar

    def alta_producto(self, producto):
        for prod in self.lista_prod:
            if prod.id == producto.id:
                prod_en_cuestion = prod
                prod_en_cuestion.unidades += producto.unidades
                return 'Como el producto ya existia, se han actualizado sus unidades.'
        
        self.lista_prod.append(producto)
        return 'Se ha añadido el producto.'

    def stock(self, id, unidades):
        for producto in self.lista_prod:
            if producto.id == id:
                producto.unidades += unidades
            return producto.unidades
        
    def recuperar_producto(self, criterio, valor):
        pass

    def baja(self, prod):
        self.lista_prod.remove(prod)

    def verificar_disponibilidad(self, id, cantidad):
        for producto in self.lista_prod:
            if producto.id == id:
                if producto.unidades >= cantidad:
                    return f'Tu artículo está disponible y hay {cantidad} o más en stock.'
                return f'Tu artículo solo tiene {producto.unidades} ud en stock.'
            return f'No se encuentra el articulo con el id {id}.'
    
    @property
    def mostrar_productos(self):
        for producto in self.lista_prod:
            print(f'--------------------------------\nID: {producto.id}\nNOMBRE: {producto.nombre}\nPRECIO: {producto.precio}\nDESCRIPCIÓN: {producto.descripcion}\nUNIDADES: {producto.unidades}')
        print('--------------------------------')

    def historial_movimientos(self, producto):
        return self.lista_mov