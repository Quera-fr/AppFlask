from flask import Flask, render_template, request
import warnings, time


def date_time():
    day = time.localtime().tm_mday
    month = time.localtime().tm_mon
    year = time.localtime().tm_year
    return f'{day}/{month}/{year}'


date = date_time()
warnings.filterwarnings('ignore')

app = Flask(__name__)

# Page d'acceuil
@app.route('/', methods=['GET'])
def app_home():
    return render_template("index.html", date=date)


# Page d'action
@app.route('/submit/', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        try:
            img_url = request.form['input_text']
            return render_template("submit.html", img=img_url, prediction='Chat', accuracy='45')       
        except:
            return render_template("submit.html")


app.run(host="0.0.0.0", port=8000)