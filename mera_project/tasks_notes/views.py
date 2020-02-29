from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

def profile_view(request):
	return render(request, 'tasks_notes/index.html')

def login_view(request):
	if request.method == 'POST':
		form= AuthenticationForm(data=request.POST)
		if form.is_valid():
			user=form.get_user()
			login(request,user)
			#return redirect('profile')
			return render (request, 'tasks_notes/index.html')
	else: 
		form= AuthenticationForm()
	return render(request, 'registeration/login.html', {'form':form})

def additem_view(request):
    name = request.POST['expense_name']    
    expense_cost = request.POST['cost']  
    expense_date = request.POST['expense_date']
    ExpenseInfo.objects.create(expense_name=name,cost=expense_cost,date_added=expense_date,user_expense=request.user)
    return HttpResponseRedirect('app')

def signup_view(request):
	if request.method == 'POST':
		form= UserCreationForm(request.POST)
		if form.is_valid():
			user=form.save()
			login(request,user)
			return redirect('login')
	else: 
		form=UserCreationForm()
	return render(request, 'tasks_notes/signup.html',{'form':form})

			