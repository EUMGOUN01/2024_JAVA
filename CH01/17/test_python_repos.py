# 17-3
# python_repos.py에서는 status_code 값을 출력해서 호출이 성공적이었는지 확인했음.
# pytest를 사용해 status_code 값이 200이라고 단언하는 test_python_repos.py 프로그램 만드시오.
# 다른 어서션도 생각해보세요. 예를 들어 몇개의 항목이 변환되는지 예상하거나,
# 저장소의 총 숫자가 일정 숫자보다 크다고 단언하는 어서션을 만드시오.

import requests
import pytest

def test_github_api():
    # API 호출
    url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
    headers = {'Accept': 'application/vnd.github.v3+json'}
    r = requests.get(url, headers=headers)
    
    # 상태 코드가 200인지 확인
    assert r.status_code == 200, f"Expected status code 200, but got {r.status_code}"
    
    # 응답 데이터를 변수에 저장
    response_dict = r.json()
    
    # 저장소의 총 숫자가 0보다 큰지 확인
    total_repos = response_dict['total_count']
    assert total_repos > 0, f"Expected more than 0 repositories, but got {total_repos}"
    
    # 반환된 항목의 수가 0보다 큰지 확인
    repo_dicts = response_dict['items']
    assert len(repo_dicts) > 0, f"Expected more than 0 items, but got {len(repo_dicts)}"
    
    # 각 항목이 예상된 키를 가지고 있는지 확인
    required_keys = {'name', 'owner', 'stargazers_count', 'html_url', 'created_at', 'updated_at', 'description'}
    for repo_dict in repo_dicts:
        assert required_keys.issubset(repo_dict.keys()), f"Missing keys in repo_dict: {repo_dict.keys()}"

# pytest를 실행하기 위한 코드
if __name__ == "__main__":
    pytest.main()