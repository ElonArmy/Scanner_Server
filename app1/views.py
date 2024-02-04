# views.py
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from .func import temp1
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
import requests


def upload_image(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        result = temp1(name)  # 완료
        context['result'] = json.dumps(result)  # JSON 형식으로 변환합니다.
        context['image_name'] = name
        return render(request, 'app1/page2.html', context)
    return render(request, 'app1/main.html')

@csrf_exempt
def update_points(request):
    context = {}
    if request.method == 'POST':
        points = json.loads(request.body)
        print(points) 
        #사용자가 최종 수정한 점을 모델에 보내서 이미지 변환 수행해야함
        
        # 모델 API의 엔드포인트 URL == 플라스크 서버
        model_api_url = 'http://127.0.0.1:5000/perspective_transform'
        
        # 모델 API로 POST 요청, 좌표를 보낸다.
        response = requests.post(model_api_url, json={'points': points})
        
        if response.status_code == 200:
            # 응답으로 받은 바이너리 데이터를 이미지 파일로 저장
            image_path = './media/received_image.jpg'
            with open(image_path, 'wb') as f:
                f.write(response.content)
            
            # 저장된 이미지의 URL을 템플릿에 전달
            image_url = './media/received_image.jpg'
            context['image_url'] = image_url
            return render(request, 'app1/page3.html', context)
        else:
            # 실패 응답 처리
            return HttpResponse("이미지를 받는 데 실패했습니다.", status=400)
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'})


    
def page3(request):
    context = {}
    return render(request, 'app1/page3.html', context)
