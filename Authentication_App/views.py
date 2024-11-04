from django.shortcuts import render, redirect
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate, login, logout
from customauth.models import MyUser
from django.http import JsonResponse
import jdatetime

def singup(request):  # This function is just for phone_number accept
    phone_number = request.GET.get('phone_number', None)  # Get phone_number
    data = {
        'is_taken': MyUser.objects.filter(phone_number=phone_number).exists()  # Check phone_number
    }
    return JsonResponse(data)

def signup_show(request):
    context = {"response": []}  # For messages
    
    if request.user.is_authenticated:  # If user is already logged in
        return redirect('/')  # Redirect to homepage
    
    if request.method == "POST":  # For registering
        full_name = request.POST.get('full_name')
        phone_number = request.POST.get('phone_number')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        
        if MyUser.objects.filter(phone_number=phone_number).exists():
            return JsonResponse({'error': 'این شماره تلفن قبلاً ثبت شده است.'})        

        if password1 != password2:  # If passwords don't match
            context['response'].append('رمز عبور ها مطابقت ندارند')
            return render(request, 'Login_app/SingUp.html', context) 

        # Create the user using your custom manager
        user = MyUser.objects.create_user(phone_number=phone_number, password=password1, full_name=full_name) 
        login(request, user)  # Automatically log in the user after registration       
        return redirect('/')  # Redirect to homepage
    
    return render(request, "Authentication_App/signup.html", context)


def login_show (request):
    if request.user.is_authenticated == True: #It says, if user has done authenticate, you gotta donnt watch Login page to that person
        return redirect('/') #go to this link : http://127.0.0.1:8000/
        
    if request.method == "POST": 
        phone_number = request.POST.get('phone_number') #get phone_number's
        password = request.POST.get('password') #get passwords's text
        user = authenticate(request, phone_number =phone_number, password= password) #check password and phone_number

        if user is not None: # if informations were correct
            login(request, user) # enter to your pannel
            return redirect('/') #go to this link : http://127.0.0.1:8000/
            
    return render(request, "Authentication_App/login.html")


def profile_show(request):
    user = request.user 

    if request.method == "POST":
        gender = request.POST.get('gender', user.gender)

        # Date of Birth Handling
        day = request.POST.get('day')
        month = request.POST.get('month')
        year = request.POST.get('date')  # Year field

        if day and month and year:
            try:
                # Convert to a Jalali date and then to a Gregorian date for saving
                jalali_date = jdatetime.date(int(year), int(month), int(day))
                date_of_birth = jalali_date.togregorian().strftime("%Y-%m-%d")
                user.date_of_birth = date_of_birth
            except (ValueError, ValidationError):
                # Handle invalid date (e.g., user entered incorrect day, month, or year)
                return render(request, "Authentication_App/profile.html", {
                    'user': user,
                    'error_message': "Please enter a valid date."
                })
        
        # Handle other fields as before
        email = request.POST.get('email', user.email)
        country = request.POST.get('country', user.country)
        state = request.POST.get('state', user.state)
        city = request.POST.get('city', user.city)
        profile_picture = request.FILES.get('profile_picture', user.profile_picture)

        # Update user fields if new data is provided
        user.gender = gender
        user.email = email
        user.country = country
        user.state = state
        user.city = city
        if profile_picture:
            user.profile_picture = profile_picture  # Update only if a new image is uploaded

        user.save()
        return redirect('/')
    
    return render(request, "Authentication_App/profile.html", {'user': user})



def Logout_show(request): #for logout 
    logout(request)
    return redirect('/') #go to this link : http://127.0.0.1:8000/



            
