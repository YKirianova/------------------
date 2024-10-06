import json
import random
from assistant.utility_functions import UtilityFunctions


class CommandProcessor:
    def __init__(self):
        self.data = self.load_speech()
        self.utility = UtilityFunctions()

    def load_speech(self):
        try:
            with open("data/speech.json", "r", encoding="utf-8") as file:
                data = json.load(file)
            return data
        except json.JSONDecodeError as e:
            print(f"Помилка завантаження JSON: {e}")
            return []

    def process_command(self, text):
        for phrase in self.data:
            for input_words in phrase["input"]:
                if input_words in text.lower():
                    output = random.choice(phrase["output"])
                    function_name = phrase.get("function")
                    if function_name:
                        func = getattr(self.utility, function_name, None)
                        if func:
                            output_func = func(text)
                            for key in output_func.keys():
                                output = output.replace(
                                    f"[{key}]", str(output_func[key]))
                    return output
        return None
