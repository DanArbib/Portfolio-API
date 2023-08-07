import openai
from ..conf import *
import os


def generate_answer(question: str) -> str:
    '''
    Calls the OpenAI API to generate an answer based on the input question.
    :param question: The input question for which the answer is to be generated.
    :return: A string response containing the generated answer.
    '''

    # Openai init key
    openai.api_key = os.environ.get('OPENAI_API_KEY')

    if len(question) < 1:
        return ''

    if len(question) < 5:
        return f'-- {SHORT_QUESTION_MSG}'

    if len(question) > 200:
        return f'-- {LONG_QUESTION_MSG}'

    prompt = f'''If the following QUESTION is related to Python code, give a short answer.
                 If it is not related to Python code, respond back with only
                 the two letters "NO". QUESTION: {question}.'''

    response = openai.Completion.create(model="text-davinci-003", prompt=prompt, temperature=0, max_tokens=400)
    answer = response['choices'][0]['text'].replace('!', '').replace('"', '', )

    # Filter none related questions
    if len(answer) < 10 or answer.lower() == 'no':
        return f'-- {NONE_RELATED_QUESTION_MSG}'

    return f'-- {answer}'

