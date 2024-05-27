# Hacker News API를  matplotlib에서 Plotly로 변경

import requests
import plotly.graph_objs as go

# API 호출을 통해 Hacker News의 인기 글 가져오기
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f"상태 코드: {r.status_code}")

# 각 글에 대한 정보 처리
submission_ids = r.json()
submission_dicts = []
for submission_id in submission_ids[:10]:
    try:
        # 각 글에 대한 별도의 API 호출
        url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
        r = requests.get(url)
        print(f"id: {submission_id}\t상태: {r.status_code}")
        response_dict = r.json()
        
        # 각 글에 대한 딕셔너리 생성
        submission_dict = {
            'title': response_dict['title'],
            'hn_link': f"http://news.ycombinator.com/item?id={submission_id}",
            'comments': response_dict['descendants'],
        }
        submission_dicts.append(submission_dict)
    except KeyError:
        print(f"데이터가 없는 글 건너뛰기: {submission_id}")

# 댓글 수에 따라 글 정렬
submission_dicts = sorted(submission_dicts, key=lambda x: x['comments'], reverse=True)

# 시각화를 위한 데이터 준비
titles = [submission['title'] for submission in submission_dicts]
comment_counts = [submission['comments'] for submission in submission_dicts]
hn_links = [submission['hn_link'] for submission in submission_dicts]

# Plotly 그래프 생성
fig = go.Figure(data=[go.Bar(
    y=titles,
    x=comment_counts,
    orientation='h',  # 수평 막대 그래프
    marker=dict(color='skyblue')  # 막대 색상 설정
)])

# 그래프 레이아웃 설정
fig.update_layout(
    title='Hacker News에서 가장 활발한 토론 글',
    xaxis_title='댓글 수',
    yaxis_title='제목',
    height=600,  # 그래프 높이 설정
)

# 각 막대를 클릭하여 해당 페이지로 이동할 수 있도록 설정
def update_url(trace, points, selector):
    if points.point_inds:
        selected_index = points.point_inds[0]
        import webbrowser
        webbrowser.open(hn_links[selected_index])

# 이벤트 리스너 추가
fig.data[0].on_click(update_url)

# 그래프 출력
fig.show()