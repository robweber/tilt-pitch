import json

class PitchConfig:

    def __init__(self, data: dict):
        self.webhook_urls = list()
        self.__dict__.update(data)


    @staticmethod
    def load():
        file_path = "pitch.json"
        file_open = open(file_path, "r").read()
        config_raw = json.loads(file_open)
        return PitchConfig(config_raw)
