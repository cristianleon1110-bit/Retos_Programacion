# El Sistema de Descuentos "Cliente VIP"

## Escenario
Una tienda tecnológica quiere premiar la fidelidad, pero proteger sus ganancias.

## El Problema
Un cliente recibe un **20% de descuento** si su compra es mayor a **$500.000**. Pero, si el cliente es miembro **VIP**, el descuento sube al **30%** siempre que la compra supere los **$500.000**. Si la compra es menor a esa cifra, los miembros **VIP** solo reciben un **10%** y los clientes normales nada.

## Reglas de Descuento
- **Compra > $500.000**:
  - Cliente VIP: 30% de descuento
  - Cliente normal: 20% de descuento
- **Compra ≤ $500.000**:
  - Cliente VIP: 10% de descuento
  - Cliente normal: 0% de descuento

## Reto para el Estudiante
Estructurar los condicionales para calcular el precio final correcto según el tipo de cliente y el monto.
