from flask import Flask, redirect

app = Flask(__name__)


@app.route('/')
def redir():
    return redirect("https://github.com/elizabeth-c-chen")
    

if __name__ == '__main__':
    app.run(port=8050)