from django.urls import path
from . import views #同階層のviewsを読み込む

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:thread_id>/', views.detail, name='detail'),
]