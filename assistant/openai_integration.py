import openai


class OpenAIIntegration:
    def __init__(self):
        self.api_key = "YOUR_API_KEY"

    def get_response(self, text):
        try:
            prompt = f'''Ти маєш генерувати відповіді для голосового помічника, без зайвого тексту, 
            все, що ти сгенеруєш - я буду озвучувати користувачу. Давай короткі відповіді.
            Нижче надаю запит користувача:
            {text}
            '''
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": prompt}
                ]
            )
            return response['choices'][0]["message"]["content"].strip()
        except Exception as e:
            print(f"Помилка OpenAI: {e}")
            return "Вибачте, я не можу відповісти зараз."
