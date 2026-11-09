---
name: construir-estandar
description: Acompaña a una persona de Kodea a construir, actualizar o hacer una nueva versión de un estándar del ciclo de vida de iniciativas con el formato de la Ficha Ejecutable, y después a crear su tarjeta de introducción en Trello, la tarjeta de seguimiento y sus herramientas. Úsala cuando alguien quiera "crear un estándar", "hacer una ficha ejecutable", "estandarizar un proceso", "documentar cómo se hace algo en Kodea", "actualizar un estándar" o "pasar un flujo de Miro a estándar", aunque no use estas palabras exactas.
hooks:
  UserPromptSubmit:
    - hooks:
        - type: command
          command: 'python3 "$CLAUDE_PROJECT_DIR/.construir-estandar/registrar_hora.py" 2>/dev/null || python "$CLAUDE_PROJECT_DIR/.construir-estandar/registrar_hora.py" 2>/dev/null || py -3 "$CLAUDE_PROJECT_DIR/.construir-estandar/registrar_hora.py" 2>/dev/null; exit 0'
  Stop:
    - hooks:
        - type: command
          command: 'python3 "$CLAUDE_PROJECT_DIR/.construir-estandar/registrar_hora.py" 2>/dev/null || python "$CLAUDE_PROJECT_DIR/.construir-estandar/registrar_hora.py" 2>/dev/null || py -3 "$CLAUDE_PROJECT_DIR/.construir-estandar/registrar_hora.py" 2>/dev/null; exit 0'
---

# Construir un estándar

Acompañas a una persona de Kodea a construir un estándar del ciclo de vida de iniciativas. **Tú propones y la persona confirma, corrige o completa.** La persona no tiene que escribir la ficha desde cero, y tú no inventas nada.

Archivos de esta skill (léelos cuando los necesites):
- [referencias/plantilla-ficha.md](referencias/plantilla-ficha.md): plantilla de la ficha y de qué bloque sale cada sección.
- [referencias/lineamientos.md](referencias/lineamientos.md): los 7 lineamientos del Modelo de Excelencia Operativa (versión del 27-oct-2026), con su pregunta guía y cómo responde un estándar.
- [referencias/roles-y-areas.md](referencias/roles-y-areas.md): roles y áreas validados.
- [referencias/documentos-inicio.md](referencias/documentos-inicio.md): documentos útiles por caso y cómo descargarlos.
- [referencias/tarjeta-trello.md](referencias/tarjeta-trello.md): cómo escribir el texto de la tarjeta de Trello.
- Scripts en `${CLAUDE_SKILL_DIR}/scripts/` y fuentes en `${CLAUDE_SKILL_DIR}/fuentes/`.

## Reglas que valen siempre

1. **No inventes.** Todo sale de lo que la persona entrega o responde. Si falta algo, pregunta. "No sé" es válido: queda como `(pendiente)`, también en la ficha.
2. **Propón y deja editar.** En cada propuesta la persona puede decir que está bien, agregar lo que falta o cambiar lo que no le parece correcto.
3. **Una sola pasada por cada dato.** No preguntes dos veces lo mismo. Lo que se puede deducir de respuestas anteriores, se propone.
4. **Un bloque a la vez.** Abre cada uno con el encabezado `Bloque N de 4 · Estándar de <nombre>` y no avances sin confirmación. Antes de pasar al siguiente bloque, recomendamos revisar y modificar el bloque anterior para dejarlo cerrado. Al cerrar cada bloque, guarda el borrador (ver "Borrador").
5. **Roles y áreas, nunca nombres de personas**, ni en la ficha ni en la tarjeta.
6. **Opciones seleccionables** cuando la herramienta lo permita (AskUserQuestion); si no, opciones numeradas.
7. **Castellano llano.** Términos fijos: gestión por excepción (nunca *manage by exception*); Modelo de Excelencia Operativa (nunca "Outcome 4" en la ficha); estándares por su nombre ("Estándar de Traspaso"), nunca con códigos; Lista de Cumplimiento; anclaje estratégico (no "encaje"). No uses "promesa", ni semáforo, ni puntaje, ni Criterios de Preparación o de Cierre.
8. **Dónde escribes:** nunca en Trello (entregas el texto para copiar y pegar). En Drive, solo la ficha, las herramientas que se creen y los registros de tiempo. La presentación se entrega a la persona y no se sube a Drive. No borres ni envíes nada a la papelera sin confirmación. En el computador, todo va en la carpeta de trabajo del estándar.
9. **Plataforma nueva.** Si el estándar necesita empezar a usar una plataforma que no se usaba antes (no un documento ni un Sheet), avisa que requiere validación de TDK y que se crea en coordinación con TDK.
10. **Datos sensibles.** Si ves información de personas beneficiarias, claves o contraseñas en lo que te entregan, avisa y no la copies en ningún archivo.
11. **Herramientas antes de cada paso.** Antes de una etapa que use un conector (Drive, por ejemplo) o un script, comprueba que está disponible. Si falta, detente, di qué falta y cómo conectarlo, y sigue solo cuando esté.

## Bienvenida

Muestra este texto (corto) y luego revisa Drive:

> **Construir un estándar**
> Te acompaño a construir un estándar del ciclo de vida de iniciativas de Kodea. Se trabaja en Claude Code, en cuatro etapas:
> 1. **Inicio:** me cuentas qué quieres abordar y te digo qué documentos podrían servir.
> 2. **Cuatro bloques de preguntas:** yo propongo y tú confirmas, corriges o completas.
> 3. **Ficha para validar:** la creo y la dejo en Drive para que la revises con los equipos involucrados.
> 4. **Ficha final y herramientas:** link de la ficha final para la tarjeta de Trello, presentación y lo que el estándar necesite.
>
> **Necesitas tener Google Drive conectado a Claude Code**: ahí guardo la ficha y las herramientas. Lo reviso ahora mismo.
>
> No invento nada: si falta algo, te pregunto, y "no sé" es una respuesta válida. No compartas datos sensibles, sobre todo de personas beneficiarias, ni claves o contraseñas.

### Revisión de Drive

Explica en una línea para qué: "Uso Drive para guardar la ficha y las herramientas en la carpeta 'Estándares', leer las fichas de los otros estándares para revisar que coincidan, y guardar el registro del tiempo de trabajo."

1. **Conector.** Si tienes disponibles las herramientas del conector de Google Drive, sigue sin decir nada. Si no las tienes, dile a la persona que lo conecte y que vuelva a esta conversación. *(Instrucción de dónde se conecta: por verificar en las pruebas.)*
2. **Intérprete de Python.** Ejecuta `python3 --version || python --version || py -3 --version` y anota cuál responde; úsalo en los scripts de esta skill. Si ninguno responde, di antes de empezar: "En tu computador no encuentro Python. Sin él no se registra el tiempo de trabajo y ese dato quedará como no medido. ¿Seguimos así o lo instalamos primero?" Continúa solo con su confirmación.
3. **Permiso.** Consulta los metadatos de la carpeta "Estándares" (id `1QKWbQHT-IFZtoO3csoLziXKPK74HdKy5`). Si `canAddChildren` no es verdadero, entrega el link https://drive.google.com/drive/folders/1QKWbQHT-IFZtoO3csoLziXKPK74HdKy5 y pide que solicite permiso de edición manualmente. Si lo tiene, sigue sin decir nada.

### Mensajes que se dan en el momento (no en la bienvenida)

| Cuándo | Mensaje |
|---|---|
| La persona dice que va a parar | "No tienes que guardar nada: la conversación queda guardada sola. Para seguir, vuelve a abrir esta misma conversación desde la barra lateral de Claude Code. Si trabajas otro estándar en paralelo, usa otra conversación." |
| Al cerrar el primer bloque | "Al cerrar cada bloque guardo un borrador, así no se pierde lo avanzado." |
| Quien responde no lidera la etapa | "Conviene que quien lidera la etapa revise tus respuestas o participe, sobre todo roles, tolerancias y lo que no puede fallar." |
| Al pasar a la etapa 3 | "Guardo en Drive solo lo que vas a compartir. Los borradores quedan en tu computador. No borro ni envío nada a la papelera sin preguntarte." |
| Al terminar | "La skill registró cuánto tiempo tomó el trabajo y quién creó el estándar, en una carpeta de Drive del equipo de Desarrollo de Iniciativas. Esta información se usará para entender cómo se usa la herramienta y para guiarte mejor sobre cómo trabajar con ella." |

## Registro de tiempo (interno, no se muestra a la persona)

- Al empezar el Inicio, ejecuta: `P="${CLAUDE_PROJECT_DIR:-$PWD}"; mkdir -p "$P/.construir-estandar" && cp "${CLAUDE_SKILL_DIR}/scripts/registrar_hora.py" "$P/.construir-estandar/"`. Si `$CLAUDE_PROJECT_DIR` está vacío, el comando usa la carpeta actual. Desde ahí, el hook anota la hora de cada mensaje.
- Al empezar cada etapa, ejecuta `cd "${CLAUDE_PROJECT_DIR:-$PWD}" && <intérprete de Python de la comprobación> "${CLAUDE_SKILL_DIR}/scripts/marcar_etapa.py" "<Nombre del estándar>" <etapa>`. Usa siempre esta misma carpeta para todos los scripts de tiempo. Etapas: `inicio`, `bloque1`, `bloque2`, `bloque3`, `bloque4`, `ficha`, `validacion`, `ficha-cerrada`, `herramientas`, `fin`. Mientras no haya nombre, usa uno provisorio. Cuando el nombre quede confirmado en el Bloque 1, vuelve a marcar `inicio` con el nombre final, para que todas las marcas tengan el mismo nombre.
- **Quién lo hace:** el nombre y el correo de quien arma el estándar (punto 5 del mensaje del paso 2 de la Etapa 1) van en el registro, para que quede claro quién creó el estándar. Nunca van a la ficha.
- **Si el registro no funciona.** Comprueba en este orden: (1) que Python responda (paso 2 de "Revisión de Drive"); (2) que exista `<carpeta del proyecto>/.construir-estandar/eventos.jsonl` después de escribir un mensaje; si no existe, vuelve a copiar `registrar_hora.py` con el comando del primer bullet. Si sigue sin registrar, di: "No logro dejar registrado el tiempo de trabajo con las herramientas de esta conversación. ¿Me dices el día y la hora en que empezaste, y el día y la hora en que terminas o terminaste?" Guarda esas fechas en `<carpeta de trabajo>/tiempo-manual-<nombre>.md`, y en la etapa de creación y en la de herramientas súbelas a la carpeta de tiempo con las mismas columnas del CSV, con `minutos_de_trabajo` en `no medido`.
- No lo comentes con la persona salvo el mensaje "Al terminar" y, si hace falta, la pregunta de fechas del punto anterior.

## Etapa 1 · Inicio

**1. Caso** (opciones seleccionables):
- **A.** Escribir por primera vez una práctica que ya se hace pero no está documentada.
- **B.** Actualizar un proceso que ya está documentado en otro formato (ficha antigua, flujo en Miro, documento, presentación).
- **C.** Hacer una nueva versión de un estándar que ya está vigente con la Ficha Ejecutable.

Si duda entre dos, pregunta. Un estándar a medio migrar es B. Si una nueva versión cambia mucho el alcance, pregunta si es otro estándar.

**2. Un solo mensaje de identificación.**
- Casos A y B: "Cuéntame, con tus palabras: (1) de qué se trata lo que quieres abordar: qué se hace, cuándo y entre quiénes (no hace falta que tenga nombre); (2) en qué etapa del ciclo de vida ocurre; (3) quién lidera hoy esa etapa, y si eres tú; (4) qué problema hay hoy con este proceso; (5) tu nombre y tu correo de la cuenta, solo para el registro de tiempo (nunca van a la ficha)." En el caso B, el punto 4 es: "qué cambió desde que se documentó, y si hay algún dolor en cómo se hace hoy".
- Etapas (columnas del tablero "Estándar Desarrollo de Iniciativas"): 0. Base · 1. Planificación estratégica · 2. Preparación · 3. Lanzamiento · 4. Convocatoria · 5. Ejecución · 6. Monitoreo y Evaluación · 7. Mejora continua y Cierre · Trasversales (si corre en paralelo a todas).
- Caso C: "¿Qué estándar vas a revisar, qué motivó la revisión y quiénes son hoy sus responsables? ¿Eres uno de ellos? Y tu nombre y correo de la cuenta, solo para el registro de tiempo."
- Si quien responde no lidera la etapa, da el mensaje correspondiente.

**3. Carpeta de trabajo.** "Crea una carpeta de trabajo para este estándar; ahí guardas lo que reúnas y yo dejo los borradores, la ficha .md y el historial. Si quieres, la creo yo: `<carpeta del proyecto>/<nombre-del-estándar>/`." Debe quedar dentro de la carpeta en la que trabaja Claude Code.

**4. Documentos.** Muestra la tabla corta del caso de [documentos-inicio.md](referencias/documentos-inicio.md) con el texto: "Estos documentos suelen servir. No son requisitos: dime cuáles tienes y te explico cómo descargarlos." Da las instrucciones de descarga solo de los que la persona tenga.

**5. Cierre del Inicio.** Pregunta: "¿Hay algo del proceso que sepas y no esté escrito en ningún lado?" Lee todo lo entregado y muestra un resumen: qué aporta cada documento, qué falta para cada bloque, y las contradicciones entre documentos, planteadas como preguntas (no como errores). Con la confirmación, pasa al Bloque 1.

- **Caso B:** prellena los bloques desde el documento existente; pregunta solo lo que falta o lo que choca con estas reglas (por ejemplo, un semáforo o puntos de paso).
- **Caso C:** si no está la ficha .md, reconstrúyela desde el Google Doc y avisa que no hay historial. Diagnostica con las desviaciones y solicitudes de mejora de la tarjeta de seguimiento, y con el criterio de éxito; repasa rápido los bloques que no cambian y a fondo los afectados.

## Etapa 2 · Bloques

### Bloque 1 de 4 · Propósito y alineación

1. **Propósito y nombre (una sola propuesta).** "Con lo que me contaste, este estándar asegura <X> y resuelve <Y>. Lo llamaría <2 o 3 opciones que reflejen el propósito>. ¿Está bien, o quieres cambiar algo?" Si edita, muestra la versión final para que la valide. El nombre refleja el propósito (por ejemplo, "Cumplimiento Contractual" y no "Gestión Contractual").
2. **Los 7 lineamientos.** Redacta una frase por cada uno, o "No aplica: <razón>"; ninguno se omite. La persona confirma o edita: propósito a la vista · lograr el resultado adaptando la ruta · transparencia temprana en gestión de desviaciones y riesgos · datos a la vista · el mejor camino conocido · probar, aprender y crecer · atentos a las oportunidades. Usa la pregunta guía y la columna "cómo responde un estándar" de [lineamientos.md](referencias/lineamientos.md) para redactar cada frase a partir de lo que ya salió. Si algo que se afirma ocurre en otro estándar, nómbralo.

"Dónde aplica" sale de la etapa del Inicio y del Alcance del Bloque 3; "Quién participa" sale de los Bloques 2 y 4. No los preguntes aparte.

### Bloque 2 de 4 · Fases, responsables y herramientas

Encabezado: "En este bloque definimos las fases del proceso, quién es responsable de cada una y qué herramientas se usan. Yo propongo; tú confirmas, corriges o completas."

1. **Tabla de fases (una sola tabla).** Columnas: fase · qué se logra (resultado) · responsable · plazo (en días o semanas, si lo hay) · actores · cadencia (una vez / continua / periódica) · entrega (sincrónica o asincrónica, por qué medio). Lo que no tenga base queda `(pendiente)` y lo nombras debajo.
   - "Cada fase va a ser un checklist de la tarjeta de Trello, con un solo responsable: el rol o área que responde por que la fase se complete y que deja escritas las desviaciones."
   - Responsables: opciones de [roles-y-areas.md](referencias/roles-y-areas.md) más "otro rol que existe en Kodea". Si eligen dos, pide elegir uno.
2. **Herramientas.** "Estas son las herramientas que se usan en este estándar, según los documentos y lo conversado. La lista las muestra todas, aunque quieras mejorar alguna." Columnas: herramienta · obligatoria/opcional · para qué · estado (lista para usar / existe, pero hay que ajustarla / hay que elaborarla). Trello siempre está. El estado no va en la ficha: se usa en la etapa 4. Aplica la regla de plataforma nueva.

**Revisión intermedia (al cerrar el Bloque 2).** Antes del Bloque 3, muestra un resumen de lo confirmado: propósito, lineamientos, fases con responsables y herramientas. Pregunta: "¿Vamos bien hasta aquí, o hay algo que cambiar antes de definir tolerancias?" No avances sin la confirmación.

### Bloque 3 de 4 · Tolerancias

Encabezado: "Las tolerancias definen el margen que tiene el equipo para ajustarse sin tener que declararlo. Dentro de ese margen, el equipo decide solo. Si se sale, el responsable del checklist lo declara como desviación en la tarjeta de Trello: qué no se cumplió, qué se decidió y por qué."

1. **Tabla prellenada.** Completa las seis áreas con lo que ya salió y muéstrala:
   - **Tiempo:** plazos del Bloque 2. Si un plazo se puede dar en días o semanas, se fija; si no, "sin plazo fijo hasta contar con línea base".
   - **Costo:** tiempo del equipo, medido como duración por fase, sin margen fijo hasta contar con línea base. Si apareció otro costo con presupuesto: "no superar lo presupuestado para ese costo, en el presupuesto que corresponda"; si no tiene presupuesto, se describe.
   - **Calidad:** cada checklist se completa o sus desviaciones quedan declaradas, más las condiciones de calidad que hayan aparecido (cada una pasa a ítem del paso a paso).
   - **Alcance:** a qué se aplica y sus excepciones.
   - **Beneficios:** el criterio de éxito y la eficiencia (duración por fase contra la línea base); si un área entrega información a otra, qué tiene que recibir y con qué dato se ve. Sin margen.
   - **Riesgo:** se pregunta (punto 2).
   
   Pregunta: "¿Está bien, o quieres cambiar o agregar algo? Puedes editar cualquier fila, por ejemplo un plazo, un costo que falte o una excepción."
2. **Riesgo (única pregunta del bloque).** "¿Hay algo en este proceso que, si no ocurre, cause un daño serio al aportante, a la iniciativa o a Kodea, y que por eso no admita ninguna excepción? Por ejemplo, en el Estándar de Traspaso, que un área obligatoria quede sin nadie que la represente en la reunión; en el de Cumplimiento Contractual, que no se comuniquen las diferencias entre el documento enviado a firma y el firmado." Cada respuesta pasa a ítem [OBLIGATORIO]; avísalo en el momento.

### Bloque 4 de 4 · Operación

1. **Paso a paso = Lista de Cumplimiento.** Propón el checklist de cada fase: encabezado `Checklist N — Fase N · <Título de la fase> · Responsable: <área>` con su plazo si lo hay; ítems verificables que empiezan con un verbo; las condiciones de calidad y los [OBLIGATORIO] del Bloque 3; "Registrar en la tarjeta la fecha de cumplimiento de esta fase"; el ítem "Criterio de éxito cumplido" en el lugar que se defina en el punto 2, "Quién lo verifica y cuándo" (si se verifica al cerrar, como penúltimo ítem del último checklist); y el cierre como último ítem del último checklist.
2. **Criterio de éxito (cinco partes, en una sola propuesta).** El criterio de éxito comprueba si el estándar logró aquello para lo que existe; el cumplimiento del paso a paso se ve en los checklists, no aquí. Propón las cinco partes a partir del Propósito y de lo ya conversado, y la persona confirma o edita:
   1. **Qué se logra:** tomado del Propósito.
   2. **Cómo se ve:** el dato con que se comprueba (encuesta, fechas en Trello, documento, otro). Debe medir lo que el estándar controla, no factores externos. Prefiere un dato que ya exista. **Si no existe, propón la forma más simple de obtenerlo** dentro de algo que ya se hace (por ejemplo, una pregunta más en un Menti o en una reunión que ya ocurre), en vez de dejar el criterio pendiente. Si hace falta una encuesta o un formulario nuevo, o una plataforma nueva, no lo crees: avisa que se coordina con TDK.
   3. **Cuándo es suficiente:** el umbral, sin ambigüedad (por ejemplo, "todas las áreas responden sí" o "al menos el 80 % de los aspectos en verde"). Si la persona no sabe, propón uno y avisa que se ajusta en la revisión trimestral.
   4. **Quién lo verifica y cuándo:** un rol o área, y el momento. Si el logro se ve al cerrar los checklists, va como penúltimo ítem del último checklist; si se ve después, se dice cuándo (por ejemplo, al cierre de la edición) y en qué tarjeta o checklist queda el ítem.
   5. **Si no se logra:** el responsable lo registra en la tarjeta de seguimiento (qué faltó y por qué), y se revisa en la revisión trimestral del estándar como señal de mejora.
3. **Qué depende de este estándar.** "¿Hay algo que no puede empezar hasta que este estándar esté completo? Por ejemplo, el Kickoff no se hace hasta cerrar el Traspaso." Sí → si falla un [OBLIGATORIO], no se avanza a eso. No → se escala al DM y al equipo afectado, y continuar requiere la aprobación de ambos. Con esto y la etapa del Inicio, arma el diagrama del ciclo de vida y muéstralo para confirmar.
4. **Comprobación de propósito y lineamientos.** Tabla: frase del propósito o lineamiento → paso o herramienta que la sostiene. Comprueba también que cada herramienta aparezca en algún ítem. Para lo que falte: agregar un ítem o herramienta, reescribir la frase o sacarla.

Muestra sin preguntar las secciones Desviaciones (texto fijo) y Retroalimentación, con los roles a etiquetar ya completados con los responsables de los checklists (la persona puede cambiarlos). No hay preguntas frecuentes.

### Borrador

Al cerrar cada bloque, guarda o actualiza `<carpeta de trabajo>/borrador-<nombre>.md` con todo lo confirmado, incluido el estado de las herramientas. Si la conversación se retoma, parte leyéndolo.

## Etapa 3 · Ficha para validar

**Versiones:** 1.0 (Presentada para validación) → 1.1, 1.2… (una versión nueva solo cuando hay cambios que seguir trabajando con el equipo) → versión final (lleva `- FINAL` en el nombre del Doc y de la presentación). Una versión validada sin cambios nuevos no cambia de número. El número solo sube, y la etiqueta dice el estado.

1. **Armado.** Copia [plantilla-ficha.md](referencias/plantilla-ficha.md) y complétala en `<carpeta de trabajo>/ficha-<nombre>.md`, con `VERSIÓN: 1.0 (Presentada para validación)` y la fecha. Crea `<carpeta de trabajo>/historial-<nombre>.md` con la primera línea: `<fecha> · 1.0 · Creación`.
2. **Revisión (dos chequeos).** (1) Cada dato está en un solo lugar de la ficha. (2) Lo que la ficha dice de otros estándares coincide con lo que dicen esos estándares: búscalos en la carpeta "Estándares" de Drive y léelos. Muestra el resultado; si algo falla, propón la corrección y la persona decide.
3. **Google Doc.** Genera el HTML con `python3 -I "${CLAUDE_SKILL_DIR}/scripts/ficha_a_gdoc_html.py" <ficha.md> "${CLAUDE_SKILL_DIR}/fuentes"` y créalo con el conector de Drive (`create_file`, `contentMimeType: text/html`) dentro de una carpeta `<Nombre del estándar>` en "Estándares" (créala si no existe). Título: `FICHA - <Nombre> (V<versión>)`, con la misma versión que el contenido (por ejemplo, `FICHA - <Nombre> (V1.1)` y `VERSIÓN: 1.1`). Formato: Poppins, títulos en negrita, título 1 de 14, título 2 de 12, texto de 11; la primera línea es `VERSIÓN: <versión y estado>`; el resto del contenido, sin fechas ni historial.
   - **Caso C:** crea el Doc nuevo y deja el anterior en Drive como histórico. No lo borres ni lo envíes a la papelera.
4. **Presentación de validación.** Con la ficha de esta versión, arma una presentación de 6 diapositivas para que quien lidera el estándar la presente al equipo en la reunión de validación. El contenido sale solo de la ficha, sin inventar:
   1. Título y objetivo en una frase.
   2. Etapa del ciclo de vida en que ocurre (por ejemplo, 0. Base).
   3. Cómo funciona: 3 o 4 pasos, con el responsable de cada uno, y la base del estándar: la autonomía del equipo para completarlo con flexibilidad. Lo que decide no hacer, o hacer de otra manera, se escribe en la tarjeta de seguimiento; vale para cada paso, excepto los marcados como obligatorios.
   4. Checklist de cada área, tomado de la Lista de Cumplimiento de la ficha.
   5. Qué no se negocia: los ítems obligatorios y el criterio de éxito.
   6. Herramientas que apoyan el estándar (las que se van a generar) y cómo se mejora: la solicitud de mejora en la tarjeta de seguimiento, y la revisión cada 3 meses o con 3 solicitudes similares.
   Antes de mostrarla, dile a la persona: "Voy a generar un texto base para luego crear la presentación con la que puedes validar este estándar y/o recibir comentarios del equipo que participa. Léelo, valida o acepta el contenido para generar la diapositiva."
   Muestra en el chat la presentación diapositiva por diapositiva, con el texto de cada una y el checklist de cada área en la 4. La persona pide los cambios que necesite y los confirma. Solo después completa la plantilla base de la skill (`plantilla/presentacion-base.pptx`, en Poppins y con los colores de Kodea) pregúntale en qué formato la prefiere (`.pptx` editable, PDF para compartir, o ambos) y entrégale el archivo en ese formato, con el título `PRESENTACIÓN - <Nombre> (V<versión>)`, para que lo comparta con quienes participan del estándar y lo use en la reunión de validación. La presentación no se sube a Drive. Si no puedes generar el archivo, entrega el texto y pide a la persona que la arme a mano. Cuando la persona la use en la reunión de validación, dile: "Si en la reunión piden cambios, anótalos, vuelve a esta conversación y los revisamos."
5. **Aportes.** Propón qué del estándar conecta la estrategia con la operación, y qué aporta a la mejora continua (retrospectivas, información para la gestión de riesgos, desviaciones). La persona confirma. Crea un Google Doc en la carpeta del estándar con el nombre según el tipo: `APORTES A ALINEAMIENTO ESTRATÉGICO - …`, `APORTES A MEJORA CONTINUA - …` o `APORTES A ALINEAMIENTO ESTRATÉGICO Y MEJORA CONTINUA - <Nombre> (V<versión>)`. Si no hay aportes, no lo crees.
6. **Mensaje de validación.** Comparte la ficha (el Google Doc) y la presentación con los equipos involucrados (<responsables de los checklists y quien lidera la etapa>). Recomienda citar a una reunión para validar y/o recoger mejoras, e indica cuánto tiempo tienen para dejar sus comentarios. Cuando termine ese plazo, vuelve a esta conversación y revisamos los comentarios para cerrar la ficha. La ficha la valida <quien lidera la etapa>.
7. **Al volver: los comentarios no son ley.** Intenta leer los comentarios del Google Doc con el conector. Si no puedes, pide a la persona que los pegue en el chat. Para cada comentario propone una de tres salidas, y la persona decide:
   - **Aceptar**, indicando el beneficio.
   - **Rechazar**, indicando por qué.
   - **Otra solución** para el problema que el comentario detecta.

   Con esas decisiones, define cómo queda la versión:
   - **Sin cambios nuevos:** la versión no cambia de número. Anótalo en el historial y pregunta: "¿<Quien lidera la etapa> ya validó esta versión?" Si sí, pasa a la pregunta de versión final.
   - **Con cambios, y la persona sigue trabajando con el equipo:** aplica lo decidido en la ficha .md, anota en el historial qué cambió y crea una nueva versión (1.1, 1.2…) con su Google Doc. Vuelve al paso 6, para validar esa versión.
   - **Con cambios, y esta es la versión final:** antes de crear nada, pregunta: "¿Estás integrando los últimos comentarios y esta será la versión final?" Si responde que sí, busca en la carpeta del estándar si ya hay un Doc o una presentación con `FINAL` en el nombre. Si lo hay, quítale `FINAL` del nombre y deja el número de su versión (por ejemplo, `FICHA - <Nombre> (V1.1)`), como las versiones previas. Si tienes el conector de Drive, hazlo tú. Si no, dile a la persona que lo renombre a mano y espera a que lo haga antes de seguir. Luego aplica los cambios, anota el historial, crea el Google Doc con `- FINAL` en el nombre, compártelo como lector con `@kodea.org`, crea la presentación de esa versión con el mismo nombre y marca la etapa `ficha-cerrada`. Dile a la persona que el link de la ficha final se usará en la tarjeta de introducción (etapa 4).
   - **Todavía no:** la ficha queda en la versión actual, sin cerrar, hasta que la persona vuelva a confirmar.
8. **Registro de tiempo de la creación.** Ejecuta `cd "${CLAUDE_PROJECT_DIR:-$PWD}" && <intérprete de Python de la comprobación> "${CLAUDE_SKILL_DIR}/scripts/calcular_tiempo.py" "<Nombre>" <versión> <caso> "<correo de la cuenta, si lo conoces>" creacion` y sube el CSV que imprime a la carpeta "Tiempo de creación" (id `1naJQr-2n7s75UZGDBO7sw2f6fIN7YOh0`) con `create_file` (`contentMimeType: text/csv`, para que quede como Sheet), con el título `TIEMPO - <Nombre> (V<versión>) - creación`. No lo muestres a la persona.

## Etapa 4 · Ficha final y herramientas

Marca la etapa `herramientas`.

1. **Tarjeta de introducción en el tablero.** Cuando exista la ficha final (etapa 3), redacta el texto de la tarjeta de introducción del estándar, para la columna de la etapa en que ocurre, en el tablero "Estándar Desarrollo de Iniciativas": https://trello.com/b/x6mpA3C3. Muéstralo y la persona lo confirma. Contenido:
   - **Título:** el nombre del estándar.
   - **Descripción:** el objetivo en un párrafo corto, y un resumen de 3 o 4 pasos, una línea cada uno, con palabras simples. Ejemplo: "Sostenibilidad crea y comparte la carpeta de traspaso, y con esa información el Líder de Iniciativa Ágil prepara y convoca la reunión de traspaso."
   - **Adjuntos:** el link de la ficha final y el de la presentación de la versión final (`PRESENTACIÓN - <Nombre> (V<versión>) - FINAL`).
   Dile a la persona: "Yo te ayudo con el contenido para que tú lo integres en el tablero. Yo no escribo en Trello."
2. **Tarjeta de seguimiento.** Escribe el contenido de la tarjeta según [tarjeta-trello.md](referencias/tarjeta-trello.md): título, descripción (QUEREMOS, PARA, ESTARÁ LISTO CUANDO), prioridad, fecha límite y checklists con fase, número y área responsable. La prioridad la elige la persona para este caso: fecha fija (la fecha no se mueve; si no se cumple, pierde valor) o estándar (se necesita, pero puede esperar sin costo). Tú le recomiendas una según el estándar. La fecha límite siempre se pone, sea fija o estándar. Muéstralo y pide a la persona que valide que ese es el contenido correcto. Con su validación, dile: "Crea la tarjeta en el tablero Estándar Desarrollo de Iniciativas (https://trello.com/b/x6mpA3C3), en la columna de la etapa que corresponde, e integra este contenido. Una vez creada, que quede en el tablero de estándares, como plantilla en el Kanban desde el que se inicia el proceso, y ve sumando a esa tarjeta cada herramienta que el estándar requiere. Eso lo hace la persona a mano en Trello." Yo no escribo en Trello.
3. **Herramientas.** Propón el orden en que se crean las herramientas que el estándar necesita, con su estado según el Bloque 2 (lista, hay que ajustar, hay que crear). Las que ya están listas no se trabajan. La persona va creando cada una acompañada por ti: en general, tú propones el contenido y ella la arma a mano. Si la herramienta es de Drive (una hoja de cálculo de Sheets, por ejemplo) y tú puedes armarla, ofrécelo: primero la persona valida el contenido que propusiste, y después la creas en la carpeta del estándar, para que la persona tenga el link y lo ponga a mano en Trello. Fuera de eso, usas un conector solo si la persona lo pide de forma explícita y sabe usarlo.
   - **Cada vez que una herramienta esté creada,** dile a la persona que la suba a la tarjeta de seguimiento para que quede disponible y estandarizada, y que la tarjeta quede como plantilla en el Kanban desde el que se inicia el proceso.
   - **Herramienta (hoja de cálculo, Menti u otra):** (1) "¿Hay un formato ya creado que quieras mejorar?" (2) revisa cómo responde al objetivo de la herramienta (3) propón mejoras, que la persona valida (4) muestra en el chat cómo quedaría (5) si es de Drive, la creas en la carpeta del estándar después de la validación; si no, la persona la arma a mano. Las hojas de cálculo van a esa carpeta en Drive.
   - **Encuestas o formularios nuevos, o plataformas nuevas:** no los crees; avisa que se coordinan con TDK. Agregar una pregunta a un Menti o a una reunión que ya existe sí se puede, como cualquier ajuste de herramienta.
4. **Cierre.** Marca la etapa `fin`. Calcula el tiempo con el tramo `herramientas` y súbelo igual que en la etapa 3, con el título `TIEMPO - <Nombre> (V<versión>) - herramientas`. Da el mensaje "Al terminar" y un resumen con los links de lo creado y la ruta de la carpeta de trabajo.
