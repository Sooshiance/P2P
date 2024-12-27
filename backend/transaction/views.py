from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .repositories import SharedFileRepository, PeerRepository
from .serializers import (
    SharedFileSerializer,
    PeerSerializer,
)
from .tasks import delete_shared_file_async


class SharedFileListCreateAPIView(generics.ListCreateAPIView):
    queryset = SharedFileRepository.get_all_shared_files()
    serializer_class = SharedFileSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer: SharedFileSerializer):
        owner = self.request.user
        file = self.request.data.get("file")
        name = self.request.data.get("name")
        SharedFileRepository.create_shared_file(owner=owner, file=file, name=name)


class SharedFileDetailAPIView(generics.RetrieveDestroyAPIView):
    queryset = SharedFileRepository.get_all_shared_files()
    serializer_class = SharedFileSerializer
    permission_classes = [IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        file_id = self.kwargs.get("pk")
        delete_shared_file_async.delay(file_id)
        return Response(status=status.HTTP_204_NO_CONTENT)


class PeerListCreateAPIView(generics.ListCreateAPIView):
    queryset = PeerRepository.get_all_peers()
    serializer_class = PeerSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        ip_address = self.request.client_ip
        PeerRepository.create_peer(user=user, ip_address=ip_address)


class PeerDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PeerRepository.get_all_peers()
    serializer_class = PeerSerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        user = self.request.user
        ip_address = self.request.client_ip
        PeerRepository.update_peer_ip(user=user, ip_address=ip_address)
