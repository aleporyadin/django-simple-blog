from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.views import View
from django.urls import reverse
#from django.http import HttpResponseRedirect, HttpResponse
from django.template.loader import render_to_string
from .models import Post, Comment
from django.contrib.auth.decorators import login_required
from .forms import CommentForm
from taggit.models import Tag
from django.db.models import Q


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated 

class HelloView(APIView):
    permission_classes = (IsAuthenticated,)      
    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)

class PostListView(ListView):
    model = Post
    template_name = 'blog/articles.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5

    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs)
        context['list_tags'] = Tag.objects.all()
        return context

        
    
    


class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 5
    

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')
    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs)
        context['list_tags']=Tag.objects.all()
        return context

class PostDetailView(DetailView):
    model = Post
    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs)
        context['list_tags']=Tag.objects.all()
        return context




class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content', 'image','tags']#'tags'

    def form_valid(self, form):
        form.instance.author = self.request.user

        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content', 'image','tags']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'
    
    def delete(self, request, *args, **kwargs):
        result = super().delete(request, *args, **kwargs)
        Tag.objects.filter(post=None).delete()
        return result
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def home(request):

    # context = {
    #     'posts': Post.objects.all(),
    # }
    return render(request, 'blog/home.html')
def articles(request):
    context = {
        'posts': Post.objects.all(),
    }
    return render(request, 'blog/articles.html',context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

def tagged(request, slug):
    
    tag = get_object_or_404(Tag, slug=slug)
    list_tags= Tag.objects.all()
    posts = Post.objects.filter(tags=tag)
    
    context = {
        
        'tag':tag,
        'list_tags':list_tags,
        'posts':posts,
    }
    return render(request, 'blog/articles.html', context)

def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        
        form = CommentForm(request.POST)

        if form.is_valid():
            form.instance.author = request.user
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post-detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment_to_post.html', {'form': form})



@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('post-detail', pk=comment.post.pk)

@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('post-detail', pk=comment.post.pk)

def approved_comments(self):
    return self.comments.filter(approved_comment=True)