import configparser
import json
import os
from flask import Flask, jsonify

# Initialize the Flask application
app = Flask(__name__)

def read_configurations(file_path):
    """
    Function to read configuration settings from a file and return them as a dictionary.
    :param file_path: Path to the configuration file.
    :return: Dictionary containing configuration settings.
    """
    config_parser = configparser.ConfigParser()
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Configuration file '{file_path}' not found.")
    
    config_parser.read(file_path)
    config_data = {}
    
    for section in config_parser.sections():
        config_data[section] = {}
        for key, value in config_parser.items(section):
            config_data[section][key] = value
    
    return config_data

def save_as_json_file(data, json_file_path):
    """
    Function to save data as JSON to a specified file.
    :param data: Data to be saved.
    :param json_file_path: Path to the JSON file.
    """
    with open(json_file_path, 'w') as json_file:
        json.dump(data, json_file, indent=4)

# Paths to configuration and JSON files
config_file_path = 'config.ini'
json_file_path = 'config.json'

try:
    # Read configuration data from the file
    config_data = read_configurations(config_file_path)
    
    # Save configuration data as JSON
    save_as_json_file(config_data, json_file_path)
    print(f"Configuration data saved to '{json_file_path}'")
except Exception as e:
    print(f"Error: {e}")

@app.route('/', methods=['GET'])
def get_configuration():
    """
    Endpoint to fetch the saved configuration data.
    :return: JSON response containing configuration data.
    """
    try:
        with open(json_file_path, 'r') as json_file:
            config_data = json.load(json_file)
        return jsonify(config_data), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
