from flask import Flask

def wrap_html(greet):
    html = greet
    return html

app = Flask(__name__)

@app.route('/')
def hello_world():
    greet = 'Welcome to CI/CD'
    html = wrap_html(greet)
    return html

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
