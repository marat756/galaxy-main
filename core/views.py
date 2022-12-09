from django.shortcuts import render
from .models import Post, TopPost
from django.views.generic import TemplateView

def main(request):
    posts = Post.objects.all()
    tposts = TopPost.objects.all()
    context = {
        'posts': posts,
        'tposts': tposts,
    }
    return render(request, 'index.html', context)

class AboutView(TemplateView):
    template_name = 'about.html'

