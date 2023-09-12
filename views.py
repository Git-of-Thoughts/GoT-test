from django.shortcuts import render
from .models import Board, Pin, Comment, Follow

def home(request):
    boards = Board.objects.all()
    return render(request, 'home.html', {'boards': boards})

def board_detail(request, board_id):
    board = Board.objects.get(id=board_id)
    return render(request, 'board_detail.html', {'board': board})

def pin_detail(request, pin_id):
    pin = Pin.objects.get(id=pin_id)
    return render(request, 'pin_detail.html', {'pin': pin})

def comment_detail(request, comment_id):
    comment = Comment.objects.get(id=comment_id)
    return render(request, 'comment_detail.html', {'comment': comment})

def follow_detail(request, follow_id):
    follow = Follow.objects.get(id=follow_id)
    return render(request, 'follow_detail.html', {'follow': follow})
