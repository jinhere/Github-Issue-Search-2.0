import requests
import pandas as pd
import os
import numpy as np
import yaml

GITHUB_TOKEN="[YOURGITHUBTOKEN]"
HEADERS = {"Authorization": f"token {GITHUB_TOKEN}"}
PER_PAGE = 100  # 한 페이지당 최대 결과 수

def extract_string(input_string):
    # 입력된 문자열에서 마지막에서 두 번째 '/' 이후의 문자열을 추출합니다.
    parts = input_string.rstrip('/').split('/')  
    if len(parts) >= 2:
        return '/'.join(parts[-2:]) 
    return None  

def fetch_issue_templates(repo):
    """
    ISSUE_TEMPLATE 폴더 내 파일 이름과 내용을 가져옵니다.
    """
    url = f"https://api.github.com/repos/{repo}/contents/.github/ISSUE_TEMPLATE"
    response = requests.get(url, headers=HEADERS)

    if response.status_code != 200:
        print(f"REST API 요청 실패: {response.status_code}, {response.text}")
        return []

    data = response.json()
    files = []

    for entry in data:
        if entry["type"] == "file":
            file_response = requests.get(entry["download_url"], headers=HEADERS)
            if file_response.status_code == 200:
                # Parsing the content as YAML
                try:
                    file_content = yaml.safe_load(file_response.text)
                    files.append({"name": entry["name"], "content": file_content})
                except yaml.YAMLError as e:
                    print(f"YAML 파싱 실패: {e}")
            else:
                print(f"파일 가져오기 실패: {file_response.status_code}, {file_response.text}")

    return files
    
def fetch_issues(repo, query, per_page=PER_PAGE):
    
    """
    특정 레포지토리에서 키워드를 기준으로 이슈 검색
    """
    url = "https://api.github.com/search/issues"
    params = {
        "q": f"type:issue + {query} repo:{repo}",
        "per_page": per_page
    }

    results = []
    page = 1

    while True:
        print(f"Fetching page {page}...")
        params["page"] = page
        response = requests.get(url, headers=HEADERS, params=params)
        if response.status_code != 200:
            print(f"Error: {response.status_code}, {response.text}")
            break

        data = response.json()
        results.extend(data.get("items", []))
        
        # 다음 페이지 없으면 종료
        if "next" not in response.links:
            break

        page += 1

    return results



def save_issues_to_df(issues):

    issue_data = []

    for issue in issues:
        print(issue['number'])

        issue_data.append({
            "IssueNum": issue.get("number"),
            "URL": issue.get("html_url"),
            "Title": issue.get("title"),
            "Body": issue.get("body"), 

        })

    # DataFrame 생성 
    df = pd.DataFrame(issue_data)
    
    return df




