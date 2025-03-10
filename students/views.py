from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Student
from .forms import StudentForm

def home(request):
    students = Student.objects.all()
    form = StudentForm()
    
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    
    context = {
        'students': students,
        'form': form,
    }
    return render(request, 'students/home.html', context)

def update_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = StudentForm(instance=student)
    
    context = {
        'form': form,
        'student': student,
    }
    return render(request, 'students/update_student.html', context)

def delete_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    
    if request.method == 'POST':
        student.delete()
        return redirect('home')
    
    context = {
        'student': student,
    }
    return render(request, 'students/delete_student.html', context)
