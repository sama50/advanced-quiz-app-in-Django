from django.db import models
from django.contrib.auth.models import User
import uuid
# Create your models here.

class TypeQuiz(models.Model):
    user = models.ForeignKey(to=User,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    number_of_queation = models.IntegerField(default=0)
    quiz_id = models.UUIDField(default=uuid.uuid4())
    def __str__(self):
        return f"{self.name}"
    def first_queation(self):
        if QuizQuestions.objects.filter(typequiz=self).exists():
            return QuizQuestions.objects.filter(typequiz=self).first().id
        return -1

class QuizQuestions(models.Model):
    typequiz = models.ForeignKey(to=TypeQuiz, on_delete=models.CASCADE)
    title = models.TextField()

    def __str__(self):
        return f"{self.title}"
    
    def quiz_options(self):
        return OptionsOfQuiz.objects.filter(quiz_questions=self)

class OptionsOfQuiz(models.Model):
    quiz_questions = models.ForeignKey(to=QuizQuestions, on_delete=models.CASCADE)
    option = models.CharField(max_length=256)

    def __str__(self):
        return f"{self.quiz_questions.title} -> {self.option}"

class Candidates(models.Model): 
    quiz_type = models.ForeignKey(to=TypeQuiz,on_delete=models.CASCADE,default=None)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(max_length=30)

    def __str__(self):
        return self.email

class CandidatesAnswer(models.Model):
    quiz_type = models.ForeignKey(to=TypeQuiz,on_delete=models.CASCADE)
    candidate = models.ForeignKey(to=Candidates,on_delete=models.CASCADE)
    queation = models.ForeignKey(to=QuizQuestions,on_delete=models.CASCADE)
    answer = models.CharField(max_length=256)
