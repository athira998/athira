from django.shortcuts import render

# Create your views here.
from django.shortcuts import redirect, render
from studentapp . models import Student
# Create your views here.

def add_student1(request):
    return render(request,'addstudent.html')

def add_student_details(request):
    if request.method=='POST':
        sname=request.POST['s_name']
        saddress=request.POST['s_address']
        sage=request.POST['s_age']
        sgender=request.POST['s_gender']
        semail=request.POST['s_email']
        sjdate=request.POST['s_jdate']
        squalification=request.POST['s_qualification']
        spno=request.POST['s_pno']
        st=Student(s_name=sname,s_address=saddress,s_age=sage,s_gender=sgender,s_email=semail,s_jdate=sjdate,s_qualification=squalification,s_pno=spno)
        st.save()
        print('hi')
        return redirect('show_student')

def show_student(request):
    std=Student.objects.all()
    return render(request,'show.html',{'students':std})

def ind_details(request,pk):
    st=Student.objects.get(id=pk)
    return render(request,'ind.html',{'students':st})




def edit(request,pk):
    st=Student.objects.get(id=pk)
    return render(request,'edit.html',{'students':st})

def edit_student(request,pk):
    if request.method=='POST':
        st=Student.objects.get(id=pk)
        st.s_name=request.POST.get('s_name')
        st.s_address=request.POST.get('s_address')
        st.s_age=request.POST.get('s_age')
        st.s_gender=request.POST.get('s_gender')
        st.s_email=request.POST.get('s_email')
        st.s_jdate=request.POST.get('s_jdate')
        st.s_qualification=request.POST.get('s_qualification')
        st.s_pno=request.POST.get('s_pno')
        st.save()
        return redirect('show_student')
    return render(request,'edit.html')

def delete(request,pk):
    st=Student.objects.get(id=pk)
    st.delete()
    return redirect('show_student')