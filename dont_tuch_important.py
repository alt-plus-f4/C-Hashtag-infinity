import mysql.connector
from helium import *
import time
from bs4 import BeautifulSoup
from datetime import datetime


def remove_html_tags(text):
    """Remove html tags from a string"""
    import re
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)


# format of the date it expects %d%d-%m(3letter word)-%y%y example:11-Jan-22
def date_formatting(date):

    month_list = ["Jan", "Feb", "Mar", "Apr", "May", "June", "Jul", "Aug", "Sep", "Oct", "Noe", "Dec"]

    date_list = date.split("-")
    return_date = int(date_list[2])

    for index in range(len(month_list)):
        if month_list[index] == date_list[1]:
            return_date = return_date * 100 + index + 1

    return_date = return_date * 100 + int(date_list[0])
    return return_date


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
               "(title,date,data,link)"
               "values(%s,%s,%s,%s)")

    my_cursor.execute(command, data)
    db.commit()

    '''
    # fetching the data from query
    my_cursor.execute("SELECT * FROM data")

    for i in my_cursor:
        print(i)'''

    # sorts table by dates
    command = ("SELECT * FROM `data` WHERE 1 ORDER BY date Desc")

    my_cursor.execute(command)


def get_news(my_dates, news_dict):

    for i in range(0,6):
        url = news_dict[my_dates[i]]

        browser = helium.start_chrome(url, headless=False)

        time.sleep(1)
        soup = BeautifulSoup(browser.page_source, 'html.parser')
        results = BeautifulSoup(str(soup.find_all('div', {'class': 'text'})), 'html.parser').find_all('p')

        results = str(results)
        end_point = results.find("-end-")
        results = results[:end_point]

        results = remove_html_tags(str(results))
        results = results.replace(", , ", "")

        title = url.split('/')
        title = title[len(title) - 1].replace("-", " ")
        date = date_formatting(my_dates[i])

        write_to_sql((title, date, results, url))

        '''print(title)
        print(date)
        print(results)
        print(url)
        print("---------------------------------------------------------------------")
        '''


def load_news():

    url = "https://www.nasa.gov/press-release/coverage-activities-set-for-first-rollout-of-nasa-s-mega-moon-rocket"
    default_url = "https://www.nasa.gov"

    # headless should be True in the finished versionn
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

    # scraping the news from the provided links
    get_news(my_dates, news_dict)


load_news()
