from django.urls import path
from django.contrib.auth import views as auth_views
from .views import  register, CustomLoginView, dashboard, transaction_form_view, transaction_list_view, goal_form_view, generate_report, goal_list_view, goal_delete, generate_bar_chart

urlpatterns = [
    path('', dashboard, name = 'dashboard'),
    path('login/', CustomLoginView.as_view(), name = 'login'),
    path('register/', register, name = 'register'),
    path('transaction/add/', transaction_form_view, name = 'transaction_add'),
    path('transactions/', transaction_list_view, name = 'transaction_list'),
    path('goal/add', goal_form_view, name = 'goal_add'),
    path('generate-report/', generate_report, name = 'generate_report'),
    path('goals/', goal_list_view, name  = 'goal_list'),
    path('goal/<int:id>/delete/', goal_delete, name  = 'goal_delete'),
    path('generate-chart/', generate_bar_chart, name  = 'generate_bar_chart'),
    
]
