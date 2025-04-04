## 5분마다 한 번씩 서울의 기온을 CSV 형식으로 저장

import requests
import csv
from datetime import datetime
import os ##system fuction// os.mkdir('folder name')하면 폴더 만들어짐

MY_API_KEY = os.getenv('OPENWEATHER_API_KEY')
CITY = 'Seoul'
URL = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={MY_API_KEY}&units=metric"

response = requests.get(URL)
data = response.json()##서울의 기온 하나만 받아오도록
temp = data['main']['temp']### 위에서 접근한 방식 그대로
time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

csv_filename = 'seoul_weather.csv'
header = ['time','temp']

#csv를 만들건데 , 'seoul_weather.csv'가 없다면 생성. 있다면 갱신
file_exist = os.path.isfile(csv_filename)

with open(csv_filename, 'a',newline = '') as file:### 'a'mode = 없으면write, 있으면 쓰기모드로 불러오기  'w'모드는 무조건 덮어쓰기함
    writer = csv.writer(file)

    ##만약 csv가 없었다면, 헤더도 없었던 것
    if not file_exist:
        writer.writerow(header)
    writer.writerow([time, temp])

    print("서울 기온 저장 완료!!")
