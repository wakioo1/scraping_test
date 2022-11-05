#import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import csv
import pprint
import pandas as pd

#weddriverの作成
driver_path = "./chromedriver"
service = Service(executable_path=driver_path) #executable_pathを指定
browser = webdriver.Chrome(service=service) #serviceを渡す

#webサイトにアクセス
browser.get('https://scraping-for-beginner.herokuapp.com/login_page')
time.sleep(2)

#ユーザー名の入力
elem_username = browser.find_element(By.ID,'username')
elem_username.send_keys('imanishi')
time.sleep(2)

#パスワードの入力
elem_password = browser.find_element(By.ID,'password')
elem_password.send_keys('kohei')
time.sleep(2)

#ログインボタンのクリック
elem_login_btn = browser.find_element(By.ID,'login-btn')
elem_login_btn.click()
time.sleep(2)

#テキストデータの取得(1項目ごと'ID要素')
elem = browser.find_element(By.ID,('name'))
name = elem.text
print(name)
time.sleep(2)

elem_hobby = browser.find_element(By.ID,('hobby'))
hobby = elem_hobby.text
hobby.replace('\n',',')
print(hobby)
time.sleep(2)

#１活で取得
elems_th = browser.find_elements(By.TAG_NAME,('th'))
keys = []
for elem_th in elems_th:
    key = elem_th.text
    keys.append(key)
print(keys)
time.sleep(2)

elems_td = browser.find_elements(By.TAG_NAME,('td'))
values = []
for elem_td in elems_td:
    value = elem_td.text.replace('\n','・')
    values.append(value)
print(values)
time.sleep(2)

#CSV形式での抽出
df = pd.DataFrame()
df['項目'] = keys
df['値'] = values
#df.to_csv('test.csv')
df.to_csv('app_test.csv', index=False)