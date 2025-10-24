import json, os

class LayoutConverter:
    @staticmethod
    def load_data_maps(file_path):
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Файл словника не знайдено: {file_path}")
        with open(file_path, 'r', encoding='utf-8') as char:
            data = json.load(char)
        return data

    def __init__(self, maps_file_path):
        self.maps = self.load_data_maps(maps_file_path)

    def convert(self, text, direction):
        if not text:
            return None
        if direction is None:
            return text

        char_map = self.maps.get(direction, {})
        result = []

        for char in text:
            converter = char_map.get(char, char)
            result.append(converter)

        return ''.join(result)

# converter_ukr = LayoutConverter('data/maps_ukr_eng.json')
# result = converter_ukr.convert("ghbdsn", "EN_TO_UKR")