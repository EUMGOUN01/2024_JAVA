import pandas as pd
import plotly.express as px

# CSV 파일을 절대 경로를 사용하여 읽어서 데이터프레임으로 저장
file_path = r'c:\\Python\\CH01\\16\\earthquakes.csv'
data = pd.read_csv(file_path)

# 데이터프레임에서 위도와 경도를 사용하여 지진 관측소의 위치를 시각화하고 색상 지정
fig = px.scatter_geo(data, lat='LATITUDE', lon='LONGITUDE', hover_name='STATION_NA', color='NETWORK_ST', projection='natural earth')
fig.update_geos(showcountries=True, countrycolor="RebeccaPurple", showland=True, landcolor="LightGreen", showocean=True, oceancolor="LightBlue")
fig.update_layout(title='Earthquake Stations')
fig.show()

