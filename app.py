from flask import Flask, jsonify, request
import requests  # Para realizar solicitudes HTTP

app = Flask(__name__)

@app.route('/flask', methods=['GET'])
def flask_endpoint():
    # Ejemplo: consulta al servicio Express.js
    express_url = "http://express-service-url/api/express"
    express_response = requests.get(express_url)
    
    # Procesar respuesta de Express.js
    if express_response.status_code == 200:
        data = express_response.json()
        return jsonify({"from_flask": "Hello from Flask!", "express_data": data})
    else:
        return jsonify({"error": "Failed to connect to Express.js"}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
