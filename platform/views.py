from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
import logging
log = logging.getLogger(__name__)
def index(request):
    log.debug(request.user)
    return render(request, 'platform/index.html')
def contact(request):
    return render(request, 'platform/contact.html')
def header(request):
    return render(request, 'platform/header.html')
def logout(request):
    log.info("HELLO")
    auth_logout(request)
    return redirect('/')
def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            auth_login(request, user)
            return redirect('/')
            # Redirect to a success page.
        else:
            return render(request, 'trt/login/deactivated.html')
            # Return a 'disabled account' error message
    else:
        raise
        # Return an 'invalid login' error message.
        return render(request, 'login/invalid.html')
def manage_account(request):
    return
