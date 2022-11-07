from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

driver_path = "./chromedriver"
service = Service(executable_path=driver_path)
browser = webdriver.Chrome(service=service)

#webサイトにアクセス
browser.get('https://scraping-for-beginner.herokuapp.com/ranking/')
time.sleep(2)

#観光地名の取得
elem_rankingBox = browser.find_element(By.CLASS_NAME,'u_areaListRankingBox')
elem_title = elem_rankingBox.find_element(By.CLASS_NAME,'u_title')
title = elem_title.text.split('\n')[1]
print(title)

#総合評価の取得
elem_rank = browser.find_element(By.CLASS_NAME,('u_rankBox'))
elem_rank = elem_rank.find_element(By.CLASS_NAME),('evaluateNumber')
elem_rank.text
print(elem_rank)

#各項目の評価を取得