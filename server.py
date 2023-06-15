import os
import openai
from flask import Flask, request, jsonify
from schema_fetch import getSchema
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# API_KEY = os.getenv('API_KEY')
# HOST = os.getenv('HOST')
# DATABASE = os.getenv('DATABASE')
# USER = os.getenv('USER')
# PASSWORD = os.getenv('PASSWORD')

# Set OpenAI API key
# openai.api_key = API_KEY

# Fetch the schema from the database
# schema = getSchema('postgresql+psycopg2://USER:PASSWORD@HOST/DATABASE')

# Define a route to generate text using GPT-3
@app.route('/open-ai/query', methods=['POST'])
def generate_query():
    # Set OpenAI API key
    openai.api_key = request.json['api_key']
    # Fetch the schema from the database
    host = request.json['host']
    conn = 'postgresql+psycopg2://' + user + ':' + password + '@' + host + '/' + database
    schema = getSchema(conn)

    # Get prompt text from request
    prompt = ''.join(schema) + "\n###" + request.json['prompt']
    print(prompt)
    # Set OpenAI API parameters
    model_engine = "code-davinci-002"  # choose a GPT-3 engine
    max_tokens = 512  # maximum number of tokens generated
    temperature = 0  # controls the randomness of the generated text
    stop_sequence = ["#", ";"]  # character sequence to stop text generation
    # Call OpenAI API to generate text
    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=max_tokens,
        temperature=temperature,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        stop=stop_sequence
    )
    # Return generated text in JSON format
    return jsonify({'text': response.choices[0].text})


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=int(os.environ.get('PORT', 5050)))
