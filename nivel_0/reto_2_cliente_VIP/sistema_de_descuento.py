# Entrada de datos
monto = float(input("Ingrese el monto de la compra: "))
tipo_cliente = input("Ingrese el tipo de cliente (VIP/Normal): ").strip().lower()

# Proceso
if monto > 500000:
    if tipo_cliente == "vip":
        descuento = 0.30
    else:
        descuento = 0.20
else:
    if tipo_cliente == "vip":
        descuento = 0.10
    else:
        descuento = 0.0

# Cálculo del precio final
precio_final = monto - (monto * descuento)

# Salida
print("Descuento aplicado:", descuento * 100, "%")
print("Precio final a pagar: $", precio_final)