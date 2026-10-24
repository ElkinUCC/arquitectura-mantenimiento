# E02 - Recursos computacionales y línea base

**Solicitud empresarial:**

Operaciones necesita conocer el comportamiento de la aplicación y evaluar posibles impactos en los recursos cuando aumente el número de órdenes.

**Versión/fecha/entorno:**

- Versión: completar con la versión real.
- Fecha: completar.
- Entorno: Windows, aplicación local y navegador.
- Responsable: estudiante.

**Archivos y componentes observados:**

- Backend Flask y proceso Python.
- Frontend web.
- Base de datos SQLite.
- Herramientas: Administrador de tareas y DevTools del navegador.

**Acciones reproducidas, paso a paso:**

1. Iniciar la aplicación y esperar 60 segundos.
2. Abrir F12 y seleccionar Network → Fetch/XHR.
3. Consultar las órdenes.
4. Registrar el estado HTTP, duración y tamaño de respuesta.
5. Repetir la operación tres veces y registrar CPU y RAM.

**Resultado observado (captura, prueba, log):**

Pendiente de medición. Registrar las tres observaciones reales y adjuntar capturas de Network y del Administrador de tareas.

**Interpretación arquitectónica:**

Las mediciones permiten establecer una línea base local, pero no demuestran por sí solas la capacidad máxima del sistema ni un cuello de botella.

**Clasificación: OBSERVADO / CÓDIGO / DOCUMENTADO / SUPUESTO / PROPUESTO**

OBSERVADO cuando se hayan ejecutado y registrado las mediciones.

**Riesgo, alternativa y pendiente:**

No se dispone de objetivos de rendimiento ni de carga de producción. Se requiere una prueba de carga representativa para obtener conclusiones sobre capacidad.

**Criterio de aceptación comprobado:**

Pendiente. Deben registrarse tres mediciones con fecha, entorno, operación, unidades y limitaciones.