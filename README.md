--------------------------------------------------------------
#   PROGRAMA DE VOZ A TEXTO SIMPLE
--------------------------------------------------------------

Primero que nada clonar o descargar el proyecto

Si tienes Git:
git clone https://github.com/nerivel97/Reconocimiento_voz.git

O descargar el ZIP y extraerlo


# EJECUCION DEL .EXE


# REQUISITOS:
1.- Tu dispositivo debe contar con acceso a Internet.



# COMO EJECUTAR:
1.- Descargar el archivo .exe llamado "ReconocimientoVoz.exe"

2.- Ejecutar el archivo .exe descargado.
   Consideraciones "O J O"
   Algunos dispositivos no les permite ejecutar el archivo debido a su antiviruz o por el mismo windows defender, por lo tanto si ese es el caso debes de desactivar el Windows defender o el antiviruz que lo este bloqueando.

3.- Una vez ejecutado el archivo aparecera una ventana parecida a una terminal, el cual debera aparecer con un texto parecido:

      ====================
      VOZ A TEXTO SIMPLE  
      ====================
      Micrófono configurado correctamente
         • Se usará el micrófono predeterminado del sistema

      ------------------------------
      OPCIONES:
      1. Hablar para transcribir
      2. Salir del programa
      Selecciona una opción (1-2):

   Esto significara que el archivo ha sido ejecutado correctamente.



# EJECUCION EN VISUAL STUDIO (POR SI SE REQUIERE HACER UN CAMBIO Y VISUZALIZARLO AL MOMENTO)


# Requisitos:
1. Python 3.8 o superior
Descargar desde: python.org

Durante la instalación, MARCAR la opción: "Add Python to PATH"


2. Visual Studio Code
Descargar desde: code.visualstudio.com


3. Extensiones recomendadas para VS Code
Python (Microsoft)



# COMO EJECUTAR:

1. Abrir el proyecto en VS Code
Abrir Visual Studio Code

File → Open Folder → Seleccionar la carpeta del proyecto


2. Abrir terminal en VS Code
Ctrl + SHIFT + ñ 

O Terminal → New Terminal


3. Instalar las dependencias
Ejecutar en la terminal:

# Instalar SpeechRecognition y PyAudio
pip install speechrecognition pyaudio

# Si hay error con PyAudio en Windows, probar:
pip install pipwin
pipwin install pyaudio

# O alternativas:
python -m pip install speechrecognition pyaudio

# Ejecucion del programa:
# Método 1: Desde la terminal de VSC
# Navegar a la carpeta del proyecto (si no está ahí)
cd ruta/a/tu/carpeta

# Ejecutar el programa
python reconocimiento_voz.py



# Método 2: Desde el botón de ejecución de VS Code
Dar click derecho en el archivo "reconocimiento_voz.py" y luego dar click izquierdo en "Run Python File in terminal"


