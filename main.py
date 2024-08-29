from audio_capture import AudioCapture
from sentiment_analysis import SentimentAnalysis
from chat_simulation import ChatSimulation

# Configurações
MODEL_PATH = "./models/pt-br"
API_KEY = ""

def main():
    audio_capture = AudioCapture(MODEL_PATH)
    chat_simulation = ChatSimulation(API_KEY)

    audio_capture.list_devices()
    audio_capture.start_stream()

    try:
        while True:
            text = audio_capture.transcribe()
            if text:
                print(f"Transcrição: {text}")
                # Assumindo que todas as mensagens são felizes
                sentiment = "happy"
                response = chat_simulation.generate_response(text, sentiment)
                print(f"Resposta Simulada: {response}")
    except KeyboardInterrupt:
        print("Interrompido pelo usuário")
    except Exception as e:
        print(f"Erro durante a execução: {e}")
    finally:
        audio_capture.close()

if __name__ == "__main__":
    main()