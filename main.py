import speech_recognition as sr
import time

def configurar_microfono():
    recognizer = sr.Recognizer()
    print("🎤 Micrófonos disponibles:")
    for index, name in enumerate(sr.Microphone.list_microphone_names()):
        print(f"   {index}: {name}")
    return recognizer

def reconocer_voz(recognizer):
    try:
        with sr.Microphone() as source:
            print("\n Calibrando micrófono para ruido ambiental...")
            recognizer.adjust_for_ambient_noise(source, duration=1)
            print("Habla ahora (máximo 10 segundos)...")
            print("Espera el mensaje para comenzar a hablar\n")
            time.sleep(0.5)
            print("--- HABLA AHORA ---")
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)
            print("--- FIN DE GRABACIÓN ---")
            print("Procesando audio...")
            texto = recognizer.recognize_google(audio, language='es-MX')
            print(f"Texto reconocido: {texto}")
            return texto
    except sr.WaitTimeoutError:
        print("Tiempo de espera agotado. No se detectó la voz.")
    except sr.UnknownValueError:
        print("No se pudo entender el audio. Por favor hablar más claro.")
    except sr.RequestError as e:
        print(f"Error en el servicio de reconocimiento: {e}")
    except Exception as e:
        print(f"Error inesperado: {e}")
    return None

def main():
    print("=" * 50)
    print("ESCRIBIENDO DE VOZ A TEXTO")
    print("=" * 50)
    recognizer = configurar_microfono()
    while True:
        print("\n" + "-" * 30)
        print("OPCIONES:")
        print("1. Hablar para transcribir")
        print("2. Salir del programa")
        opcion = input("Selecciona una opción (1-2): ").strip()
        if opcion == "1":
            reconocer_voz(recognizer)
        elif opcion == "2":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor elige 1 o 2.")

if __name__ == "__main__":
    main()
