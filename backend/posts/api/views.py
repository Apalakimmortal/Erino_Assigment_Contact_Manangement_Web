from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from ..models import User
from .serializers import UserSerializer
from rest_framework.response import Response



class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=True, methods=['put'])
    def update_contact(self, request, pk=None):
        contact = self.get_object()
        serializer = UserSerializer(contact, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    @action(detail=True, methods=['delete'])
    def delete_contact(self, request, pk=None):
        contact = self.get_object()
        contact.delete()
        return Response(status=204)