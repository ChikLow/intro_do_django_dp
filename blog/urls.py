from django.urls import path
from .views import post_list, post_detail, posts_by_author

urlpatterns = [
    path('', post_list, name='post_list'),
    path('post/<int:post_id>/', post_detail, name='post_detail'),
    path('author/<int:author_id>/', posts_by_author, name='posts_by_author'),
]
