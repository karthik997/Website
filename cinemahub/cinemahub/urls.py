"""cinemahub URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url
from theatre.views import movie_list,MovieListView, MovieDetailView, theatre_createview
from django.views.generic import TemplateView
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', TemplateView.as_view(template_name='home.html')),
    url(r'^movies/$', MovieListView.as_view()),
    url(r'^movies/create/$', theatre_createview),
    #url(r'^movies/(?P<slug>\w+)/$', MovieListView.as_view()),
    url(r'^movies/(?P<slug>[\w-]+)/$', MovieDetailView.as_view()),
    #url(r'^movies/fantasy/$', FantasyMovieListView.as_view()),
    url(r'^about/$', TemplateView.as_view(template_name='about.html')),
    url(r'^contact/$', TemplateView.as_view(template_name='contact.html')),
]
