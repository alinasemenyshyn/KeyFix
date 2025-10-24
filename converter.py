import json, os


class LayoutConverter:
    @staticmethod
    def load_data_maps(file_path):
        """Завантажує словник конвертації з JSON файлу"""
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Файл словника не знайдено: {file_path}")

        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data

    def __init__(self, maps_file_path):
        """Ініціалізує конвертер з файлу словника"""
        self.maps_file_path = maps_file_path
        self.maps = self.load_data_maps(maps_file_path)

    def convert(self, text, direction):
        """
        Конвертує текст згідно з напрямком

        Args:
            text (str): Текст для конвертації
            direction (str): Напрямок конвертації (напр. "EN_TO_UKR")

        Returns:
            str: Конвертований текст
        """
        if not text:
            return text

        if direction is None:
            return text

        if direction not in self.maps:
            raise KeyError(
                f"Напрямок '{direction}' не знайдено. "
                f"Доступні: {list(self.maps.keys())}"
            )

        # Конвертація
        char_map = self.maps[direction]
        result = [char_map.get(char, char) for char in text]
        return ''.join(result)

    def get_available_directions(self):
        """Повертає список доступних напрямків конвертації"""
        return list(self.maps.keys())