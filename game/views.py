import re
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render

from game.forms import SearchGameForm
from game.models import GameData, Move


def index(request):
    context = {
        'form': SearchGameForm(),
    }
    return render(request, 'game/index.html', context)


def get_games(moverow):
    moves = []
    moveitem = moverow.split(" ")
    for move in moveitem:
        if '.' in move:
            if re.search('[a-zA-Z]', move):moves.append(move.split('.')[1])
        else:
            if re.search('[a-zA-Z]', move):moves.append(move)
    count = GameData.objects.filter(moves__move_no=1,moves__move=moves[0]).count()
    games = []
    if count:
        games = GameData.objects.filter(moves__move_no=1,moves__move=moves[0])[:5]
    return count,games


def search_by_moves(request):
    form = SearchGameForm(request.POST)
    context = {}
    if form.is_valid():
        moves = form.cleaned_data.get('moves','')
        count, games = get_games(moves)
        context.update({'moves':moves, 'games':games, 'count':count})
        return render(request,'game/search_by_moves.html', context)
    return HttpResponseRedirect(reverse('game:index'))
