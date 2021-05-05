from flask import Flask ,render_template , request
from flask_uploads import UploadSet, configure_uploads, IMAGES
from flask_cors import CORS, cross_origin
from document_similarity import predict

app = Flask(__name__)
cors = CORS(app,resources={r"/upload/*": {"origins":"*"}})
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/home',methods=['GET','POST'])
def home():
    welcome = "Hey People!"
    return welcome

@app.route('/upload',methods=['GET','POST'])
@cross_origin()
def upload():
    if request.method == 'POST':
        
        prediction = predict(source_doc,target_docs)
        answer = "Score: ".format(prediction['sim_score'])

        return answer

    return render_template('upload.html')


if __name__ == "__main__":
    app.run(port=5000,debug=True)