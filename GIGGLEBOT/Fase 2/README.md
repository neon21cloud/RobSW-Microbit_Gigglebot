# Fase 2 - Búsqueda de Balizas y Secretos

## Descripción

Sistema avanzado de localización donde el GiggleBot detecta balizas, recoge sus secretos y los entrega a un árbitro. Implementa algoritmos de búsqueda basados en la potencia de señal recibida.

## Archivos Incluidos

- **FASE2-1-LeeBalizasySecretos.py** - Búsqueda de balizas y recogida de secretos
- **FASE2-2-MetayArbitro.py** - Navegación a la meta y entrega de datos
- **referee.py** - Programa del árbitro (capacidad de recepción aumentada a length=128)

## Arquitectura

### Programa 1: Búsqueda y Recogida (FASE2-1-LeeBalizasySecretos.py)

**Funcionalidad**:
- Busca una o varias balizas en el entorno
- Calcula la media de potencias recibidas
- Se mueve hacia puntos de mayor potencia
- Recoge los secretos de cada baliza
- Almacena ID y secreto en una matriz

**Algorithm**:
- No es distancia física sino potencia de señal
- Estaciona para calcular media de potencias
- Decisiones de movimiento basadas en potencia
- Comportamiento puede parecer errático pero es óptimo

**Display**:
- Muestra ID de baliza detectada
- Diamante mientras calcula media
- Potencia media calculada
- Secreto cuando comunica con baliza
- Lista final de IDs y secretos (máx. 5)

### Programa 2: Meta y Árbitro (FASE2-2-MetayArbitro.py)

**Funcionalidad**:
- El GiggleBot navega hacia la meta
- Comunica con el árbitro
- Envía matriz completa de secretos
- Recibe confirmación del árbitro

**Display**:
- 'M' mientras se mueve
- Cara feliz al llegar a la meta
- Mensaje de confirmación del árbitro

### Árbitro (referee.py)

**Funcionalidad**:
- Recibe datos de los GiggleBots
- Valida la información
- Envía confirmación

**Importante**: 
- Tiene capacidad de recepción ampliada (length=128)
- Sin esta ampliación no recibe el mensaje completo

## Requisitos

- 1-4 GiggleBots con Microbit
- Balizas configuradas
- Microbit con programa del árbitro
- Mu Editor con opción "reducir código" habilitada
- Pilas completamente cargadas

## Limitaciones Conocidas

⚠️ **Memoria**:
- Programas optimizados al máximo
- Necesario activar "reducir código" en Mu Editor
- Máximo 5 balizas almacenables

⚠️ **Errores Esperados**:
- OSError I2C al cargar (se resuelve en GiggleBot)
- Requiere pilas en buen estado

## Uso

1. Carga FASE2-1-LeeBalizasySecretos.py en GiggleBot 1 (o más)
2. Carga FASE2-2-MetayArbitro.py en el mismo GiggleBot (después o en otro)
3. Carga referee.py en un Microbit separado
4. Ejecuta FASE2-1 para buscar y recoger secretos
5. Ejecuta FASE2-2 para entregar datos al árbitro

## Valida

✅ Probado hasta 4 balizas simultáneamente
✅ Probado con 2 GiggleBots y 5 Microbits

## Rango Obligatorio y Opcional

Los programas de Fase 2 cumplen tanto la parte obligatoria como la opcional de la entrega de la convocatoria extraordinaria.
