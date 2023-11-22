from rest_framework.response import Response
from rest_framework.views import APIView

from apps.models import *


class AddNewBoard(APIView):
    def post(self, request):
        new_boards = request.data['boards']
        for newBoard in new_boards:
            board = Board.objects.create(
                name=newBoard
            )
            board.save()
        return Response({"reason": "版块初始化成功"}, status=200)
