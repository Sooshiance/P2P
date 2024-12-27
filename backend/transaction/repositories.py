from typing import BinaryIO

from django.shortcuts import get_object_or_404

from .models import SharedFile, Peer
from user.models import User

class SharedFileRepository:
    @classmethod
    def get_shared_file(file_id):
        return get_object_or_404(SharedFile, pk=file_id)

    @classmethod
    def create_shared_file(owner: User, file: BinaryIO, name):
        shared_file = SharedFile.objects.create(owner=owner, file=file, name=name)
        return shared_file

    @classmethod
    def get_shared_files_by_owner(owner: User):
        return SharedFile.objects.filter(owner=owner)

    @classmethod
    def delete_shared_file(file_id):
        shared_file = __class__.get_shared_file(file_id)
        shared_file.delete()

    @classmethod
    def get_all_shared_files():
        return SharedFile.objects.all()


class PeerRepository:
    @classmethod
    def get_peer_by_user(user) -> Peer:
        return Peer.objects.filter(user=user).first()

    @classmethod
    def get_peer(peer_id):
        return get_object_or_404(Peer, pk=peer_id)

    @classmethod
    def create_peer(user, ip_address):
        peer = Peer.objects.create(user=user, ip_address=ip_address)
        return peer

    @classmethod
    def update_peer_ip(user: User, ip_address):
        peer: Peer = __class__.get_peer_by_user(user)
        peer.ip_address = ip_address
        peer.save()
        return peer

    @classmethod
    def get_all_peers():
        return Peer.objects.all()

    @classmethod
    def delete_peer(peer_id):
        peer: Peer = __class__.get_peer(peer_id)
        peer.delete()
