```mermaid
graph TD
    A([Inicio]) --> B[Leer nacimiento, actual, consulta]
    B --> C[edad_actual = actual - nacimiento]
    C --> D[Mostrar edad actual]

    D --> E{¿consulta > actual?}
    
    E -- Sí --> F[Edad futura = consulta - nacimiento]
    F --> G[Mostrar edad futura]
    
    E -- No --> H{¿consulta == actual?}
    
    H -- Sí --> I[Mostrar edad actual]
    
    H -- No --> J{¿consulta >= nacimiento?}
    
    J -- Sí --> K[Edad pasada = consulta - nacimiento]
    K --> L[Mostrar edad pasada]
    
    J -- No --> M[Mostrar "No había nacido"]
    
    G --> N([Fin])
    I --> N
    L --> N
    M --> N
```