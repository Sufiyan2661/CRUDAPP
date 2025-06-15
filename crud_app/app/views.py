from django.conf import settings
from django.shortcuts import render,redirect,HttpResponse
from .forms import UserForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import NewStudent
from .forms import ContactForm
from django.core.mail import send_mail,BadHeaderError
# Create your views here.


def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')


def registration(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            password = form.cleaned_data['password']
            
            
            
            User.objects.create_user(
                username=username,
                email=email,
                first_name=first_name,
                last_name=last_name,
                password=password
            )
            
            
            
            user = authenticate(
                username=username,
                password=password
            )
            
            
            if user is not None:
                login(request,user)
                
            return redirect('data')
    else:
        form = UserForm()
        
    return render(request,'registration.html',{'forms':form})



def user_login(request):
    if request.method == 'POST':
        username = request.POST['user']
        password = request.POST['pas']
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('data')
        else:
            messages.error(request,'Username and password didn`t match')
    return render(request,'login.html')



def contact(request):
    
    form = ContactForm(request.POST or None)
    print("The contac")
    if form.is_valid():
        email = form.cleaned_data.get('email')
        message = form.cleaned_data.get('message')
        name = form.cleaned_data.get('name')
        subject = 'Site contact form'
        from_email = settings.EMAIL_HOST_USER
        to_email = [email]
        contact_message = f"{name,message,email}"
        
        try:
            send_mail(subject,contact_message,from_email,to_email)
        except BadHeaderError:
            return HttpResponse('Invalid header found')
        return redirect('sucess')
    context = {
        'form':form,
    }
    return render(request,'contact.html',context)

@login_required
def data(request):
    data  = NewStudent.objects.all()
    context={"data":data}
    return render(request,'data.html',context)



@login_required
def insertData(request):
    print("The function get called")
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        age = request.POST.get('age')
        gender = request.POST.get('gender')

        query = NewStudent(
            name=name,
            email=email,
            age=age,
            gender=gender
        )
        query.save()
        messages.success(request, "Data Inserted Successfully")
        print("Data inserted Succesfully")
        return redirect('data')  # safe redirect

    # If accessed via GET, redirect to data view instead of rendering directly
    return redirect('data')



@login_required
def updateData(request,id):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        age = request.POST['age']
        gender = request.POST['gender']
        
        
        
        edit = NewStudent.objects.get(id=id)
        edit.name=name
        edit.email=email
        edit.age=age
        edit.gender=gender
        edit.save()
        messages.warning(request,'Data Updated Successfully') 
        return redirect('data')
    d = NewStudent.objects.get(id=id)
    context={'d':d}
    return render(request,'edit.html',context)




def deleteData(request,id):
    d=NewStudent.objects.get(id=id)
    d.delete()
    messages.error(request,'Data deleted Successfully')
    return redirect('data')



def succes(request):
    return render(request,'succes.html')

       






    



