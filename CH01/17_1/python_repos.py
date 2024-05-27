# 17-3
# python_repos.py에서는 status_code 값을 출력해서 호출이 성공적이었는지 확인했음.
# pytest를 사용해 status_code 값이 200이라고 단언하는 test_python_repos.py 프로그램 만드시오.
# 다른 어서션도 생각해보세요. 예를 들어 몇개의 항목이 변환되는지 예상하거나,
# 저장소의 총 숫자가 일정 숫자보다 크다고 단언하는 어서션을 만드시오.

import requests

# Make an API call and store the response.
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

# Store API response in a variable.
response_dict = r.json()
print(f"Total repositories: {response_dict['total_count']}")

# Explore information about the repositories.
repo_dicts = response_dict['items']
print(f"Repositories returned: {len(repo_dicts)}")

print("\nSelected information about each repository:")
for repo_dict in repo_dicts:
    print(f"Name: {repo_dict['name']}")
    print(f"Owner: {repo_dict['owner']['login']}")
    print(f"Stars: {repo_dict['stargazers_count']}")
    print(f"Repository: {repo_dict['html_url']}")
    print(f"Created: {repo_dict['created_at']}")
    print(f"Updated: {repo_dict['updated_at']}")
    print(f"Description: {repo_dict['description']}")