# E01 - Contexto, requisitos y alcance

**Solicitud empresarial:**

El área de Operaciones necesita registrar órdenes de mantenimiento de equipos de bodega y consultarlas posteriormente. Se requiere identificar las funciones existentes, las restricciones del sistema y las necesidades que aún deben confirmarse.

**Versión/fecha/entorno:**

- Versión revisada: completar con la versión o commit real del proyecto.
- Fecha: completar con la fecha de revisión.
- Entorno: entorno local de desarrollo.
- Responsable: estudiante.

**Archivos y componentes observados:**

- `frontend/index.html`: formulario y presentación de órdenes.
- `frontend/app.js`: interacción con la API.
- `backend/app/ordenes/controladores.py`: operaciones HTTP.
- `backend/app/ordenes/servicios.py`: validación de datos.
- `backend/app/ordenes/modelos.py`: modelo de orden.

**Acciones reproducidas, paso a paso:**

1. Revisar el formulario web e identificar los campos equipo y descripción.
2. Inspeccionar los controladores y localizar GET y POST de órdenes.
3. Revisar el servicio y el modelo para identificar validaciones y campos almacenados.
4. Relacionar las funciones encontradas con los requisitos RF-01, RF-02 y RN-01.

**Resultado observado (captura, prueba, log):**

Pendiente de completar con la inspección real. Se debe identificar el formulario, las rutas existentes y los campos del modelo. Adjuntar capturas o referencias al código revisado.

**Interpretación arquitectónica:**

El problema empresarial es registrar y consultar órdenes. La solución de referencia utiliza una interfaz web, una API Flask y persistencia relacional. No se debe asumir que existen cuentas de usuario, roles o integraciones que no estén implementados.

**Clasificación: OBSERVADO / CÓDIGO / DOCUMENTADO / SUPUESTO / PROPUESTO**

CÓDIGO para las funciones confirmadas mediante inspección. OBSERVADO para las operaciones reproducidas. SUPUESTO para necesidades aún no confirmadas.

**Riesgo, alternativa y pendiente:**

Faltan datos confirmados de concurrencia, objetivos de rendimiento, retención y seguridad. Se debe solicitar esa información antes de establecer requisitos adicionales.

**Criterio de aceptación comprobado:**

Pendiente de comprobar. Se acepta cuando el documento diferencia el problema, los requisitos, las funciones verificadas, las restricciones y los asuntos pendientes.