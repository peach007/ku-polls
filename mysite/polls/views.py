from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpRequest
from django.template import loader

from .models import Question
from django.http import Http404
from django.shortcuts import get_object_or_404, render


# Create your views here.


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    content = {
        'lastwsr question_list': latest_question_list,
    }
    return HttpResponse(output)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'qusetion': question})
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question dose not exist")
    # return render(request, 'polls/detail.html', {'question': question})
    # return HttpResponse("You're looking at question %s." % question_id)

def result(request, question_id):
    response = "You' re looking at the result of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)