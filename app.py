# == Your Routes Here ==


# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.

import os
from flask import Flask, request

# Create a new Flask app
app = Flask(__name__)

@app.route('/hello', methods=['GET'])
def get_hello():
    return 'Hello!'

@app.route('/submit', methods=['POST'])
def post_submit():
    name = request.form['name']
    message = request.form['message']
    return f'Thanks {name}, yout send this message: "{message}"'

@app.route('/wave', methods=['GET'])
def get_wave():
    name = request.form['name']
    return f'I am waving at {name}'

@app.route('/count_vowels', methods=['POST'])
def post_count_vowels():
    text = request.form['text']
    vowel_num = 0
    for letter in text:
        if letter in "aeiou":
            vowel_num +=1
    return f'There are {vowel_num} vowels in "{text}"'

@app.route('/sort-names', methods=['POST'])
def post_sort_name():
    names = request.form['names'].split(',')
    sorted_names = sorted(names)
    return ','.join(sorted_names)

@app.route('/return_names', methods=['POST'])
def post_add_name():
    names = request.form['names'].split(',')
    add_name = request.form['add_name']
    names.append(add_name)
    return ', '.join(names)


if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))

