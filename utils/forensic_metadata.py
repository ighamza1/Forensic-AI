import hashlib
import os
from PIL import Image
from PIL.ExifTags import TAGS


# ==========================================
# Generate File Hashes
# ==========================================


import hashlib

def generate_hashes(file_path):
    """Calculate MD5, SHA-1 and SHA-256 from the original file bytes."""

    hashers = {
        "md5": hashlib.md5(),
        "sha1": hashlib.sha1(),
        "sha256": hashlib.sha256()
    }

    with open(file_path, "rb") as image_file:
        while True:
            chunk = image_file.read(1024 * 1024)

            if not chunk:
                break

            for hasher in hashers.values():
                hasher.update(chunk)

    return {
        name: hasher.hexdigest()
        for name, hasher in hashers.items()
    }




# ==========================================
# Extract Image Metadata
# ==========================================

def extract_metadata(image_path):

    metadata = {}


    try:

        image = Image.open(image_path)


        metadata["filename"] = os.path.basename(image_path)

        metadata["format"] = image.format

        metadata["width"] = image.width

        metadata["height"] = image.height

        metadata["mode"] = image.mode


        file_size = os.path.getsize(image_path)

        metadata["size"] = round(
            file_size / (1024 * 1024),
            2
        )


        # EXIF DATA

        exif_data = image.getexif()


        exif = {}


        if exif_data:

            for key,value in exif_data.items():

                tag = TAGS.get(
                    key,
                    key
                )

                exif[tag] = str(value)



        metadata["exif"] = exif



    except Exception as e:


        metadata["error"] = str(e)



    return metadata