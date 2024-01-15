# views.py
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from .func import temp1
from django.http import JsonResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
import json

import json

def upload_image(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        result = temp1(name)  #####################
        context['result'] = json.dumps(result)  # JSON 형식으로 변환합니다.
        context['image_name'] = name
        return render(request, 'app1/page2.html', context)
    return render(request, 'app1/main.html')

@csrf_exempt
def update_points(request):
    if request.method == 'POST':
        points = json.loads(request.body)####################
        print(points) 
        
        #사용자가 수정한 4개의 점 -> 스캔결과 끝


        # points를 저장하거나 처리하는 코드를 여기에 작성합니다.
        return JsonResponse({'status': 'ok'})  # JSON 응답을 반환합니다.
    else:
        return JsonResponse({'status': 'error'})
    
def page3(request):
    return render(request, 'app1/page3.html')