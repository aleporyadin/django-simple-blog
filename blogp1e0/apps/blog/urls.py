from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView,
    add_comment_to_post,
    about,
    comment_approve,
    comment_remove,
    tagged,
    articles,
    home,
    HelloView
)
urlpatterns = [
    path('', home, name='blog-home'),

    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),

    path('hello/', HelloView.as_view(), name='hello'),
    path('post/<int:pk>/comment/', add_comment_to_post, name='add-comment-to-post'),
    path('post/<int:pk>/comment/approve/', comment_approve, name='comment_approve'),
    path('post/<int:pk>/comment/remove/', comment_remove, name='comment_remove'),

    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),

    path('tag/<slug:slug>/', tagged, name="tagged"),
    path('article/', PostListView.as_view(), name='blog-articles'),

    path('about/', about, name='blog-about'),
]
# urlpatterns += [
#     url(r'^captcha/', include('captcha.urls')),
# ]