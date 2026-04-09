# La Central Hidroeléctrica (Lógica de Alerta)

## Escenario
Una represa necesita un sistema de alerta temprana para prevenir inundaciones.

## El Problema
El sistema monitorea:
- **Nivel de agua** (en metros)
- **Velocidad de llenado** (bajo, medio, alto)

## Reglas de Control de Compuertas

| Condición | Acción |
|-----------|--------|
| Nivel > 100m Y velocidad "alta" | Abrir Compuerta A |
| Nivel > 100m Y velocidad "media" | Abrir Compuerta B |
| Nivel > 120m (cualquier velocidad) | Abrir AMBAS compuertas + Alarma General |
| Cualquier otro caso | Compuertas cerradas |

## Notas Importantes
- Si el nivel es **> 120m**, la Alarma General se activa independientemente de la velocidad
- Las compuertas A y B son mutuamente excluyentes, EXCEPTO cuando se alcanza 120m

## Reto para el Estudiante
Manejar rangos numéricos y variables de texto (o estados numéricos) para controlar múltiples salidas.
