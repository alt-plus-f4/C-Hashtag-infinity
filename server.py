import requests
import json
from bs4 import BeautifulSoup
from helium import *
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route("/")
@cross_origin()
def index():
    return render_template("index.html")


@app.route("/news")
@cross_origin()
def news():
    return render_template("news.html")


fp = open("static\jsons\mars.json")

data = json.load(fp)
fp.close()
# print(data["img"])


@app.route("/solar_system")
@cross_origin()
def solar_system():
    return render_template("solar_system.html", title=data["title"], content=data["content"], img=data["img"])


@app.route("/about")
@cross_origin()
def about():
    return render_template("about.html")


@app.route("/search", methods=['GET'])
@cross_origin()
def search_page(all_searches=[]):
    # TODO Errors
    return render_template()


@app.route('/articles', methods=['GET'])
@cross_origin()
def articles():
    result = []
    input_str = request.args.get("search")

    req = requests.get(
        f"https://nasasearch.nasa.gov/search/news?affiliate=nasa&channel=1616&query={input_str}&sort_by=r")
    answers = BeautifulSoup(req.text, features="html.parser").find_all(class_="content-block-item result")

    for answer in answers:
        title = answer.find("h4", {"class": "title"}).find("a").text
        description = answer.find("span", {"class": "description"}).text
        link = answer.find("h4", {"class": "title"}).find("a")["href"]
        result.append({"title": title, "description": description, "link": link})

    return jsonify(result)


@app.route('/article', methods=['GET'])
@cross_origin()
def article_by_url():
    result = {}
    input_url = request.args.get("url")

    browser = helium.start_chrome(input_url, headless=True)
    html = browser.page_source
    # soup = BeautifulSoup(html, 'lxml')
    #
    # a = soup.find('section', 'wrapper')
    # req = requests.get(input_url)
    answer = BeautifulSoup(html, features="html.parser")
    title = answer.find("h1", {"class": "title"}).text
    print(title)
    # print(answer)

    return result


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
