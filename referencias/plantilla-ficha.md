# Plantilla de la Ficha Ejecutable

Claude copia esta plantilla al armar la ficha (etapa 3) y la completa solo con lo confirmado en los bloques. Lo que quedó sin respuesta va como `(pendiente)`. Las líneas entre `<…>` se reemplazan; los textos sin `<…>` son fijos y no se cambian.

Origen de cada sección:

| Sección | Sale de |
|---|---|
| Propósito y lineamientos | Bloque 1 |
| Dónde aplica y quién participa | Inicio (etapa), Bloque 3 (alcance), Bloque 2 (responsables), Bloque 4 (participantes en los ítems) |
| Herramientas | Bloque 2 |
| Hitos | Bloque 2 (tabla de fases: actores, duración, cadencia, entrega, resultado) |
| Paso a paso | Bloque 4 (con fases y plazos del Bloque 2, y calidad y riesgo del Bloque 3) |
| Criterio de éxito | Bloque 4 |
| Tolerancias | Bloque 3 |
| Desviaciones | Texto fijo + respuesta del Bloque 4 sobre qué depende del estándar |
| Ciclo de vida | Inicio + Bloque 4 |
| Retroalimentación | Texto fijo + responsables del Bloque 2 |

---

```
═══════════════════════════════════════════════════════════════════════════════
FICHA EJECUTABLE: ESTÁNDAR DE <NOMBRE>
VERSIÓN: 1.0 (Presentada para validación)
FECHA CREACIÓN: <fecha>
═══════════════════════════════════════════════════════════════════════════════

PROPÓSITO

<Qué asegura este estándar y qué problema resuelve, en 1 o 2 frases.>

Responde a los lineamientos del Modelo de Excelencia Operativa de Kodea:

| Lineamiento | Cómo lo operacionaliza este estándar |
|---|---|
| 1. Propósito y estrategia | <cómo, o "No aplica: <razón>"> |
| 2. Cumplir en tiempo y forma lo comprometido | <…> |
| 3. Declarar a tiempo las desviaciones y/o riesgos | <…> |
| 4. Usar bien el tiempo y los recursos del equipo | <…> |
| 5. Decidir con datos compartidos y accesibles | <…> |
| 6. Aprender y llevar lo aprendido al siguiente ciclo | <…> |

═══════════════════════════════════════════════════════════════════════════════
DÓNDE APLICA Y QUIÉN PARTICIPA
═══════════════════════════════════════════════════════════════════════════════

DÓNDE APLICA
• Etapa del ciclo de vida: <etapa>
• Se aplica a: <a qué, y sus excepciones si las hay>

QUIÉN PARTICIPA
• <Rol o área> — responsable del Checklist <N>
• <Rol o área> — participa en <qué>
• ...

<Solo si algún responsable es un área:> Cuando se use la tarjeta en cada 
caso, cada ítem se asigna en Trello a la persona del área que esté a cargo.

═══════════════════════════════════════════════════════════════════════════════
HERRAMIENTAS
═══════════════════════════════════════════════════════════════════════════════

• Trello (obligatoria) — tarjeta de seguimiento del estándar: un checklist 
  por fase, las fechas de cumplimiento y las desviaciones declaradas
• <Herramienta> (obligatoria/opcional) — <para qué>

═══════════════════════════════════════════════════════════════════════════════
HITOS
═══════════════════════════════════════════════════════════════════════════════

El cumplimiento de cada hito queda registrado con fecha en la tarjeta de 
Trello.

Hito 1: <nombre> (Fase 1)
├─ Actores: <roles o áreas>
├─ Duración: <plazo, o "sin plazo fijo hasta contar con línea base">
├─ Cadencia: <una vez / continua / periódica>
├─ Entrega: <sincrónica o asincrónica, por qué medio>
└─ Resultado: <qué queda al terminar>

═══════════════════════════════════════════════════════════════════════════════
PASO A PASO (LISTA DE CUMPLIMIENTO)
═══════════════════════════════════════════════════════════════════════════════

El paso a paso son los checklists de la tarjeta de Trello de seguimiento. 
Cada checklist corresponde a una fase y tiene un solo responsable, que es 
quien deja escritas las desviaciones. Los ítems marcados [OBLIGATORIO] no 
admiten desviación.

CHECKLIST 1 — Fase 1 · <qué se hace> · Responsable: <rol o área>
<Plazo: <cuánto, entre qué momentos> — solo si la fase tiene plazo>
☐ <ítem que se puede verificar, empezando con un verbo>
☐ [OBLIGATORIO] <ítem que no admite desviación>
☐ Registrar en la tarjeta la fecha de cumplimiento de esta fase

CHECKLIST <N> — Fase <N> · <qué se hace> · Responsable: <rol o área>
☐ <ítem>
☐ Registrar en la tarjeta la fecha de cumplimiento de esta fase
☐ Criterio de éxito cumplido
☐ Registrar el resultado en la tarjeta y cerrar el estándar

═══════════════════════════════════════════════════════════════════════════════
CRITERIO DE ÉXITO
═══════════════════════════════════════════════════════════════════════════════

<Qué logra el estándar, tomado del Propósito>. Se cumple cuando:

☑ <condición observable>

Se verifica con: <dato que ya existe, por ejemplo una encuesta, las fechas 
en Trello o un documento>. Se revisa en cada caso, en el último checklist.

═══════════════════════════════════════════════════════════════════════════════
TOLERANCIAS PRINCE2
═══════════════════════════════════════════════════════════════════════════════

TIEMPO      <plazos fijados, o "sin plazo fijo hasta contar con línea base">. 
            La línea base se construye con las fechas registradas en Trello 
            y se revisa cada 3 meses.
COSTO       Tiempo del equipo, medido como duración por fase, sin margen fijo 
            hasta contar con línea base. <Si hay otro costo: "<costo>: no 
            superar lo presupuestado para ese costo, en el presupuesto que 
            corresponda" / sin presupuesto: se describe.>
CALIDAD     Cada checklist se completa o sus desviaciones quedan declaradas.
            <Condiciones de calidad propias, si las hay: van como ítems del 
            paso a paso.>
ALCANCE     <a qué se aplica; excepciones, si las hay>
BENEFICIOS  El criterio de éxito, y la eficiencia: duración de cada fase 
            comparada con la línea base. <Si un área entrega información a 
            otra: qué tiene que recibir, y con qué dato se ve.>
RIESGO      <lo que no puede fallar nunca, y su ítem [OBLIGATORIO]; o "No hay 
            ítems de cero tolerancia">

═══════════════════════════════════════════════════════════════════════════════
DESVIACIONES
═══════════════════════════════════════════════════════════════════════════════

Qué es una desviación: un ítem de la lista que no se cumple, una 
tolerancia que se supera o un plazo que no se cumple. También cuentan las 
que no dependen del equipo, cuando el equipo las reconoce.

Toda desviación se declara, sin excepción. Declararla no es reportar un 
error: es dejar escrita una decisión del equipo responsable. Sirve para 
dar flexibilidad al equipo y para levantar información sobre cómo se usa 
realmente el estándar (qué pasos sobran o faltan).

Quién la declara: el responsable del checklist donde ocurre.
Cuándo: a tiempo, en cuanto se decide no cumplir o se sabe que no se va a 
cumplir. No después.
Qué se escribe: qué no se hizo, qué se decidió en su lugar y por qué.
Dónde: en la tarjeta de Trello de seguimiento de este estándar.

SI FALLA UN ÍTEM [OBLIGATORIO]
<Usar una sola variante:>
[Si algo depende de este estándar] Este estándar es condición para 
<qué>: no se avanza a <qué> mientras haya un ítem [OBLIGATORIO] sin 
cumplir.
[Si nada depende de este estándar] Se escala al Delivery Manager (DM) y 
al equipo afectado porque el ítem no se completó, y continuar requiere la 
aprobación de ambos.

═══════════════════════════════════════════════════════════════════════════════
CICLO DE VIDA: DÓNDE SE APLICA
═══════════════════════════════════════════════════════════════════════════════

<etapa o estándar anterior> → [ESTÁNDAR DE <NOMBRE>] → <lo que depende de 
este estándar, o la etapa siguiente>

═══════════════════════════════════════════════════════════════════════════════
RETROALIMENTACIÓN Y MEJORA CONTINUA
═══════════════════════════════════════════════════════════════════════════════

Todos los estándares contemplan un mecanismo simple de retroalimentación y 
mejora continua.

Cualquier persona que use el estándar puede reportar si algo no funcionó 
bien, generó fricción o quedó ambiguo, para que el estándar se ajuste con 
el uso real y no quede fijo desde su primera versión.

Cómo se hace:
Ir al tablero "Estándar Desarrollo de Iniciativas" y dejar el reporte o 
mejora en "Comentarios y actividad" de este estándar, etiquetando a 
<responsables de los checklists>. No requiere un formulario ni una 
instancia formal aparte.

El estándar se revisa formalmente cada 3 meses, o antes si se acumulan 3 
o más comentarios similares sobre el mismo punto — lo que ocurra primero. 
La revisión toma esos comentarios acumulados y decide si el estándar 
necesita una nueva versión.

═══════════════════════════════════════════════════════════════════════════════
```
