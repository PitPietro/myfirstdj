# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin)
from django.shortcuts import render
from .models import Post
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)


title_pit = 'Pit Blog - '

# from django.http import HttpResponse


# Handle the traffic from the homepage of the blog
# It takes as parameter the HttpResponse and return
# what the user should see when he is sent to the blog's route


# Homepage
def home(request):
    # the context dictionary passes information to the HTML template
    context = {
        'context_posts': Post.objects.all()
    }
    return render(request, 'blog/homepage.html', context)
    # return HttpResponse('<h1>Pit Blog - Homepage</h1>')


class PostListView(ListView):
    model = Post
    template_name = 'blog/homepage.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post-detail.html'
    context = {'title': title_pit + 'Create'}


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    """
    1) get the post it is trying to update
    2) check if the current user is the author of the post
    """

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author


# About page
def about(request):
    context = {'title': title_pit + 'About'}
    return render(request, 'blog/about.html', context)

# list of dictionaries to fake some information on the blog
# posts = [
#     {
#         'author': 'Red Hot Chili Peppers',
#         'title': 'Blood Sugar Sex Magik',
#         'comment': 'Is their the 5th studio album. Its musical style differed notably from the techniques '
#         ' employed on the band\'s previous album Mother\'s Milk (1989), and featured minimal use of heavy '
#         ' metal guitar riffs. ',
#         'release_date': '24 September 1991'
#     },
#     {
#         'author': 'Led Zeppelin',
#         'title': 'Led Zeppelin IV',
#         'comment': 'Their untitled 4th studio album is commonly known as Led Zeppelin IV. It was produced by '
#                    'guitarist Jimmy Page and recorded between December 1970 and February 1971, mostly in the country '
#                    'house Headley Grange. The album is notable for featuring "Stairway to Heaven", which has been '
#                    'described as the band\'s signature song. ',
#         'release_date': '8 November 1971'
#     },
#     {
#         'author': 'Queen',
#         'title': 'Jazz',
#         'comment': 'Jazz is their 7th studio album. Produced by Roy Thomas Baker, the album artwork was suggested by '
#                    'Roger Taylor, who previously saw a similar design painted on the Berlin Wall. The album\'s '
#                    'varying musical styles were alternately praised and criticised. It reached number two in the UK '
#                    'Albums Chart and number six on the US Billboard 200. Jazz has sold over five million copies '
#                    'worldwide. ',
#         'release_date': '10 November 1978'
#     }
# ]
