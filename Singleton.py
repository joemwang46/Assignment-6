import json
from typing import Any

class Config:
    _instance = None
    _config_data: dict[str, Any] = {}

    def __new__(cls, config_path: str = "config.json"):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._load_config(config_path)
        return cls._instance

    def _load_config(self, config_path: str):
        with open(config_path, "r") as f:
            self._config_data = json.load(f)

    def get(self, key: str, default: Any = None) -> Any:
        return self._config_data.get(key, default)
