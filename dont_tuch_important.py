
from helium import *
import time
import selenium
from bs4 import BeautifulSoup





Path = "C:\Program Files (x86)\chromedriver.exe"


url = "https://www.nasa.gov/press-release/coverage-activities-set-for-first-rollout-of-nasa-s-mega-moon-rocket"

browser = helium.start_chrome(url, headless=False)

driver = helium.get_driver()

driver.get("https://www.nasa.gov/press-release/coverage-activities-set-for-first-rollout-of-nasa-s-mega-moon-rocket")

time.sleep(1)
soup = BeautifulSoup(browser.page_source, 'html.parser')
results = soup.find_all('li',{'class':'ember-view'})




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




    print(time_stamp)
    print(answer)
    print("\n")




