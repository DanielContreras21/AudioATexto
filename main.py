import speech_recognition as sr
from tqdm import tqdm

filename = "audio.wav"
output_file = "transcripción_audio.txt"

r = sr.Recognizer()

try:
    with sr.AudioFile(filename) as source:
        duration = int(source.DURATION)
        full_transcription = ""
        print("Transcribiendo audio...\n")

        # tqdm muestra una barra que avanza en cada iteración
        for i in tqdm(range(0, duration, 10), desc="Progreso", unit="fragmento"):
            try:
                audio_data = r.record(source, duration=10)
                text = r.recognize_google(audio_data, language="es-ES")
                full_transcription += text + " "
            except sr.UnknownValueError:
                full_transcription += "[No se pudo entender el fragmento]\n"
            except sr.RequestError as e:
                print(f"\nError al comunicarse con servicios de Google: {e}")
                break

        with open(output_file, "w", encoding="utf-8") as f:
            f.write(full_transcription)
        
        print(f"\n✅ Transcripción completada y guardada en {output_file}")
except FileNotFoundError:
    print(f"❌ El archivo {filename} no se encontró. Asegúrate de que el archivo exista.")
except ValueError as e:
    print(f"❌ Error con el archivo de audio: {e}")
except Exception as e:
    print(f"⚠️ Ocurrió un error inesperado: {e}")
