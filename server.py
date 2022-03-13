import requests
import json
import mysql.connector
from bs4 import BeautifulSoup
from helium import *
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS, cross_origin
from daily_news import NasaApi

db = mysql.connector.connect(
    # host should be changed to the address of the sqlserver
    host="localhost",
    # port is changed from default
    port=3306,
    # user should be client_server
    # user should have read/write permissions  to the tale
    user="client_server",
    # database should hold the database name
    database="hacktues"

)
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

fp = open("static\jsons\mars.json", "r", encoding='utf-8')
planet_data = json.load(fp)

fp.close()

my_cursor = db.cursor()

# fetching the data from query
my_cursor.execute("SELECT * FROM data")

database_dict = {}
database_list = []

for i, el in enumerate(my_cursor):
    if i == 6:
        break

    database_dict["title"] = el[0]
    database_dict["data"] = el[2]
    database_dict["link"] = el[3]
    database_dict["description"] = el[4]

    database_list.append(database_dict)
    database_dict = {}

print(database_list)


@app.route("/", methods=['GET'])
@cross_origin()
# TODO get the values from the database
def index(mylist=database_list):
    return render_template("index.html",
                           title0=mylist[0]["title"], data0=mylist[0]["description"], link0=mylist[0]["link"],
                           title1=mylist[1]["title"], data1=mylist[1]["description"], link1=mylist[1]["link"],
                           title2=mylist[2]["title"], data2=mylist[2]["description"], link2=mylist[2]["link"],
                           title3=mylist[3]["title"], data3=mylist[3]["description"], link3=mylist[3]["link"],
                           title4=mylist[4]["title"], data4=mylist[4]["description"], link4=mylist[4]["link"],
                           title5=mylist[5]["title"], data5=mylist[5]["description"], link5=mylist[5]["link"])


@app.route("/entertainment")
@cross_origin()
def entertainment():
    return render_template("calculator.html")


@app.route("/solar_system")
@cross_origin()
def solar_system():
    # return render_template("solar_system.html", title=data["title"], content=data["content"], img=data["img"])
    return render_template("solar_system.html")


@app.route("/about")
@cross_origin()
def about():
    return render_template("about.html")


'''
@app.route("/search", methods=['GET'])
@cross_origin()
def search_page(all_searches=[]):
    # TODO Errors
    return render_template("search_page")
'''


@app.route('/articles', methods=['GET'])
@cross_origin()
def articles():
    result = []
    input_str = request.args.get("search")

    req = requests.get(
        f"https://nasasearch.nasa.gov/search/news?affiliate=nasa&channel=1616&query={input_str}&sort_by=r")
    answers = BeautifulSoup(req.text, features="html.parser").find_all(class_="content-block-item result")

    for answer in answers:
        title = answer.find("h4", {"class": "title"}).find("a")
        link = title["href"]
        description = answer.find("span", {"class": "description"}).text.strip()
        # img = "https://www.northropgrumman.com/wp-content/uploads/space-facebook.jpg"
        result.append({"title": title.text.strip(), "description": description, "link": link})

    return index(result)


@app.route('/article', methods=['GET'])
@cross_origin()
def article_by_url():
    result = {}
    input_url = request.args.get("url")

    browser = helium.start_chrome(input_url, headless=True)
    html = browser.page_source
    answer = BeautifulSoup(html, features="html.parser")

    text = ""
    title = ""
    img = ""

    if "nasa.gov" in input_url:
        title = answer.find("h1", {"class": "title"}).text
        img = "https://nasa.gov" + answer.find("div", {"class": "dnd-drop-wrapper"}).find("img")["src"]
        text_list = answer.find("div", {"class": "text"}).find_all("p")

        text = ""
        for texts in text_list:
            if "<strong>" not in str(texts):
                text += texts.text
            else:
                break

    else:
        title = answer.find("h1", {"class": "post-title"}).text
        img = answer.find("figure", {"class": "featured wp-caption"}).find("img")["src"]
        text_list = answer.find("div", {"class": "tablet-wrapper"}).find_all("p")

        text = ""
        for texts in text_list:
            text += texts.text

    result = {"title": title, "img": img, "data": text}

    return render_template("test_search.html", content=result["data"], title=result["title"], img=result["img"])


@app.route('/solar_system/article', methods=['GET'])
@cross_origin()
def article_by_planet():
    input_id = request.args.get("id")

    if 0 <= int(input_id) <= 7:
        return render_template("test_search.html", content=planet_data[input_id]["data"],
                               title=planet_data[input_id]["title"], img=planet_data[input_id]["img"])
    else:
        return "L"


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
