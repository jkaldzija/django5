from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from apps.users.serializers import MeSerializer


class MeView(generics.RetrieveAPIView):
    serializer_class = MeSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user
