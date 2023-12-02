import json
import os
from typing import Optional

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_FILE_PATH = os.path.join(CURRENT_DIR, '..', 'config.json')

class Config():
    config = None

    def __init__(self) -> None:
        if self.config is None:
            self.config = self.load_from_file()
    
    @staticmethod
    def load_from_file() -> dict:
        with open(CONFIG_FILE_PATH, 'r') as f:
            data = json.load(f)
        return data

    def get_option(self, option: str) -> Optional[str]:
        return self.config.get(option, None)