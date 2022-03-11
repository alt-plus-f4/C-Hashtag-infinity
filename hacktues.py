import mysql.connector

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
