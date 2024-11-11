precio_de_producto = 0
precio_final=0
descuento = 0
precio_de_producto = int(input("Ingrese el precio del producto:"))

if precio_de_producto < 100:
    descuento = precio_de_producto * 0.02
    precio_final = precio_de_producto - descuento
else:
    descuento = precio_de_producto * 0.10
    precio_final = precio_de_producto - descuento
print(f"El precio final es: {precio_final}")