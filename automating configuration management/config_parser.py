# automating configuration management tasks is essential for maintaining consistency and managing infrastructure efficiently.
import configparser
import json
from flask import Flask, jsonify
import os

app = Flask(__name__)

CONFIG_FILE = 'config.ini'
OUTPUT_FILE = 'config.json'

def read_config(file_path):
    config = configparser.ConfigParser()
    try:
        config.read(file_path)
        if not config.sections():
            raise FileNotFoundError(f"No sections found in the config file: {file_path}")

        config_dict = {section: dict(config.items(section)) for section in config.sections()}
        return config_dict
    except FileNotFoundError as e:
        print(f"Error: {e}")
        return None
    except Exception as e:
        print(f"Error reading the config file: {e}")
        return None

def save_to_json(data, output_file):
    try:
        with open(output_file, 'w') as json_file:
            json.dump(data, json_file, indent=4)
    except Exception as e:
        print(f"Error saving to JSON file: {e}")

@app.route('/', methods=['GET'])
def get_config():
    if os.path.exists(OUTPUT_FILE):
        with open(OUTPUT_FILE, 'r') as json_file:
            data = json.load(json_file)
            return jsonify(data)
    else:
        return jsonify({"error": "Configuration file not found"}), 404

if __name__ == '__main__':
    config_data = read_config(CONFIG_FILE)
    if config_data:
        save_to_json(config_data, OUTPUT_FILE)
        print("Configuration data saved to JSON.")
    else:
        print("Failed to read and save configuration data.")
    
    app.run(debug=True)