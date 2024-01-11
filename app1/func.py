# func.py
import os
from PIL import Image
import random

def temp1(image_name):
    image_path = os.path.join('media', image_name)  # 이미지 경로를 설정합니다.
    with Image.open(image_path) as img:
        width, height = img.size  # 이미지의 너비와 높이를 가져옵니다.
    points = []
    for _ in range(4):  # 4개의 랜덤한 좌표를 생성합니다.
        x = random.randint(0, width - 1)
        y = random.randint(0, height - 1)
        points.append((x, y))
    return points


