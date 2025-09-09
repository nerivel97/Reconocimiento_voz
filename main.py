# PROGRAMA DE RECONOCIMIENTO DE VOZ
# Convierte voz a texto usando la librería SpeechRecognition

import speech_recognition as sr  # Biblioteca principal para reconocimiento de voz
import time  # Para manejar pausas y temporizadores entre grabaciones

# -----------------------------------------
# FUNCIÓN: configurar_microfono
# Configura el reconocedor sin mostrar la lista de micrófonos.
# -----------------------------------------
def configurar_microfono():
    recognizer = sr.Recognizer()  # Se crea un objeto "Recognizer" que será el encargado de procesar el audio
    
    # Configuración optimizada para fluidez
    recognizer.pause_threshold = 2.0  # Permite pausas de hasta 2 segundos
    recognizer.energy_threshold = 300  # Ajuste de sensibilidad del micrófono
    
    print("Micrófono configurado correctamente")
    print("   • Se usará el micrófono predeterminado del sistema")
    
    return recognizer  # Retorna el objeto recognizer para usarlo en otras funciones

def reconocer_voz(recognizer):
    try:
        # Abrir el micrófono como fuente de audio
        with sr.Microphone() as source:
            print("\n Calibrando micrófono para ruido ambiental...")
            # Ajuste automático al ruido de fondo para mejorar la precisión
            recognizer.adjust_for_ambient_noise(source, duration=1)
            
            # Instrucciones al usuario
            print("Habla ahora (máximo 10 segundos)...")
            print("   • Puedes hacer pausas breves")
            print("   • Espera el mensaje para comenzar a hablar\n")
            
            # Pausa breve antes de empezar
            time.sleep(0.5)
            print("--- HABLA AHORA ---")
            
            # Captura de audio:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)
            
            print("--- FIN DE GRABACIÓN ---")
            print("Procesando audio...")
            
            # Convierte el audio en texto usando la API gratuita de Google
            texto = recognizer.recognize_google(audio, language='es-MX')
            
            # Mostrar el texto reconocido
            print(f"Texto reconocido: {texto}")
            return texto  # Retorna el texto para usarlo en otras partes del programa
            
    # Manejo de errores comunes:
    except sr.WaitTimeoutError:
        print("Tiempo de espera agotado. No se detectó voz.")
    except sr.UnknownValueError:
        print("No se pudo entender el audio. Intenta hablar más claro.")
    except sr.RequestError as e:
        print(f"Error en el servicio de reconocimiento: {e}")
    except Exception as e:
        print(f"Error inesperado: {e}")
    
    return None  # Si ocurre un error, se devuelve None

# -----------------------------------------
# FUNCIÓN PRINCIPAL (main)
# Controla el flujo del programa
# -----------------------------------------
def main():
    """Función principal que ejecuta el programa"""
    print("=" * 20)
    print("VOZ A TEXTO SIMPLE")
    print("=" * 20)
    
    # Configurar el reconocedor de voz, que es el microfono predeterminado del dispositivo
    recognizer = configurar_microfono()
    
    # Bucle principal para que el usuario pueda elegir opciones
    while True:
        print("\n" + "-" * 30)
        print("OPCIONES:")
        print("1. Hablar para transcribir")
        print("2. Salir del programa")
        
        # Se pide la opción al usuario
        try:
            opcion = input("Selecciona una opción (1-2): ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\n Programa interrumpido")
            break
        
        if opcion == "1":
            # Llamada a la función que reconoce la voz
            texto = reconocer_voz(recognizer)
            
            # El texto ya se imprime dentro de reconocer_voz
            # Aquí podríamos guardar el texto en un archivo o usarlo en otra función jeje
                    
        elif opcion == "2":
            print("Adios")
            break  # Sale del bucle y termina el programa
        else:
            print("Opción no válida. Por favor elige 1 o 2.")

#Este es el punto de entrada y salida del programa

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error crítico: {e}")
        input("Presiona Enter para salir...")

