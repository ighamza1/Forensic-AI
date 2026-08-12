# from flask import Flask, render_template, request, send_file

# import torch
# from PIL import Image
# from torchvision import transforms

# import os
# import time

# from werkzeug.utils import secure_filename

# from utils.real_fake_model_loader import load_real_fake_model
# from utils.manipulation_model_loader import load_manipulation_model

# from utils.report_generator import generate_report


# # =====================================================
# # Flask Setup
# # =====================================================

# app = Flask(__name__)


# # =====================================================
# # Load Models
# # =====================================================

# real_fake_model, device = load_real_fake_model()

# manipulation_model, _ = load_manipulation_model()



# # =====================================================
# # Image Transform
# # =====================================================

# transform = transforms.Compose([

#     transforms.Resize((224,224)),

#     transforms.ToTensor()

# ])



# # =====================================================
# # Upload Configuration
# # =====================================================

# UPLOAD_FOLDER = "static/uploads"

# os.makedirs(
#     UPLOAD_FOLDER,
#     exist_ok=True
# )


# REPORT_DATA = {}


# ALLOWED_EXTENSIONS = {

#     "png",
#     "jpg",
#     "jpeg"

# }



# def allowed_file(filename):

#     return (

#         "." in filename

#         and

#         filename.rsplit(".",1)[1].lower()
#         in ALLOWED_EXTENSIONS

#     )



# # =====================================================
# # Home
# # =====================================================

# @app.route("/")
# def home():

#     return render_template(
#         "index.html"
#     )



# # =====================================================
# # Prediction
# # =====================================================

# @app.route("/predict", methods=["POST"])
# def predict():


#     global REPORT_DATA



#     # ----------------------------
#     # Validate Upload
#     # ----------------------------

#     if "image" not in request.files:

#         return "No image uploaded."


#     file = request.files["image"]


#     if file.filename == "":

#         return "No image selected."


#     if not allowed_file(file.filename):

#         return "Unsupported image format."



#     # ----------------------------
#     # Save Image
#     # ----------------------------

#     filename = secure_filename(
#         file.filename
#     )


#     unique_filename = (

#         f"{int(time.time())}_{filename}"

#     )


#     filepath = os.path.join(

#         UPLOAD_FOLDER,

#         unique_filename

#     )


#     file.save(filepath)



#     print("="*70)

#     print(
#         "Uploaded:",
#         filepath
#     )



#     start = time.time()



#     # ----------------------------
#     # Image Information
#     # ----------------------------


#     image_file = Image.open(filepath)


#     width, height = image_file.size

#     image_format = image_file.format

#     color_mode = image_file.mode


#     file_size = round(

#         os.path.getsize(filepath)

#         /
#         (1024*1024),

#         2

#     )



#     image = image_file.convert(
#         "RGB"
#     )


#     image = transform(image)

#     image = image.unsqueeze(0)

#     image = image.to(device)



#     # =====================================================
#     # MODEL 1
#     # =====================================================


#     with torch.no_grad():


#         output = real_fake_model(image)


#         probabilities = torch.softmax(
#             output,
#             dim=1
#         )


#         real_fake_confidence = (

#             probabilities.max().item()
#             *
#             100

#         )


#         prediction = torch.argmax(

#             output,

#             dim=1

#         ).item()



#     real_fake_classes = [

#         "Fake",

#         "Real"

#     ]


#     real_fake_result = (

#         real_fake_classes[prediction]

#     )



#     print("\nMODEL 1")

#     print(
#         "Prediction:",
#         real_fake_result
#     )

#     print(

#         "Confidence:",
#         round(real_fake_confidence,2)

#     )




#     # =====================================================
#     # MODEL 2
#     # =====================================================


#     manipulation_result = "Not Applicable"

#     manipulation_confidence = None



#     if real_fake_result == "Fake":


#         with torch.no_grad():


#             output = manipulation_model(image)


#             probabilities = torch.softmax(

#                 output,

#                 dim=1

#             )


#             manipulation_confidence = (

#                 probabilities.max().item()

#                 *

#                 100

#             )


#             prediction = torch.argmax(

#                 output,

#                 dim=1

#             ).item()



#         manipulation_classes = [

#             "AI Generated",

#             "DeepFake",

#             "FaceSwap"

#         ]


#         manipulation_result = (

#             manipulation_classes[prediction]

#         )



#         print("\nMODEL 2")

#         print(

#             "Prediction:",

#             manipulation_result

#         )



#     # =====================================================
#     # Risk Assessment
#     # =====================================================


#     if real_fake_result == "Real":


#         risk = "LOW"


#     elif manipulation_result == "AI Generated":


#         risk = "MEDIUM"


#     else:


#         risk = "HIGH"




#     # =====================================================
#     # Recommendation
#     # =====================================================


#     if real_fake_result == "Real":


#         recommendation = (

#             "The uploaded image appears authentic. "
#             "No evidence of AI manipulation detected."

#         )


#     elif manipulation_result == "AI Generated":


#         recommendation = (

#             "This image appears AI-generated. "
#             "It should not be considered authentic evidence."

#         )


#     elif manipulation_result == "DeepFake":


#         recommendation = (

#             "DeepFake manipulation detected. "
#             "Manual forensic verification recommended."

#         )


#     else:


#         recommendation = (

#             "FaceSwap manipulation detected. "
#             "Identity replacement is suspected."

#         )




#     # =====================================================
#     # Timing
#     # =====================================================


#     inference_time = round(

#         time.time()-start,

#         3

#     )



#     # =====================================================
#     # Save Report Data
#     # =====================================================


#     REPORT_DATA = {


#         "examiner":

#             "FAI Automated System",


#         "filename":

#             unique_filename,


#         "image_path":

#             filepath,


#         "real_fake":

#             real_fake_result,


#         "manipulation":

#             manipulation_result,


#         "real_fake_confidence":

#             round(real_fake_confidence,2),


#         "manipulation_confidence":

#             (

#                 round(manipulation_confidence,2)

#                 if manipulation_confidence

#                 else None

#             ),


#         "width":

#             width,


#         "height":

#             height,


#         "format":

#             image_format,


#         "mode":

#             color_mode,


#         "size":

#             file_size,


#         "time_taken":

#             inference_time,


#         "recommendation":

#             recommendation

#     }



#     print(
#         "Inference:",
#         inference_time,
#         "seconds"
#     )


#     print("="*70)



#     # =====================================================
#     # Render Result
#     # =====================================================


#     return render_template(

#         "index.html",


#         filename=unique_filename,


#         image_path=filepath,


#         real_fake=real_fake_result,


#         manipulation=manipulation_result,


#         real_fake_confidence=

#             round(real_fake_confidence,2),


#         manipulation_confidence=

#             (

#             round(manipulation_confidence,2)

#             if manipulation_confidence

#             else None

#             ),


#         width=width,


#         height=height,


#         file_size=file_size,


#         image_format=image_format,


#         color_mode=color_mode,


#         inference_time=inference_time,


#         risk=risk,


#         recommendation=recommendation

#     )



# # =====================================================
# # Generate PDF Report
# # =====================================================

# @app.route("/download_report")
# def download_report():


#     if not REPORT_DATA:


#         return "No analysis report available."



#     report_name = (

#         "FAI_Forensic_Report.pdf"

#     )


#     report_path = os.path.join(

#         "static",

#         report_name

#     )



#     generate_report(

#         REPORT_DATA,

#         report_path

#     )



#     return send_file(

#         report_path,

#         as_attachment=True,

#         download_name=report_name

#     )



# # =====================================================
# # Run
# # =====================================================

# if __name__ == "__main__":
#     app.run(
#         host="127.0.0.1",
#         port=5000,
#         debug=False,
#         use_reloader=False
#     )

from flask import (
    Flask,
    render_template,
    request,
    send_file,
    send_from_directory
)

import torch
from PIL import Image
from torchvision import transforms

import os
import sys
import time

from werkzeug.utils import secure_filename

from utils.real_fake_model_loader import load_real_fake_model
from utils.manipulation_model_loader import load_manipulation_model

from utils.report_generator import generate_report


# =====================================================
# Resource Path
# =====================================================

def resource_path(relative_path):

    if getattr(sys, "frozen", False):

        base_path = sys._MEIPASS

    else:

        base_path = os.path.abspath(
            os.path.dirname(__file__)
        )

    return os.path.join(
        base_path,
        relative_path
    )


# =====================================================
# Writable Application Data
# =====================================================

if getattr(sys, "frozen", False):

    APP_DATA = os.path.join(
        os.environ.get(
            "LOCALAPPDATA",
            os.path.expanduser("~")
        ),
        "Forensic AI"
    )

else:

    APP_DATA = os.path.join(
        os.path.abspath(
            os.path.dirname(__file__)
        ),
        "runtime_data"
    )


UPLOAD_FOLDER = os.path.join(
    APP_DATA,
    "uploads"
)

REPORT_FOLDER = os.path.join(
    APP_DATA,
    "reports"
)


os.makedirs(
    UPLOAD_FOLDER,
    exist_ok=True
)

os.makedirs(
    REPORT_FOLDER,
    exist_ok=True
)


# =====================================================
# Flask Setup
# =====================================================

app = Flask(
    __name__,
    template_folder=resource_path("templates"),
    static_folder=resource_path("static")
)


# =====================================================
# Load Models
# =====================================================

real_fake_model, device = load_real_fake_model()

manipulation_model, manipulation_device = (
    load_manipulation_model()
)


# =====================================================
# Image Transform
# =====================================================

transform = transforms.Compose([

    transforms.Resize(
        (224, 224)
    ),

    transforms.ToTensor()

])


# =====================================================
# Report Data
# =====================================================

REPORT_DATA = {}


# =====================================================
# Allowed Extensions
# =====================================================

ALLOWED_EXTENSIONS = {

    "png",
    "jpg",
    "jpeg"

}


def allowed_file(filename):

    return (

        "."
        in filename

        and

        filename.rsplit(
            ".",
            1
        )[1].lower()

        in ALLOWED_EXTENSIONS

    )


# =====================================================
# Home
# =====================================================

@app.route("/")
def home():

    return render_template(
        "index.html"
    )


# =====================================================
# Uploaded Images
# =====================================================

@app.route(
    "/uploads/<filename>"
)
def uploaded_file(filename):

    return send_from_directory(
        UPLOAD_FOLDER,
        filename
    )


# =====================================================
# Prediction
# =====================================================

@app.route(
    "/predict",
    methods=["POST"]
)
def predict():

    global REPORT_DATA


    # =================================================
    # Validate Upload
    # =================================================

    if "image" not in request.files:

        return "No image uploaded."


    file = request.files["image"]


    if file.filename == "":

        return "No image selected."


    if not allowed_file(
        file.filename
    ):

        return "Unsupported image format."


    # =================================================
    # Save Image
    # =================================================

    filename = secure_filename(
        file.filename
    )


    unique_filename = (

        f"{int(time.time() * 1000)}_"
        f"{filename}"

    )


    filepath = os.path.join(
        UPLOAD_FOLDER,
        unique_filename
    )


    file.save(
        filepath
    )


    print("=" * 70)

    print(
        "Uploaded:",
        filepath
    )


    start = time.time()


    # =================================================
    # Image Information
    # =================================================

    image_file = Image.open(
        filepath
    )


    width, height = image_file.size

    image_format = image_file.format

    color_mode = image_file.mode


    file_size = round(

        os.path.getsize(filepath)
        /
        (1024 * 1024),

        2

    )


    image = image_file.convert(
        "RGB"
    )


    image = transform(
        image
    )


    image = image.unsqueeze(
        0
    )


    image = image.to(
        device
    )


    # =================================================
    # MODEL 1 — REAL / FAKE
    # =================================================

    with torch.no_grad():

        output = real_fake_model(
            image
        )


        probabilities = torch.softmax(
            output,
            dim=1
        )


        real_fake_confidence = (

            probabilities.max().item()
            *
            100

        )


        prediction = torch.argmax(
            output,
            dim=1
        ).item()


    real_fake_classes = [

        "Fake",
        "Real"

    ]


    real_fake_result = (

        real_fake_classes[
            prediction
        ]

    )


    print("\nMODEL 1")

    print(
        "Prediction:",
        real_fake_result
    )

    print(
        "Confidence:",
        round(
            real_fake_confidence,
            2
        )
    )


    # =================================================
    # MODEL 2 — MANIPULATION
    # =================================================

    manipulation_result = (
        "Not Applicable"
    )

    manipulation_confidence = None


    if real_fake_result == "Fake":

        manipulation_input = image.to(
            manipulation_device
        )


        with torch.no_grad():

            output = manipulation_model(
                manipulation_input
            )


            probabilities = torch.softmax(
                output,
                dim=1
            )


            manipulation_confidence = (

                probabilities.max().item()
                *
                100

            )


            prediction = torch.argmax(
                output,
                dim=1
            ).item()


        manipulation_classes = [

            "AI Generated",
            "DeepFake",
            "FaceSwap"

        ]


        manipulation_result = (

            manipulation_classes[
                prediction
            ]

        )


        print("\nMODEL 2")

        print(
            "Prediction:",
            manipulation_result
        )

        print(
            "Confidence:",
            round(
                manipulation_confidence,
                2
            )
        )


    # =================================================
    # Risk Assessment
    # =================================================

    if real_fake_result == "Real":

        risk = "LOW"

    elif manipulation_result == "AI Generated":

        risk = "MEDIUM"

    else:

        risk = "HIGH"


    # =================================================
    # Recommendation
    # =================================================

    if real_fake_result == "Real":

        recommendation = (

            "The uploaded image appears authentic. "
            "No evidence of AI manipulation detected."

        )

    elif manipulation_result == "AI Generated":

        recommendation = (

            "This image appears AI-generated. "
            "It should not be considered authentic evidence."

        )

    elif manipulation_result == "DeepFake":

        recommendation = (

            "DeepFake manipulation detected. "
            "Manual forensic verification recommended."

        )

    else:

        recommendation = (

            "FaceSwap manipulation detected. "
            "Identity replacement is suspected."

        )


    # =================================================
    # Timing
    # =================================================

    inference_time = round(

        time.time() - start,

        3

    )


    # =================================================
    # Report Data
    # =================================================

    REPORT_DATA = {

        "examiner":
            "FAI Automated System",

        "filename":
            unique_filename,

        "image_path":
            filepath,

        "real_fake":
            real_fake_result,

        "manipulation":
            manipulation_result,

        "real_fake_confidence":
            round(
                real_fake_confidence,
                2
            ),

        "manipulation_confidence":

            (
                round(
                    manipulation_confidence,
                    2
                )

                if manipulation_confidence is not None

                else None
            ),

        "width":
            width,

        "height":
            height,

        "format":
            image_format,

        "mode":
            color_mode,

        "size":
            file_size,

        "time_taken":
            inference_time,

        "risk":
            risk,

        "recommendation":
            recommendation

    }


    print(
        "Inference:",
        inference_time,
        "seconds"
    )

    print("=" * 70)


    # =================================================
    # Render Result
    # =================================================

    return render_template(

        "index.html",

        filename=unique_filename,

        image_path=True,

        real_fake=real_fake_result,

        manipulation=manipulation_result,

        real_fake_confidence=
            round(
                real_fake_confidence,
                2
            ),

        manipulation_confidence=

            (
                round(
                    manipulation_confidence,
                    2
                )

                if manipulation_confidence is not None

                else None
            ),

        width=width,

        height=height,

        file_size=file_size,

        image_format=image_format,

        color_mode=color_mode,

        inference_time=inference_time,

        risk=risk,

        recommendation=recommendation

    )


# =====================================================
# Generate PDF Report
# =====================================================

@app.route(
    "/download_report"
)
def download_report():

    if not REPORT_DATA:

        return (
            "No analysis report available."
        )


    timestamp = int(
        time.time() * 1000
    )


    report_name = (

        f"FAI_Forensic_Report_"
        f"{timestamp}.pdf"

    )


    report_path = os.path.join(

        REPORT_FOLDER,

        report_name

    )


    # =================================================
    # Generate Fresh Report
    # =================================================

    generate_report(

        REPORT_DATA,

        report_path

    )


    if not os.path.exists(
        report_path
    ):

        return (
            "Failed to generate report."
        )


    return send_file(

        report_path,

        as_attachment=True,

        download_name=report_name

    )


# =====================================================
# Run
# =====================================================

if __name__ == "__main__":

    app.run(

        host="127.0.0.1",

        port=5000,

        debug=False,

        use_reloader=False

    )