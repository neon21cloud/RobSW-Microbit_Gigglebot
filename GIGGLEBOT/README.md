# GIGGLEBOT - Proyecto de Robótica Educativa

Proyecto educativo de robótica con el robot GiggleBot, dividido en tres fases progresivas de complejidad creciente.

## Descripción General

El proyecto GiggleBot implementa un robot educativo capaz de navegar, detectar balizas y comunicarse con otros robots. El sistema está limitado por la memoria del Microbit, lo que requiere optimizaciones específicas.

## Fases del Proyecto

### 🏁 Fase 1 - Ejercicios Fundamentales
**Archivos**: `gigg_EJ1.py` a `gigg_EJ6.py`

Siete ejercicios progresivos que cubren:
- Movimiento básico del GiggleBot
- Control de motores
- Sensores
- Interacción con el entorno
- Programación modulada

### 🎯 Fase 2 - Búsqueda de Balizas y Secretos
**Archivos**: `FASE2-1-LeeBalizasySecretos.py`, `FASE2-2-MetayArbitro.py`, `referee.py`

El GiggleBot localiza una o varias balizas, recoge sus secretos y los entrega a un árbitro.

**Estructura**:
- **Programa 1**: Busca balizas, calcula media de potencias, recoge secretos
- **Programa 2**: Navega a la meta, envía datos al árbitro
- **Arbitro**: Recibe y valida la información

**Características**:
- Búsqueda inteligente basada en potencia de señal
- Almacenamiento en matrices
- Comunicación con árbitro
- Display con estado y información

### 👥 Fase 3 - Trabajo en Equipo (Arquitectura Jefe-Esclavo)
**Archivos**: `FASE3-1-CocheJefe.py`, `FASE3-1-CocheEsclavo.py`, `FASE3-2-MetayArbitro_AmbosCoches.py`, `referee.py`

Sistema de dos GiggleBots coordinados:
- **Jefe**: Busca nuevas balizas, distribuye tareas
- **Esclavo**: Recibe órdenes, ejecuta búsquedas asignadas

**Estructura**:
- **Parte 1**: Comunicación y coordinación (limitada por memoria)
- **Parte 2**: Movimiento a meta y entrega de datos

## Requisitos

- 2 GiggleBots (para Fase 1-2) o 2 GiggleBots + 2 Microbits (para Fase 3)
- Múltiples Microbits según la fase
- Mu Editor con opción "reducir código" habilitada
- Pilas completamente cargadas en los GiggleBots

## Notas Importantes

⚠️ **Limitaciones de Memoria**:
- Los programas están optimizados para máxima compresión
- Es necesario activar "reducir código" en Mu Editor
- Algunas funciones se omiten en Fase 3 por limitaciones de memoria

⚠️ **Errores Esperados**:
- OSError I2C al cargar en Microbit (se resuelve cuando se instala en el GiggleBot)
- Requiere pilas en buen estado para funcionamiento correcto

🎯 **Algoritmo de Búsqueda**:
- No es distancia física sino potencia de señal
- Calcula media de potencias para decisiones de movimiento
- Comportamiento puede parecer errático pero es óptimo para búsqueda

## Uso

1. Carga el programa correspondiente a cada fase en el Microbit
2. Instala el Microbit en el GiggleBot
3. Ejecuta según las instrucciones de la fase específica
4. Consulta los archivos de aclaraciones para detalles adicionales

## Autor

Proyecto educativo de programación avanzada en robótica
