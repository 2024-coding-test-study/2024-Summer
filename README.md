# :green_book: 2024 코딩 테스트 스터디 소개
* 약 2달간 진행되는 코딩 테스트를 위한 스터디
  - 2달간 [이것이 코딩테스트다](https://github.com/ndb796/python-for-coding-test) 책 마스터하고 백준과 프로그래머스에서 기출문제 풀이 예정
* 언어: Python과 Java

## :one: 진행 방식
1. 매주 [Issue등록](https://github.com/2024-coding-test-study/2024Study/issues) 후 브랜치 생성   
   - 매주 정해진 문제말고 본인이 따로 푼 문제도 Issue등록 후 브랜치에서 문제 풀이 진행   
2. 브랜치에서 작업 후, [PR올리기](https://github.com/2024-coding-test-study/2024Study/pulls)
   - PR을 템플릿 양식에 맞춰서 작성
   - 따로 푼 문제도 PR올리기   
3. 매주 토요일 16시 모임에서 각자 PR 발표와 코드 리뷰 진행
   - 문제를 못 푼 사람일 경우, 풀지 못한 원인 분석 후 당일에 같이 풀어보기
   - 코드 리뷰 후, main 브랜치에 merge   
4. 코드 리뷰 받고, 수정할 부분이 있으면 수정해서 코드 올리기

## :two: PR 규칙
- PR 템플릿에 맞게 작성
- main branch에 merge되면, merge된 브랜치는 삭제
- Reviewer는 본인을 제외한 나머지 멤버 추가     

## :three: Commit Message 규칙
> 커밋 메시지 규칙을 정한 이유는 히스토리 확인할 때 편하기도 하고, 나중에 협업할 때 꽤 도움이 될 것 같아서 추가했습니다
```
type : subject

body
```
#### :heavy_check_mark: Type
- **Add**: 소스 코드 파일 추가
- **Refactor**: 소스 코드 수정
- **Style**: 소스 코드 형식(format) 수정, 변수 네이밍 수정, 주석 추가/삭제 등 
    - (코드 동작에 영향이 없는 수정)
- **Chore**: 그 외 기타 작업

#### :heavy_check_mark: Subject
- 50자 이하의 간단한 제목을 사용한다.
    > ex) Add: 홍길동.py / Add: 홍길동.java <br>
    > ex) Refactor: 완전 탐색 -> 이분 탐색 <br>
    > ex) Style: 함수명 변경

#### :heavy_check_mark: Body(optional)
- 부연 설명을 작성한다.
    > ex) input으로 주어진 배열의 원소들이 오름차순으로 정렬되어 있다는 특징을 이용하여, 탐색 알고리즘을 이분 탐색으로 수정하였습니다.    
    > 따라서 시간 복잡도가 O(n²) -> O(nlogn) 으로 최적화 되었습니다.
- 한 줄에 72자를 넘기지 않는다.


## :four:Directory 구조
```
└── 📂 Week01
       ├── 📂문제_이름
       │      ├── 💾홍길동.py
       │      ├── 💾...
       │      └── 💾홍길동.java
       ├── 📂...
       └── 📂문제_이름
└── 📂 Week02
       ├── 📂문제_이름
       │      ├── 💾홍길동.py
       │      ├── 💾...
       │      └── 💾홍길동.java
       ├── 📂...
       └── 📂문제_이름
```

[참고 리포지토리](https://github.com/Study-CodingTest/Study/blob/main/README.md)
