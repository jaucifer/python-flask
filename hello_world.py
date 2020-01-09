from flask import Flask

app = Flask(__name__)

def wrap_html(greet):
    html = """
        <html>
        <body>
            <div style='font-size:80px;'>
            <center>
                <image height="600" width="531" src="https://secure.meetupstatic.com/photos/event/2/a/a/3/600_452110915.jpeg">
                <br>
                {0}<br>
            </center>
            </div>
        </body>
        </html>""".format(greet)
    return html

@app.route('/')
def hello_world():
    greet = 'Welcome to CI/CD'
    html = wrap_html(greet)
    return html

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
