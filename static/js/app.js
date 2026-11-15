// =====================================================
// FAI - Tactical Evidence Drag/Drop & Ingestion Engine
// =====================================================

const input = document.getElementById("imageInput");
const browseBtn = document.getElementById("browseBtn");
const uploadCard = document.querySelector(".upload-card");
const preview = document.getElementById("previewImage");
const loading = document.getElementById("loading");
const uploadForm = document.getElementById("uploadForm");

// =====================================================
// Browse Trigger
// =====================================================
if (browseBtn && input) {
    browseBtn.addEventListener("click", () => {
        input.click();
    });
}

// =====================================================
// File Change Listener
// =====================================================
if (input) {
    input.addEventListener("change", () => {
        if (input.files && input.files.length > 0) {
            previewFile(input.files[0]);
        }
    });
}

// =====================================================
// Drag & Drop Handling
// =====================================================
if (uploadCard) {
    ["dragover", "dragenter"].forEach(eventName => {
        uploadCard.addEventListener(eventName, (event) => {
            event.preventDefault();
            event.stopPropagation();
            uploadCard.classList.add("dragover");
        });
    });

    ["dragleave", "drop"].forEach(eventName => {
        uploadCard.addEventListener(eventName, (event) => {
            event.preventDefault();
            event.stopPropagation();
            uploadCard.classList.remove("dragover");
        });
    });

    uploadCard.addEventListener("drop", (event) => {
        const files = event.dataTransfer.files;
        if (!files || files.length === 0) return;

        const file = files[0];
        const allowedTypes = ["image/jpeg", "image/png"];

        if (!allowedTypes.includes(file.type)) {
            alert("ALERT: Invalid payload type. Upload JPG, JPEG or PNG only.");
            return;
        }

        try {
            const dataTransfer = new DataTransfer();
            dataTransfer.items.add(file);
            input.files = dataTransfer.files;
        } catch (error) {
            console.error("Failed to map file to stream input:", error);
        }

        previewFile(file);
    });
}

// =====================================================
// Stream Preview Generator
// =====================================================
function previewFile(file) {
    if (!file || !file.type.startsWith("image/")) {
        alert("ALERT: Incompatible file stream detected.");
        return;
    }

    const reader = new FileReader();
    reader.onload = function (event) {
        if (preview) {
            preview.src = event.target.result;
            preview.style.display = "block";
        }
    };
    reader.readAsDataURL(file);
}

// =====================================================
// Diagnostics HUD Display Trigger
// =====================================================
if (uploadForm) {
    uploadForm.addEventListener("submit", () => {
        if (loading) {
            loading.style.display = "flex";
        }
    });
}