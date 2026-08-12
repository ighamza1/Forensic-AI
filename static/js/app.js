// =====================================================
// FAI - File Upload & Drag/Drop Handler
// =====================================================

const input = document.getElementById("imageInput");
const browseBtn = document.getElementById("browseBtn");
const uploadCard = document.querySelector(".upload-card");
const preview = document.getElementById("previewImage");
const loading = document.getElementById("loading");
const uploadForm = document.getElementById("uploadForm");


// =====================================================
// Browse Button
// =====================================================

if (browseBtn && input) {

    browseBtn.addEventListener("click", () => {

        input.click();

    });

}


// =====================================================
// File Input Change
// =====================================================

if (input) {

    input.addEventListener("change", () => {

        if (input.files && input.files.length > 0) {

            previewFile(input.files[0]);

        }

    });

}


// =====================================================
// Drag Over
// =====================================================

if (uploadCard) {

    uploadCard.addEventListener("dragover", (event) => {

        event.preventDefault();

        event.stopPropagation();

        uploadCard.classList.add("dragover");

    });


    // =================================================
    // Drag Enter
    // =================================================

    uploadCard.addEventListener("dragenter", (event) => {

        event.preventDefault();

        event.stopPropagation();

        uploadCard.classList.add("dragover");

    });


    // =================================================
    // Drag Leave
    // =================================================

    uploadCard.addEventListener("dragleave", (event) => {

        event.preventDefault();

        event.stopPropagation();

        uploadCard.classList.remove("dragover");

    });


    // =================================================
    // Drop
    // =================================================

    uploadCard.addEventListener("drop", (event) => {

        event.preventDefault();

        event.stopPropagation();

        uploadCard.classList.remove("dragover");


        const files = event.dataTransfer.files;


        if (!files || files.length === 0) {

            return;

        }


        const file = files[0];


        // ---------------------------------------------
        // Validate File Type
        // ---------------------------------------------

        const allowedTypes = [

            "image/jpeg",
            "image/png"

        ];


        if (!allowedTypes.includes(file.type)) {

            alert(
                "Unsupported image format. Please upload JPG, JPEG or PNG."
            );

            return;

        }


        // ---------------------------------------------
        // Put dropped file into file input
        // ---------------------------------------------

        try {

            const dataTransfer = new DataTransfer();

            dataTransfer.items.add(file);

            input.files = dataTransfer.files;

        }

        catch (error) {

            console.error(
                "Could not assign dropped file:",
                error
            );

        }


        // ---------------------------------------------
        // Preview
        // ---------------------------------------------

        previewFile(file);

    });

}


// =====================================================
// Preview File
// =====================================================

function previewFile(file) {

    if (!file) {

        return;

    }


    // ---------------------------------------------
    // Validate Image
    // ---------------------------------------------

    if (!file.type.startsWith("image/")) {

        alert(
            "Please select a valid image file."
        );

        return;

    }


    // ---------------------------------------------
    // Create Preview
    // ---------------------------------------------

    const reader = new FileReader();


    reader.onload = function (event) {

        if (preview) {

            preview.src = event.target.result;

            preview.style.display = "block";

        }

    };


    reader.onerror = function () {

        console.error(
            "Unable to read the selected image."
        );

    };


    reader.readAsDataURL(file);

}


// =====================================================
// Show Loading Screen
// =====================================================

if (uploadForm) {

    uploadForm.addEventListener("submit", () => {

        if (loading) {

            loading.style.display = "flex";

        }

    });

}