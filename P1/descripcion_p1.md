
# **Parte 1**

## **Generación y compilación del archivo `.proto`**

### 1. **Definición del archivo `.proto`**
   
Generar un archivo `.proto` que sirva como base para la comunicación entre servicios utilizando gRPC. Este archivo definirá la estructura de los mensajes intercambiados entre el cliente y el servidor.
Para generar este archivo, utilizar la siguiente estructura:

-   **`taxi_id`**: Un campo de tipo `int64` que identifica de manera única cada taxi.
-   **`conductor_id`**: Un campo de tipo `string` que almacena el identificador del conductor.
-   **`pasajero_id`**: Un campo de tipo `repeated string` que permitirá almacenar múltiples identificadores de pasajeros. En las siguientes secciones,  cada estudiante deberá utilizar su código de la Universidad Privada Boliviana (UPB) como uno de los identificadores.
-   **`costo_estimado`**: Un campo de tipo `float` que representa el costo estimado del viaje.


Incluir capturas de pantalla del archivo .proto que muestren el código utilizado durante la creación y análisis del archivo.

### **2. Compilación del Archivo `.proto`**

Compilar el archivo `.proto` creado previamente para generar el código fuente necesario que permita la implementación de la comunicación mediante gRPC.

#### 2.1 Instrucciones:

a.  **Preparación del entorno**:
    - Asegurarse de tener instalado el compilador de Protocol Buffers (protoc). Si no está instalado, descargarlo e instalarlo desde [el sitio oficial de Protocol Buffers](https://developers.google.com/protocol-buffers).

b.  **Compilación del archivo**:
   -   Abrir una terminal o línea de comandos.
   -   Navegar hasta el directorio donde se encuentra el archivo `.proto`. `protoc --python_out=. nombre_del_archivo.proto`
   -   En el comando, `--python_out=.` indica que el código generado debe ser en Python y se debe almacenar en el directorio actual. Es posible cambiar la opción según el lenguaje de implementación deseado (por ejemplo, `--java_out=.` para Java). Para este proyecto se utiliza el lenguaje de Python

  
c.  **Documentación de la salida**:
   - Observar la salida en la terminal al ejecutar el comando. Si el proceso es exitoso, generalmente no se muestra ningún mensaje de error.
   - Documentar cualquier mensaje de salida, especialmente si indica errores o advertencias, y explicar cómo resolverlos. En particular:
        -   El comando introducido en la terminal.
        -   Cualquier salida o mensaje generado durante la compilación.
        -   Los archivos generados en el directorio de trabajo, si es posible.
  
d.  **Análisis**:   
- **Revisión de los archivos generados**: Verificar y documentar que los archivos generados después de la compilación se encuentran en la misma dirección del archivo `.proto`. Explicar cómo estos archivos se integran en el desarrollo de la aplicación gRPC.


### **3.Generación del client-stub**

En esta sección se va a implementar y ejecutar un script en Python que utilice el código fuente generado para enviar una solicitud de mensaje y observar su formato. Documentar en su reporte los pasos indicados e incluir comentarios y análisis de las salidas generadas

#### 3.1 Instrucciones:

a.  **Preparación del entorno**:
- Asegurarse de que todas las bibliotecas se encuentren en la dirección donde se encuentra el archivo `parte_1a.py`.

b.  **Completar el código en el archivo `parte_1a.py`**:

El archivo `parte_1a.py` contiene un esqueleto de código que debe ser completado para generar un mensaje. Se deben llenar las elipsis (`...`) con los valores y tipos de datos apropiados según lo definido en el archivo `.proto`. Agregar comentarios al código generado 

- Importar los módulos generados por el compilador de Protocol Buffers. Esto incluirá el módulo con las definiciones de los mensajes (`Viaje`).

- Utilizar el mensaje definido en el módulo importado para crear una nueva instancia del mensaje. Rellenar los campos del mensaje con los valores correspondientes:
    -   `taxi_id`: Debe ser un número único que identifique al taxi.
    -   `conductor_id`: Utilizar un identificador fijo, como en el ejemplo 'Sist\_dist'.
    -   `pasajero_id`: Incluir una lista de tres pasajeros. Estos codigos corresponden al códigos de estudiante, asegurándose de modificarlos adecuadamente para que reflejen el ejemplo dado con 'Codigo\_UPB', 'Codigo\_UPB+10', 'Codigo\_UPB+20'.
    -   `costo_estimado`: Asignar un valor estimado al costo del viaje.

c.  **Ejecución del código**:
- Ejecutar el script `parte_1a.py` en un entorno que soporte Python y gRPC.

- Observar la salida impresa que muestra el formato del mensaje de solicitud.



### 4. Procesamiento de Datos de Solicitud y Generación de Mensajes gRPC

Para los mensajes de solicitud del cliente, se almacenaron estos solicitud en un archivo JSON. En esta sección se va a generar las solicitudes correspondientes, serializarlas a formato binario, y realizar un análisis gráfico del costo estimado.
Para esta sección, completar el archivo `parte_1b.py`

#### Instrucciones:

a.  **Datos de mensaje de solicitud**:
-  Utilizar los datos del archivo `sample_request_data.json` que contiene una serie de mensajes de solicitud para ser procesados.

b.  **Generar solicitudes gRPC en el archivo `parte1_b.py`**:

-   Iterar sobre cada mensaje de solicitud en los datos JSON cargados.
-   Utilizar el stub de cliente para generar el mensaje de solicitud para cada entrada de datos.
-   Serializar las solicitudes a formato binario utilizando el método `SerializeToString()`.

c.  **Guardar los mensajes en formato binario**:

-   Almacenar los mensajes serializados en formato binario en un archivo llamado `output_p1b.bin`. 
-   Comentar acerca el tamaño en memoria utilizado por los archivos de entrada json y el archivo codificado bin.

d.  **Impresión de mensajes convertidos**:

-   Imprimir en la consola los primeros 10 mensajes convertidos a formato binario para verificar la correcta serialización.

e.  **Generación de una gráfica del costo estimado**:

-   Crear una gráfica que muestre el costo estimado indicado en cada mensaje vs el id del taxi.
-   Guardar esta gráfica en un archivo de imagen para su análisis posterior.

f.  **Documentación y Comentarios**:

-   Comentar cada parte del código en `parte1_b.py` explicando qué se realiza en cada paso.
-   Documentar los pasos realizados y la implementación del script.