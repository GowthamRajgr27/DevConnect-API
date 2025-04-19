from rest_framework import generics, permissions
from .models import Profile
from .serializers import ProfileSerializer

class ProfileCreateView(generics.CreateAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ProfileDetailView(generics.RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class ConnectView(generics.UpdateAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        profile = Profile.objects.get(user=request.user)
        target = Profile.objects.get(pk=pk)
        if target in profile.connections.all():
            profile.connections.remove(target)
        else:
            profile.connections.add(target)
        profile.save()
        return Response({'status': 'updated'})
