from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

from .models import Members


def index(request):
    my_members = Members.objects.all().values()
    template = loader.get_template('index.html')
    context = {
        'my_members': my_members,
    }
    return HttpResponse(template.render(context, request))


def add(request):
    template = loader.get_template('add.html')
    return HttpResponse(template.render({}, request))


def add_record(request):
    first = request.POST['first']
    last = request.POST['last']
    member = Members(firstname=first, lastname=last)
    member.save()
    return HttpResponseRedirect(reverse('index'))


def delete(request, id):
    member = Members.objects.get(id=id)
    member.delete()
    return HttpResponseRedirect(reverse('index'))


def update(request, id):
    my_member = Members.objects.get(id=id)
    template = loader.get_template('update.html')
    context = {
        'my_member': my_member,
    }
    return HttpResponse(template.render(context, request))


def update_record(request, id):
    first = request.POST['first']
    last = request.POST['last']
    member = Members.objects.get(id=id)
    member.firstname = first
    member.lastname = last
    member.save()
    return HttpResponseRedirect(reverse('index'))
