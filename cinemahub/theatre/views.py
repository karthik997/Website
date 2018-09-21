from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import MovieReview
from django.views.generic import TemplateView, ListView, DetailView
from .forms import TheatreCreateForms

def theatre_createview(request):
	form = TheatreCreateForms()
	if request.method == "POST":
		# title = request.POST.get("title")
		# genre = request.POST.get("genre")
		# director = request.POST.get("director")
		form = TheatreCreateForms(request.POST)
		if form.is_valid():
			obj = MovieReview.objects.create(
					movie_name = form.cleaned_data.get('movie_name'),
					genre = form.cleaned_data.get('genre'),
					director = form.cleaned_data.get('director')
				)
			return HttpResponseRedirect("/movies/")
		if form.errors:
			print(form.errors)
	template_name = 'theatre/form.html'
	context = {"form":form}
	return render(request, template_name, context)

def movie_list(request):
	template_name = 'theatre/movie_list.html'
	qs = MovieReview.objects.all()
	context = {
		'list': qs
	}
	return render(request, template_name, context)

"""class MovieListView(ListView):
	queryset = MovieReview.objects.all()
	template_name = 'theatre/movie_list.html'"""

class MovieListView(ListView):
	#template_name = 'theatre/movie_list.html'
	def get_queryset(self):
		slug  = self.kwargs.get("slug")
		if slug:
			queryset = MovieReview.objects.filter(
					Q(genre__iexact=slug) |
					Q(genre__icontains=slug)
				)
		else:
			queryset = MovieReview.objects.all()
		return queryset

class MovieDetailView(DetailView):
	queryset = MovieReview.objects.all()
	# def get_context_data(self, *args, **kwargs):
	#  	print(self.kwargs)
	#  	context = super(MovieDetailView, self).get_context_data(*args, **kwargs)
	#  	return context
	# def get_object(self, *args, **kwargs):
	# 	rest_id = self.kwargs.get('rest_id')
	#  	obj = get_object_or_404(MovieReview, id=rest_id)
	#  	return obj
