import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

youtube = input('Do you want to search a channel or a video?: ')
youtube = youtube.lower()
y1, y2 = False, False

if youtube == 'channel' or youtube == 'youtuber':
    youtube1 = input('what channel or youtuber?: ')
    y1 = True
else:
    youtube2 = input('what video topic?: ')
    y2 = True
driver = webdriver.Chrome(ChromeDriverManager().install())


def onYoutube():
    driver.get('https://www.youtube.com/')
    driver.maximize_window()


def channel():
    onYoutube()
    a = driver.find_element_by_xpath("//input[@id='search']")
    a.send_keys(youtube1)
    a.submit()
    driver.find_element_by_xpath('//*[@id="avatar-section"]/a').click()


def video():
    onYoutube()
    a = driver.find_element_by_xpath("//input[@id='search']")
    a.send_keys(youtube2)
    a.submit()


if y1:
    channel()
elif y2:
    video()
