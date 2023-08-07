from app import app
from .scripts.gpt import generate_answer
from flask import jsonify, request

@app.route("/api/questions", methods=['POST'])
def data():
    '''
    Handles incoming POST requests containing questions and generates answers using gpt.
    :return: A JSON response containing the generated answer.
    '''

    if request.method == 'POST':

        # Extract the 'question' data from the JSON payload
        question = request.json.get('question')

        # Call gpt to generate the answer
        answer = generate_answer(question)

        return jsonify({f'response': answer})





