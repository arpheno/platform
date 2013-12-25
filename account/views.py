from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import *
from django.views.generic import UpdateView
from django.utils.translation import gettext as _
from django.contrib.auth.models import Group


def new(request):
    username = request.POST['username']
    password = request.POST['password']
    user = User.objects.create_user(username,username, username)
    user.is_staff = True
    g = Group.objects.get(name='dbteam')
    g.user_set.add(user)
    user.save()
    return redirect('/')

def out(request):
    logout(request)
    return redirect('/')
def auth(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'trt/login/deactivated.html')
    else:
        return render(request, 'login/invalid.html')

class AccountForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','email',]
    def __init__(self, *args, **kwargs):
        super(AccountForm, self).__init__(*args, **kwargs)
        f = self.fields.get('user_permissions', None)
        if f is not None:
            f.queryset = f.queryset.select_related('content_type')
class UserProfile(UpdateView):
    form_class = AccountForm
    template_name = 'account/profile.html'
    def post(self, request, **kwargs):
        instance = User.objects.get(username=self.request.user)
        form = AccountForm(request.POST,instance=instance) # A form bound to the POST data
        #if form.is_valid(): # All validation rules pass
        form.save()
        return redirect('/')
    def get(self, request, **kwargs):
        self.object = User.objects.get(username=self.request.user)
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        context = self.get_context_data(object=self.object, form=form)
        return self.render_to_response(context)
    def get_object(self, queryset=None):
        return self.request.user
