# 16-9 세계 화재
# world_fires_1_day.csv 파일이 있습니다.
# 이 파일에는 세계 각 곳에서 일어난 화재의 위도와 경도, 규모 같은 정보가 있음.
# latitude,longitude,brightness,scan,track,acq_date,acq_time,satellite,confidence,version,bright_t31,frp,daynight
# 데이터 처리 방법, 지도화 방법, 화재의 영향을 받은 부분을 지도에 표시.

# file_path = 'c:\\Python\\CH01\\16\\world_fires_1_day.csv' 

import pandas as pd
import folium
from folium.plugins import HeatMap, MarkerCluster

# CSV 파일 로드
file_path = 'c:\\Python\\CH01\\16\\world_fires_1_day.csv' 
df = pd.read_csv(file_path)

# 데이터 확인
print(df.head())
print(df.columns)

# 결측치 확인
print(df.isnull().sum())

# 필요한 컬럼 선택
df = df[['latitude', 'longitude', 'brightness', 'acq_date', 'acq_time', 'confidence', 'frp', 'daynight']]

# 'acq_date'와 'acq_time'을 datetime 타입으로 변환
df['acq_time'] = df['acq_time'].astype(str).str.zfill(4)  # 'acq_time' 컬럼을 문자열로 변환하고 4자리로 채우기
df['acq_datetime'] = pd.to_datetime(df['acq_date'] + ' ' + df['acq_time'], format='%Y-%m-%d %H%M')

# 중복된 'acq_date'와 'acq_time' 컬럼 삭제
df = df.drop(columns=['acq_date', 'acq_time'])

# 데이터 확인
print(df.head())

# 지도 생성 (중심 좌표는 임의로 설정)
m = folium.Map(location=[20, 0], zoom_start=2)

# HeatMap을 사용하여 화재 데이터를 지도에 추가
heat_data = [[row['latitude'], row['longitude'], row['brightness']] for index, row in df.iterrows()]
HeatMap(heat_data).add_to(m)

# 지도 저장
m.save('world_fires_map.html')

# 마커 클러스터링을 사용하여 화재 데이터를 지도에 추가
marker_cluster = MarkerCluster().add_to(m)

for index, row in df.iterrows():
    folium.Marker(
        location=[row['latitude'], row['longitude']],
        popup=f"Brightness: {row['brightness']}<br>Confidence: {row['confidence']}<br>FRP: {row['frp']}",
        icon=folium.Icon(color='red' if row['daynight'] == 'D' else 'blue')
    ).add_to(marker_cluster)

# 클러스터링된 지도 저장
m.save('world_fires_clustered_map.html')