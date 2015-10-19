__author__ = 'aziz'

from . import views
from django.conf.urls import patterns, url
from django.contrib import admin

admin.autodiscover()
urlpatterns = patterns('',
                       # ex: /sondages/
                       url(r'^$', views.IndexView.as_view(), name='index'),
                       # ex: /sondages/5
                       url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
                       # ex: /sondages/5/results/
                       url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
                       # ex: /sondages/5/vote/
                       url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
                       # modif
                       url(r'^Sondage/$', 'sondages.views.Sondage'),

                       url(r'^register/$', 'sondages.views.DrinkerRegistration'),
                       url(r'^login/$', 'sondages.views.LoginRequest'),
                       url(r'^logout/$', 'sondages.views.LogoutRequest'),
                       url(r'^Results/$', views.ResultstList.as_view()),
                       url(r'^Questions/$', views.QuestionList.as_view()),


                       )
