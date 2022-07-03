from flask import Flask, request, redirect, url_for
from bot import TranslateBot

# from unicodedata import name
# from requests import request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello():
    if request.method == 'POST':
        user = request.form['nm']
        
        return redirect(url_for('success'), name=user)
    return 'Hello World :3'

@app.route('/convert', methods=['POST','GET'])
def convert():
    convert = ''
    if request.method == 'POST':
        data = request.get_json()
        message = data.get('message')

        if message:
            convert = TranslateBot(message).getMsg()
            return { 'message': convert }, 201
        
        return { 'error': 'wrong key value' }, 400
    return { 'error': 'cannot post with empty payload' }, 400

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=3000)