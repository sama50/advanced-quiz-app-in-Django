from django.shortcuts import render, redirect
from django.contrib.auth import login,logout,authenticate
from app.models import TypeQuiz,QuizQuestions, OptionsOfQuiz, Candidates, CandidatesAnswer
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    if request.method == 'POST':
        quiz_name = request.POST.get('quiz_name')
        number_of_queation = request.POST.get('queation_number')
        quiz_type = TypeQuiz(user=request.user,name=quiz_name,number_of_queation=number_of_queation)
        quiz_type.save()
        return redirect(f"add/{quiz_type.id}/")
    user_created_quiz = TypeQuiz.objects.filter(user=request.user)
    return render(request,'home.html',{'user_quiz':user_created_quiz})

def quiz_details(request,qid):
    typequiz = TypeQuiz.objects.get(quiz_id=qid)
    queations = QuizQuestions.objects.filter(typequiz=typequiz)
    candidates = Candidates.objects.filter(quiz_type=typequiz)
    return render(request,'quiz_details.html',{'queations':queations,'candidates':candidates})

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request=request,username=username,password=password)
        print(user)
        if user is not None:
            login(request,user)
            return redirect('/')
    return render(request,'login.html')

def fillform(request,qid,id):
    if request.method == 'POST':
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        quiz_type = TypeQuiz.objects.get(quiz_id=qid)
        candidate = Candidates(quiz_type=quiz_type,email=email,first_name=first_name,last_name=last_name)
        candidate.save()
        return redirect(f"/{qid}/{id}/{candidate.id}")
    return render(request,'fillform.html')

def add_queations(request,id):
    typequiz=TypeQuiz.objects.get(id=id)
    if request.method == 'POST':
        queation = request.POST.get('queation')
        option1 = request.POST.get('option1')
        option2 = request.POST.get('option2')
        option3 = request.POST.get('option3')
        option4 = request.POST.get('option4')
        quiz_queation = QuizQuestions(typequiz=typequiz,title=queation)
        quiz_queation.save()
        OptionsOfQuiz(quiz_questions=quiz_queation,option=option1).save()
        OptionsOfQuiz(quiz_questions=quiz_queation,option=option2).save()
        OptionsOfQuiz(quiz_questions=quiz_queation,option=option3).save()
        OptionsOfQuiz(quiz_questions=quiz_queation,option=option4).save()
    queations = QuizQuestions.objects.filter(typequiz=typequiz)
    return render(request,'add_queations.html',{'queations':queations})

def quiz(request,qid,id,user_id):
    if request.method == 'POST': 
        print(request.POST['queations_id'])
        print(request.POST['selected_option'])
        print(user_id)
        if QuizQuestions.objects.filter(id=id).exists():
            quiz_type = TypeQuiz.objects.get(quiz_id=qid)
            candidate = Candidates.objects.get(id=user_id)
            queation = QuizQuestions.objects.get(id=request.POST['queations_id'])
            CandidatesAnswer(quiz_type=quiz_type,candidate=candidate,queation=queation,answer=request.POST['selected_option']).save()
            if QuizQuestions.objects.filter(id=id+1).exists():
                return redirect(f"/{qid}/{id+1}/{user_id}")
            return redirect(f"/done/")
    print("coming..............................")
    type_quiz = TypeQuiz.objects.get(quiz_id=qid)
    queations = QuizQuestions.objects.get(typequiz=type_quiz,id=id)
    return render(request,'quiz.html',{'queations':queations})

def donequiz(request):
    return render(request,'donepage.html')

def user_logout(request):
    logout(request)
    return redirect('login_user')
