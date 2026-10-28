# Texto de la tarjeta de seguimiento en Trello

Claude **no escribe en Trello**. Escribe en el chat el texto completo de la tarjeta, listo para copiar y pegar, con la estructura fija de las tarjetas de Kodea (título, metadatos, descripción y checklists), adaptada a una tarjeta de seguimiento de estándar. Modelo real: tarjeta plantilla `XQsGU4xy` ("Estándares de cumplimiento y traspaso · [Nombre Iniciativa] · [Nombre Aportante]"), tablero "Estándar Desarrollo de Iniciativas", columna "0. Base".

Todo sale de lo confirmado en los bloques. Nada se inventa. Nunca nombres de personas: solo roles y áreas.

## Estructura de la respuesta (en este orden, sin secciones extra)

**0. DÓNDE CREARLA**
- Tablero "Estándar Desarrollo de Iniciativas", columna de la etapa del estándar.
- Marcarla como plantilla de Trello (menú de la tarjeta → Convertir en plantilla), para que los equipos la copien en su Kanban en cada caso.

**1. TÍTULO DE LA TARJETA**
```
Estándar de <Nombre> · [Nombre Iniciativa] · [Nombre Aportante]
```
(Los corchetes son campos que se completan cada vez que se usa la plantilla.)

**2. METADATOS DE LA TARJETA**
- **Miembros:** ninguno en la plantilla. Se agregan al usarla en cada caso (la persona a cargo de cada checklist).
- **Vencimiento:** N/A en la plantilla.
- **Etiquetas:** las oficiales del tablero que correspondan, o ninguna.
- **Adjuntos:** el PDF de la ficha y, cuando exista, la presentación de sensibilización.

**3. DESCRIPCIÓN** (en un bloque de código, para copiar y pegar en la descripción)
```
**QUEREMOS**: <verbo en infinitivo + qué asegura el estándar, tomado del Propósito>.

**PARA:** <beneficio, tomado del Propósito y del criterio de éxito>.

**ESTARÁ LISTO CUANDO:**

- <criterio de éxito cumplido>
- Todos los checklists están completos o con sus desviaciones declaradas, y no hay ítems [OBLIGATORIO] sin cumplir.

**LEER ANTES DE USAR**

:point_right: A continuación encontrarás 3 títulos que te servirán de guía del proceso entero. Solo el primero requiere que agregues información.

#### **I. Información de apoyo:** [completar]

**<Dato que se completa en cada caso>:** [completar]
**<Fecha de inicio del plazo>:** [fecha]
**Fecha límite para <acción> (+<plazo>):** [fecha]
<una línea por cada plazo de las tolerancias de Tiempo; si no hay plazos, solo los datos de apoyo>

#### **II. ¿Cómo usar esta tarjeta?**

Cada área trabaja solo su(s) checklist(s) y, antes de salir, deja todo sincronizado con el Kanban de quien toma la posta. Este es el paso a paso:

1. <Responsable del Checklist 1> completa el Checklist 1 y <a quién entrega o avisa>.
2. <Responsable del Checklist 2> completa el Checklist 2 y <…>.
<una línea por checklist, en orden; la última dice quién cierra la tarjeta>

#### **III. Responsables y desviaciones**

La persona encargada de un checklist es responsable de que todos sus ítems se cumplan. Si quieres cambiar el orden interno de las acciones dentro de tu checklist, ¡adelante!

**Si algo no se cumple** (un ítem, un plazo o una tolerancia), es una desviación. El responsable del checklist la declara a tiempo, como comentario en esta tarjeta: qué no se hizo, qué se decidió en su lugar y por qué. Si es un plazo, menciona al Delivery Manager. Declarar una desviación no es reportar un error: es dejar escrita una decisión del equipo, y sirve para levantar información sobre cómo se usa realmente el estándar.

**Los ítems marcados [OBLIGATORIO] no admiten desviación.** <Variante del Bloque 4: "Si uno no se cumple, no se <avanza a lo que depende del estándar>." o "Si uno no se cumple, se escala al Delivery Manager y al equipo afectado, y continuar requiere la aprobación de ambos.">
```

**4. CHECKLISTS**
Uno por fase, en el mismo orden y con las mismas palabras que el paso a paso de la ficha. Para cada checklist:
- El nombre va **fuera** del bloque de código: `Checklist N — Fase X · <Responsable> (<qué se hace>)`.
- Los ítems van **dentro de un bloque de código de texto plano, un ítem por línea**, sin viñetas, sin numeración y sin casillas `[ ]`. Así, al pegarlos en "Añadir elemento" del checklist, Trello crea un ítem por línea.

Ejemplo de formato:

Checklist 1 — Fase 1 · Sostenibilidad (Creación)
```
Crear el cuaderno en NotebookLM
Compartir el cuaderno con Cumplimiento y Operaciones
Registrar en esta tarjeta la fecha de cumplimiento de esta fase
```

**Por probar:** si Trello separa bien los ítems que empiezan con `[OBLIGATORIO]`. Si no, se avisa a la persona que esos ítems se agregan uno por uno.

## Comprobación antes de entregar

- Los checklists dicen exactamente lo mismo que el paso a paso de la ficha.
- No aparece ningún nombre de persona.
- Cada plazo de las tolerancias tiene su línea en "I. Información de apoyo".
