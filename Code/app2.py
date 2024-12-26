import streamlit as st
from processData import *
from processSimilarity import findDuplicate
from gpt import *
import re
import pandas as pd


# Set the page config
st.set_page_config(page_title='Github Easy Solve',
                   layout='wide',
                   page_icon='📊')

# Title
st.title('Github Easy Solve')

# 사용자 입력 폼
# 세션 상태 초기화
if "repo_submitted" not in st.session_state:
    st.session_state.repo_submitted = False
if "issue_submitted" not in st.session_state:
    st.session_state.issue_submitted = False

# 첫 번째 폼: Repository Link 입력
with st.form("input_form1"):
    
    rep_link = st.text_input("Repository Link:")
    submitted_rep_link = st.form_submit_button("Confirm")

# 첫 번째 폼이 제출되면 세션 상태 갱신
if submitted_rep_link:
    st.session_state.repo_submitted = True
    repo = extract_string(rep_link)
    st.session_state.repo = repo
    
    # repository의 issue_template 다운 받아오는 코드
    files = fetch_issue_templates(repo)
    # issue_template의 body 중에서 type: input or textarea인 애들의 attribute->label가져와서 개수만큼 text_input생성
    data=files[0]['content']
    labels = [] 
    for item in data['body']:
        if item['type'] in ['input', 'textarea']:
            labels.append(item['attributes']['label'])
    st.session_state.labels = labels

# 두 번째 폼: 필드 입력
if st.session_state.repo_submitted:
    inputs = {} # user input을 dictionary로 저장.
    with st.form("input_form2"):
        labels=st.session_state.labels
        for label in labels:
            user_input =st.text_input(f"{label}:")
            inputs[label] = user_input
        submitted = st.form_submit_button("Done!")
    
    # 두 번째 폼이 제출되면 세션 상태 갱신
    if submitted:
        st.session_state.issue_submitted = True

    # 두 번째 폼 제출 후 결과 출력
    if st.session_state.issue_submitted:
        repo = st.session_state.repo  
        
        # 각 항목이 너무 길기때문에 검색 키워드만 추출하는 코드.
        query_lst=re.findall(r'\b\w*error\w*\b', c3, flags=re.IGNORECASE)
        df_lst=[]

        for query in query_lst:
            issues = fetch_issues(repo, query)
            df =save_issues_to_df(issues)
            df_lst.append(df)
        
        # combined_df: IssueNum 고유한 이슈들만 모은 df
        combined_df = pd.concat(df_lst).drop_duplicates(subset='IssueNum').reset_index(drop=True)
        df.to_csv('./combined_df.csv', index=False)

        simval,duplicate=findDuplicate(inputs,combined_df,labels)

        # 결과 출력합시다~ 
        if not duplicate.empty: # duplicate exists
            st.header("Duplicate issue exists!")
            st.subheader(f"Issue [#{duplicate.IssueNum}]({duplicate.URL}) matches your issue. ") # {simval*100:.2f}% 

            st.subheader("💡Summary of the issue")
            result1 = process_url_with_command(duplicate.URL, "summarize this issue in this url as title, problem and state")
            st.write(result1)
            st.subheader("🛠️Solution")
            result2 = process_url_with_command(duplicate.URL, "summarize the final solution of this issue in this url")
            st.write(result2)
            st.write("")
            st.subheader(f"If Issue [#{duplicate.IssueNum}]({duplicate.URL}) isn't the case for you...")
            st.write(f"[Commit your new issue at {repo}](https://github.com/{repo}/issues/new/choose)")

        else: # duplicate doesn't exist
            pass
    
