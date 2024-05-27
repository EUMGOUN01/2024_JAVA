# 시트카는 온대 우림 기후에 위치하므로 강우량이 상당
# sitka_weather_2018_full.csv 파일에는 일일 강우량 나타내는 PRCP 헤더가 있습니다. 이 데이터를 시각화 하시오.
# "STATION","NAME","DATE","AWND","PGTM","PRCP","SNWD","TAVG","TMAX","TMIN","WDF2","WDF5","WSF2","WSF5","WT01","WT02","WT04","WT05","WT08"

import pandas as pd
import plotly.graph_objs as go

# CSV 파일 로드
df = pd.read_csv('c:\\Python\\CH01\\16\\sitka_weather_2018_full.csv')

# 강우량(PRCP) 데이터 추출
dates = pd.to_datetime(df['DATE'])
prcp = df['PRCP']

# Plotly 그래프 생성
fig = go.Figure()

# 강우량(PRCP) 시계열 그래프 추가
fig.add_trace(go.Scatter(x=dates, y=prcp, mode='lines', name='강우량', line=dict(color='blue')))

# 그래프 레이아웃 설정
fig.update_layout(
    title='시트카 2018년 일일 강우량',
    xaxis_title='날짜',
    yaxis_title='강우량 (inches)',
)

# 그래프 출력
fig.show()