from django.shortcuts import render, redirect, get_object_or_404
from .forms import StudentForm
from .models import Student
# Create your views here.



def student_form(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('student_list')

    else:
        form = StudentForm()

    return render(request, 'student_form.html', {'form': form})


def student_list(request):
    student_list = Student.objects.all()
    ctx = {'student_list': student_list}
    return render(request, 'student_list.html', ctx)

def student_edit(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)

    return render(request, 'student_form.html', {'form': form})

def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    student.delete()
    return redirect('student_list')