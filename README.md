# python-azure-ai-textanalytics

Este proyecto es un **ejercicio didáctico** desarrollado en Python que utiliza el **SDK oficial de Azure AI Text Analytics** para detectar el idioma de un texto ingresado por el usuario desde consola.

⚠️ **Importante**
El código de este repositorio fue **tomado y adaptado del curso oficial de Microsoft**:

**AI-102: Designing and Implementing a Microsoft Azure AI Solution**
<https://microsoftlearning.github.io/AI-102-AIEngineer/>

Este repositorio **no tiene fines comerciales ni productivos** y existe únicamente con **propósitos educativos y de aprendizaje**.

## 1\. ¿Qué hace este programa en general?

Este programa:

1. Lee **credenciales de Azure** desde un archivo `.env`
2. Pide al usuario que escriba un texto
3. Envía ese texto al servicio **Azure AI Text Analytics**
4. Azure detecta **el idioma del texto**
5. El programa imprime el idioma detectado
6. El ciclo se repite hasta que el usuario escribe `"quit"`

## 2\. Importaciones: traer funcionalidades externas

```bash
from dotenv import load_dotenv
import os
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential
```

### ¿Qué significa esto?

En Python, **importar** es como decir:

```text
“Voy a usar herramientas que no vienen incluidas por defecto”.
```

#### Explicación de cada import

- `load_dotenv`
  - Lee variables desde un archivo `.env`
  - Evita escribir claves secretas directamente en el código
- `os`
  - Permite acceder a variables del sistema operativo
  - Aquí se usa para leer variables de entorno
- `TextAnalyticsClient`
  - Es el **cliente oficial de Azure** para usar Text Analytics
  - Es el objeto que “habla” con Azure
- `AzureKeyCredential`
  - Representa la **clave secreta** para autenticarse contra Azure

## 3\. Función `main()`: el punto principal del programa

```bash
def main():
```

En Python, una función agrupa instrucciones que cumplen un propósito.
`main()` es la función principal del programa.

### 3.1 Variables globales

```bash
global cog_endpoint
global cog_key
```

Esto indica que esas variables:

- Se usarán en **otras funciones**
- No serán solo locales a `main()`

En este caso, se necesitan luego en `GetLanguage()`.

### 3.2 Bloque `try / except`

```bash
try:
    ...
except Exception as ex:
    print(ex)
```

Esto sirve para:

- Capturar errores
- Evitar que el programa se caiga abruptamente
- Mostrar el error de forma controlada

Ejemplo de errores posibles:

- Clave incorrecta
- Endpoint mal configurado
- Problemas de red

## 4\. Cargar variables de entorno (.env)

```bash
load_dotenv()
cog_endpoint = os.getenv('COG_SERVICE_ENDPOINT')
cog_key = os.getenv('COG_SERVICE_KEY')
```

### ¿Qué está pasando aquí?

1. `load_dotenv()`:

    - Lee el archivo `.env`
    - Carga sus valores en el sistema

2. `os.getenv(...)`:

    - Obtiene valores del entorno
    - Ejemplo típico en `.env`:

        COG_SERVICE_ENDPOINT="<https://mi-recurso.cognitiveservices.azure.com/>"

        COG_SERVICE_KEY="mi_clave_secreta"

Esto es **una buena práctica de seguridad**, porque:

- No expones claves en GitHub
- Puedes cambiar credenciales sin tocar el código

## 5\. Ciclo `while`: pedir texto al usuario

```bash
userText =''
while userText.lower() != 'quit':
```

### ¿Qué hace este ciclo?

- Se repite indefinidamente
- Solo termina cuando el usuario escribe `"quit"`

`lower()` convierte el texto a minúsculas para evitar errores como:

- `Quit`
- `QUIT`
- `QuIt`

### 5.1 Leer texto del usuario

```bash
userText = input('\nEnter some text ("quit" to stop)\n')
```

- `input()` pausa el programa
- Espera a que el usuario escriba algo
- Devuelve ese texto como una cadena (`str`)

### 5.2 Llamar a la función de detección de idioma

```bash
language = GetLanguage(userText)
print('Language:', language)
```

Aquí ocurre lo importante:

1. Se llama a la función `GetLanguage`
2. Se envía el texto del usuario
3. Azure devuelve el idioma detectado
4. Se imprime el resultado

## 6\. Función `GetLanguage(text)`

```bash
def GetLanguage(text):
```

Esta función:

- Recibe un texto
- Se conecta a Azure
- Devuelve el idioma detectado

### 6.1 Crear las credenciales

```bash
credential = AzureKeyCredential(cog_key)
```

Esto crea un objeto que contiene:

- Tu **clave de Azure**
- Que será usada para autenticar la solicitud

### 6.2 Crear el cliente de Azure

```bash
client = TextAnalyticsClient(endpoint=cog_endpoint,credential=credential )
```

Piensa en el cliente como:

```text
“El objeto que sabe cómo hablar con Azure Text Analytics”
```

Aquí se configura con:

- El endpoint (dirección del servicio)
- La credencial (clave)

### 6.3 Llamar al servicio de detección de idioma

```bash
detectedLanguage = client.detect_language(documents=[text])[0]
```

Puntos clave:

- Azure espera una **lista de documentos**
  - Por eso `[text]` (aunque sea solo uno)
- El resultado es una lista
- `[0]` toma el primer (y único) resultado

### 6.4 Extraer el nombre del idioma

```bash
return detectedLanguage.primary_language.name
```

El objeto devuelto contiene mucha información, pero aquí solo interesa:

- El idioma principal
- Su nombre (por ejemplo: `"Spanish"`, `"English"`)

La función devuelve ese valor a `main()`.

## 7\. Punto de entrada del programa

```bash
if __name__ == "__main__":
    main()
```

Esto significa:

- Si este archivo se ejecuta directamente:
  - Se ejecuta `main()`
- Si se importa desde otro archivo:
  - `main()` **no se ejecuta automáticamente**

Es una **convención estándar en Python**.

## 8\. Resumen conceptual (muy importante)

Este código te enseña varios conceptos fundamentales:

- Uso de **funciones**
- Manejo de **variables de entorno**
- Consumo de **APIs en la nube**
- Uso de **SDKs oficiales**
- Control de errores con `try / except`
- Interacción con el usuario (`input`)
- Bucles (`while`)

## 📦 9\. Instalación y ejecución con Poetry

### a\. Clonar el repositorio

```bash
git clone https://github.com/wiltrovira/python-azure-ai-textanalytics
cd python-azure-ai-textanalytics
```

### b\. Instalar dependencias

```bash
poetry install
```

### c\. Ejecutar validaciones de calidad del código

Ejecuta todas las validaciones automáticas de calidad de código definidas en tu proyecto, usando el entorno virtual gestionado por Poetry.

```bash
poetry run pre-commit run --all-files
```

### d\. Ejecutar el programa

```bash
poetry run python src/python-azure-ai-textanalytics/main.py
```
