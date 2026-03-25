# MICROBIT - Ejercicios de Programación

Colección de ejercicios y proyectos personales de programación para BBC Micro:bit, desde basico a más avanzado.

## Descripción

Micro:bit es una placa microcontroladora educativa con múltiples sensores integrados. Este repositorio contiene una serie de ejercicios que exploran sus capacidades:
- Pantalla LED 5x5
- 2 botones programables
- Sensores: acelerómetro, brújula, termómetro
- Comunicación inalámbrica
- Conexión I2C con periféricos

## Contenido

### 🎮 Juegos Avanzados
- **Juego.py** - Juego de relleno de pantalla con acelerómetro
  * Control del cursor mediante inclinación del Microbit
  * Objetivo: Iluminar los 25 píxeles LED de la pantalla
  * Sistema de 10 niveles con dificultad creciente
  * Sensibilidad que aumenta con cada nivel completado
  * Mecánica: El cursor deja rastro que debes completar

- **Juego V2.py** - Versión avanzada con dos fases dinámicas
  * **Fase 1 (Primeros niveles)**: Rellena pantalla con rastro continuo
  * **Fase 2 (Niveles finales)**: Cambia la lógica, solo cuenta píxeles específicos (intensidad 7)
  * Animación de reloj de carga entre niveles
  * Más desafiante: La dificultad y las reglas evolucionan
  * Incluye bugs documentados como feature learning

### 🔵 Básico
- **Basic_A-boton.terminate-reset.py** - Control de botones
- **Basic_A-Smiley.py** - Animación de caras en display LED
- **Basic_mb_smiley.py** - Caras con interacción
- **Basic_A-datagraphvalues.py** - Gráficos de datos

### 🧭 Sensores
- **Brujula.py** - Lectura de brújula con números
- **Brujula con Numeros.py** - Brújula con display numérico
- **Brujula con Letras.py** - Brújula con indicaciones de dirección (N, S, E, O)
- **Cuenta Pasos.py** - Acelerómetro para contar pasos

### 📡 Comunicación
- **Morse Sender.py** - Envío de mensajes en código Morse
- **Morse Receiver.py** - Recepción de mensajes en código Morse

### 📊 Multimedia
- **Basic_mb_media.py** - Acceso a reproducción de sonidos

## Requisitos

- Micro:bit
- Mu Editor o similar
- Cable USB para conectar Micro:bit a la computadora
- Python 3.x (en la computadora para desarrollo)

## Uso

1. Descarga el archivo Python correspondiente
2. Abre Mu Editor y conecta tu Micro:bit
3. Abre el archivo en Mu Editor
4. Haz clic en "Flash" para cargar el programa en la placa
5. Observa el comportamiento en el display LED u otro componente

## 🎮 Juegos - Guía Rápida

### Juego.py - "Rellena la Pantalla"

**Objetivo**: Iluminar todos los píxeles de la pantalla LED (5x5)

**Cómo Jugar**:
1. Inclina el Microbit para mover el cursor (píxel más brillante)
2. El cursor deja rastro mientras se mueve
3. Llena todos los 25 píxeles para completar el nivel
4. **Dificultad**: 10 niveles, cada uno más rápido que el anterior
5. **Controles**: Más sensibles en niveles avanzados

**Mecánica Técnica**:
- Usa acelerómetro para entrada
- Posición del cursor se reduce en sensibilidad según nivel
- Track de píxeles iluminados en tiempo real
- Detecta cuando llegas a 25/25 píxeles

### Juego V2.py - "Rellena la Pantalla Avanzado"

**Objetivo**: Ídem, pero con reglas que cambian según progresa el juego

**Dos Fases**:

1. **Fase 1 (niveles 1-5, FIN > 25)**:
   - Rellena con el rastro del cursor (intensidad 7)
   - El movimiento deja píxeles en la pantalla
   - Objetivo: Llenar los 25 píxeles

2. **Fase 2 (niveles 6-10, FIN ≤ 25)**:
   - **Las reglas cambian**: Solo cuentan píxeles de intensidad exacta 7
   - Mucho más difícil porque algunos píxeles no cuentan
   - Progreso borrado parcialmente al cambiar de fase
   - Requiere estrategia diferente

**Características Avanzadas**:
- Animaciones de reloj de carga entre niveles
- Feedback visual de progreso
- Transición dinámica de dificultad
- Bugs conocidos documentados en el código

**Bugs Conocidos** (documentados en el código):
- Salta niveles sin jugar en ciertos casos
- Reloj de carga antes de victoria
- Números adicionales en mensajes



## Notas

- Los programas utilizan MicroPython, un subconjunto de Python optimizado para microcontroladores
- Algunos programas requieren componentes adicionales como el brújula
- Los programas comienzan a ejecutarse automáticamente al encender la placa

## Conceptos Educativos Avanzados

### Juegos - Importancia Pedagógica

Los juegos incluidos no son simples: implementan conceptos avanzados de programación:

- **Entrada en Tiempo Real**: Lectura continua del acelerómetro
- **Gestión de Estado**: Rastreo de múltiples variables (posición, píxeles, nivel)
- **Algoritmos Adaptativos**: Cambio dinámico de dificultad y reglas
- **Detección de Condiciones**: Conteo y evaluación de píxeles
- **Programación Orientada a Eventos**: Respuesta a movimiento y condiciones
- **Optimización**: Límites de memoria del Microbit requieren código eficiente
- **Depuración**: Bugs documentados para aprender a identificar y documentar problemas
- **Game Design**: Balanceo de dificultad, transiciones de fases, feedback al usuario

## Autor

Proyecto educativo de introducción a microcontroladores
