from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView
from . models import ApiList, ActiveApiList
# Create your views here.

class ApiView(TemplateView):
    template_name = "user_dashboard/dashboard.html"

    def get_context_data(self, **kwargs):
        context = super(ApiView, self).get_context_data(**kwargs)
        context['api_lists'] = ApiList.objects.all()
        return context

    def addapi(self, request, *args, **kwargs):
        context = super(ApiView, self).get_context_data(**kwargs)
        context['mylist'] = ApiList.objects.get(pk=id)
        mylist = []
        if request:
            mylist.append(context)
        return render(request, self.template_name, {'mylist': mylist})

class ConfigureApiView(TemplateView):
    template_name = 'user_dashboard/configure_api.html'


