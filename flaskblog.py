from flask import Flask
app = Flask(__name__)

@app.route('/')
@app.route('/home')
def hello():
    return "Hello MMMM!"

@app.route('/about')
def about():
    return "Hello about!"

if __name__ == '__main__':
    app.run(debug=True)