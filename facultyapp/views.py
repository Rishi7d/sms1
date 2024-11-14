from django.core.mail import send_mail
from django.shortcuts import render, redirect


# Create your views here.

def FacultyHomePage(request):
    return render(request, 'facultyapp/FacultyHomePage.html')

#def add_student(request):
#    if request.method == 'POST':
#        form = StudentForm(request.POST)
#        if form.is_valid():
#            form.save()
#            return redirect('student_list')
#    else:
#        form = StudentForm()
#    return render(request, 'facultyapp/add_student.html', {'form': form})

from django.contrib.auth.models import User
from .models import StudentList
from .forms import StudentForm, MarksForm
from django.shortcuts import redirect, render
def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            register_number = form.cleaned_data['Register_Number']
            try:
                user = User.objects.get(username=register_number)
                student.user = user  # Assign the matching User to the student
            except User.DoesNotExist:
                form.add_error('Register_Number', 'No user found with this Register Number')
                return render(request, 'facultyapp/add_student.html', {'form': form})
            student.save()
            return redirect('facultyapp/student_list')
    else:
        form = StudentForm()
    return render(request, 'facultyapp/add_student.html', {'form': form})


from .forms import AddCourseForm, StudentForm
def add_course(request):
    if request.method == 'POST':
        form = AddCourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('facultyapp:FacultyHomePage')
    else:
        form = AddCourseForm()
    return render(request, 'facultyapp/add_course.html', {'form': form})


from .models import AddCourse
from .models import StudentList

def student_list(request):
    course = request.GET.get('course')
    section = request.GET.get('section')
    student_courses = AddCourse.objects.all()
    if course:
        student_courses = student_courses.filter(course=course)
    if section:
        student_courses = student_courses.filter(section=section)
    students = StudentList.objects.filter(id__in=student_courses.values('student_id'))
    course_choices = AddCourse.COURSE_CHOICES
    section_choices = AddCourse.SECTION_CHOICES
    context = {
        'students': students,
        'course_choices': course_choices,
        'section_choices': section_choices,
        'selected_course': course,
        'selected_section': section,
    }
    return render(request, 'facultyapp/student_list.html', context)

from .models import StudentList

def post_marks(request):
    if request.method == "POST":
        form = MarksForm(request.POST)
        if form.is_valid():
            marks_instance = form.save(commit=False)
            marks_instance.save()

            # Retrieve the User email based on the student in the form
            student = marks_instance.student
            student_user = student.user
            user_email = student_user.email

            subject = 'Marks Entered'
            message = f'Hello, {student_user.first_name}  marks for {marks_instance.course} have been entered. Marks: {marks_instance.marks}'
            from_email = 'rishiraja118@gmail.com'
            recipient_list = [user_email]
            send_mail(subject, message, from_email, recipient_list)

            return render(request, 'facultyapp/post_marks.html')
    else:
        form = MarksForm()
    return render(request, 'facultyapp/post_marks.html', {'form': form})