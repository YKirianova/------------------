from assistant.speech_recognition import SpeechRecognition
from assistant.command_processor import CommandProcessor
from assistant.openai_integration import OpenAIIntegration
from assistant.output import say


class VoiceAssistant:
    def __init__(self):
        self.speech_recognition = SpeechRecognition()
        self.command_processor = CommandProcessor()
        self.openai_integration = OpenAIIntegration()
        self.greeting_message = "Я твій голосовий помічник, чим можу допомогти?"

    def run(self):
        say(self.greeting_message)
        print("Готовий слухати...")

        while True:
            text = self.speech_recognition.listen()
            if text:
                print(f"Ви сказали: {text}")
                response = self.command_processor.process_command(text)

                if not response:
                    # Використання OpenAI, якщо команда не розпізнана
                    response = self.openai_integration.get_response(text)

                print(f"Відповідь: {response}")
                say(response)
