from django.urls import path
from .views import upload_image, update_points, page3

urlpatterns = [
    path('', upload_image, name='upload_image'),
    path('update-points/', update_points, name='update_points'),
    path('page3/', page3, name='page3'),
]
