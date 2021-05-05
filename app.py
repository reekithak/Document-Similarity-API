from flask import Flask ,render_template , request
from flask_uploads import UploadSet, configure_uploads, IMAGES
from flask_cors import CORS, cross_origin
from document_similarity import predict

app = Flask(__name__)
cors = CORS(app,resources={r"/upload/*": {"origins":"*"}})
app.config['CORS_HEADERS'] = 'Content-Type'
model_path = r'Models\GoogleNews-vectors-negative300.bin'

@app.route('/')
def my_form():
    return "NULL-Navigate"

@app.route('/home',methods=['GET','POST'])
def home():
    welcome = "Hey People!"
    return welcome

@app.route('/upload',methods=['GET','POST'])
@cross_origin()
def upload():
    
    if request.method == "POST":
        source = request.form['source']
        target = request.form['target']
        source = source.lower()
        target = target.lower()

        prediction = predict(source,[target],model_path)
        answer = "Score: {}".format(prediction)

        return answer

    return render_template('upload.html')


if __name__ == "__main__":
    app.run(port=5000,debug=True)