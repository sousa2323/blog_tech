from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Post

    
class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context["post"] = Post.objects.order_by('-id')[:6].all()
        return context
    

    