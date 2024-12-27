from typing import BinaryIO

from rest_framework import serializers

from .models import SharedFile, Peer
from .tasks import create_shared_file_async, process_file_download

from user.models import User
# from user.serializers import UserSerializer


class SharedFileSerializer(serializers.ModelSerializer):
    owner = serializers.StringRelatedField()

    class Meta:
        model = SharedFile
        fields = ["pk", "owner", "file", "name", "created_at"]
        read_only_fields = ["pk", "owner", "created_at"]

    def create(self, validated_data):
        owner: User = self.context["request"].user
        file: BinaryIO = validated_data.pop("file")
        name = validated_data["name"]
        # we create the file asynchronously via celery

        create_shared_file_async.delay(owner.pk, file.read(), file.name)
        # we return only name and id and when a file is created we can return the full information
        return {"name": name, "pk": None}


class SharedFileDownloadSerializer(serializers.Serializer):
    file_id = serializers.UUIDField()

    def get_file_content(self):
        result = process_file_download.delay(self.validated_data["file_id"])
        return result.get()


class PeerSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()

    class Meta:
        model = Peer
        fields = ["pk", "user", "ip_address", "last_seen"]
        read_only_fields = ["pk", "user", "last_seen"]
