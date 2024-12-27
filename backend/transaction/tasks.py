from django.core.files.base import ContentFile

from celery import shared_task

from .repositories import SharedFileRepository

from user.models import User


@shared_task
def create_shared_file_async(owner_id, file_content, file_name):
    owner = User.objects.get(pk=owner_id)
    file = ContentFile(file_content, name=file_name)
    SharedFileRepository.create_shared_file(owner=owner, file=file, name=file_name)


@shared_task
def delete_shared_file_async(file_id):
    SharedFileRepository.delete_shared_file(file_id=file_id)


@shared_task
def process_file_download(file_id):
    shared_file = SharedFileRepository.get_shared_file(file_id=file_id)
    # Simulate processing: read file content & send to peer.
    with shared_file.file.open("rb") as file_obj:
        file_content = file_obj.read()
    return file_content  # or send to the peer
