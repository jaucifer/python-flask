from flask import Flask

def wrap_html(greet):
    html = format(greet)
    return html

app = Flask(__name__)

@app.route('/')
def hello_world():
    greet = 'Welcome to CI/CD'
    return html

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
