from flask import Flask, render_template
from bs4 import BeautifulSoup
import requests
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/petrolprices")
def petrolprices():
    now = datetime.now()
    url = "https://www.ndtv.com/fuel-prices/petrol-price-in-all-state"
    response = requests.get(url).text
    soup = BeautifulSoup(response, "html.parser")
    table = soup.find_all("tr")[1:]
    states = []

    for row in table:
        row = list(filter(lambda x: x != "\n", row))
        state_name = row[0].text
        state_price = row[1].text.replace("\u20b9/", "Rs/")
        states.append({"State":state_name,"Price":state_price})

    # return states
    return render_template("prices.html", states = states, date=str(now.date()), time = now.strftime("%H:%M:%S"))

if __name__ == '__main__':
    app.run(debug=True, port=5001)