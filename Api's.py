import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

search = input('What do you want to search?:')
userName = 'username'
passwords = 'password'
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://clever.com/oauth/instant-login?client_id=49df5998bd885075875d&district_id=527bac1858c5a34a0c0000d0')
driver.maximize_window()
driver.find_element_by_xpath('//*[@id="bySelection"]/div[2]').click()
driver.find_element_by_id('userNameInput').send_keys(userName)
driver.find_element_by_id('passwordInput').send_keys(passwords)
driver.find_element_by_id('submitButton').click()
driver.find_element_by_id('active_class').click()
driver.find_element_by_xpath('//*[@id="active_class"]/option[3]').click()
driver.find_element_by_xpath('//*[@id="location_selector"]/p[2]/label/input').click()
driver.find_element_by_id("loginButton").click()


driver.find_element_by_xpath('//*[@id="a3k-app-container"]/div/nav/div[3]/div[6]/div/span[1]').click()
searcher = driver.find_element_by_xpath('//*[@id="a3k-app-container"]/div/nav/div[3]/div[5]/form/input[1]')
searcher.send_keys(search)
searcher.submit()
print('complete')
