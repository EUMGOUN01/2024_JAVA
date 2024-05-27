# 17-1 문제
# python_repos.py 수정해서 다른 언어로 만들어진 인기 있는  프로젝트를 시각화 하시오.

import requests
import matplotlib.pyplot as plt

# GitHub API 호출을 통해 JavaScript로 작성된 인기 있는 저장소 가져오기
url = 'https://api.github.com/search/repositories?q=language:javascript&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

# API 응답을 변수에 저장
response_dict = r.json()
print(f"Total repositories: {response_dict['total_count']}")

# 저장소 정보 탐색
repo_dicts = response_dict['items']
print(f"Repositories returned: {len(repo_dicts)}")

# 시각화를 위한 데이터 준비
repo_names = []
stars = []

for repo_dict in repo_dicts:
    repo_names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])

# 데이터 시각화
plt.figure(figsize=(10, 6))
plt.barh(repo_names, stars, color='skyblue')
plt.xlabel('Stars')
plt.ylabel('Repository')
plt.title('Top Starred JavaScript Repositories on GitHub')
plt.gca().invert_yaxis()
plt.show()