carrito=[]
n_productos=int(input("ingresa el numero de tus productos"))
for i in range(n_productos):
    productos=input("ingresa el producto a tu carrito")
    carrito.append(productos)
    print("lista creada correctamente")
    print(f"tu carrito contiene{carrito}")
    