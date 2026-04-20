```mermaid
graph TD
    A([INICIO]) --> B[Leer precio, pago]

    B --> C[Calcular cambio = pago - precio]

    C --> D{¿cambio == 0?}

    D -- Sí --> E[Mostrar "No hay cambio"]
    E --> Z([FIN])

    D -- No --> F[Mostrar "Cambio total"]

    F --> G[Definir denominaciones<br/>[500,200,100,50,20,10,5,1]]

    G --> H[Inicializar i = 0]

    H --> I{¿i < tamaño lista?}

    I -- No --> Z

    I -- Sí --> J[denominación = lista[i]]

    J --> K{¿cambio >= denominación?}

    K -- Sí --> L[cantidad = cambio // denominación]
    L --> M[cambio = cambio % denominación]
    M --> N[Mostrar cantidad]
    N --> O[i = i + 1]
    O --> I

    K -- No --> P[i = i + 1]
    P --> I
```