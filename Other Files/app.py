from flask import Flask, request, render_template


app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('upload.html')

@app.route('/', methods=['POST','GET'])
def my_form_post():
    if request.method == "POST":
        source = request.form['source']
        target = request.form['target']
        source_processed = source.upper()
        target_processed = target.upper()
        return {"source":source_processed,
        "target":target_processed}
        
    return render_template('upload.html')


if __name__ == "__main__":
    app.run(port=5000,debug=True)