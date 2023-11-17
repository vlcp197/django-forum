from django.http import HttpResponse
from models import Board


def home(request):
    boards = Board.objects.all()
    boards_names = list()

    for board in boards:
        boards_names.append(board)

    response_html = '<br>'.join(boards_names)

    return HttpResponse(response_html)
