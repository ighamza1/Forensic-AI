 import hashlib
import os
from PIL import Image
from PIL.ExifTags import TAGS


# ==========================================
# Generate File Hashes
# ==========================================

def generate_hashes(file_path):

    hashes = {
        "md5": None,
        "sha1": None,
        "sha256": None
    }


    with open(file_path, "rb") as file:

        data = file.read()


        hashes["md5"] = hashlib.md5(data).hexdigest()

        hashes["sha1"] = hashlib.sha1(data).hexdigest()

        hashes["sha256"] = hashlib.sha256(data).hexdigest()


    return hashes



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