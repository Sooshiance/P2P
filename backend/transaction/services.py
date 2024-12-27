from .repositories import SharedFileRepository, PeerRepository


class SharedFileService:
    @staticmethod
    def get_shared_file(file_id):
        return SharedFileRepository.get_shared_file(file_id)

    @staticmethod
    def share_file(owner, file, name):
        return SharedFileRepository.create_shared_file(owner, file, name)

    @staticmethod
    def get_user_shared_files(owner):
        return SharedFileRepository.get_shared_files_by_owner(owner)

    @staticmethod
    def get_all_shared_files():
        return SharedFileRepository.get_all_shared_files()

    @staticmethod
    def delete_shared_file(file_id):
        SharedFileRepository.delete_shared_file(file_id)


class PeerService:
    @staticmethod
    def register_peer(user, ip_address):
        peer = PeerRepository.get_peer_by_user(user)
        if peer:
            return PeerRepository.update_peer_ip(user, ip_address)
        return PeerRepository.create_peer(user, ip_address)

    @staticmethod
    def get_peer(peer_id):
        return PeerRepository.get_peer(peer_id)

    @staticmethod
    def get_user_peer(user):
        return PeerRepository.get_peer_by_user(user)

    @staticmethod
    def get_all_peers():
        return PeerRepository.get_all_peers()

    @staticmethod
    def delete_peer(peer_id):
        PeerRepository.delete_peer(peer_id)
