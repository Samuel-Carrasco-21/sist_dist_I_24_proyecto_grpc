# **Parte 2**

## **Desarrollo de un Archivo Protofile para Servicio de Transporte**

En esta sección del proyecto, se elabora inicialmente la estructura de un archivo .proto, el cual define tanto la estructura de datos como los servicios requeridos para iniciar un viaje en un servicio de transporte utilizando gRPC

### **1. Estructura Propuesta:**

El archivo `.proto` propuesto contiene definiciones de mensajes para las solicitudes de inicio de viaje y sus respuestas, un enum para los tipos de viaje, y un mensaje para la ubicación geográfica.

#### Instrucciones:

**a. Configuración Inicial**

- Definir la sintaxis del protofile como `proto3`, que es la versión más reciente y recomendada de Protocol Buffers.

**b. Importaciones Necesarias**:
-   Importar `google/protobuf/timestamp.proto` para utilizar el tipo de dato `Timestamp` que permite registrar momentos específicos en el tiempo de manera precisa.

**c. Definición de Tipos de Datos Complejos**:

-   **`ubicacion`**: Definir un mensaje que contenga la latitud y longitud como `double` para capturar la ubicación geográfica con precisión.
-   **`tipoViaje`**: Usar un `enum` para definir los tipos de viaje disponibles (`REGULAR`, `POOL`, `PREMIUM`), facilitando la selección clara del tipo de servicio deseado.

**d. Mensajes de Solicitud y Respuesta**:
    
-   **`StartRequest`**: Crear un mensaje que incluya:
    -   `taxi_id` y `conductor_id` para identificar el vehículo y el conductor.
    -   `pasajero_id` como lista para incluir uno o más pasajeros.
    -   `tipoViaje` para especificar el tipo de viaje utilizando el `enum tipoViaje`.
    -   `ubicacion` para indicar el punto de inicio del viaje.
    -   `tiempo` para registrar el momento en que se solicita el viaje.
-   **`StartResponse`**: Definir un mensaje que responda con un `id` único para el viaje y el `costo_cliente`, indicando el costo calculado para el cliente.
**e. Definición del Servicio gRPC**:
    
-   **`Viaje_rpc`**: Definir un servicio que incluya el método `Start`, el cual toma un `StartRequest` y devuelve un `StartResponse`. Esto establece el protocolo de comunicación entre cliente y servidor.

**g. Documentación**:
    
-   Documentar cada campo dentro de los mensajes y el servicio para asegurar que futuros desarrolladores y usuarios entiendan su propósito y uso.


### 2. Compilación del Archivo Protofile Utilizando un Script Bash

Una vez definida la estructura del archivo `.proto`, esta sección procederá a compilar el archivo .proto desarrollado previamente. Esta compilación generará el código fuente necesario para implementar la comunicación mediante gRPC, utilizando un script Bash.

#### Instrucciones:

**a. Preparación del Script Bash**:

-   Crear un archivo con extensión `.sh` en el mismo directorio donde se encuentra el archivo `.proto`.
-   Nombrar el archivo de manera descriptiva, como `compile_proto.sh`.

**b. Contenido del Script**:
    
-   El script debe incluir instrucciones para utilizar el módulo `grpc_tools.protoc` de Python. Este módulo facilita la compilación de archivos `.proto` para generar código fuente en Python.
-   Los comandos dentro del script deben especificar que se generarán dos tipos de archivos de Python:
    -   **Archivos `.py` regulares**: Estos archivos contienen las clases derivadas de las estructuras definidas en el `.proto`, como mensajes y enums, y son esenciales para manipular estos objetos dentro del código Python.
    -   **Archivos `_grpc.py`**: Estos archivos contienen el código necesario para implementar los servicios de gRPC definidos en el `.proto`. Incluyen las clases de stubs para clientes y servidores, que son cruciales para enviar y recibir llamadas a través de gRPC. La razón por la que se generan estos archivos es para separar las definiciones de la estructura de datos de la lógica de comunicación gRPC, manteniendo así el código organizado y modular.
-   Establecer el directorio actual como el lugar de búsqueda de archivos de importación y destino para los archivos generados.

**c. Ejecución del Script**:
    
-   Dar permisos de ejecución al archivo script utilizando el comando apropiado en la terminal.
-   Ejecutar el script desde la terminal para iniciar la compilación del archivo `.proto`.
   
**d. Verificación de Resultados**:
    
-   Verificar que los archivos de código fuente han sido creados correctamente en el directorio especificado.
-   Comprobar la ausencia de errores en la salida de la terminal para confirmar que la compilación fue exitosa.

**e. Documentación**:   
-   Documentar el propósito de cada comando dentro del script para que los usuarios y otros desarrolladores entiendan su función.
-   Explicar cómo los archivos generados serán utilizados en el desarrollo de la aplicación gRPC.