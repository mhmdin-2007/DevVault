from django.urls import path

from .views import PostDetailView, PostListView, PostCreateView, PostUpdateView, PostDeleteView

app_name = 'posts'

urlpatterns = [
    path('', PostListView.as_view(), name='home'),
    path('post/create/', PostCreateView.as_view(), name='post_create'),
    path('post/<str:slug>/update/', PostUpdateView.as_view(), name='post_update'),
    path('post/<str:slug>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('post/<str:slug>/', PostDetailView.as_view(), name='post_detail'),
]