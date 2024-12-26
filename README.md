# 오픈소스 ISSUE_TEMPLATE 기반 이슈 검색 솔루션(2024 2학기 소프트웨어융합캡스톤디자인)
* 소프트웨어융합학과 김유진
<br>
<br>

## Overview
* ### 과제의 배경과 필요성<br>

<img width="626" alt="image" src="https://github.com/user-attachments/assets/b8b7eeb2-84f4-4f01-b473-9a5d375606eb" />

<br><br>
시간이 지나면서 GitHub Issues에는 방대한 양의 이슈들이 축적되었습니다. 하지만 사용자가 이러한 이슈를 효과적으로 탐색할 수 있는 GitHub의 '이
슈 검색 기능'은 그 역할을 충분히 하지 못한다고 느꼈습니다. 현재의 키워드 검색 방식은 검색어 구성에 
따라 결과가 크게 달라지며, 사용자들이 다양한 조합을 시도해야 하는 번거로움이 있습니다. 이는 사용자가 
깃허브에서 본인의 문제와 동일한 이슈를 찾는 과정에서 많은 시간을 소모하게 만듭니다. <br><br>

만약 사용자가 검색어 구성에 대한 고민 없이 한 번의 검색으로 자신의 에러와 동일한 이슈가 존재하는지, 
그리고 해결방법에 대한 요약을 바로 찾을 수 있다면?
<br><br>
<br>
* ### 솔루션 간단 소개<br>

<img width="461" alt="image" src="https://github.com/user-attachments/assets/d08b9c93-b099-4f76-9f50-4f1525ae9740" />
<br>
<br>

## 솔루션 구체적 설명
1. 본인이 사용하는 오픈소스 프로젝트의 주소를 입력
![image](https://github.com/user-attachments/assets/718be9ec-f6b4-424d-833d-d7fec40754f8)
2. ISSUE_TEMPLATE 기반 필드 동적 구성 및 사용자 정보 입력
![image](https://github.com/user-attachments/assets/bb95b014-2d26-4dff-ad43-2220493521e4)

3. 사용자 이슈 데이터와 수집된 이슈들 각각의 유사도 비교 및 가장 유사한 이슈 산출(내부로직)
4. 최종결과 출력<br>
![image](https://github.com/user-attachments/assets/ad5f9a26-50b2-4313-a545-714c834f15b8)

- OpenAI API를 활용해 이슈의 제목, 상세 내용, 에러 해결법 요약<br>
- 사용자가 요약된 것을 읽어보고 본인의 이슈와는 맞지 않다고 판단할 경우를 대비해, "새 이슈 등록" <br>
<br>

## 기술 스택
- 서버, 클라이언트 구현: Python, Streamlit 라이브러리
- 외부 API 사용: GitHub Developer API, OpenAI API
<br>

## 데모영상 
https://drive.google.com/file/d/1iD8h5xjw8IhhTrPJ3fUjJOG2rYCB9AlS/view?usp=sharing 
