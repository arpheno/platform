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
    response_data = {}
    trainers=["bkawlatow@gmail.com", "erginozgun1@gmail.com", "geo.gkioka@gmail.com", "serazification@gmail.com", "goran.vukalovic@gmail.com", "shomyserbia@gmail.com", "till.schultz@haw-hamburg.de", "tanju.kahyaoglu@gmail.com", "michalwesolkowski@gmail.com", "dominic.angerer@gmail.com", "arpheno@gmail.com", "gunda.cizevska@gmail.com", "irmabalic1@gmail.com", "petko.grozdanovski@eestec-sk.org.mk", "viktorijanikolovska@gmail.com", "oliver-richter@bluewin.ch", "bococan@hotmail.com", "daviddias.p@gmail.com", "dc.develi@gmail.com", "egondzic@gmail.com", "emincica@gmail.com", "geislert@student.ethz.ch", "matic.mj@gmail.com", "vanjapancic@gmail.com", "vukica.jekic@gmail.com", "thanvrat@gmail.com", "witowski.maciej@gmail.com", "xristoskonsta@gmail.com", "milosdenic88@gmail.com", "nesatdereli@gmail.com", "tackast@yahoo.com", "jmdbo1991@gmail.com", "eemreg@gmail.com", "emilia.buhaev@eestec.ro", "igorsocec@gmail.com", "mihaela.maracine@eestec.ro", "milossavicevic@gmail.com", "milica.fcdb.stupar@gmail.com", "uzupan@gmail.com", "polec.marta@gmail.com", "christoph.t.weber@gmail.com", "cosmin.rudeanu@eestec.ro", "d.materowski@gmail.com", "kasp.piotr@gmail.com", "mk.defender@gmail.com", "dukesapen@gmail.com", "hmduc85@gmail.com", "ivan.kovacevic12@gmail.com", "lexa.caprariu@gmail.com", "tolic.aleksandar@gmail.com", "nedimhadzija@gmail.com", "smajic.nermin@gmail.com", "renata.niedziela@gmail.com", "omurcankumtepe@gmail.com", "eddincer@gmail.com", "grega.kespret@gmail.com", "greggchrysos@gmail.com", "lukailic@gmail.com", "lukalacan@gmail.com", "blaz.roser@gmail.com", "cagatay@ieee.metu.edu.tr", "ionut.sava@eestec.ro", "ivan.kechina@gmail.com", "mario.markovic1985@gmail.com", "flavia.fiscu@gmail.com", "markovic.snezana@gmail.com", "kradulaski@gmail.com", "cvetkovic.stevan@gmail.com", "denisrudonja@gmail.com", "denizea@gmail.com", "dijana.karlecik@gmail.com", "faris.nizamic@gmail.com", "fbakhtiyar@gmail.com", "ozcanhu@gmail.com", "tagikhaniyev@gmail.com", "semir.hadzimuratovic@gmail.com", "borut.ceh@gmail.com", "marijanovic@gmail.com", "marko.obrknezev@gmail.com", "aleksandra321@gmail.com", "flo@chaoflow.net", "maria.viziteu@gmail.com", "dejan.pangercic@gmail.com"]

    if username not in trainers:
        response_data['status'] = 'notatrainer'
        response_data = json.dumps(response_data)
        return HttpResponse(response_data, content_type="application/json")
    try:
        user = User.objects.create_user(username, username, password)
        user.save()
        g = Group.objects.get(name='trainer')
        g.user_set.add(user)
        g.save()
        response_data['status'] = 'success'
    except:
        response_data['status'] = 'failure'
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
        fields = ['first_name', 'last_name', ]

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
