from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from django.shortcuts import redirect
from django.contrib import messages
from django.db.models import Sum
from .models import Transaction, Goal
from .forms import RegisterForm, TransactionForm, GoalForm
from .admin import TransactionResource
from io import BytesIO
import matplotlib.pyplot as plt
import numpy as np
# Create your views here.

@method_decorator(never_cache, name='dispatch')
class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    redirect_authenticated_user = True


@never_cache
def register(request):
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            messages.success(request, 'Account created successfully!')
            return redirect('dashboard')
    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form': form})


@never_cache
def dashboard(request):
    if request.user.is_authenticated:
        transactions = Transaction.objects.filter(user = request.user)
        goals = Goal.objects.filter(user = request.user)

        total_income = Transaction.objects.filter(user = request.user, transaction_type = 'Income').aggregate(total = Sum('amount'))['total'] or 0

        total_expense = Transaction.objects.filter(user = request.user, transaction_type = 'Expense').aggregate(total = Sum('amount'))['total'] or 0

        net_savings = total_income - total_expense

        remaining_savings = net_savings

        goal_progress = []
        for goal in goals:
            if remaining_savings >= goal.target_amount:
                goal_progress.append({'goal': goal, 'progress': 100 })
                remaining_savings = remaining_savings - goal.target_amount

            elif remaining_savings > 0:
                progress = (remaining_savings / goal.target_amount)* 100
                goal_progress.append({'goal': goal, 'progress': progress })
                remaining_savings = 0

            else:
                goal_progress.append({'goal': goal, 'progress': 0})

        context = {
            'transactions': transactions,
            'goals': goals,
            'total_income' :  total_income,
            'total_expense' : total_expense,
            'net_savings': net_savings,
            'goal_progress': goal_progress
        } 

    else:
        context = {
            'total_income' :  0,
            'total_expense' : 0,
            'net_savings': 0
        }

    return render(request, 'dashboard.html', context)

@login_required
def transaction_form_view(request):
    if request.method == "POST":
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save(commit = False)
            transaction.user = request.user
            transaction.save()
            messages.success(request, 'Transaction added successfully!')
            return redirect('dashboard')
    else:
        form = TransactionForm()

    return render(request, 'add_transaction.html', {'form': form})


@login_required
def transaction_list_view(request):
    transactions = Transaction.objects.filter(user = request.user)

    return render(request, 'transaction_list.html', {'transactions': transactions})


@login_required
def goal_form_view(request):
    if request.method == "POST":
        form = GoalForm(request.POST)
        if form.is_valid():
            goal = form.save(commit = False)
            goal.user = request.user
            goal.save()
            messages.success(request, 'Goal created successfully!')
            return redirect('dashboard')
    else:
        form = GoalForm()

    return render(request, 'add_goal.html', {'form': form})


@login_required
def generate_report(request):
    user_transactions = Transaction.objects.filter(user = request.user)
    dataset = TransactionResource().export(user_transactions)
    response = HttpResponse(dataset.csv, content_type = 'text/csv; charset = utf-8')
    response['Content-Disposition'] = 'attachment; filename = "Transaction_report.csv"'

    return response


@login_required
def goal_list_view(request):
    goals = Goal.objects.filter(user = request.user)

    return render(request, 'goal_list.html', {'goals': goals})
 

@login_required
def goal_delete(request, id):
    goal = get_object_or_404(Goal, pk = id)

    if request.method == "POST":
        goal.delete()
        messages.success(request, 'Goal deleted successfully!')
        return redirect('goal_list')
    
    
@login_required
def generate_bar_chart(request):
    transactions = Transaction.objects.filter(user=request.user)

     # Aggregate Income by date
    income_data = transactions.filter(transaction_type='Income') \
                              .values('date') \
                              .annotate(total_income=Sum('amount')) \
                              .order_by('date')
    # Aggregate Expense by date
    expense_data = transactions.filter(transaction_type='Expense') \
                               .values('date') \
                               .annotate(total_expense=Sum('amount')) \
                               .order_by('date')

    # Get all unique dates
    all_dates = sorted(set([item['date'] for item in income_data] + [item['date'] for item in expense_data]))
    dates_str = [d.strftime('%Y-%m-%d') for d in all_dates]

    # Prepare income and expense lists aligned to all_dates
    income_amounts = [float(next((item['total_income'] for item in income_data if item['date'] == d), 0)) for d in all_dates]
    expense_amounts = [float(next((item['total_expense'] for item in expense_data if item['date'] == d), 0)) for d in all_dates]

    # Create grouped bar chart
    x = np.arange(len(all_dates))  # label locations
    width = 0.4  # width of bars

    plt.figure(figsize=(12, 6))
    plt.bar(x - width/2, income_amounts, width, label='Income', color='green')
    plt.bar(x + width/2, expense_amounts, width, label='Expense', color='red')
    plt.xlabel('Date')
    plt.ylabel('Amount')
    plt.title('Income vs Expense Over Time')
    plt.xticks(x, dates_str, rotation=45, ha='right')
    plt.legend()
    plt.tight_layout()

    # Save chart to BytesIO
    buffer = BytesIO()
    plt.savefig(buffer, format='pdf')
    plt.close()
    buffer.seek(0)

    response = HttpResponse(buffer, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename = Income_vs_Expense.pdf'
    return response