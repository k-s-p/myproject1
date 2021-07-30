from django.urls import path
from . import views #同階層のviewsを読み込む

app_name = 'pgfansite'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:thread_id>/', views.detail, name='detail'),
    path('<int:thread_id>/res_insert/', views.res_insert, name='res_insert'),
    path('thread/', views.thread, name='thread'),
    path('newthread/', views.newthread, name='newthread'),
]