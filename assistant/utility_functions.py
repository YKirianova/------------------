import time
import random
import requests


class UtilityFunctions:
    def get_time(self, text: str):
        current_time = time.localtime()
        output_time = f"{current_time.tm_hour}:{current_time.tm_min}"
        return {"час": output_time}

    def get_random_number(self, text: str):
        return {"число": random.randint(0, 100)}

    def get_dollar_currency(self, text: str):
        try:
            result = requests.get(
                "https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5")
            data = result.json()
            return {"курс": data[1]["sale"]}
        except (requests.RequestException, IndexError, KeyError) as e:
            print(f"Помилка запиту або обробки даних: {e}")
            return {"курс": "невідомий"}
