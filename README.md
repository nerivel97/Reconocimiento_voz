# Reconocimiento de voz a texto

Este programa convierte tu voz en texto utilizando la librería **SpeechRecognition** de Python.  
Permite grabar audio desde el micrófono y transcribirlo en tiempo real mediante el servicio de Google.

---

## Requisitos previos

1. **Python 3.8+** instalado en tu computadora.  
   - Descarga desde: [https://www.python.org/downloads/]

2. **Visual Studio Code (VSC)** instalado.  
   - Descarga desde: [https://code.visualstudio.com/]

3. Instalar las dependencias necesarias. Abre una terminal y ejecuta:



*pip install SpeechRecognition pyaudio*

Si despues de esto en la terminal no hay error, ir hasta --- Como ejecutar

De lo contrario seguir indicaciones siguientes.

⚠ En algunos sistemas, pyaudio puede dar problemas de instalación.
Si falla, usa esta alternativa:

Descarga el .whl de PyAudio para tu versión de Python.

Luego instala con:
pip install nombre_del_archivo.whl




--- Cómo ejecutar el programa en VS Code ---
Clona o descarga este repositorio en tu computadora.

Abre la carpeta del proyecto en Visual Studio Code.

Abre el archivo main.py (o el nombre que le hayas puesto al programa).

En la terminal integrada de VS Code, ejecuta:
*python main.py*

O de lo contrario hacer clic derecho en el archivo y dar click en: *Run Python File in Terminal*

El programa mostrará un menú en consola como este:
1. Hablar para transcribir
2. Salir del programa
Selecciona la opción 1, habla por el micrófono y espera la transcripción.

Para terminar, selecciona la opción 2.

--- Notas ---
El programa reconoce voz en español (México) (es-MX).

Es necesario tener un micrófono funcional conectado al sistema.

El reconocimiento se hace usando el servicio gratuito de Google Speech Recognition.
