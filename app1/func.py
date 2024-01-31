# func.py
import os
from PIL import Image
import requests

def temp1(image_name):
    image_path = os.path.join('media', image_name)  # 이미지 경로설정
    
    # 여기에 예측된 점을 가져와야함
    # points = [[714, 461], [2505, 644],[223, 3553], [2488, 3654]]    
    
    # 모델 API URL 로컬호스트주소
    url = 'http://127.0.0.1:5000/predict'
    
    # 이미지 파일을 바이너리 형식으로 열기
    with open(image_path, 'rb') as img_file:
        # API에 POST 요청 보내기
        response = requests.post(url, files={'file': img_file})
        
    # API 응답 확인 및 처리
    if response.status_code == 200:
        # 예측된 좌표 추출
        points = response.json()
    else:
        # 에러 처리 임시값으로 제공
        points = [[400, 461], [500, 644],[223, 600], [500, 600]]  
        # points = None
        
    return points


