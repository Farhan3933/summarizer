from flask import Flask, request, jsonify
from flask_cors import CORS
from transformers import pipeline

app = Flask(__name__)
CORS(app)

summarizer = pipeline("summarization", model="iamj33l/my_longer_summarization_model")

@app.route('/summarize', methods=['POST'])
def summarize():

    data = request.json
    text = data.get('text', '')

    if not text:
        return jsonify({'error': 'Text is required'}), 400
    
    summary = summarizer(text)[0]['summary_text']

    return jsonify({'summary': summary})

if __name__ == '__main__':
    app.run(debug=True)
