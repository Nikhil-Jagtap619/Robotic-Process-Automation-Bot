from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
path = "C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(path)
driver.get('https://www.youtube.com/')
time.sleep(3)

search = driver.find_element_by_name('search_query')
search.send_keys('Muhuhaha')
search.send_keys(Keys.RETURN)
time.sleep(3)

select = driver.find_element_by_xpath('//*[@id="avatar-section"]/a')
select.send_keys(Keys.RETURN)
time.sleep(3)

videoTitle = driver.find_elements_by_id('scroll-container')
array = list()
for title in videoTitle:
    titleArr = title.text.split("\n")
    array.extend(titleArr)
array.pop(0)
print(array)
for name in array:
    for i in range(10):
        if (name[0] == str(i)) or (name[-1:-4]=="ago"):

            array.remove(name)

for i in range(0,len(array),2):
    for j in range(1,len(array),2):
        print(array[i], array[j])
        break




driver.close()


