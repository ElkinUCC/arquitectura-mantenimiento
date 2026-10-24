# E11 - Decisión final y ADR-001

**Solicitud empresarial:**

Analizar cómo evolucionar la consulta de órdenes para atender un posible crecimiento sin afectar innecesariamente a los consumidores actuales de la API.

**Versión/fecha/entorno:**

- Versión: completar.
- Fecha: completar.
- Entorno: revisión del código y evidencias E01–E10.
- Responsable: estudiante.

**Archivos y componentes observados:**

- `backend/app/ordenes/controladores.py`.
- `backend/app/ordenes/repositorios.py`.
- Evidencias E01–E10.
- `expediente/decisiones/ADR-001.md`.

**Acciones reproducidas, paso a paso:**

1. Revisar el método de consulta del repositorio.
2. Confirmar si la consulta establece un límite de registros.
3. Comparar mantener el endpoint actual con diseñar una consulta paginada compatible.
4. Analizar consecuencias sobre el contrato, la compatibilidad y las pruebas.
5. Elaborar el ADR-001 con contexto, alternativas, decisión propuesta, riesgos y validación.
6. Relacionar las conclusiones con las evidencias disponibles.

**Resultado observado (captura, prueba, log):**

Pendiente de completar con la revisión del código y el índice de evidencias. El manual de referencia identifica una consulta que devuelve todos los registros sin límite; este hallazgo debe verificarse en la versión examinada.

**Interpretación arquitectónica:**

Una consulta sin límite podría requerir revisión si crece el volumen de datos. La paginación permitiría solicitar subconjuntos de registros, pero debe diseñarse considerando el orden estable, los metadatos, la compatibilidad y los consumidores existentes.

**Clasificación: OBSERVADO / CÓDIGO / DOCUMENTADO / SUPUESTO / PROPUESTO**

CÓDIGO para el comportamiento confirmado de la consulta y PROPUESTO para la paginación y la decisión pendiente de aprobación.

**Riesgo, alternativa y pendiente:**

- Alternativa A: conservar el endpoint actual.
- Alternativa B: diseñar una consulta paginada compatible.
- Riesgos: cambios incompatibles, resultados inconsistentes entre páginas y esfuerzo adicional de implementación y pruebas.
- Pendientes: caracterizar la carga, revisar consumidores y definir objetivos de calidad.

**Criterio de aceptación comprobado:**

Pendiente. El ADR-001 debe incluir al menos dos alternativas, criterios de comparación, consecuencias, riesgos, validación futura y una condición concreta para revisar la decisión. La paginación no debe presentarse como implementada ni como una mejora de rendimiento ya demostrada.