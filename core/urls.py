from django.urls import path
from .views import *

app_name = 'core'
urlpatterns = [
    path('', index_home, name="home"),
    path('post-new-question', post_question, name="add_question"),
    path('question/<int:id>/', question_overview, name="question_detail"),
    path('likes-answer/<int:id>/', like_answer, name="likes_answer"),
    
]
