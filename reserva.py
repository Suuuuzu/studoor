import sys
sys.path.append('/usr/local/lib/python3.6/site-packages')
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import urllib.request
from urllib.parse import urljoin
import time
import re
import mysql.connector
from datetime import datetime

def main():
    
    options = Options()

    # Headlessモードを有効にする（コメントアウトするとブラウザが実際に立ち上がります）
    options.set_headless(True)
    
    driver = webdriver.Chrome('/usr/local/bin/chromedriver',  chrome_options=options)

    # url = "https://reserva.be/kandaong"
    # data = urllib.request.urlopen(url)
    # soup = BeautifulSoup(data, "lxml")

    # room_urls = []
    # #部屋毎の詳細リンクを取得
    # for el in soup.find_all("a", class_="btn decision"):   
    #     room_url = el.get("onclick")
    #     room_url = re.search(r"href=\'.+\'", room_url).group()[7:-1]
    #     room_urls.append(room_url)
    
    # print(room_urls)

    url = "https://reserva.be/kandaong/reserve?mode=service_staff&search_evt_no=3eeJwzMjAzNgEAAvsBAA"
    data = urllib.request.urlopen(url)
    soup = BeautifulSoup(data, "lxml")

    driver.get(url)
    # 日にちを指定し時間単位の予約状況を確認
    driver.find_element_by_id('calendar_day_20200220').click()

    #空室状況カレンダーのtable取得
    table = driver.find_elements_by_class_name("week")[0]
    thead = table.find_elements(By.TAG_NAME, "thead")
    #　日付一覧
    days = thead[0].find_elements_by_class_name("thday_date")
    line = "      "
    #　選択した日付のみ取得
    for j in range(0,1):
        line += days[j].text
        line += "   "

    print(line)

    tbody = table.find_elements(By.TAG_NAME, "tbody")

    # 選択した日付の時間単位の空室状況を取得
    base_id = "isd_20200220_"    
    for i in range(6,24):
        time = str(i)
        #時間のidを設定
        #時間毎にfind_idで見つかれば空室、そうでなければ予約ずみ
        if i < 10:
            full_time = "0" + time + "00"
            reserv_id = base_id + full_time
            if tbody[0].find_elements_by_id(reserv_id):
                print(full_time + "   ○")
            else:
                print(full_time + "   ×")
        else:
            full_time = time + "00"        
            reserv_id = base_id + full_time 
            if tbody[0].find_elements_by_id(reserv_id):
                print(full_time + "   ○")
            else:
                print(full_time + "   ×")       
    
    driver.close()
    driver.quit()

if __name__ == '__main__':
    main()

