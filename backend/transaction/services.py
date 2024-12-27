from .repositories import SharedFileRepository, PeerRepository


class SharedFileService:
    @classmethod
    def get_shared_file(self, file_id):
        return SharedFileRepository.get_shared_file(file_id)

    @classmethod
    def share_file(self, owner, file, name):
        return SharedFileRepository.create_shared_file(owner, file, name)

    @classmethod
    def get_user_shared_files(self, owner):
        return SharedFileRepository.get_shared_files_by_owner(owner)

    @classmethod
    def get_all_shared_files(self):
        return SharedFileRepository.get_all_shared_files()

    @classmethod
    def delete_shared_file(self, file_id):
        SharedFileRepository.delete_shared_file(file_id)


class PeerService:
    @classmethod
    def register_peer(self, user, ip_address):
        peer = PeerRepository.get_peer_by_user(user)
        if peer:
            return PeerRepository.update_peer_ip(user, ip_address)
        return PeerRepository.create_peer(user, ip_address)

    @classmethod
    def get_peer(self, peer_id):
        return PeerRepository.get_peer(peer_id)

    @classmethod
    def get_user_peer(self, user):
        return PeerRepository.get_peer_by_user(user)

    @classmethod
    def get_all_peers(self):
        return PeerRepository.get_all_peers()

    @classmethod
    def delete_peer(self, peer_id):
        PeerRepository.delete_peer(peer_id)
