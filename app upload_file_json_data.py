from flask import Flask,request,jsonify,make_response,render_template,\
    redirect,url_for,redirect,Response,send_from_directory
import pandas as pd
import os,sys,uuid
# =============================================================================================
app = Flask(__name__,template_folder='templates')
# =============================================================================================
@app.route('/',methods=['GET','POST'])
# =============================================================================================
def index():
    # ---------------------------------------------------------------------------
    if request.method == 'GET':
    # ---------------------------------------------------------------------------
        return render_template('index.html')
    # ---------------------------------------------------------------------------
    elif request.method == 'POST':
        # ---------------------------------------------------------------------------
        username = request.form['username']
        password = request.form['password']
        if username == 'username' and password == 'password':
            return 'Success'
        else:
            return 'Failure'
# =============================================================================================
@app.route('/file_upload', methods=['POST'])
# =============================================================================================
def file_upload():
    file = request.files['file']
    if (file.content_type == 'text/plain') or (file.content_type == 'text/csv'):
        return file.read().decode()
    elif (file.content_type == 'application/vnd.ms-excel') or \
          (file.content_type == 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'):
          df = pd.read_excel(file)
          return df.to_html()
# =============================================================================================
@app.route('/convert_csv',methods=['POST'])
# =============================================================================================
def convert_csv():
    file = request.files['file']
    df = pd.read_excel(file)
    response = Response(
        df.to_csv(),
        mimetype='text/csv',
        headers={
            'Content-Disposition': 'attachment; filename=result.csv'
        }
    )
    return response
# =============================================================================================
@app.route('/convert_csv_two', methods=['POST'])
def convert_csv_two():
    file = request.files['file']
    df = pd.read_excel(file)
    if not os.path.exists('downloads'):
        os.makedirs('downloads')
    filename = f'{uuid.uuid4()}.csv'
    df.to_csv(os.path.join('downloads',filename))
    return render_template('download.html',filename=filename)

@app.route('/downloads/<filename>')
def download(filename):
    return send_from_directory('downloads',filename,download_name='result.csv')

@app.route('/handle_json',methods=['POST'])
def handle_json():
    greeting = request.json['greeting']
    name = request.json['name']
    
    with open('file_txt','w') as f:
        f.write(f'{greeting}, {name}')
        
    return jsonify({'message': 'Successfully written!'})
# =============================================================================================
if __name__ == '__main__':
# =============================================================================================
    app.run(host='127.0.0.1',port=5000,debug=True)