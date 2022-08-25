import requests
from flask import Flask,render_template,request,redirect,url_for,session

app = Flask(__name__)

@app.route('/')
def idk():
    return render_template('weather.html')

@app.route('/',methods=['GET','POST'])
def city():
    if request.method == 'POST':
        city = request.form.getlist('variable')
        url = "INSERT API"
        r = requests.get(url.format(city[0])).json()    
        try:
            conditions = {
                'city':city[0],
                'temperature':r['main']['temp'],
                'description':r['weather'][0]['description'],
                'icon':r['weather'][0]['icon']
            }
            submission_successful = True
            icon_link = 'http://openweathermap.org/img/wn/{}@2x.png'
            icon = icon_link.format(conditions.get("icon"))
            return render_template('weather.html',conditions=conditions,submission_successful=submission_successful,icon=icon)
        except:
            return render_template('weather.html')


if __name__ == "__main__":
    app.run(debug=True)

    
