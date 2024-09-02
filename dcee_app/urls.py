from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('login/', views.login_view, name='login'),
    path('pdf_upload/', views.pdf_upload, name='pdf_upload'),
    path('question_answer/', views.question_answer, name='question_answer'),
    path('password-reset/', views.forgot_password_view, name='password_reset'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='forgot_password.html'), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
    path('about/', views.about, name='about'),
    path('', views.index, name='index'),
    path('vote/', views.vote, name='vote'),
    path('all-questions/', views.all_questions, name='all_questions'),
    
]
