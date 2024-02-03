# Scanner_Server
- 1차 수정
- one branch

## 설정
### 깃 레포 불러오기
  - 불러올 경로에서 레포 불러오기
    ``` 
    git clone https://github.com/ElonArmy/Scanner_Server.git
    ```
  - 브랜치를 동기화 한다.
    ```
    git pull origin main
    ```
  - 브랜치 확인  
    ```
    git branch main
    ```
    
### 가상환경 설치(windows)
  - pip업데이트
    ```
    python.exe -m pip install --upgrade pip 
    ```
  - 가상환경 생성
    ```
    python -m venv myvenv
    ```
  - 가상환경 실행
    ```
    source myvenv/Scripts/activate
    ```
  - 패키지 설치
    ```
    pip install -r requirement.txt
    ```
### 장고 서버 실행
  - DB마이그레이션실행
    ```
    python manage.py migrate
    ```
  - 서버실행
    ```
    python manage.py runserver
    ```
  - http://127.0.0.1:8000/ 로들어가서 실행확인
  - 터미널에서 ctrl+c 서버 종료
  - 추가사항
    - 포트변경 
      ```
      python manage.py runserver 8080
      ```
    - 디버그 모드 확인