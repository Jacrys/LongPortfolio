from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Question, Choice, Passage, Explanation
from django.shortcuts import render, get_object_or_404


def home(request):
    return render(request, 'index/home.html', {})


def test1(request):
    return render(request, 'index/test1.html', {})


def test2(request):
    return render(request, 'index/test2.html', {})


def test3(request):
    return render(request, 'index/test3.html', {})


def test4(request):
    return render(request, 'index/test4.html', {})


def test5(request):
    return render(request, 'index/test5.html', {})


def test6(request):
    return render(request, 'index/test6.html', {})


def test7(request):
    return render(request, 'index/test7.html', {})


def test8(request):
    return render(request, 'index/test8.html', {})


def final(request):
    return render(request, 'index/final.html', {})


def tips(request):
    return render(request, 'index/tips.html', {})


def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Sorry, Question does not exist")
    return render(request, 'index/details.html', {'question': question})
#need to add a "submit" request function under details so we know what the user selected as their choice.#


def result(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'index/results.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        return HttpResponseRedirect(reverse('results', args=(question.id,)))
