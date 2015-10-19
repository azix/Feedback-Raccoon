from django.shortcuts import render, get_object_or_404, render
from django.utils.datastructures import MultiValueDictKeyError
from django.http import *
from django.core.urlresolvers import reverse
from django.views import generic
from django.views.generic import ListView
from django.contrib import auth
from django.core.context_processors import csrf
from django.utils import timezone
from django.views.generic import TemplateView
from django.conf import settings
from django.contrib.auth.decorators import login_required
# modification
from django.template import RequestContext
from sondages.forms import SondageForm

from .models import Question, Choice
import datetime
# tuto 1
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from sondages.forms import RegistrationForm, LoginForm
from django.contrib.auth.models import User
from sondages.models import Drinker
from django.contrib.auth import authenticate, login, logout
from sondages.models import Results
from sondages.models import GroupQuestionRelationship


class IndexView(generic.ListView):
    model = GroupQuestionRelationship
    template_name = 'sondages/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Retturn the last five published questions."""
        return Question.objects.all()

    # for e in GroupQuestionRelationship.objects.all():
    #     print(e.gqr_group)




class DetailView(generic.DetailView):
    model = Question
    template_name = 'sondages/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'sondages/results.html'


@login_required
def vote(request, question_id):
    try:
        my_field_value = request.POST['comment']
    except MultiValueDictKeyError:
        my_field_value = None

    p = get_object_or_404(Question, pk=question_id)
    result = Results()
    #
    try:

        selected_choice = p.choice_set.get(pk=request.POST['choice'])



    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form
        return render(request, 'sondages/detail.html', {
            'question': p, 'error_message': "You didn't select a choice.",
        })

    selected_choice.votes += 1
    if p.anonymous == False:

        # selected_choice.user = request.user.drinker
        result.users = request.user.drinker

    else:
        # selected_choice.user = None
        result.users = None

    result.questions = p
    result.votes = selected_choice
    result.comment = my_field_value
    result.save()

    return HttpResponseRedirect(reverse('sondages:results', args=(p.id,)))  # modification


@login_required
def Sondage(request):
    if request.method == 'POST':
        form = SondageForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')

    else:
        form = SondageForm()

    return render(request, 'sondages/Sondage.html', {'form': form})


# Create your views here.
def DrinkerRegistration(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/')

    form = RegistrationForm()  # this will be used in get request

    if request.method == 'POST':
        form = RegistrationForm(request.POST)  # This willbe used in POSt request
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password'])
            user.save()
            sondages = Drinker(user=user, name=form.cleaned_data['name'], birthday=form.cleaned_data['birthday'])
            sondages.save()
            return HttpResponseRedirect('/login/')
        else:
            return render_to_response('sondages/register.html', {'form': form},
                                      context_instance=RequestContext(request))


    else:
        ''' user is not submitting the form , show them a blank registration form'''
        form = RegistrationForm()
        context = {'form': form}
        return render_to_response('sondages/register.html', context, context_instance=RequestContext(request))


def LoginRequest(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/')
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            sondages = authenticate(username=username, password=password)
            if sondages is not None:
                login(request, sondages)
                return HttpResponseRedirect('/')
            else:
                return render_to_response('sondages/login.html', {'form': form},
                                          context_instance=RequestContext(request))
        else:
            return render_to_response('sondages/login.html', {'form': form}, context_instance=RequestContext(request))
    else:
        ''' user is not submitting the form, show the login form '''
        form = LoginForm()
        context = {'form': form}
        return render_to_response('sondages/login.html', context, context_instance=RequestContext(request))


def LogoutRequest(request):
    logout(request)
    return HttpResponseRedirect('/login/')


class ResultstList(ListView):
    model = Results


class QuestionList(ListView):
    model = Question

