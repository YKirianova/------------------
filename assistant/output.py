# Створіть файл output.py у вашій папці з проєктом

from gtts import gTTS
import os

# Функція для озвучення тексту


def say(text):
    print(f"Бот каже: {text}")  # Додатково виводимо текст в консоль
    tts = gTTS(text=text, lang='uk')  # Використання Google Text-to-Speech
    tts.save("output.mp3")  # Зберігаємо аудіо у файл
    os.system("mpg321 output.mp3")  # Програємо аудіо (встановіть mpg321)
