import json
from pathlib import Path
DATA_DIR = Path(__file__).parent




def load_json(filename):
    file_path = DATA_DIR / filename

    with open(file_path) as file:
        return json.load(file)