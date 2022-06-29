from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy     # namespace 사용을 위한 라이브러리
from .models import Bookmark

class BookmarkListView(ListView) :
    model = Bookmark

class BookmarkCreateView(CreateView) :
    model = Bookmark
    fields = ['site_name', 'url']   # 사용할 필드 지정
    success_url = reverse_lazy('list')    # 처리 성공 후 이동할 url (리스트 페이지로 이동)
    # 기본적으로 create, update 뷰클래스의 템플릿 파일명은 '_form' 이 접미사로 붙는다.
    template_name_suffix = '_create'   # 템플릿 파일명을 bookmark_create.html 로 설정함

class BookmarkDetailView(DetailView) :
    model = Bookmark

class BookmarkUpdateView(UpdateView) :
    model = Bookmark
    fields = ['site_name', 'url']  # 사용할 필드 지정
    template_name_suffix = '_update'   # 템플릿 파일명을 bookmark_update.html 로 설정함

class BookmarkDeleteView(DeleteView) :
    model = Bookmark
    success_url = reverse_lazy('list')   # 삭제 후에 이동할 경로 설정




