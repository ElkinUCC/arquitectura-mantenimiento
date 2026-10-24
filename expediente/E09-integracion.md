# E09 - Integración HTTP, sincronía y persistencia

**Solicitud empresarial:**

Comprobar que la API registra órdenes válidas, rechaza entradas incorrectas y conserva la información después de reiniciar el backend.

**Versión/fecha/entorno:**

- Versión: completar.
- Fecha: completar.
- Entorno: aplicación local, PowerShell y navegador.
- Responsable: estudiante.

**Archivos y componentes observados:**

- `backend/app/ordenes/controladores.py`.
- `backend/app/ordenes/servicios.py`.
- `backend/app/ordenes/repositorios.py`.
- `backend/app/ordenes/modelos.py`.
- Base de datos configurada en el entorno.

**Acciones reproducidas, paso a paso:**

1. Ejecutar GET `/api/ordenes` y verificar la respuesta.
2. Ejecutar POST `/api/ordenes` con una orden válida.
3. Comprobar que la respuesta sea HTTP 201.
4. Enviar datos inválidos y verificar el rechazo HTTP 400.
5. Confirmar que el registro inválido no se haya insertado.
6. Reiniciar Flask sin reinicializar la base de datos.
7. Consultar nuevamente las órdenes.

**Resultado observado (captura, prueba, log):**

Pendiente de completar con las respuestas HTTP, capturas y resultados reales. Los resultados esperados son 200 para consulta, 201 para registro válido y 400 para entrada inválida.

**Interpretación arquitectónica:**

La comunicación entre frontend y API utiliza HTTP/JSON. El flujo de registro pasa por el controlador, el servicio y el repositorio. La persistencia depende del almacenamiento configurado.

**Clasificación: OBSERVADO / CÓDIGO / DOCUMENTADO / SUPUESTO / PROPUESTO**

OBSERVADO cuando se ejecuten las pruebas; CÓDIGO para las funciones confirmadas por inspección.

**Riesgo, alternativa y pendiente:**

Una validación insuficiente podría aceptar datos incorrectos. Un error de conexión debe diferenciarse de una respuesta HTTP de error. Está pendiente confirmar la persistencia mediante una prueba de reinicio.

**Criterio de aceptación comprobado:**

Pendiente. Se debe demostrar el contrato de la API, el rechazo de entradas inválidas sin inserción y la conservación de los registros tras reiniciar el backend.