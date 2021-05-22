from rest_framework import generics
from rest_framework.response import Response


from core.models import Client
from core.serializers import ClientSerializer

# Create your views here.
class ClientList(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = ClientSerializer(queryset, many=True)
        return Response(serializer.data)
