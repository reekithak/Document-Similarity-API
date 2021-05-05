from flask import Flask, request, render_template


app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('upload.html')

@app.route('/type', methods=['POST','GET'])
def my_form_post():
    if request.method == "POST":
        text = request.form['source']
        processed_text = text.upper()
        return processed_text
    return render_template('upload.html')


if __name__ == "__main__":
    app.run(port=5000,debug=True)