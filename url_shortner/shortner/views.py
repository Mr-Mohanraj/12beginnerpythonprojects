from django.shortcuts import render, redirect
from . import models
from random import randint


# Create your views here.
def index(request):
    if request.method == 'POST':
        old_short_link = request.POST['short_link']
        print(old_short_link)
        short_link_ = models.UrlLink.objects.filter(short_link=old_short_link).get()
        print(type(short_link_.link))
        return redirect(short_link_.link)
    return render(request, 'index.html')


def shortLink():
    short_link = ''.join([str(randint(0, 9)) for _ in range(10)])
    return short_link


def home(request):
    if request.method == 'POST':
        shortlink = shortLink()
        full_link = request.POST['link']
        data_link = models.UrlLink(link=full_link, short_link=shortlink)
        data_link.save()
    link_list = models.UrlLink.objects.all()
    context = {"link_list": link_list}
    return render(request, template_name='main.html', context=context)
