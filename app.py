from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/openInputText')
def open_input_text():
    return render_template('openInputText.html')

@app.route('/handle_input', methods=['POST'])
def handle_input():
    data = request.json
    text = data['text']
    print(f"text: {text}")
    return jsonify({'status': 'success', 'text': text})

@app.route('/CVprocessing')
def cv_processing():
    return render_template('CVprocessing.html')

if __name__ == '__main__':
    app.run(debug=True)
