import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
chrome_options = Options()
chrome_options.add_argument("--headless")
userName = 'username'
passwords = 'password'
driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
driver.get("https://clever.com/oauth/instant-login?client_id=6a4a79f457ee2bf81ea3&district_id=527bac1858c5a34a0c0000d0")
driver.find_element_by_xpath('//*[@id="bySelection"]/div[2]').click()
driver.find_element_by_id('userNameInput').send_keys(userName)
driver.find_element_by_id('passwordInput').send_keys(passwords)
driver.find_element_by_id('submitButton').click()
driver.maximize_window()

a = 'Assignment'
b = 'ActivityName'
print(f"{a : <50} {b : >10}")

for i in range(2,8):
    try:
        Assignment = driver.find_element_by_xpath('/html/body/div[4]/div[1]/div[2]/div[6]/div[2]/div/div/div[3]/div[3]/div/table/tbody/tr[' +str(i)+']/td[1]').text
    except NoSuchElementException:
        if i == 2:
                print(f"All Assignments completed, Congrats")
                break
    else:
        ActivityName = driver.find_element_by_xpath('/html/body/div[4]/div[1]/div[2]/div[6]/div[2]/div/div/div[3]/div[3]/div/table/tbody/tr[' +str(i)+']/td[3]').text
        print(f"{Assignment : <50} {ActivityName : >20}")
