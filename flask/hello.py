from flask import Flask
from flask import request
from flask import redirect
app=Flask(__name__)

@app.route('/')
def main_page():
    user_agent = request.headers.get('User-Agent')
    return 'Your browser is <h1>%s</h1>' % user_agent

@app.route('/<name>')
def links(name):
    return redirect('http://www.google.com')

if __name__ == '__main__':
    app.run(debug=True)
