precio1=float(input("introduce el precio del producto 1"))
precio2=float(input("introduce el precio del producto 2"))
precio3=float(input("introduce el precio del producto 3"))
precio4=float(input("introduce el precio del producto 4"))
total=precio1+precio2+precio3+precio4
if total>2000:
    total=(total-(total*.10))
    print(total)
else:
    print("NO TIENES DESCUENTO")    
