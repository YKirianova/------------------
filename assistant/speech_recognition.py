import speech_recognition as sr


class SpeechRecognition:
    def __init__(self):
        self.recognizer = sr.Recognizer()

    def listen(self):
        with sr.Microphone() as source:
            print("Готовий слухати...")
            try:
                audio = self.recognizer.listen(
                    source, timeout=5, phrase_time_limit=5)
                text = self.recognizer.recognize_google(
                    audio, language="uk-UA")
                return text
            except sr.UnknownValueError:
                print("Не вдалося розпізнати звук")
                return None
            except sr.RequestError as e:
                print(f"Помилка запиту до Google Speech Recognition; {e}")
                return None
            except sr.WaitTimeoutError:
                print("Помилка очікування: тайм-аут")
                return None
