from django.shortcuts import render


def index(request):
    context = {
        'msg': "hello",
    }
    return render(request, 'game/index.html', context)
