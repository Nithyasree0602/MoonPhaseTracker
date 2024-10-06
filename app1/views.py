from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from django.http import HttpResponse



def index(request):
    return render(request,'index.html')

def index1(request):
    return render(request,'login.html')

def index2(request):
    return render(request,'signup.html')

def index3(request):
    return render(request,'calender.html')

def index5(request):
    return render(request,'symptoms.html')

def index6(request):
    return render(request,'diet.html')

def index4(request):
    return render(request,'sett.html')

def index7(request):
    return render(request,'shop.html')


from django.contrib.auth import authenticate, login

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')  # Redirect to dashboard upon successful login
        else:
            return render(request, 'login.html', {'error_message': 'Invalid email or password'})
    else:
        return render(request, 'login.html')
    
    
    

from django.contrib.auth.models import User

def signup_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        # Check if the email is already registered
        if User.objects.filter(email=email).exists():
            return render(request, 'signup.html', {'error_message': 'Email is already registered'})
        # Create a new user
        user = User.objects.create_user(username=email, email=email, password=password)
        user.first_name = name
        user.save()
        # Redirect to login page upon successful sign-up
        return redirect('login')
    else:
        return render(request, 'signup.html')
    
    
from django.shortcuts import render
from django.http import JsonResponse

def settings_view(request):
    if request.method == 'POST':
        # Handle form submission here
        # You can access the form data using request.POST.get() or request.POST['field_name']
        # Save the settings to the database or perform any other necessary action
        return JsonResponse({'message': 'Settings saved successfully'})
    else:
        return render(request, 'sett.html')
    
from django.http import JsonResponse

def add_to_cart(request):
    if request.method == 'POST':
        # Retrieve data from the request
        product_name = request.POST.get('product_name')
        price = request.POST.get('price')
        
        # Process the data (e.g., add the product to the cart)
        # Here you might want to add the product to a session variable or database
        
        # Return a JSON response indicating success
        return JsonResponse({'message': 'Product added to cart successfully'})
    else:
        # Return an error response if the request method is not POST
        return JsonResponse({'error': 'Method not allowed'}, status=405)
    

