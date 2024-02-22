from flask import Flask, jsonify
import requests
import json

app = Flask(__name__)


data = {}
with open("data.json", 'r') as file:
    data = json.load(file)

@app.route('/health')
def health():
    return jsonify({"status": "it is ok"})

@app.route('/diag')
def diag_check():
    api_url = "https://www.travel-advisory.info/api"
    response = requests.get(api_url)
    api_status = response.json().get('api_status', {})
    return jsonify({"api_status": api_status})

@app.route('/convert/<country_name>')
def convert(country_name):
    for country_code, country_info in data.get('data', {}).items():
        if country_info.get('name') == country_name:
            return jsonify({"country_code": country_code, "country_name": country_name})

    return jsonify({"error": f"Country '{country_name}' not found, please retype."})

if __name__ == '__main__':
    app.run(debug=True)
