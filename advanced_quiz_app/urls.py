from django.contrib import admin
from django.urls import path
from app.views import quiz, donequiz, login_user, home, quiz_details, fillform, user_logout,add_queations
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name='home'),
    path('add/<int:id>/',add_queations,name='add_queations'),
    path('<uuid:qid>/<int:id>/',fillform,name='fillform'),
    path('<uuid:qid>/<int:id>/<int:user_id>/',quiz,name='quiz'),
    path('quiz-deatils/<uuid:qid>/',quiz_details,name='quiz_details'),
    path('done/',donequiz,name='done_quiz'),
    path('login/',login_user,name='login_user'),
    path('logout/',login_user,name='logout_user')
]
