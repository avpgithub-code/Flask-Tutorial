from flask import Flask,request,jsonify,make_response

app = Flask(__name__)

@app.route('/')
def index():
    return "<h2>Hellow World<h2>"

@app.route('/hello', methods=['GET','POST'])
def hello():
    if request.method == 'GET':
        return "Hello GET World\n",200
    elif request.method == 'POST':
        return "Hellow POST World\n"
    else:
        pass

@app.route('/greet/<name>')
def greeet(name):
    return f"Hello, {name}"

@app.route('/handle_url_params')
def handle_params():
    if ('greeting' in request.args.keys()) and ('name' in request.args.keys()):
        greeting = request.args['greeting']
        name = request.args['name']
        return f"{greeting}, {name}! How are you!!"
    else:
        return f"Missing Some Parameters"



if __name__ == '__main__':
    app.run(host='127.0.0.1',port=5000,debug=True)