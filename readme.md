
### Green Space API 

---

✅ 최근 업데이트 : 2022.11.28 (월)

🖥 배포 도메인 : http://greenspaceapi.herokuapp.com


---

**1. 실행 방법**

* 해당 서버는 파이썬 3 버전을 지원합니다.
* pip install -r requirements.txt 로 필요한 라이브러리를 다운합니다.
* 이후 아래 두 명령어를 순차적으로 실행합니다.
  * python manage.py makemigrations
  * python manage.py migrate
* 장고를 실행합니다.
  * python manage.py runserver
* http://127.0.0.1:8000/ 에서 실행되는 서버를 볼 수 있습니다.
  * 또는 상단의 배포 링크를 통해서도 접속 가능합니다.
  * 관리자 계정은 admin, admin1234*로 접속 가능합니다.

---

**2. 구현 기능**

1) 유저 (/users) 

|기능|URL|Method|Body 내용|
|----|----|----|----|
|토큰으로 유저 정보 받아오기|/profile|GET|-|
|유저 토큰 리프레시|/signin/refresh|POST|refresh (string token)|
|유저 생성하기|/signup|POST|nickname, username, password|
|로그인|/signin|POST|nickname, password|
|로그아웃|/signout|POST|refresh|
|탈퇴|/delete|DELETE|-|
|유저 정보 수정|/profile|PATCH|nickname, username, point, open (수정 원하는 부분만)|
|자신이 팔로우하고 있는 유저 리스트|/followinglist|GET|-|
|자신을 팔로우하고 있는 유저 리스트|/followedlist|GET|-|
|팔로우/언팔로우|/following|POST|nickname|
|사용자 검색|/|GET|-|

2) 아이템 구매 및 조회 (/shop)

|기능|URL|Method|Body 내용|
|----|----|----|----|
|사용자의 Buy 리스트|/buy|GET|-|
|아이템 구매|/buy|POST|item (아이템 이름)|
|구매한 아이템 되팔기|/buy|DELETE|item|
|Space 꾸밀 Buy 정하기|/buy|PATCH|item|
|모든 아이템 리스트|/items|GET|-|
|모든 배지 리스트|/badges|GET|-|
|사용자의 space 정보|/space|GET|-|
|다른 사용자 space 정보|/space|POST|nickname|

3) 녹색 제품 (/products)

|기능|URL|Method|Body 내용|
|----|----|----|----|
|모든 녹색 제품 리스트|/|GET|-|
|북마크 등록/제거|/mark/<int:product_id>|GET|-|
|북마크 리스트|/mark|GET|-|

4) 게시물 (/post)

|기능|URL|Method|Body 내용|
|----|----|----|----|
|사용자의 모든 게시물|/|GET|-|
|게시물 수정|/<id>|PATCH|image, text|
|게시물 업로드|/|POST|image, text|
|게시물 삭제|/<id>|DELETE|-|


