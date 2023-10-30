from django.contrib import admin
from app.models import TypeQuiz,QuizQuestions, OptionsOfQuiz, Candidates, CandidatesAnswer
# Register your models here.

@admin.register(TypeQuiz)
class TypeQuizAdmin(admin.ModelAdmin):
    list_display = ('id','user','name','number_of_queation')



@admin.register(QuizQuestions)
class QuizQuestionsAdmin(admin.ModelAdmin):
    list_display = ('id','typequiz','title')


@admin.register(OptionsOfQuiz)
class OptionsOfQuizAdmin(admin.ModelAdmin):
    list_display = ('id','quiz_questions','option')

@admin.register(Candidates)
class CandidatesAdmin(admin.ModelAdmin):
    list_display = ('id','first_name','last_name','email')

@admin.register(CandidatesAnswer)
class CandidatesAnswerAdmin(admin.ModelAdmin):
    list_display = ('id','quiz_type','candidate','queation','answer')