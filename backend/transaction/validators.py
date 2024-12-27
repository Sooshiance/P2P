import os
from typing import BinaryIO

from rest_framework.exceptions import ValidationError


def allowed_files_validator(value: BinaryIO):
    ext = os.path.splitext(value.name)[1]
    valid_extensions = [".png", ".jpg", ".jpeg", ".pdf", ".docx", ".odt"]
    if ext.lower() not in valid_extensions:
        raise ValidationError(
            "Unsupported file extension. Allowed extensions: " + str(valid_extensions)
        )
