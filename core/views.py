from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q


from django.views.generic import TemplateView, DetailView, ListView
from .models import Post, Banner, Destaques, Categories

    
class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context["post"] = Post.objects.order_by('-created')[:6].all()
        context["banner"] = Banner.objects.order_by('-created_banner')[:1].all()
        return context    
    
    


def search_results(request):
	if request.method == "POST":
		query = request.POST['query']
		venues = Post.objects.filter(title__contains=query)
	
		return render(request, 
		'search_results.html', 
		{'query':query,
		'venues':venues})
	else:
		return render(request, 
		'search_results.html', 
		{})

def search_view(request, search_id):
	search = Post.objects.get(pk=search_id)
	return render(request, 'view/search_view.html', {'search': search})



