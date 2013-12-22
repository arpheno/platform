from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
def logout(request):
    auth_logout(request)
    return redirect('/trt/')
def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            auth_login(request, user)
            return redirect('/trt/')
            return render(request, 'trt/index.html')
            # Redirect to a success page.
        else:
            return render(request, 'trt/login/deactivated.html')
            # Return a 'disabled account' error message
    else:
        # Return an 'invalid login' error message.
        return render(request, 'trt/login/invalid.html')
def manage_account(request):
    return
