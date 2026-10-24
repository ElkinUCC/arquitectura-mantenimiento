# E04 - Diagrama C4 Container

**Solicitud empresarial:**

Mostrar cómo colaboran los componentes principales de la solución para registrar, consultar y almacenar órdenes de mantenimiento.

**Versión/fecha/entorno:**

- Versión: completar.
- Fecha: completar.
- Entorno: proyecto local y diagrams.net.
- Responsable: estudiante.

**Archivos y componentes observados:**

- `frontend/index.html`.
- `frontend/app.js`.
- `backend/app/__init__.py`.
- `backend/app/ordenes/controladores.py`.
- `backend/app/ordenes/servicios.py`.
- `backend/app/ordenes/repositorios.py`.
- `backend/app/ordenes/modelos.py`.

**Acciones reproducidas, paso a paso:**

1. Revisar la interfaz web y las solicitudes que envía.
2. Inspeccionar las rutas y responsabilidades del backend.
3. Identificar la persistencia utilizada.
4. Dibujar el frontend, la API Flask y la base de datos.
5. Etiquetar las conexiones HTTP/JSON y ORM/SQL.
6. Exportar el diagrama a PDF.

**Resultado observado (captura, prueba, log):**

Pendiente de adjuntar el diagrama exportado y las referencias del código que sustentan sus elementos.

**Interpretación arquitectónica:**

La solución de referencia utiliza una aplicación web cliente, una API Flask y un almacén relacional. El backend organiza responsabilidades internas, por lo que corresponde a un monolito modular y no a microservicios independientes.

**Clasificación: OBSERVADO / CÓDIGO / DOCUMENTADO / SUPUESTO / PROPUESTO**

CÓDIGO para los componentes inspeccionados y DOCUMENTADO para el diagrama elaborado.

**Riesgo, alternativa y pendiente:**

Debe verificarse el almacén realmente configurado. SQLite es la opción inicial del manual; MySQL es una variante opcional que requiere validación independiente.

**Criterio de aceptación comprobado:**

Pendiente. La vista debe representar los mismos límites del C4 Context y mostrar correctamente componentes, responsabilidades y protocolos.