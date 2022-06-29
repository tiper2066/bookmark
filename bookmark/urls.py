from django.urls import path
from .views import BookmarkListView, BookmarkCreateView, BookmarkDetailView, BookmarkUpdateView, BookmarkDeleteView

urlpatterns = [
    # 127.0.0.1:8000/bookmark/ 가 홈. 클래스형 뷰 사용명시 (as_view())
    path('', BookmarkListView.as_view(), name = 'list'),
    path('add/', BookmarkCreateView.as_view(), name = 'add'),
    # <int:pk> 는 정수형의 primary key를 의미한다. <pk> 는 문자타입이다.
    path('detail/<int:pk>/', BookmarkDetailView.as_view(), name = 'detail'),
    path('update/<int:pk>/', BookmarkUpdateView.as_view(), name = 'update'),
    path('delete/<int:pk>/', BookmarkDeleteView.as_view(), name = 'delete'),
]