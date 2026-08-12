# Forensic AI (FAI)

## AI-Based Digital Forensic System for Detecting AI-Generated and Manipulated Human Face Images

Forensic AI (FAI) is an AI-powered digital forensic system developed as a Final Year Project (FYP).

The system analyzes human face images to determine whether an image appears to be real or fake and, when a fake image is detected, attempts to identify the type of manipulation.

The system is designed to support digital forensic analysis and defamation-risk assessment.

---

# Project Overview

Forensic AI combines deep learning, digital image analysis, metadata extraction, cryptographic hashing, and automated forensic reporting into a desktop application.

The system currently uses a two-stage AI detection pipeline.

### Stage 1 — Real/Fake Detection

The first model determines whether an uploaded image appears to be:

- Real
- Fake

### Stage 2 — Manipulation Classification

If the image is classified as fake, the second model attempts to classify the manipulation as:

- AI Generated
- DeepFake
- FaceSwap

The result is then used to produce a forensic risk assessment and recommendation.

---

# Main Features

- AI-generated image detection
- Real/Fake image classification
- DeepFake detection
- FaceSwap detection
- Manipulation classification
- Confidence scores
- Forensic risk assessment
- Image metadata extraction
- MD5 hash generation
- SHA-1 hash generation
- SHA-256 hash generation
- Evidence image preservation
- Automated forensic PDF report generation
- Electron desktop application
- Flask-based backend
- Windows installer
- FAI application branding

---

# System Architecture

The application follows a layered architecture:

```text
User
 |
 v
Electron Desktop Application
 |
 v
Flask Web Interface
 |
 v
Image Upload
 |
 v
Image Preprocessing
 |
 +-----------------------------+
 |                             |
 v                             v
Real/Fake Model          Image Metadata
 |                             |
 v                             v
Real / Fake               Metadata + Hashes
 |
 | Fake
 v
Manipulation Model
 |
 +-------------+-------------+
 |             |             |
 v             v             v
AI Generated  DeepFake    FaceSwap
 |
 v
Risk Assessment
 |
 v
Forensic Report Generator
 |
 v
PDF Report