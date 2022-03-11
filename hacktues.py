import requests
from bs4 import BeautifulSoup
import mysql.connector
from urllib.request import Request,urlopen
import lxml.html



# getting list with news links

link = "https://www.esa.int/Science_Exploration/Human_and_Robotic_Exploration/Orion/The_making_of_the_European_Service_Modules"

req = Request(link, headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()

with requests.Session() as c:
    soup = BeautifulSoup(webpage, 'lxml')


response = requests.post(link)
tree = lxml.html.fromstring(response.text)
print(response.text)















db = mysql.connector.connect(
    # host should be changed to the adress of the sqlserver
    host="localhost",
    # port is changed from default
    port=3305,
    # user should be client_server
    user="client_server",
    database="hacktues_test"

)

my_cursor = db.cursor()

# adding new info to the data table in thee query
command = ("INSERT INTO data" 
           "(title,date,data)"
           "values(%s,%s,%s)")

# data to e pushed to the query
data = ("test_2",123456,"data_2")

my_cursor.execute(command, data)
db.commit()

# fetching the data from query
my_cursor.execute("SELECT * FROM data")

for i in my_cursor:
    print(i)
