import requests
from bs4 import BeautifulSoup


def search(input_str):
    req = requests.get(f"https://nasasearch.nasa.gov/search/news?affiliate=nasa&channel=1616&query={input_str}&sort_by=r")
    answers = BeautifulSoup(req.text, features="html.parser").find(class_="results-wrapper").prettify()
    print(answers)
    return answers


with open("test_search.html", "w") as fp:
    fp.write('<!DOCTYPE html><html lang="en"><body>')
    fp.write(search("mars"))
    fp.write('</body></html>')

