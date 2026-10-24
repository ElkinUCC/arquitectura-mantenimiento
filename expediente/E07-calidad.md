# E07 - Atributos de calidad y escenarios RAR

**Solicitud empresarial:**

Analizar cómo responderá el sistema ante el crecimiento del número de órdenes y ante la indisponibilidad de la API, considerando también la integridad de los registros.

**Versión/fecha/entorno:**

- Versión: completar.
- Fecha: completar.
- Entorno: aplicación local y documentación arquitectónica.
- Responsable: estudiante.

**Archivos y componentes observados:**

- `backend/app/ordenes/controladores.py`.
- `backend/app/ordenes/servicios.py`.
- `backend/app/ordenes/repositorios.py`.
- `frontend/app.js`.
- Evidencias E01, E02 y E06.

**Acciones reproducidas, paso a paso:**

1. Identificar los atributos de calidad relevantes: integridad, rendimiento y disponibilidad.
2. Definir un escenario de crecimiento del listado.
3. Definir un escenario de indisponibilidad del backend.
4. Establecer qué componente responde y cómo medir el resultado.
5. Registrar los objetivos que todavía deben aprobarse.

**Resultado observado (captura, prueba, log):**

Pendiente de ejecutar y documentar los escenarios. Se deben recopilar tiempos de respuesta, resultados de consultas y evidencia del comportamiento del frontend ante una falla.

**Interpretación arquitectónica:**

El rendimiento y la disponibilidad condicionan el diseño de la consulta, el contrato de la API y el manejo de errores. Los objetivos numéricos deben acordarse con el negocio.

**Clasificación: OBSERVADO / CÓDIGO / DOCUMENTADO / SUPUESTO / PROPUESTO**

DOCUMENTADO para los escenarios definidos; OBSERVADO cuando las pruebas se ejecuten.

**Riesgo, alternativa y pendiente:**

El crecimiento podría aumentar el tiempo y tamaño de las respuestas. Una API desconectada impide consultar temporalmente los datos. Faltan volúmenes, umbrales y objetivos de disponibilidad aprobados.

**Criterio de aceptación comprobado:**

Pendiente. Deben quedar documentados los escenarios EC-01 y EC-02 con fuente, estímulo, ambiente, artefacto, respuesta y método de medición.