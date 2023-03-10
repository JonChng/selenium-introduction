from selenium import webdriver
from selenium.webdriver.common.by import By


chromedriver_path = "/Users/jonathanchng/Downloads/chromedriver_mac64/chromedriver"
driver = webdriver.Chrome(chromedriver_path)

driver.get("https://www.python.org/")

content = driver.find_element(By.XPATH,'//*[@id="content"]/div/section/div[2]/div[2]/div/ul')
items = content.find_elements(By.TAG_NAME,"li")

count = 0
events = {}

for item in items:

    time = item.find_element(By.TAG_NAME, "time").text
    event = item.find_element(By.TAG_NAME, "a").text
    data = {
        'time':time,
        'event':event
    }

    events[count] = data

    count += 1

print(events)

driver.close()


