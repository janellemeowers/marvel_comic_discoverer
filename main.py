import requests
from datetime import datetime
import hashlib
import random
from flask import Flask, render_template, request, redirect, url_for, flash
import os
#intall python-dotenv in terminal
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] =os.getenv('FLASK_KEY')


URL = "https://gateway.marvel.com/v1/public/"

PUBLIC_KEY =os.getenv('M_PUBLIC')

API =os.getenv('M_API')

#current time
dt = datetime.now()

#timestamp
ts = datetime.timestamp(dt)

data = f"{ts}{API}{PUBLIC_KEY}"

hashm5 = hashlib.md5(data.encode()).hexdigest()


global comics_data, max


@app.route('/', methods=["GET", "POST"])
def home():
    global comics_data, max
    if request.method == 'POST':
        hero = request.form.get("hero").lower()
        response = requests.get(URL + f"characters?nameStartsWith={hero}&ts={ts}&apikey={PUBLIC_KEY}&hash={hashm5}")
        char = response.json()['data']['results']

        if response.json()['data']['count'] == 0:
            flash("No character found, try again.", "error")
            return redirect(url_for('home'))

        comics = char[0]['comics']['available']
        print(comics)

        # get by ID request
        if comics > 10:
            # go with first option
            sh = char[0]
        else:
            # go with second
            sh = char[1]

        heroId = sh["id"]

        # find limit of results
        if comics < 100:
            max = comics
        elif comics > 100:
            max = 100

        comics_res = requests.get(
            URL + f"/characters/{heroId}/comics?limit={max}&ts={ts}&apikey={PUBLIC_KEY}&hash={hashm5}")
        comics_data = comics_res.json()['data']['results']

        return redirect(url_for('get_result'))

    return render_template("index.html")



@app.route("/result", methods=["GET", "POST"])
def get_result():
    num = random.randint(0, max)
    comic = comics_data[num]
    title = comic['title']
    des = comic['description']
    url = comic['urls'][0]['url']

    image_path = comic['images'][0]['path']
    img_ext = comic['images'][0]['extension']
    image = f"{image_path}.{img_ext}"

    #Go Again and Back Buttons
    if "again" in request.form:
        return redirect(url_for("get_result"))
    elif "back" in request.form:
        return redirect(url_for("home"))

    return render_template("result.html", title=title, des=des, url=url,image=image )


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5004)