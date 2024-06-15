from flask import Flask, request, jsonify, render_template
from backend import getMeSomeJuicyAnswers
from cvToModel import getAnswersFromCV

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/CVprocessing')
def file_input():
    return render_template('CVprocessing.html')  # Template for /fileInput

@app.route('/openInputText')
def openInputText():
    return render_template('new_openInputText.html')  # Your main template


@app.route('/handleText', methods=['POST'])
def handle_input():
    text = request.form['inputText']
    print(f"text: {text}")

    # Process the text using your backend function
    results = getMeSomeJuicyAnswers(text)
    print(f"results: {results}")

    return jsonify({'status': 'success', 'results': results})


@app.route('/handleFilePath', methods=['POST'])
def handle_file_path():
    file_path = request.form['filePath']
    print(f"file_path: {file_path}")

    # Process the file path using your backend function
    procText = getAnswersFromCV(file_path)

    results = getMeSomeJuicyAnswers(procText)
    print(f"results: {results}")

    return jsonify({'status': 'success', 'results': results})


if __name__ == '__main__':
    app.run(debug=True)
