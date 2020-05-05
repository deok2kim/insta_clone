from django.urls import path
from .views import PhotoList, PhotoCreate, PhotoUpdate, PhotoDelete, PhotoDetail

app_name = "photo"
urlpatterns = [
    # as_view() 를 붙여줘야 generic view가 생성됨
    path('create/', PhotoCreate.as_view(), name='create'),
    path('delete/<int:pk>/', PhotoDelete.as_view(), name='delete'),
    path('update/<int:pk>/', PhotoUpdate.as_view(), name='update'),
    path('detail/<int:pk>/', PhotoDetail.as_view(), name='detail'),
    path('', PhotoList.as_view(), name='index'),

]