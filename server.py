import requests
from bs4 import BeautifulSoup
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/articles', methods=['GET'])
@cross_origin()
def articles():
    result = []
    input_str = request.args.get("search")

    req = requests.get(
        f"https://nasasearch.nasa.gov/search/news?affiliate=nasa&channel=1616&query={input_str}&sort_by=r")
    answers = BeautifulSoup(req.text, features="html.parser").find_all(class_="content-block-item result")
    # titles = answers.find_all("")

    for answer in answers:
        title = answer.find("h4", {"class": "title"}).find("a").text
        description = answer.find("span", {"class": "description"}).text
        link = answer.find("h4", {"class": "title"}).find("a")["href"]
        result.append({"title": title, "description": description, "link": link})

    return jsonify(result)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
