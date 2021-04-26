from flask import Flask, request, render_template,jsonify
from similarity import compute_wer

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/join', methods=['GET','POST'])
def my_form_post():
    text1 = request.form['text1']
    text2 = request.form['text2']
    s = str(compute_wer(text1, text2))+"%"
    print(text1, text2, s)
    result = {
        "Text1": "text1: "+ str(text1),
        "Text2": "text2: "+ str(text2),
        "similarity percentage": "similarity percentage: " +s
    }
    result = {str(key): value for key, value in result.items()}
    
    return jsonify(result=result)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=3000, debug=True)
