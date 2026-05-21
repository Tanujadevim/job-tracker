from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Job
from .forms import JobForm

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('job_list')
    else:
        form = UserCreationForm()
    return render(request, 'jobs/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('job_list')
    else:
        form = AuthenticationForm()
    return render(request, 'jobs/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def job_list(request):
    jobs = Job.objects.filter(user=request.user)
    return render(request, 'jobs/job_list.html', {'jobs': jobs})

@login_required
def job_add(request):
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.user = request.user
            job.save()
            return redirect('job_list')
    else:
        form = JobForm()
    return render(request, 'jobs/job_form.html', {'form': form, 'title': 'Add Job'})

@login_required
def job_edit(request, pk):
    job = get_object_or_404(Job, pk=pk, user=request.user)
    if request.method == 'POST':
        form = JobForm(request.POST, instance=job)
        if form.is_valid():
            form.save()
            return redirect('job_list')
    else:
        form = JobForm(instance=job)
    return render(request, 'jobs/job_form.html', {'form': form, 'title': 'Edit Job'})

@login_required
def job_delete(request, pk):
    job = get_object_or_404(Job, pk=pk, user=request.user)
    if request.method == 'POST':
        job.delete()
        return redirect('job_list')
    return render(request, 'jobs/job_confirm_delete.html', {'job': job})