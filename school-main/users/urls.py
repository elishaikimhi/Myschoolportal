from django.urls import path
from .views import SignUpView, TeacherSignUpView, StudentSignUpView


urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('signup/student/', StudentSignUpView.as_view(), name='student_signup'),
    path('signup/teacher/', TeacherSignUpView.as_view(), name='teacher_signup'),
]
