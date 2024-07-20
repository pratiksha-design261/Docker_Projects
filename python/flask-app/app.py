from flask import Flask, jsonify, render_template

app = Flask(__name__)

@app.route('/status', methods=['GET'])
def status():
    return jsonify({"message": "Server is up and running"}), 200

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

