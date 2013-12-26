from django.shortcuts import render
from django.views.generic.base import View


class History(View):

    def get(self, request, **kwargs):
        return render(request, 'history/index.html')
