# 샌프란 시스코
# 샌프란 시스코의 기온은 시트카나 데스 밸리 중 어느 쪽에 가까울까요?
# 샌프란 시스코 데이터를 내려받아 최고 기온과 최저 기온 그래프를 만드세요.

# sitka_weather_2018_full.csv
# "STATION","NAME","DATE","AWND","PGTM","PRCP","SNWD","TAVG","TMAX","TMIN","WDF2","WDF5","WSF2","WSF5","WT01","WT02","WT04","WT05","WT08"

# death_valley_2018_full.csv
# "STATION","NAME","DATE","PRCP","SNOW","SNWD","TMAX","TMIN","TOBS"

import pandas as pd
import matplotlib.pyplot as plt

# 데이터 파일 경로
sitka_data_file = "c:\\Python\\CH01\\16\\sitka_weather_2018_full.csv"
death_valley_data_file = "c:\\Python\\CH01\\16\\death_valley_2018_full.csv"

# 데이터 불러오기
sitka_data = pd.read_csv(sitka_data_file)
death_valley_data = pd.read_csv(death_valley_data_file)

# 시간 데이터를 날짜 형식으로 변환
sitka_data['DATE'] = pd.to_datetime(sitka_data['DATE'])
death_valley_data['DATE'] = pd.to_datetime(death_valley_data['DATE'])

# 그래프 그리기
plt.figure(figsize=(10, 6))

# 샌프란시스코 최고 기온 그래프
plt.plot(sitka_data['DATE'], sitka_data['TMAX'], color='b', label='Sitka, AK')

# 샌프란시스코 최저 기온 그래프
plt.plot(sitka_data['DATE'], sitka_data['TMIN'], color='r', label='Sitka, AK')

# 그래프 제목과 축 라벨 설정
plt.title('Daily High and Low Temperatures - 2018', fontsize=16)
plt.xlabel('Date', fontsize=14)
plt.ylabel('Temperature (F)', fontsize=14)
plt.legend()

# 그래프 출력
plt.tight_layout()
plt.show()