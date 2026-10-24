# Arquitectura de Software — Gestión de Órdenes de Mantenimiento

## 1. Descripción del proyecto

Este proyecto analiza la arquitectura de un sistema web para registrar y consultar órdenes de mantenimiento de equipos de bodega, como montacargas y bandas transportadoras.

El trabajo busca identificar los componentes del sistema, verificar su funcionamiento, evaluar atributos de calidad y justificar posibles mejoras arquitectónicas.

## 2. Objetivos

- Identificar los requisitos funcionales y las restricciones.
- Analizar la arquitectura mediante diagramas C4.
- Examinar las responsabilidades y dependencias de los componentes.
- Verificar la integración HTTP y la persistencia de datos.
- Evaluar rendimiento, disponibilidad, seguridad y riesgos.
- Comparar alternativas arquitectónicas y documentar una decisión mediante un ADR.

## 3. Tecnologías

- **Frontend:** HTML, CSS y JavaScript.
- **Backend:** Python y Flask.
- **API:** HTTP con intercambio de datos JSON.
- **Persistencia:** SQLite mediante Flask-SQLAlchemy.
- **Diagramas:** diagrams.net.
- **Entorno de ejecución:** Windows y Python.

La configuración de MySQL es una alternativa opcional que requiere validación independiente.

## 4. Arquitectura general

La solución de referencia utiliza un monolito modular con responsabilidades separadas:

1. **Frontend:** presenta el formulario y las órdenes.
2. **Controladores:** reciben las solicitudes HTTP y devuelven las respuestas.
3. **Servicios:** validan los datos y coordinan las operaciones.
4. **Repositorios:** realizan las consultas y guardan los registros.
5. **Modelos y ORM:** representan los datos y gestionan la persistencia.

El flujo de comunicación es:

Frontend → API Flask → Servicio → Repositorio → Base de datos.

## 5. Requisitos principales

- RF-01: registrar órdenes con equipo y descripción obligatorios.
- RF-02: consultar órdenes y su estado.
- RN-01: conservar las órdenes después de reiniciar el backend.
- INV-01: analizar el crecimiento del listado y sus posibles impactos.
- INV-02: comprobar el comportamiento del cliente cuando la API no responde.
- SEG-01: revisar los límites de exposición y la autenticación.

Los objetivos cuantitativos de rendimiento, concurrencia y disponibilidad están pendientes de definición.

## 6. Estructura del expediente

```text
expediente/
├── E01-contexto.md
├── E02-recursos.md
├── E03-contexto-c4.md
├── E04-contenedores.md
├── E05-propuesta.md
├── E06-alternativas.md
├── E07-calidad.md
├── E08-modularidad.md
├── E09-integracion.md
├── E10-riesgos.md
├── E11-decision.md
├── indice-evidencias.md
├── capturas/
├── diagramas/
├── mediciones/
└── decisiones/
    └── ADR-001.md
```

## 7. Ejecución local

Los siguientes comandos corresponden al procedimiento de referencia del manual y deben ejecutarse desde PowerShell.

Crear el entorno virtual e instalar dependencias:

```powershell
cd backend
py -m venv .venv
$PY = Join-Path (Get-Location) '.venv\Scripts\python.exe'
& $PY -m pip install -r requirements.txt
Copy-Item .env.example .env -Force
```

Inicializar la base de datos e iniciar el backend:

```powershell
& $PY .\init_db.py
& $PY .\app.py
```

Abrir en el navegador:

`http://127.0.0.1:5000`

Verificar el estado del backend:

`http://127.0.0.1:5000/health`

## 8. Pruebas de verificación

Se deben ejecutar y documentar las siguientes comprobaciones:

- Consulta de órdenes mediante GET `/api/ordenes`.
- Registro de órdenes mediante POST `/api/ordenes`.
- Rechazo de datos inválidos con respuesta HTTP 400.
- Conservación de registros después de reiniciar Flask.
- Comportamiento del frontend cuando el backend está detenido.
- Medición del tiempo de respuesta bajo condiciones documentadas.

Los resultados deben registrarse con evidencias reales.

## 9. Decisión arquitectónica

El ADR-001 analiza la posibilidad de incorporar una consulta paginada para gestionar el crecimiento del listado de órdenes.

La decisión permanece propuesta hasta revisar los consumidores existentes, caracterizar la carga y definir los criterios de aceptación. La paginación no se considera implementada por el solo hecho de documentarla.

## 10. Seguridad y limitaciones

La aplicación de referencia no implementa autenticación y está destinada al análisis local. No debe exponerse públicamente sin controles de seguridad adicionales.

Las mediciones locales no demuestran por sí solas escalabilidad ni disponibilidad de producción.

## 11. Estado de la entrega

La entrega se considera completa cuando las evidencias E01–E11, los diagramas, las pruebas, el índice de evidencias y el ADR-001 estén documentados y respaldados por los archivos correspondientes.

**Proyecto académico:** Arquitecturas de Software y Computacional.
**Responsable:** completar con el nombre del estudiante.
**Fecha:** completar con la fecha de entrega.
