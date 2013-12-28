from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.views.generic import UpdateView
from django.contrib.auth.models import Group
from django.forms import ModelForm
import json
from django.http import HttpResponse


def new(request):
    username = request.POST['username']
    password = request.POST['password']
    user = User.objects.create_user(username, username, password)
    user.is_active = False
    user.save()
    response_data = {}
    response_data['status'] = 'success'
    response_data = json.dumps(response_data)
    return HttpResponse(response_data, content_type="application/json")


def out(request):
    logout(request)
    return redirect('/')


def auth(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    data = {}
    if user is not None:
        if user.is_active:
            login(request, user)
            if user.is_staff:
                data['staff'] = True
            else:
                data['staff'] = False
            data['status'] = 'success'
            data = json.dumps(data)
            return HttpResponse(data, content_type="application/json")
        else:
            data['status'] = 'inactive'
    else:
        data['status'] = 'invalid'
    return HttpResponse(json.dumps(data), content_type="application/json")


class AccountForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', ]

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
        form = AccountForm(request.POST, instance=instance)
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
