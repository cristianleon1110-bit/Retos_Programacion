def controlar_compuertas(nivel_agua, velocidad_llenado):
    
    # Estado inicial
    if nivel_agua == 0 and velocidad_llenado == "baja":
        print("Estado inicial: sistema en reposo")

    # Primera condición
    if nivel_agua > 100 and velocidad_llenado == "alta":
        return "Abrir compuerta A"

    # Segunda condición
    elif nivel_agua > 100 and velocidad_llenado == "media":
        return "Abrir compuerta B"

    # Tercera condición (caso crítico)
    elif nivel_agua > 120:
        return "Abrir varias compuertas y activar alarma general"

    # Caso por defecto
    else:
        return "Compuertas cerradas"


# 🔍 Ejemplos de uso
print(controlar_compuertas(110, "alta"))   # compuerta A
print(controlar_compuertas(110, "media"))  # compuerta B
print(controlar_compuertas(130, "baja"))   # alarma
print(controlar_compuertas(80, "baja"))    # cerradas