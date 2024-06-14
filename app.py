from flask import Flask, render_template, request, jsonify
import backend as backend

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
    results = backend.getMeSomeJuicyAnswers(text)

    print(f"text: {text}")
    print(f"results: {results}")

    return jsonify({'status': 'success', 'results': results})

@app.route('/CVprocessing')
def cv_processing():
    return render_template('CVprocessing.html')

@app.route('/pdf')
def cv_pdf():
    return render_template('pdf_.html')

if __name__ == '__main__':
    app.run(debug=True)
