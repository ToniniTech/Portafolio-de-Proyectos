import carrito
from producto import productos


carrito1 = carrito.Carrito(1, productos)

def main():
    "Prueba funcional de las clases"

    print('------ CARRITO -------') # Agregamos, eliminamos y editamos productos
    print(carrito1.agregarProducto('algodon',3))
    print(carrito1.agregarProducto('queso',3))
    print(carrito1.agregarProducto('arroz',5))
    print(carrito1.agregarProducto('chocolate', 3))
    print(carrito1.agregarProducto('cafe', 2))
    print()
    print(carrito1.eliminarProducto('arroz'))
    print(carrito1.editarProducto('chocolate', 115))
    print()
    print('----- DETALLE CARRITO -----')
    for item in carrito1.obtenerItems():
        print(f"{item.producto.nombre} {item.producto.marca} ---> {item.producto.precio}$ * {item.cantidad} = {item.cantidad*item.producto.precio}$")


if __name__ == "__main__":
    main()



