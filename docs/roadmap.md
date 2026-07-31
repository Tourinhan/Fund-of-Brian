# Roadmap

> Versión pública. El documento interno completo incluye análisis de mercado,
> estrategia de financiación y go-to-market detallado que no se publica — lo que
> sigue es la visión, las fases y los principios de arquitectura que las sostienen.

---

## El punto de partida

Un fondo de VC especializado en Digital Health, late seed / Series A, construyendo
un sistema operativo de inversión sobre Claude (Anthropic) y monday.com desde junio
2026.

El primer módulo en producción es el **Dealflow Screener**: un flujo que analiza
automáticamente el deck de una startup contra el ICP del fondo, clasifica la
compañía y crea el ítem en el Pipeline con todos los campos correctamente rellenados.

No es una demo. Es un sistema probado en producción, con deals reales, errores
reales y soluciones reales.

## Restricción de partida: construcción en solitario

Esto se construye en solitario, sin fecha de calendario fija por fase, hasta que
haya validación de producto real — un fondo externo usando el pipeline de forma
recurrente, con feedback positivo explícito. El co-fundador técnico se incorpora
después de esa validación, no antes. Mientras se está solo, solo hay ancho de banda
real para un track de trabajo pesado a la vez — todo lo demás tiene que ser barato
de construir (reutiliza algo que ya existe) o trabajo de scoping que un co-fundador
pueda ejecutar rápido cuando llegue.

## Visión

Construir el sistema operativo estándar para fondos early stage — empezando por un
fondo real como laboratorio. La ventaja competitiva no es la tecnología (Claude está
disponible para todos) sino el conocimiento operativo: saber exactamente qué flujos
necesita un fondo, cómo se clasifican los deals, qué campos importan, dónde falla la
automatización y cómo se corrige. Ese conocimiento solo se consigue operando un
fondo real.

## Fase 0 — Precondiciones

Resolver lo que bloquearía comercializar el sistema el día que se decida hacerlo:
titularidad de IP, vehículo societario si se factura a terceros.

## Fase 1 — Núcleo en solitario

Objetivo: que el pipeline core llegue a nivel "grado IC" — suficientemente bueno
como para sostener una decisión de inversión real sin reescritura mayor.

**Track A — Pipeline core** (secuencial, prioridad única de ingeniería):
1. Dealflow Screener ✅ en producción
2. Review one-pager — generación automática para el dealflow meeting
3. Analysis / IC memo — memo completo con red flags, preguntas al equipo, capaz de
   sostener una decisión de IC sin reescritura mayor

**Track B — Fund intelligence** (paralelo, bajo coste — reorganización de datos que
ya existen, no ingeniería nueva):
- Historial de deals descartados y aprobados, con scoring y decay explícitos
- Portfolio Management — el espejo de Dealflow Meetings para la fase post-inversión
  (razonamiento de board, métricas, riesgos, hitos)

Fin de Fase 1 = Track A a nivel IC-grade y Track B con el histórico estructurado al
100%. No hay fecha de calendario — hay una barra de calidad.

## Fase 2 — Expansión de adopción

Usar el pipeline ya maduro de Fase 1 como base de credibilidad para abrir el
reporting a LPs y portfolio — el ángulo comercial más fácil de vender en frío a un
segundo o tercer fondo que todavía no confía en el criterio del sistema.

Compliance (SOC 2, RBAC, segregación multi-fondo) se documenta en esta fase, no se
construye — es trabajo de ingeniería pesado que espera al co-fundador técnico.

## Fase 3 — Con co-fundador (post-validación)

Multi-CRM (el fondo elige su stack, el sistema se adapta), multi-sector (ICP y
flujos configurables), compliance real, integraciones de datos externos, y el
arranque de una capa de efectos de red: benchmarking agregado y anonimizado entre
varios fondos que use el sistema — cada fondo nuevo mejora la señal para los
anteriores. No tiene valor por debajo de un número mínimo de fondos contribuyendo,
así que no se lanza comercialmente antes de ese umbral.

## Fase 4 — Platform + Exit Prediction

Objetivo: cerrar el ciclo completo del negocio de un fondo, con predicción de exits
como módulo insignia — condicional al volumen de dato multi-fondo acumulado en Fase
3, no a una fecha de calendario.

Módulos upsell: LP Relations, Fundraising Kit, Co-investor Network (agregado,
histórico — nunca pipeline en vivo), Fund Analytics.

## Por qué tiene sentido construirlo así

El problema es universal — miles de fondos de VC y PE early stage operan con el
mismo caos: dealflow desordenado, análisis inconsistente, conocimiento institucional
que se pierde cuando se va un analista. Los jugadores establecidos de CRM dominan la
capa de relación, no la de juicio analítico. El moat es el conocimiento operativo
codificado deal a deal, reforzado por datos agregados una vez existe la capa de
efectos de red — hasta entonces es un moat más blando y replicable, y eso es
deliberadamente honesto sobre dónde está el proyecto hoy.

## La arquitectura que lo hace posible

El motor (flujos de trabajo, generación de documentos, integración con CRM) es
genérico; el conocimiento del dominio (ICP, señales, campos, lógica de
clasificación) vive en archivos de configuración intercambiables. Un fondo de otro
sector debería poder hacer onboarding configurando su propio `CLAUDE.md` y sus
`skills/`. El motor no cambia — cambia el contexto.

## Regla arquitectónica transversal: fuente única de verdad

Aprendizaje directo de producción, no teórico: un módulo mantuvo durante semanas una
tabla propia del estado de las compañías en watchlist, en paralelo al estado real en
el CRM. Se desincronizó sin que nadie lo notara — el sistema lo diagnosticaba semana
a semana y nadie lo corregía, porque corregir el documento a mano no es un proceso
sostenible.

Regla resultante, aplica a todo módulo futuro que trackee estado: ningún archivo o
módulo debe cachear un dato que el sistema de origen ya mantiene como verdad viva.
Se consulta en vivo, nunca se copia. Lo único que un módulo puede conservar por su
cuenta es conocimiento que ningún otro sistema guarda — razonamiento, objeciones,
checkpoints cualitativos.

## Stack actual

| Capa | Herramienta |
|---|---|
| AI | Claude (Anthropic) via Claude Projects |
| CRM | monday.com |
| Conocimiento | Archivos MD en el proyecto (CLAUDE.md, skills/) |
| Automatización | MCP conectado a Claude |

---

*Última actualización: julio 2026 · versión pública*
