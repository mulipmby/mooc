from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import RaffleEntry
from django.contrib.auth import authenticate

def index(request):
    return render(request, 'pages/index.html')

def start_quiz(request):
    request.session['score'] = 0
    request.session['tried_already'] = False
    return redirect('quiz')

def quiz(request):
    if request.method == 'POST':
        answer1 = int(request.POST.get('answer1', 0))
        answer2 = int(request.POST.get('answer2', 0))
        answer3 = int(request.POST.get('answer3', 0))
        answer4 = int(request.POST.get('answer4', 0))

        correct_answers = 0
        if answer1 == 2:
            correct_answers += 1
        if answer2 == 4:
            correct_answers += 1
        if answer3 == 1:
            correct_answers += 1
        if answer4 == 15:
            correct_answers += 1

        request.session['score'] = correct_answers
        request.session['tried_already'] = True   
        if correct_answers > 0:
            return redirect('finish')
        else:
            return redirect('fail')

    tried_already = request.session.get('tried_already', False)
    score = request.session.get('score', 0)

    if tried_already and score == 0:
        return HttpResponse("Cheater")
    else:
        request.session['tried_already'] = False
        return render(request, 'pages/quiz.html')
    
def finish(request):
    score = request.session.get('score', 0)
    if score > 0:
        return render(request, 'pages/finish.html', {'score': score})
    else: 
        return HttpResponse("Cheater")
    
def fail(request):
    score = request.session.get('score', 0)
    return render(request, 'pages/fail.html', {'score': score})

def raffle(request):
    if request.method == 'POST':
        name = request.POST.get('name', '').strip() 
        email = request.POST.get('email', '').strip() 

        RaffleEntry.objects.create(name=name, email=email)
        return HttpResponse("Thank you for participating in the raffle!")
    return redirect('finish')

def timedout(request):
    return render(request, 'pages/timedout.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('index')

    return render(request, 'pages/login.html')