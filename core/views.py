from django.shortcuts import render,redirect,get_object_or_404

# Create your views here.
from .models import Question, Answer
from .forms import  PostQuestionForm,AnswerForm
from django.http import HttpResponseNotAllowed
from django.contrib.auth.decorators import login_required

@login_required
def index_home(request):
    questions = Question.objects.all()
    return render(request, "core/home.html", {'questions': questions})



@login_required
def post_question(request):
    if request.method == 'POST':
        form = PostQuestionForm(request.POST)
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        return redirect('core:home')

    else:
        form = PostQuestionForm()
        return render(request, "core/add-quest.html", {'form':form})

@login_required
def question_overview(request, id):
    question = get_object_or_404(Question, id=id)
    answers = Answer.objects.filter(question=question)
    if request.method == 'POST':
        if request.user == question.user:
            return redirect('core:home')
        form = AnswerForm(request.POST)
        instance = form.save(commit=False)
        instance.user = request.user
        instance.question = question
        instance.save()
        return redirect('core:home')
    else:
        form = AnswerForm()
        return render(request, 'core/detail.html',{'question':question,'form':form,'answers':answers})
    


from django.http import JsonResponse
from django.db.models import F
@login_required
def like_answer(request, id):
    answer = get_object_or_404(Answer, id=id)

    # Prevent users from liking their own answer
    if request.user == answer.user:
        return JsonResponse({'error': "You cannot like your own answer"}, status=400)

    # Atomic update to prevent race conditions
    Answer.objects.filter(id=id).update(likes=F('likes') + 1)
    
    # Fetch the updated answer
    updated_answer = Answer.objects.get(id=id)
    
    return JsonResponse({'likes': updated_answer.likes})
