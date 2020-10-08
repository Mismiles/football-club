from django.views import generic
from .models import Post


class match_list(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'matches/matches.html'
    paginate_by = 3


class match_detail(generic.DetailView):
    model = Post
    template_name = 'matches/match_detail.html'
