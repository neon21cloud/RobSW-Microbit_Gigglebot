# Fase 3 - Trabajo en Equipo (Arquitectura Jefe-Esclavo)

## Descripción

Sistema avanzado de coordinación con dos GiggleBots: un Jefe que busca balizas y distribuye tareas, y un Esclavo que ejecuta las órdenes recibidas. Implementa comunicación robusta entre robots.

## Archivos Incluidos

- **FASE3-1-CocheJefe.py** - Programa del coche Jefe (Parte 1: Búsqueda)
- **FASE3-1-CocheEsclavo.py** - Programa del coche Esclavo (Parte 1: Ejecución)
- **FASE3-2-MetayArbitro_AmbosCoches.py** - Programa para ambos coches (Parte 2: Entrega)
- **referee.py** - Programa del árbitro (mismo de Fase 2)
- **equipo.txt** - Archivo de configuración de equipo

## Arquitectura del Sistema

### Roles

**Jefe (FASE3-1-CocheJefe.py)**:
- Busca nuevas balizas en el entorno
- Asigna IDs de baliza al esclavo
- Recibe confirmación de secretos
- Espera mientras el esclavo trabaja

**Esclavo (FASE3-1-CocheEsclavo.py)**:
- Recibe ID de baliza asignado por el jefe
- Busca y recoge el secreto de esa baliza
- Comunica el secreto al jefe
- Espera nuevas órdenes

### Organización en Partes

**Parte 1: Comunicación sin Movimiento**
- Los coches comunican y coordinan búsqueda
- No implementan movimiento por limitaciones de memoria
- Código estructurado para permitir movimiento futuro
- Displays muestran toda la comunicación

**Parte 2: Movimiento y Entrega**
- Ambos coches se mueven a la meta
- Entregan sus secretos al árbitro
- Reciben confirmación

## Protocolo de Comunicación - Parte 1

### Ejemplo de Ejecución (Displays)

```
Jefe: IDesc: 144
      (Asigna baliza 144 al esclavo)

Esclavo: ESC: 144
         (Confirma recepción)

Esclavo (tras conseguir secreto):
         SEC:elSecreto
         (Envía "Ready?" al jefe)

Jefe: ID?
      Cara Confusa
      (Buscando nuevos IDs)
```

## Requisitos

- **Mínimo**: 2 GiggleBots + 5 Microbits
- **Recomendado**: 2 GiggleBots + 5 Microbits (1 árbitro)
- Mu Editor con opción "reducir código" habilitada
- Pilas completamente cargadas
- Balizas suficientemente cerca para comunicación

## Limitaciones Conocidas

⚠️ **Memoria - Parte 1**:
- No incluye movimiento por falta de memoria
- Solo comunicación y coordinación
- Código preparado para futuro movimiento
- Balizas y coches deben estar cerca para comunicar

⚠️ **Memoria - Parte 2**:
- Similar a Fase 2 pero sin problemas de coordinación
- Formato de mensaje ligeramente diferente

⚠️ **Errores Esperados**:
- OSError I2C al cargar (se resuelve en GiggleBot)
- Requiere pilas en buen estado

## Uso

### Parte 1: Búsqueda y Coordinación

1. Carga FASE3-1-CocheJefe.py en GiggleBot 1
2. Carga FASE3-1-CocheEsclavo.py en GiggleBot 2
3. Enciende ambos GiggleBots
4. Observa displays para entender la coordinación
5. Modifica según necesidades específicas

### Parte 2: Entrega a Meta

1. Carga FASE3-2-MetayArbitro_AmbosCoches.py en ambos GiggleBots
2. Carga referee.py en Microbit separado
3. Enciende ambos GiggleBots
4. Navegan a la meta
5. Entregan datos al árbitro

## Notas Técnicas

- El primer ID de baliza siempre se intenta asignar al esclavo
- La comunicación Jefe-Esclavo usa protocolo estandarizado
- El árbitro recibe datos de ambos coches
- Reutiliza código del movimiento de Fase 2

## Validación

✅ Probado hasta 3 balizas simultáneamente
✅ Probado con 2 GiggleBots y 5 Microbits
✅ Sistema Jefe-Esclavo funcionando correctamente

## Arquitectura Escalable

Aunque actualmente solo soporta 2 coches, el código está estructurado para permitir:
- Crecimiento a múltiples esclavos
- Mejor distribución de carga computacional
- Sistema de coordinación centralizado
