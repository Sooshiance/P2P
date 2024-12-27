from django.shortcuts import get_object_or_404

from rest_framework import exceptions

from .models import SharedFile, Peer
from .validators import allowed_files_validator

from user.models import User


class SharedFileRepository:
    @staticmethod
    def get_shared_file(file_id):
        return get_object_or_404(SharedFile, pk=file_id)

    @staticmethod
    def create_shared_file(owner, file, name: str):
        # try:
        #     allowed_files_validator(file)
        # except exceptions.NotAcceptable as e:
        #     raise exceptions.ValidationError(detail=str(e))
        shared_file = SharedFile.objects.create(
            owner=owner, file=file, name=name
        ).save()
        return shared_file

    @staticmethod
    def get_shared_files_by_owner(owner: User):
        return SharedFile.objects.filter(owner=owner)

    @staticmethod
    def delete_shared_file(file_id):
        shared_file = __class__.get_shared_file(file_id)
        shared_file.delete()

    @staticmethod
    def get_all_shared_files():
        return SharedFile.objects.all()


class PeerRepository:
    @staticmethod
    def get_peer_by_user(user) -> Peer:
        return Peer.objects.filter(user=user).first()

    @staticmethod
    def get_peer(peer_id):
        return get_object_or_404(Peer, pk=peer_id)

    @staticmethod
    def create_peer(user, ip_address):
        peer = Peer.objects.create(user=user, ip_address=ip_address)
        return peer

    @staticmethod
    def update_peer_ip(user: User, ip_address):
        peer: Peer = __class__.get_peer_by_user(user)
        peer.ip_address = ip_address
        peer.save()
        return peer

    @staticmethod
    def get_all_peers():
        return Peer.objects.all()

    @staticmethod
    def delete_peer(peer_id):
        peer: Peer = __class__.get_peer(peer_id)
        peer.delete()
