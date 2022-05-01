from django.shortcuts import render, redirect

from word.models import Word


def index(request):
    word = Word.objects.filter(iremember=False).order_by('?')[0]
    return render(request, 'webapp/index.html', {'word': word})


def iremember(request, id):
    word = Word.objects.get(id=id)
    word.iremember = True
    word.save()
    return redirect('/')