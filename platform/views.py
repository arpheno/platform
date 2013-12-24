from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User
import logging
from forms import AccountForm
from django.views.generic import UpdateView
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
class Account(UpdateView):
    form_class = AccountForm
    model = User
    template_name = 'platform/account.html'

    def get(self, request, **kwargs):
        self.object = User.objects.get(username=self.request.user)
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        context = self.get_context_data(object=self.object, form=form)
        return self.render_to_response(context)

    def get_object(self, queryset=None):
        return self.request.user
