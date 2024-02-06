from funciones.utils import *

almacen = Almacen('Alicante')
prod1 = Producto('001', 'Leche', 7, 'Semidesnatada', 5)
prod2 = Producto('002', 'Leche', 6, 'Entera', 4)
prod3 = Producto('002', 'Leche', 6, 'Entera', 4)

print(almacen.alta_producto(prod1))
print(almacen.alta_producto(prod2))
print(almacen.alta_producto(prod3))
#almacen.baja(prod2)
almacen.mostrar_productos
print(almacen.verificar_disponibilidad('001', 5))
print(f'Ahora tu producto tiene {almacen.stock("001", 2)} unidades en stock.')