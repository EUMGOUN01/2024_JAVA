# 17-2
# hn_submissions.py의 데이터 사용해 현재 해커 뉴스에서 토론이 가장 활발한 글을 막대 그래프로 표현.
# 각 막대의 높이는 글에 달린 댓글의 숫자에 비례함.
# 막대 이름표는 글의 제목이어야 함. 이를 클릭해 해당 페이지 이동 가능.
# 그래프를 만들때 KeyError가 일어난다면 try_except 블록 사용해 문제가 있는 글을 건너뛰세요.

import requests
import matplotlib.pyplot as plt
from operator import itemgetter

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
submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse=True)

# 시각화를 위한 데이터 준비
titles = [submission['title'] for submission in submission_dicts]
comment_counts = [submission['comments'] for submission in submission_dicts]
hn_links = [submission['hn_link'] for submission in submission_dicts]

# 데이터 시각화
plt.figure(figsize=(10, 6))
bars = plt.barh(titles, comment_counts, color='skyblue')
plt.xlabel('댓글 수')
plt.ylabel('글 제목')
plt.title('Hacker News에서 가장 활발한 토론 글')

# 각 막대를 클릭하여 해당 페이지로 이동할 수 있도록 설정
def on_click(event):
    for bar, link in zip(bars, hn_links):
        if bar.contains(event)[0]:
            import webbrowser
            webbrowser.open(link)
            return

plt.gcf().canvas.mpl_connect('button_press_event', on_click)
plt.gca().invert_yaxis()
plt.show()