import os, json


class AppSettings:

    def __init__(self, settings_file="settings.json"):
        self.settings_file = settings_file
        self.default_settings = {
            "theme": "dark",
            "hotkey": "<ctrl>+<alt>+r",
            "language_pair": "eng_ua"
        }

        self.allowed_values = {
            "theme": ["dark", "light"],
            "language_pair": ["eng_ua", "ua_eng"]
            # "hotkey" немає - може бути будь-яка строка
        }
        self.settings = self._load_settings()

    def save_settings(self):
        """Зберігає налаштування у файл"""
        with open(self.settings_file, "w", encoding='utf-8') as f:
            json.dump(self.settings, f, ensure_ascii=False, indent=4)

    def update_setting(self, key, value):
        """Оновлює налаштування"""
        if key not in self.default_settings:
            raise KeyError(f"Налаштування '{key}' не існує. Доступні ключі: {list(self.allowed_values.keys())}")

        if not isinstance(value, str):
            raise TypeError(f"Можна ввести лише текстове значення. Доступні значення: {list(self.default_settings.values())}")

        if key in self.allowed_values:
            if value not in self.allowed_values[key]:
                raise ValueError(
                    f"Неправильне значення '{value}' для '{key}'. "
                    f"Доступні: {self.allowed_values[key]}"
                )

        self.settings[key] = value
        self.save_settings()

    def _load_settings(self):
        """Завантажує налаштування з файлу або створює новий"""
        try:
            with open(self.settings_file, "r", encoding='utf-8') as f:
                loaded_settings = json.load(f)
            return {**self.default_settings, **loaded_settings}

        except (FileNotFoundError, json.JSONDecodeError):
            # Створюємо файл з дефолтними налаштуваннями
            with open(self.settings_file, "w", encoding='utf-8') as f:
                json.dump(self.default_settings, f, ensure_ascii=False, indent=4)
            return self.default_settings.copy()