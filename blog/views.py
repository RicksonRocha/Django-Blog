from django.views.generic import DeleteView, ListView
from django.views.generic.detail import DetailView

from .models import Post

class PostListView(ListView):
    model = Post


class PostDetailView(DetailView):
    model = Post
