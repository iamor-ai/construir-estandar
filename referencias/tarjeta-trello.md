# Texto de la tarjeta de seguimiento en Trello

Claude **no escribe en Trello**. Escribe en el chat el texto completo de la tarjeta, para copiar y pegar. La persona lo valida antes de crearla.

Todo sale de lo confirmado en los bloques. Nada se inventa. Nunca nombres de personas: solo roles y áreas.

## Estructura de la respuesta (en este orden, sin secciones extra)

**0. DÓNDE CREARLA**
- Tablero "Estándar Desarrollo de Iniciativas" (https://trello.com/b/x6mpA3C3), en la columna de la etapa en que ocurre el estándar.
- Una vez creada, debe quedar en ese tablero como plantilla, en el Kanban desde el que se inicia el proceso. La persona lo hace a mano en Trello.

**1. TÍTULO DE LA TARJETA**
```
Estándar de <Nombre> · [Nombre de la iniciativa] · [Aportante o edición]
```
Los corchetes se completan cada vez que se usa la plantilla.

**2. METADATOS DE LA TARJETA**
- **Miembros:** ninguno en la plantilla. Se agregan al usarla en cada caso (la persona a cargo de cada checklist).
- **Vencimiento:** la fecha límite de este caso, que siempre se pone.
- **Etiquetas:** las oficiales del tablero que correspondan, o ninguna.
- **Adjuntos:** las herramientas del estándar, cada una con su link. La persona las sube a mano. La ficha final y la presentación van en la tarjeta de introducción, no aquí.

**3. DESCRIPCIÓN** (en un bloque de código, para copiar y pegar en la descripción)
```
**PRIORIDAD:** <Fecha fija o Estándar, la que la persona elige para este caso>
**FECHA LÍMITE:** [fecha]

**QUEREMOS**: <verbo en infinitivo + qué asegura el estándar, tomado del Propósito>.

**PARA:** <beneficio, tomado del Propósito y del criterio de éxito>.

**ESTARÁ LISTO CUANDO:**

- <criterio comprobable, tomado del criterio de éxito>
- <criterio comprobable>
- Todos los checklists están completos o con sus desviaciones declaradas, y no hay ítems [OBLIGATORIO] sin cumplir.

**LEER ANTES DE USAR**

La base de este estándar es la autonomía del equipo para completarlo con flexibilidad. Si decides no hacer un paso, o hacerlo de otra manera, anótalo en la sección de Desviaciones de esta tarjeta: qué no se hizo, qué se decidió en su lugar y por qué. Esto vale para cada paso, excepto los marcados como [OBLIGATORIO].

**Desviaciones.** Declarar una desviación no es reportar un error: es dejar escrita una decisión del equipo, y sirve para levantar información sobre cómo se usa realmente el estándar. Si es un plazo, menciona al Delivery Manager.

**Solicitud de mejora.** Si algo en este estándar no funcionó, anótalo en esta tarjeta como "Solicitud de mejora", con lo que te parece que sería una mejora. Va junto a las desviaciones; no es un paso más.

**Los ítems marcados [OBLIGATORIO] no admiten desviación.** <Variante del Bloque 4: "Si uno no se cumple, no se <avanza a lo que depende del estándar>." o "Si uno no se cumple, se escala al Delivery Manager y al equipo afectado, y continuar requiere la aprobación de ambos.">
```

**4. CHECKLISTS**
Uno por fase, en el mismo orden y con las mismas palabras que el paso a paso de la ficha. El nombre de cada checklist lleva el número de la fase, su título y el área responsable:
`Checklist N — Fase N · <Título de la fase> · Responsable: <área>`

- El nombre va **fuera** del bloque de código.
- Los ítems van **dentro de un bloque de código de texto plano, un ítem por línea**, sin viñetas, sin numeración y sin casillas `[ ]`. Así, al pegarlos en "Añadir elemento" del checklist, Trello crea un ítem por línea.

Ejemplo de formato:

Checklist 1 — Fase 0 · Asignación del LIA · Responsable: Sostenibilidad
```
Acordar el LIA con la Directora de Educación
Crear el accionable en Trello y agregar al LIA como miembro
```

**Por probar:** si Trello separa bien los ítems que empiezan con `[OBLIGATORIO]`. Si no, se avisa a la persona que esos ítems se agregan uno por uno.

## Comprobación antes de entregar

- El título, la prioridad, la fecha límite, la descripción y los checklists están completos.
- Los checklists dicen exactamente lo mismo que el paso a paso de la ficha.
- Cada checklist lleva número de fase, título de la fase y área responsable.
- No aparece ningún nombre de persona.
