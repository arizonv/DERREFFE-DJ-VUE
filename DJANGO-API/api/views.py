from api.models import User
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers.UserSerializers import listSerializer

@api_view(['GET'])
def user_list(request):
    queryset = User.objects.all()
    serializer = listSerializer(queryset, many=True)

    return Response(serializer.data)

