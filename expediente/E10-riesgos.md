# E10 - Rendimiento, disponibilidad, seguridad y costos

**Solicitud empresarial:**

Evaluar el comportamiento del sistema cuando aumenta el número de órdenes, cuando la API deja de responder y cuando se requiere proteger el acceso a la información.

**Versión/fecha/entorno:**

- Versión: completar.
- Fecha: completar.
- Entorno: Windows, aplicación local y navegador.
- Responsable: estudiante.

**Archivos y componentes observados:**

- `frontend/app.js`.
- `backend/app/__init__.py`.
- `backend/app/ordenes/controladores.py`.
- Base de datos configurada.
- Evidencias E02, E07 y E09.

**Acciones reproducidas, paso a paso:**

1. Medir la duración de GET `/api/ordenes` con una cantidad conocida de registros.
2. Agregar órdenes ficticias y repetir la medición.
3. Mantener la página abierta y detener Flask.
4. Solicitar las órdenes desde la interfaz y registrar el error.
5. Reiniciar Flask y comprobar la recuperación.
6. Revisar los controles de autenticación y los riesgos de exposición.

**Resultado observado (captura, prueba, log):**

Pendiente de ejecutar. Registrar las mediciones, el error de conexión y la recuperación con capturas reales.

**Interpretación arquitectónica:**

El tiempo de respuesta permite comparar condiciones de prueba. La caída del backend impide temporalmente las consultas, mientras que reiniciarlo permite evaluar la recuperación. Esto no demuestra alta disponibilidad ni escalabilidad de producción.

**Clasificación: OBSERVADO / CÓDIGO / DOCUMENTADO / SUPUESTO / PROPUESTO**

OBSERVADO para las pruebas ejecutadas; CÓDIGO para los controles confirmados mediante inspección.

**Riesgo, alternativa y pendiente:**

La aplicación de referencia no implementa autenticación. No debe exponerse públicamente sin controles adicionales. También están pendientes los objetivos de rendimiento, disponibilidad y costos operativos.

**Criterio de aceptación comprobado:**

Pendiente. Debe documentarse el impacto de la falla, la recuperación, las mediciones y los controles de seguridad pendientes, sin confundir un error de red con una respuesta HTTP 500.