import re
from nltk.corpus import stopwords

# NLTK 불용어 사전 다운로드 (처음 한 번만 실행)
import nltk
#nltk.download('stopwords')

# 불용어 제거 함수
def remove_stopwords(text):
    # 소문자화
    text = text.lower()

    # 점(.)과 공백을 제외한 특수문자 제거
    text = re.sub(r'[^a-z0-9\s.]', '', text)

    # NLTK 불용어 목록 로딩
    stop_words = set(stopwords.words('english'))

    # 단어별로 나누고 불용어 제거
    words = text.split()
    filtered_words = [word for word in words if word not in stop_words]

    # 다시 공백으로 구분된 텍스트로 합침
    return ' '.join(filtered_words)

def extract_issue_details(text, labels):
    # 정규식 패턴 생성
    patterns = {}
    for label in labels:
        # 키 값을 '### ' 다음에 오는 label로 사용
        pattern_value = rf"### {re.escape(label)}\s+(.+?)\n"
        patterns[label] = pattern_value
    
    # 추출 결과 저장
    results = {}
    for key, pattern in patterns.items():
        match = re.search(pattern, text)
        if match:
            # If the match contains multiple lines, split them and clean up spaces
            value = match.group(1).strip()
            results[key] = value.replace("\n", " ").strip()  # Replace newline with space and clean
        else:
            results[key] = None
    
    return results

# Function to compute Jaccard similarity for two strings
def jaccard_similarity(str1, str2):
    try:
        remove_stopwords(str1)
        remove_stopwords(str2)
        set1, set2 = set(str1.split()), set(str2.split())
    except Exception as e:
        return 0
    intersection = set1 & set2
    union = set1 | set2
    return len(intersection) / len(union) if union else 1.0  # Avoid division by zero

def findDuplicate(usr,df,labels):
    
    mostjac=0
    mostind=0
    for index, series in df.iterrows():
        seriesDic=extract_issue_details(series.Body,labels)
        weights={}
        for label in labels:
            weights[label]=1/len(labels)

        # Compute weighted Jaccard similarity
        weighted_similarity = sum(
            weights[key] * jaccard_similarity(usr[key], seriesDic[key]) 
            for key in usr
        )

        if weighted_similarity>mostjac:
            mostind=index
            mostjac=weighted_similarity
            print(f"{series.IssueNum} {mostind} {weighted_similarity}\n" )
        
    return (mostjac,df.iloc[mostind])
