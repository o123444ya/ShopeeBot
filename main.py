import schedule
import time
import requests
from datetime import datetime, timedelta

def task():
    print(f"執行中...\n\t目前時間:{datetime.now()}")
    r=requests.post(
        'https://seller.shopee.tw/api/v3/product/boost_product/?version=3.1.0&SPC_CDS=7d236e58-2532-441f-a1be-1050a13a04e5&SPC_CDS_VER=2',
       json={
         'id': 00000#自己抓包取得id <3
       },
       headers={
         'cookie':''#誰把餅乾丟這邊了? 不用分我吃吃嗎
       }
    )
    print(r.text)
print('開始運行')

task() #別問我為啥 初始化就對了

now = datetime.now()
next_hour = (now + timedelta(hours=1)).replace(minute=0, second=0)
delay = (next_hour - now).seconds

time.sleep(delay)

# 每隔240分鐘運行一次
schedule.every(240).minutes.do(job)
while True:
    schedule.run_pending()
    time.sleep(1)
