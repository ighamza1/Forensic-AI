# import torch
# import torch.nn as nn
# from torchvision import models

# device = torch.device("cuda" if torch.cuda.is_available() else "cpu")


# def load_manipulation_model():

#     model = models.resnet50(weights=None)

#     model.fc = nn.Sequential(
#         nn.Linear(model.fc.in_features, 512),
#         nn.ReLU(),
#         nn.Dropout(0.4),
#         nn.Linear(512, 3)
#     )

#     model.load_state_dict(
#         torch.load(
#             "models/manipulation_model.pth",
#             map_location=device
#         )
#     )

#     model.to(device)
#     model.eval()

#     return model, device

import os
import sys
import torch
import torch.nn as nn
from torchvision import models


# =====================================================
# Get Resource Path
# =====================================================

def get_resource_path(relative_path):

    if getattr(sys, "frozen", False):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(
            os.path.join(
                os.path.dirname(__file__),
                ".."
            )
        )

    return os.path.join(
        base_path,
        relative_path
    )


# =====================================================
# Load Manipulation Model
# =====================================================

def load_manipulation_model():

    device = torch.device(
        "cuda"
        if torch.cuda.is_available()
        else
        "cpu"
    )

    model_path = get_resource_path(
        os.path.join(
            "models",
            "manipulation_model.pth"
        )
    )

    print("Looking for manipulation model at:")
    print(model_path)
    print("Exists:", os.path.exists(model_path))

    if not os.path.exists(model_path):

        raise FileNotFoundError(
            f"Manipulation model not found: {model_path}"
        )


    # =================================================
    # Recreate Model Architecture
    # =================================================

    model = models.resnet50(
        weights=None
    )


    model.fc = nn.Sequential(

        nn.Linear(
            model.fc.in_features,
            512
        ),

        nn.ReLU(),

        nn.Dropout(0.4),

        nn.Linear(
            512,
            3
        )

    )


    # =================================================
    # Load State Dictionary
    # =================================================

    checkpoint = torch.load(
        model_path,
        map_location=device
    )


    # Handle both possible checkpoint formats
    if isinstance(checkpoint, dict):

        if "state_dict" in checkpoint:

            state_dict = checkpoint["state_dict"]

        elif "model_state_dict" in checkpoint:

            state_dict = checkpoint["model_state_dict"]

        else:

            state_dict = checkpoint

    else:

        raise TypeError(
            "Unsupported manipulation model format."
        )


    # Remove DataParallel prefix if present
    cleaned_state_dict = {}

    for key, value in state_dict.items():

        if key.startswith("module."):

            key = key[7:]

        cleaned_state_dict[key] = value


    model.load_state_dict(
        cleaned_state_dict
    )


    # =================================================
    # Device
    # =================================================

    model.to(device)

    model.eval()


    print(
        "Manipulation model loaded successfully."
    )

    print(
        "Device:",
        device
    )


    return model, device