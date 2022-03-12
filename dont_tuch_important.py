import mysql.connector
from helium import *
import time
from bs4 import BeautifulSoup
from datetime import datetime


def write_to_sql(data):
    db = mysql.connector.connect(
        # host should be changed to the address of the sqlserver
        host="localhost",
        # port is changed from default
        port=3305,
        # user should be client_server
        # user should have read/write permissions  to the tale
        user="client_server",
        # database should hold the database name
        database="hacktues_test"

    )

    my_cursor = db.cursor()

    # adding new info to the 'data' table in the query
    # change data to name of table
    command = ("INSERT INTO data"
               "(title,date,data)"
               "values(%s,%s,%s)")

    my_cursor.execute(command, data)
    db.commit()

    # fetching the data from query
    my_cursor.execute("SELECT * FROM data")

    for i in my_cursor:
        print(i)


def load_news():

    url = "https://www.nasa.gov/press-release/coverage-activities-set-for-first-rollout-of-nasa-s-mega-moon-rocket"
    default_url = "https://www.nasa.gov"

    browser = helium.start_chrome(url, headless=False)

    time.sleep(1)
    soup = BeautifulSoup(browser.page_source, 'html.parser')
    results = soup.find_all('li', {'class': 'ember-view'})

    news_dict = dict()
    my_dates = list()
    for i in results:
        i = str(i)

        begining = i.find("href=")
        begining += 6
        answer = str()
        time_stamp = str()

        if begining > 0:
            while i[begining] != "\"":
                answer += i[begining]
                begining += 1

        begining = i.find("title=")
        begining += 7

        if begining > 0:
            while i[begining] != "\"":
                time_stamp += i[begining]
                begining += 1

        # formatting of dates don't touch
        list_times = time_stamp.split(" ")
        time_stamp = list_times[1].replace(",", "") + "-" + list_times[0] + "-" + list_times[2].replace("20", "")

        # my dates is list with keys for news_dict
        my_dates.append(time_stamp)
        news_dict[time_stamp] = default_url + answer

        # sorting dates recently first
        my_dates.sort(key=lambda date: datetime.strptime(date, "%d-%b-%y"))
        my_dates.reverse()





write_to_sql(("test_3", 123456, "data_3"))
