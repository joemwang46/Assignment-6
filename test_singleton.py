import pytest
from Singleton import Config
import json

@pytest.fixture
def tmp_config(tmp_path):
    p = tmp_path / "config.json"
    with open(p, "w") as f:
        json.dump({"default_strategy": "MeanReversionStrategy"}, f)
    return str(p)

def test_singleton_shared_instance(tmp_config):
    c1 = Config(tmp_config)
    c2 = Config(tmp_config)
    assert c1 is c2
    assert c1.get("default_strategy") == "MeanReversionStrategy"
