from django.shortcuts import render
from django.http import HttpResponse, response
from .models import Question

# Create your views here.


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)


def detail(request, question_id):
    return HttpResponse(f"You are look at Question No. {question_id}")


def results(request, question_id):
    response = f"You are looking at the results of Question {question_id}"
    return HttpResponse(response)


def vote(request, question_id):
    return HttpResponse(f"You are voting on Question No. {question_id}")
