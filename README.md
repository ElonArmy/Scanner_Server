# Scanner_Server
- 1차 수정
- git branch main으로 재설정후 푸쉬

## 설정
### 깃 레포 불러오기
  - 불러올 경로에 git init (최초1회)
  - git remote add origin https://github.com/ElonArmy/Scanner_Server.git (최초1회)
  - git pull origin main 으로 main 브랜치를 동기화 한다. 
### 가상환경 설치(windows)
  - python.exe -m pip install --upgrade pip  ,pip업데이트(최초1회)
  - python -m venv myvenv 로 가상환경 생성(최초1회)
  - source myvenv/Scripts/activate 가상환경 실행
  - pip install -r requirement.txt 로 패키지 설치(최초1회)
### 장고 서버 실행
  - python manage.py migrate  ,DB마이그레이션실행(최초1회)
  - python manage.py runserver 서버실행
  - http://127.0.0.1:8000/ 로들어가서 실행확인
  - ctrl+c 서버 종료
  - 추가사항
    - 포트변경 python manage.py runserver 8080
    - 디버그 모드 확인