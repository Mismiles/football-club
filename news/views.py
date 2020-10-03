from django.views import generic
from .models import Post


class news_list(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'news/news.html'

class news_detail(generic.DetailView):
    model = Post
    template_name = 'news/news_detail.html'