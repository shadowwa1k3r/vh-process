from rest_framework.response import Response
from rest_framework.views import APIView
from videoprocessing.tasks import create_task


class VideoProcessAPIView(APIView):
    def post(self, request):
        id = request.data.get('id')
        name = request.data.get('name')
        print(request.data)
        task = create_task.delay(id, name)
        return Response(status=200)


