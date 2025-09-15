import os
import json
from pathlib import Path
from config import DATABASE_PATH


class Database():
    _instance = None

    def __new__(cls):
        if (cls._instance is None):
            cls._instance = super(Database, cls).__new__(cls)

            cls._instance.data = {"students": [], "courses": [
            ], "teachers": [], "classes": [], "enrollments": []}

            cls._instance.json_file = Path(DATABASE_PATH / "database.json")
            cls._instance._load_or_create_json()

        return cls._instance

    def _load_or_create_json(self):
        if os.path.exists(self.json_file):
            with open(self.json_file, 'r') as f:
                self.data = json.load(f)
        else:
            self._save_json()

    def _save_json(self):
        with open(self.json_file, 'w') as f:
            json.dump(self.data, f, indent=4)

    def add_item(self, key, value):
        self.data[key].append(value)
        self._save_json()

    def get_item(self, key):
        return self.data.get(key)
