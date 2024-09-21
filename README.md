# computer_study
computer_study

:algorithm_study!

+cs추가예정

## 깃허브 환경설정

[1]
git remote -v 로 현재 연결되어 있는 곳이 https://github.com/somsomi3/algorithm_study/가 맞는지 확인


[2]
git config --global -l을 쳤을때, 

user.name=본인 깃헙 사용자 이름

user.email=본인 깃헙 이메일 주소

...

->(만약 나오는 내용이 내 메일과 내이름이 아니라면)

git config --global user.email "본인 깃헙 이메일주소"

git config --global user.name “본인 깃헙 사용자이름"

로 내 정보들로 설정해주기!


[3]
제어판->사용자계정 -> 자격증명관리-> 윈도우자격증명 -> 일반자격증명에서, 사용자 이름 부분이 본인 이메일또는 본인 유저이름

이어야 함.

((++참고 설정:
개인 로컬 환경에서 파일 작성시 .idea폴더가 생성되는데, 이는 .gitignore처리를 해둬서 깃허브에는 올라가지 않아 충돌 오류를 발생시키지 않음.

-.idea파일이란?
: 개개인의 환경설정을 나타내는 파일로, 깃허브에 업로드시 개개인의 설정차이로 인한 문제가 생길수 있다.
따라서, 팀프로젝트를 위한 깃허브를 처음 만들때, .gitignore파일 설정으로 제외하고 업로드 가능하게끔 만들면 좋다. 

참고 블로그1: https://velog.io/@dlgkdis801/GitHub-.idea%EA%B0%80-Repository%EC%97%90-%EC%98%AC%EB%9D%BC%EA%B0%94%EB%8B%A4%EB%A9%B4

참고 블로그2:

))

## 사용방법:
 " 순서대로!
 1. git clone https://github.com/somsomi3/computer_study.git

 2. git pull origin master((항상먼저 git pull을 받아, 변동사항을 가져온후, ))
 
 3. 본인 컴퓨터에서 번호_제목.py문서 생성후, 개인 문풀
 
 4. git add, git commit -m'0829/play_game', git push origin master
    
순으로 진행"

(폴더 구조는, 날짜를 구분하지 않을 경우 불편이 많다하여.. 날짜별로 구분! -> 더 좋은 의견!!)

###알고리즘 문제를 푸는 스터디 입니다.
(예정: +CS, +면접 대비)

- 정기회의: 매주 목요일 모임(저녁 7시 이후~)
  
- 사이트: 백준, swea, 프로그래머스, 등등
  
- 언어: 파이썬, 자바 등
  

## 규칙

**`MONDAY`**  개인 알고리즘 문제 풀이 공유 후 캘린더 체크(매주 **최소 4문제 이상** 풀이)

**`THURSDAY`** 정기 모임, 본인 선정 문제 코드 설명 및 코드 리뷰 * 알고리즘 개념을 적용해 설명

**`SATURDAY`** 금주 강의에서 배운 알고리즘 개념을 바탕으로 문제 선정 및 공유 후 캘린더 체크(**개별 1문제**, 총 4문제)


※ 선정한 알고리즘 개념에 대해 Q&A도 가능하도록 개념 공부도 해올 것

※ 30분~1시간 이내 문제 풀이가 안될 경우 타인의 코드 2개 이상 보고 공부한 후 차후에 한번더 풀이할 것

※ 매주 목요일 정기 모임 전까지 공유된 ALGO(S)문제 풀이 해올 것(총 4문제)


## 파일 및 폴더 구조
백준

baekjoon/dajeong/0829/문제번호_문제명.py

baekjoon/doyeon/0829/문제번호_문제명.py

baekjoon/minkeoung/0829/문제번호_문제명.py

baekjoon/minsu/0829/문제번호_문제명.py


swea

swea/dajeong/0829/문제번호_문제명.py

swea/doyeon/0829/문제번호_문제명.py

swea/minkeoung/0829/문제번호_문제명.py

swea/minsu/0829/문제번호_문제명.py


프로그래머스

programmers/dajeong/0829/문제번호_문제명.py

programmers/doyeon/0829/문제번호_문제명.py

programmers/minkeoung/0829/문제번호_문제명.py

programmers/minsu/0829/문제번호_문제명.py


else

else/dajeong/0829/문제번호_문제명.py

else/doyeon/0829/문제번호_문제명.py

else/minkeoung/0829/문제번호_문제명.py

else/minsu/0829/문제번호_문제명.py

