from django.urls import path
from .import views
urlpatterns = [
    path('', views.blog_post_list, name='blog_post_list'),
    path('blog-post/<int:id>/', views.blog_post_detail, name='blog_post_detail'),
    path('<int:id>/comment/', views.create_comment, name='comment_create'),
    path('search/', views.search_posts, name='search_posts'),

]
