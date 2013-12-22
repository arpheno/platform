from django.shortcuts import render, redirect
from elfinder.views import ElfinderConnectorView

from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
def manage_account(request):
    return
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
def index(request):
    return render(request, 'trt/index.html')
def header(request):
    return render(request, 'trt/header.html')
def materials(request):
    if request.is_ajax():
        return render(request, 'trt/elfinder-partial.html')
    return render(request, 'trt/elfinder.html')
def connector(request):
    connector_view=ElfinderConnectorView.as_view()
    if request.user.is_superuser:
        response=connector_view(request,optionset="admin",start_path="default")
    elif request.user.is_staff:
        response=connector_view(request,optionset="staff",start_path="default")
    elif request.user.is_authenticated():
        group = request.user.groups.all()[0].name
        response=connector_view(request,optionset=group,start_path="default")
    else:
        response=connector_view(request,optionset="anon",start_path="default")
    return response
