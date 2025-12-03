from flask import Flask, jsonify, request

app = Flask(__name__)

tasks = []

@app.route('/')
def home():
    return jsonify({"message": "TaskManager API v1.0", "status": "running"})

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify({"tasks": tasks})

@app.route('/tasks', methods=['POST'])
def add_task():
    task = request.json
    tasks.append(task)
    return jsonify({"message": "Task added", "task": task}), 201
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3000)  # Cambio en feature
# if __name__ == '__main__':
#     app.run(debug=True, host='0.0.0.0', port=5000)
```

**`requirements.txt`**:
```
flask==3.0.0
pytest==7.4.3