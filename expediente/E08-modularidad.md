# E08 - Modularidad, dependencias y SOLID

**Solicitud empresarial:**

Evaluar si la organización del código facilita mantener, probar y ampliar las funcionalidades de gestión de órdenes.

**Versión/fecha/entorno:**

- Versión: completar.
- Fecha: completar.
- Entorno: inspección del código fuente.
- Responsable: estudiante.

**Archivos y componentes observados:**

- `backend/app/ordenes/controladores.py`.
- `backend/app/ordenes/servicios.py`.
- `backend/app/ordenes/repositorios.py`.
- `backend/app/ordenes/modelos.py`.

**Acciones reproducidas, paso a paso:**

1. Localizar la función `crear()` del controlador.
2. Seguir la llamada al servicio `registrar()`.
3. Revisar las validaciones del servicio.
4. Seguir la llamada al repositorio `guardar()`.
5. Identificar las operaciones de persistencia mediante SQLAlchemy.
6. Analizar la separación de responsabilidades y los principios SOLID pertinentes.

**Resultado observado (captura, prueba, log):**

Pendiente de adjuntar referencias o capturas del recorrido real del código. En el modelo de referencia, el controlador delega en el servicio y este utiliza el repositorio.

**Interpretación arquitectónica:**

La separación permite distinguir transporte HTTP, reglas de negocio y acceso a datos. Sin embargo, el servicio mantiene una dependencia directa del repositorio, por lo que cambiar la persistencia podría requerir ajustes.

**Clasificación: OBSERVADO / CÓDIGO / DOCUMENTADO / SUPUESTO / PROPUESTO**

CÓDIGO cuando se confirmen las funciones y dependencias mediante inspección; PROPUESTO para mejoras futuras.

**Riesgo, alternativa y pendiente:**

El acoplamiento puede aumentar el costo de los cambios. Una abstracción de repositorio es una alternativa si existe una necesidad concreta, pero no debe incorporarse sin justificación.

**Criterio de aceptación comprobado:**

Pendiente. El análisis debe identificar responsabilidades, dependencias y consecuencias concretas, sin tratar SOLID como una lista mecánica de cumplimiento.