from django.shortcuts import render,redirect
from .forms import SignUpForm, LoginForm
from django.contrib.auth import authenticate, login,logout
from .models import Vehicle

# Create your views here.

def index(request):
    return render(request, 'index.html')

def home(request):
    return render(request,'home.html')

def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_adim:
                login(request, user)
                return redirect('displaydetails')
            elif user is not None and user.is_superuse:
                login(request, user)
                return redirect('displaydetails')
            elif user is not None and user.is_use:
                login(request, user)
                return redirect('displaydetails')
            else:
                msg= 'invalid credentials'
        else:
            msg = 'error validating form'
    return render(request, 'login.html', {'form': form, 'msg': msg})

def register(request):
    msg = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            msg = 'user created'
            return redirect('login_view')
        else:
            msg = 'form is not valid'
    else:
        form = SignUpForm()
    return render(request,'register.html', {'form': form, 'msg': msg})

def logout_view(request):
    logout(request)
    return redirect('index')

def detailsadd(request):
    if request.method == 'POST':
            vehicle_number = request.POST.get('vehicle_number')
            vehicle_type = request.POST.get('vehicle_type')
            vehicle_model = request.POST.get('vehicle_model')
            vehicle_description = request.POST.get('vehicle_description')
            vechadd = Vehicle( vehicle_number=vehicle_number, vehicle_type=vehicle_type, vehicle_model=vehicle_model, vehicle_description=vehicle_description)
            vechadd.save()
            return render(request,'detailsadd.html',{"empaddnote":"Successfully Added Vechile"})
    elif not request.user.is_authenticated:
        return redirect('login.html')
    else:
        return render(request,'detailsadd.html',{"empnotaddnote":"No Vechile Added Try Again"})
    
def vechile_list(request):
    if not request.user.is_authenticated:
        return redirect('login.html')
    else:
        vechile_details = Vehicle.objects.all()
        return render(request, 'displaydetails.html',{'vechile_details': vechile_details})
    
def delete_data(request,vehicle_number):
    if not request.user.is_authenticated:
        return redirect('login.html')
    else:
        Vehicle.objects.filter(id=vehicle_number).delete()
        return redirect('displaydetails')
    
def editdetails(request,vehicle_number):
    my_vech_data = Vehicle.objects.get(id=vehicle_number)
    return render(request, 'editdetails.html',{'my_vech_data':my_vech_data})

def update_data(request,vehicle_number):
    my_vech_data = Vehicle.objects.get(id=vehicle_number)
    my_vech_data.vehicle_number = request.POST['vehicle_number']
    my_vech_data.vehicle_type = request.POST['vehicle_type']
    my_vech_data.vehicle_model = request.POST['vehicle_model']
    my_vech_data.vehicle_description = request.POST['vehicle_description']
    my_vech_data.save()
    return redirect('displaydetails')



