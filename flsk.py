from flask import Flask, request, jsonify

app = Flask(__name__)

dht11_data = [
    {
        "temperature": 32.80,
        "humidity": 75.00,
        "heat index": 45.01,
        "timestamp": "2024-06-13 22:10:00"
    },
    {
        "temperature": 32.30,
        "humidity": 75.00,
        "heat index": 45.01,
        "timestamp": "2024-06-13 22:20:00"
    },
    {
        "temperature": 33.50,
        "humidity": 75.00,
        "heat index": 45.01,
        "timestamp": "2024-06-13 22:30:00"
    },
]

@app.route('/sensor/dht11', methods=['POST', 'GET'])
def sensor_data():
    try:
        if request.method == 'POST':
            data = request.get_json()
            if not data:
                raise ValueError("No JSON data received")
            dht11_data.append(data)
            return jsonify({'message': 'Data received'})
        if request.method == 'GET':
            return jsonify(dht11_data)
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(port=5000, debug=True)