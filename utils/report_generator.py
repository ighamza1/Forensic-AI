

# from reportlab.platypus import (
#     SimpleDocTemplate,
#     Paragraph,
#     Spacer,
#     Table,
#     TableStyle,
#     Image
# )

# from reportlab.lib.styles import getSampleStyleSheet
# from reportlab.lib.enums import TA_CENTER
# from reportlab.lib import colors
# from reportlab.lib.units import inch

# import datetime
# import uuid
# import os
# import sys


# # =====================================================
# # Resource Path
# # =====================================================

# def resource_path(relative_path):

#     if getattr(sys, "frozen", False):

#         base_path = sys._MEIPASS

#     else:

#         base_path = os.path.abspath(
#             os.path.join(
#                 os.path.dirname(__file__),
#                 ".."
#             )
#         )

#     return os.path.join(
#         base_path,
#         relative_path
#     )


# # =====================================================
# # Generate Report
# # =====================================================

# def generate_report(data, output_path):


#     # =================================================
#     # Styles
#     # =================================================

#     styles = getSampleStyleSheet()


#     title_style = styles["Heading1"]

#     title_style.alignment = TA_CENTER

#     title_style.textColor = colors.white


#     heading = styles["Heading2"]

#     heading.textColor = colors.HexColor(
#         "#0B3C91"
#     )


#     normal = styles["BodyText"]


#     small = styles["BodyText"]

#     small.fontSize = 9


#     # =================================================
#     # PDF Setup
#     # =================================================

#     pdf = SimpleDocTemplate(

#         output_path,

#         rightMargin=35,

#         leftMargin=35,

#         topMargin=35,

#         bottomMargin=35

#     )


#     elements = []


#     # =================================================
#     # Report Information
#     # =================================================

#     report_id = (

#         "FAI-"
#         +
#         str(
#             uuid.uuid4()
#         )[:8].upper()

#     )


#     now = datetime.datetime.now()


#     report_date = now.strftime(
#         "%d %B %Y"
#     )


#     report_time = now.strftime(
#         "%I:%M:%S %p"
#     )


#     # =================================================
#     # Logo
#     # =================================================

#     logo_path = resource_path(
#         os.path.join(
#             "static",
#             "images",
#             "logo.png"
#         )
#     )


#     if os.path.exists(
#         logo_path
#     ):

#         logo = Image(

#             logo_path,

#             width=0.9 * inch,

#             height=0.9 * inch

#         )

#     else:

#         logo = Paragraph(
#             "",
#             normal
#         )


#     # =================================================
#     # Header
#     # =================================================

#     header = Table(

#         [[

#             logo,

#             Paragraph(

#                 "<font size=22>"
#                 "<b>FORENSIC AI</b>"
#                 "</font><br/>"

#                 "<font size=11>"
#                 "AI-Based Digital Image "
#                 "Authentication System"
#                 "</font>",

#                 title_style

#             )

#         ]],

#         colWidths=[

#             1.2 * inch,

#             5.8 * inch

#         ]

#     )


#     header.setStyle(
#         TableStyle([

#             (

#                 "BACKGROUND",

#                 (0, 0),

#                 (-1, -1),

#                 colors.HexColor(
#                     "#0B3C91"
#                 )

#             ),

#             (

#                 "VALIGN",

#                 (0, 0),

#                 (-1, -1),

#                 "MIDDLE"

#             ),

#             (

#                 "TOPPADDING",

#                 (0, 0),

#                 (-1, -1),

#                 15

#             ),

#             (

#                 "BOTTOMPADDING",

#                 (0, 0),

#                 (-1, -1),

#                 15

#             )

#         ])
#     )


#     elements.append(
#         header
#     )


#     elements.append(
#         Spacer(1, 20)
#     )


#     # =================================================
#     # Case Information
#     # =================================================

#     elements.append(
#         Paragraph(
#             "Case Information",
#             heading
#         )
#     )


#     case_table = Table([

#         [
#             "Report ID",
#             report_id
#         ],

#         [
#             "Examiner",
#             data.get(
#                 "examiner",
#                 "FAI System"
#             )
#         ],

#         [
#             "Date",
#             report_date
#         ],

#         [
#             "Time",
#             report_time
#         ],

#         [
#             "System",
#             "FAI Version 1.0"
#         ],

#         [
#             "Classification",
#             "Confidential"
#         ]

#     ],

#     colWidths=[

#         2.1 * inch,

#         4.2 * inch

#     ])


#     case_table.setStyle(
#         TableStyle([

#             (

#                 "GRID",

#                 (0, 0),

#                 (-1, -1),

#                 0.5,

#                 colors.grey

#             ),

#             (

#                 "BACKGROUND",

#                 (0, 0),

#                 (0, -1),

#                 colors.HexColor(
#                     "#E8F1FF"
#                 )

#             ),

#             (

#                 "FONTNAME",

#                 (0, 0),

#                 (-1, -1),

#                 "Helvetica-Bold"

#             )

#         ])
#     )


#     elements.append(
#         case_table
#     )


#     elements.append(
#         Spacer(1, 20)
#     )


#     # =================================================
#     # Evidence Image
#     # =================================================

#     elements.append(
#         Paragraph(
#             "Evidence Image",
#             heading
#         )
#     )


#     image_path = data.get(
#         "image_path"
#     )


#     if image_path and os.path.exists(
#         image_path
#     ):

#         evidence_image = Image(

#             image_path,

#             width=4.5 * inch,

#             height=4.5 * inch

#         )


#         image_table = Table(

#             [[evidence_image]],

#             colWidths=[

#                 5 * inch

#             ]

#         )


#         image_table.setStyle(
#             TableStyle([

#                 (

#                     "GRID",

#                     (0, 0),

#                     (-1, -1),

#                     1,

#                     colors.HexColor(
#                         "#0B3C91"
#                     )

#                 ),

#                 (

#                     "ALIGN",

#                     (0, 0),

#                     (-1, -1),

#                     "CENTER"

#                 )

#             ])
#         )


#         elements.append(
#             image_table
#         )


#         elements.append(
#             Spacer(1, 10)
#         )


#     # =================================================
#     # Detection Summary
#     # =================================================

#     elements.append(
#         Paragraph(
#             "Detection Summary",
#             heading
#         )
#     )


#     detection = Table([

#         [
#             "Real / Fake",
#             data.get(
#                 "real_fake"
#             )
#         ],

#         [
#             "Manipulation",
#             data.get(
#                 "manipulation"
#             )
#         ],

#         [
#             "Confidence",
#             f'{data.get("real_fake_confidence")}%'
#         ],

#         [
#             "Manipulation Confidence",

#             (

#                 "N/A"

#                 if data.get(
#                     "manipulation_confidence"
#                 ) is None

#                 else

#                 f'{data.get("manipulation_confidence")}%'

#             )

#         ]

#     ],

#     colWidths=[

#         2.5 * inch,

#         3.8 * inch

#     ])


#     detection.setStyle(
#         TableStyle([

#             (

#                 "GRID",

#                 (0, 0),

#                 (-1, -1),

#                 0.5,

#                 colors.grey

#             ),

#             (

#                 "BACKGROUND",

#                 (0, 0),

#                 (0, -1),

#                 colors.HexColor(
#                     "#E8F1FF"
#                 )

#             ),

#             (

#                 "FONTNAME",

#                 (0, 0),

#                 (-1, -1),

#                 "Helvetica-Bold"

#             )

#         ])
#     )


#     elements.append(
#         detection
#     )


#     elements.append(
#         Spacer(1, 20)
#     )


#     # =================================================
#     # Metadata
#     # =================================================

#     elements.append(
#         Paragraph(
#             "Image Metadata",
#             heading
#         )
#     )


#     metadata = Table([

#         [
#             "Filename",
#             data.get(
#                 "filename"
#             )
#         ],

#         [
#             "Resolution",

#             f'{data.get("width")} × '
#             f'{data.get("height")}'
#         ],

#         [
#             "Format",
#             data.get(
#                 "format"
#             )
#         ],

#         [
#             "Color Mode",
#             data.get(
#                 "mode"
#             )
#         ],

#         [
#             "File Size",
#             f'{data.get("size")} MB'
#         ],

#         [
#             "Inference Time",
#             f'{data.get("time_taken")} sec'
#         ]

#     ],

#     colWidths=[

#         2.5 * inch,

#         3.8 * inch

#     ])


#     metadata.setStyle(
#         TableStyle([

#             (

#                 "GRID",

#                 (0, 0),

#                 (-1, -1),

#                 0.5,

#                 colors.grey

#             ),

#             (

#                 "BACKGROUND",

#                 (0, 0),

#                 (0, -1),

#                 colors.HexColor(
#                     "#E8F1FF"
#                 )

#             )

#         ])
#     )


#     elements.append(
#         metadata
#     )


#     elements.append(
#         Spacer(1, 20)
#     )



#     # =================================================
#     # Cryptographic Hashes
#     # =================================================

#     elements.append(
#         Paragraph(
#             "Cryptographic Hashes",
#             heading
#         )
#     )

#     hashes = data.get("hashes", {})

#     hash_style = styles["BodyText"]
#     hash_style.fontName = "Courier"
#     hash_style.fontSize = 7
#     hash_style.leading = 9
#     hash_style.wordWrap = "CJK"

#     hash_table = Table(
#         [
#             [
#                 "Algorithm",
#                 "Calculated Hash"
#             ],
#             [
#                 "MD5",
#                 Paragraph(
#                     str(hashes.get("md5", "Not available")),
#                     hash_style
#                 )
#             ],
#             [
#                 "SHA-1",
#                 Paragraph(
#                     str(hashes.get("sha1", "Not available")),
#                     hash_style
#                 )
#             ],
#             [
#                 "SHA-256",
#                 Paragraph(
#                     str(hashes.get("sha256", "Not available")),
#                     hash_style
#                 )
#             ]
#         ],
#         colWidths=[
#             1.3 * inch,
#             5.0 * inch
#         ]
#     )

#     hash_table.setStyle(
#         TableStyle([
#             ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
#             ("BACKGROUND", (0, 0), (-1, 0),
#              colors.HexColor("#0B3C91")),
#             ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
#             ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
#             ("FONTNAME", (0, 1), (0, -1), "Helvetica-Bold"),
#             ("VALIGN", (0, 0), (-1, -1), "TOP"),
#             ("LEFTPADDING", (0, 0), (-1, -1), 7),
#             ("RIGHTPADDING", (0, 0), (-1, -1), 7),
#             ("TOPPADDING", (0, 0), (-1, -1), 7),
#             ("BOTTOMPADDING", (0, 0), (-1, -1), 7)
#         ])
#     )

#     elements.append(hash_table)
#     elements.append(Spacer(1, 20))

#     # =================================================
#     # Disclaimer
#     # =================================================

#     elements.append(
#         Paragraph(
#             "Disclaimer",
#             heading
#         )
#     )


#     elements.append(
#         Paragraph(

#             "This forensic report was generated "
#             "automatically by <b>Forensic AI (FAI)</b>. "
#             "The results are based on deep learning "
#             "models and should be reviewed by a qualified "
#             "forensic examiner before legal use.",

#             small

#         )
#     )


#     # =================================================
#     # Build PDF
#     # =================================================

#     pdf.build(
#         elements
#     )


import os
import sys
import uuid
import datetime
from xml.sax.saxutils import escape

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import (
    getSampleStyleSheet,
    ParagraphStyle
)
from reportlab.lib.units import inch
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    Image,
    KeepTogether
)


# =====================================================
# Theme
# =====================================================

NAVY = colors.HexColor("#10233F")
BLUE = colors.HexColor("#1769AA")
LIGHT_BLUE = colors.HexColor("#EAF2FA")
PALE_BLUE = colors.HexColor("#F4F8FC")
DARK = colors.HexColor("#243447")
GREY = colors.HexColor("#64748B")
LIGHT_GREY = colors.HexColor("#E2E8F0")
WHITE = colors.white

GREEN = colors.HexColor("#16845B")
AMBER = colors.HexColor("#B7791F")
RED = colors.HexColor("#B83245")


# =====================================================
# Resource Path
# =====================================================

def resource_path(relative_path):

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
# Safe Formatting Helpers
# =====================================================

def safe_text(value, default="Not available"):

    if value is None or str(value).strip() == "":
        value = default

    return escape(str(value))


def make_paragraph(value, style, default="Not available"):

    return Paragraph(
        safe_text(value, default),
        style
    )


def format_percentage(value):

    if value is None:
        return "Not available"

    try:
        return f"{float(value):.2f}%"
    except (ValueError, TypeError):
        return safe_text(value)


def format_file_size(value):

    if value is None:
        return "Not available"

    try:
        return f"{float(value):.2f} MB"
    except (ValueError, TypeError):
        return safe_text(value)


def get_assessment(real_fake, manipulation):

    result = str(real_fake or "").strip().lower()
    subtype = str(manipulation or "").strip().lower()

    if result == "real":

        return {
            "risk": "LOW",
            "color": GREEN,
            "summary": (
                "The model classified the submitted image "
                "as Real. This result does not independently "
                "establish the image's origin or authenticity."
            )
        }

    if result == "fake":

        if subtype == "ai generated":
            return {
                "risk": "MEDIUM",
                "color": AMBER,
                "summary": (
                    "The model classified the image as Fake "
                    "and identified it as AI Generated. "
                    "Independent verification is recommended."
                )
            }

        if subtype in ("deepfake", "faceswap", "face swap"):
            return {
                "risk": "HIGH",
                "color": RED,
                "summary": (
                    "The model classified the image as Fake "
                    "and identified a possible manipulated-face "
                    "category. Further forensic examination "
                    "is recommended."
                )
            }

        return {
            "risk": "REVIEW REQUIRED",
            "color": AMBER,
            "summary": (
                "The image was classified as Fake, but its "
                "manipulation subtype requires further review."
            )
        }

    return {
        "risk": "UNDETERMINED",
        "color": GREY,
        "summary": (
            "The system did not provide a recognized "
            "classification. Manual examination is required."
        )
    }


# =====================================================
# Automatic Recommendations
# =====================================================

def generate_recommendations(real_fake, manipulation):

    result = str(real_fake or "").strip().lower()
    subtype = str(manipulation or "").strip().lower()

    recommendations = []

    if result == "real":

        recommendations = [
            (
                "Preserve the original image file without "
                "editing or recompressing it."
            ),
            (
                "Verify the image's source, publication history "
                "and ownership using independent sources."
            ),
            (
                "Compare the image with trusted original copies "
                "where available."
            ),
            (
                "Retain the generated report and recorded "
                "cryptographic hashes for future reference."
            )
        ]

    elif result == "fake":

        recommendations = [
            (
                "Preserve the submitted image in its original "
                "form and restrict unnecessary access."
            ),
            (
                "Retain the generated report and cryptographic "
                "hashes to support subsequent file-integrity "
                "comparisons."
            ),
            (
                "Obtain the original source image, if available, "
                "for comparative examination."
            )
        ]

        if subtype == "ai generated":

            recommendations.append(
                "Seek independent verification of the image's "
                "origin and possible AI-generation history."
            )

        elif subtype in ("deepfake", "faceswap", "face swap"):

            recommendations.append(
                "Arrange a detailed examination by a qualified "
                "digital forensic examiner before drawing "
                "conclusions about the alleged manipulation."
            )

        else:

            recommendations.append(
                "Request further technical examination to "
                "identify the nature of the suspected manipulation."
            )

    else:

        recommendations = [
            (
                "Do not rely on the automated result as a final "
                "authenticity determination."
            ),
            (
                "Preserve the original file and arrange manual "
                "examination by a qualified specialist."
            )
        ]

    recommendations.extend([
        (
            "Document the source, date of collection and "
            "handling of the submitted evidence."
        ),
        (
            "Do not treat an automated classification alone "
            "as proof of defamation, intent or wrongdoing."
        )
    ])

    return recommendations


# =====================================================
# Table Styling
# =====================================================

def apply_data_table_style(table):

    table.setStyle(
        TableStyle([
            ("GRID", (0, 0), (-1, -1), 0.4, LIGHT_GREY),

            ("BACKGROUND", (0, 0), (0, -1), LIGHT_BLUE),

            ("BACKGROUND", (1, 0), (-1, -1), WHITE),

            ("FONTNAME", (0, 0), (0, -1), "Helvetica-Bold"),

            ("FONTNAME", (1, 0), (-1, -1), "Helvetica"),

            ("TEXTCOLOR", (0, 0), (-1, -1), DARK),

            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),

            ("LEFTPADDING", (0, 0), (-1, -1), 9),

            ("RIGHTPADDING", (0, 0), (-1, -1), 9),

            ("TOPPADDING", (0, 0), (-1, -1), 8),

            ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
        ])
    )


def make_section_heading(title, styles):

    return Paragraph(
        escape(title.upper()),
        styles["SectionHeading"]
    )


# =====================================================
# Page Footer
# =====================================================

def draw_page_footer(canvas, document, report_id):

    canvas.saveState()

    page_width, page_height = A4

    canvas.setStrokeColor(LIGHT_GREY)
    canvas.setLineWidth(0.6)

    canvas.line(
        42,
        36,
        page_width - 42,
        36
    )

    canvas.setFont("Helvetica", 8)
    canvas.setFillColor(GREY)

    canvas.drawString(
        42,
        23,
        "FORENSIC AI (FAI) | CONFIDENTIAL"
    )

    canvas.drawRightString(
        page_width - 42,
        23,
        f"{report_id}  |  Page {document.page}"
    )

    canvas.restoreState()


# =====================================================
# Generate Report
# =====================================================

def generate_report(data, output_path):

    data = data or {}

    # -------------------------------------------------
    # Report Information
    # -------------------------------------------------

    report_id = (
        "FAI-"
        + uuid.uuid4().hex[:8].upper()
    )

    now = datetime.datetime.now()

    report_date = now.strftime("%d %B %Y")
    report_time = now.strftime("%I:%M:%S %p")

    os.makedirs(
        os.path.dirname(os.path.abspath(output_path)),
        exist_ok=True
    )

    # -------------------------------------------------
    # Document Setup
    # -------------------------------------------------

    pdf = SimpleDocTemplate(
        output_path,
        pagesize=A4,
        rightMargin=42,
        leftMargin=42,
        topMargin=38,
        bottomMargin=52,
        title="Forensic AI - Digital Forensic Examination Report",
        author="Forensic AI (FAI)",
        subject="AI-Based Digital Image Analysis"
    )

    elements = []

    # -------------------------------------------------
    # Styles
    # -------------------------------------------------

    base_styles = getSampleStyleSheet()

    styles = {}

    styles["Title"] = ParagraphStyle(
        "FAITitle",
        parent=base_styles["Title"],
        fontName="Helvetica-Bold",
        fontSize=22,
        leading=26,
        textColor=WHITE,
        alignment=TA_LEFT,
        spaceAfter=5
    )

    styles["Subtitle"] = ParagraphStyle(
        "FAISubtitle",
        parent=base_styles["Normal"],
        fontName="Helvetica",
        fontSize=9,
        leading=13,
        textColor=colors.HexColor("#DCE8F5")
    )

    styles["SectionHeading"] = ParagraphStyle(
        "FAISectionHeading",
        parent=base_styles["Heading2"],
        fontName="Helvetica-Bold",
        fontSize=11,
        leading=15,
        textColor=NAVY,
        spaceBefore=9,
        spaceAfter=8,
        keepWithNext=True
    )

    styles["Body"] = ParagraphStyle(
        "FAIBody",
        parent=base_styles["BodyText"],
        fontName="Helvetica",
        fontSize=9,
        leading=14,
        textColor=DARK,
        alignment=TA_LEFT,
        spaceAfter=5
    )

    styles["Small"] = ParagraphStyle(
        "FAISmall",
        parent=styles["Body"],
        fontSize=8,
        leading=11,
        textColor=GREY
    )

    styles["Table"] = ParagraphStyle(
        "FAITable",
        parent=styles["Body"],
        fontSize=8.5,
        leading=12
    )

    styles["TableLabel"] = ParagraphStyle(
        "FAITableLabel",
        parent=styles["Table"],
        fontName="Helvetica-Bold",
        textColor=NAVY
    )

    styles["Hash"] = ParagraphStyle(
        "FAIHash",
        parent=styles["Table"],
        fontName="Courier",
        fontSize=7,
        leading=10,
        wordWrap="CJK"
    )

    styles["Recommendation"] = ParagraphStyle(
        "FAIRecommendation",
        parent=styles["Body"],
        leftIndent=5,
        firstLineIndent=-5,
        spaceAfter=7
    )

    # -------------------------------------------------
    # Header
    # -------------------------------------------------

    logo_path = resource_path(
        os.path.join(
            "static",
            "images",
            "logo.png"
        )
    )

    logo = Paragraph(
        "<b>FAI</b>",
        ParagraphStyle(
            "LogoFallback",
            parent=styles["Title"],
            fontSize=20
        )
    )

    if os.path.exists(logo_path):

        logo = Image(
            logo_path,
            width=0.75 * inch,
            height=0.75 * inch,
            kind="proportional"
        )

    header_text = [
        Paragraph(
            "FORENSIC AI",
            styles["Title"]
        ),
        Paragraph(
            "AI-Based Digital Forensic System",
            styles["Subtitle"]
        ),
        Paragraph(
            "DIGITAL IMAGE ANALYSIS REPORT",
            ParagraphStyle(
                "HeaderTag",
                parent=styles["Subtitle"],
                fontSize=8,
                leading=11,
                textColor=colors.HexColor("#A9D5FF")
            )
        )
    ]

    header = Table(
        [[logo, header_text]],
        colWidths=[1.0 * inch, 6.1 * inch]
    )

    header.setStyle(
        TableStyle([
            ("BACKGROUND", (0, 0), (-1, -1), NAVY),

            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),

            ("LEFTPADDING", (0, 0), (-1, -1), 14),

            ("RIGHTPADDING", (0, 0), (-1, -1), 14),

            ("TOPPADDING", (0, 0), (-1, -1), 15),

            ("BOTTOMPADDING", (0, 0), (-1, -1), 15),
        ])
    )

    elements.append(header)
    elements.append(Spacer(1, 17))

    # -------------------------------------------------
    # Report Identification
    # -------------------------------------------------

    elements.append(
        make_section_heading(
            "Report Information",
            styles
        )
    )

    case_rows = [
        ["Report ID", report_id],
        [
            "Examiner",
            safe_text(
                data.get("examiner"),
                "FAI Automated System"
            )
        ],
        ["Report Date", report_date],
        ["Report Time", report_time],
        ["System Version", "FAI Version 1.0"],
        ["Classification", "CONFIDENTIAL"]
    ]

    case_table = Table(
        [
            [
                Paragraph(
                    safe_text(row[0]),
                    styles["TableLabel"]
                ),
                Paragraph(
                    row[1] if row[0] == "Examiner"
                    else safe_text(row[1]),
                    styles["Table"]
                )
            ]
            for row in case_rows
        ],
        colWidths=[1.65 * inch, 5.45 * inch]
    )

    apply_data_table_style(case_table)

    elements.append(case_table)
    elements.append(Spacer(1, 13))

    # -------------------------------------------------
    # Detection Assessment
    # -------------------------------------------------

    real_fake = data.get("real_fake")
    manipulation = data.get("manipulation")

    assessment = get_assessment(
        real_fake,
        manipulation
    )

    elements.append(
        make_section_heading(
            "Automated Detection Results",
            styles
        )
    )

    detection_rows = [
        ["Real / Fake", safe_text(real_fake)],
        ["Manipulation Category", safe_text(manipulation)],
        [
            "Real / Fake Confidence",
            format_percentage(
                data.get("real_fake_confidence")
            )
        ],
        [
            "Manipulation Confidence",
            format_percentage(
                data.get("manipulation_confidence")
            )
        ]
    ]

    detection_table = Table(
        [
            [
                Paragraph(
                    safe_text(row[0]),
                    styles["TableLabel"]
                ),
                Paragraph(
                    row[1],
                    styles["Table"]
                )
            ]
            for row in detection_rows
        ],
        colWidths=[2.1 * inch, 5.0 * inch]
    )

    apply_data_table_style(detection_table)

    elements.append(detection_table)
    elements.append(Spacer(1, 10))

    # Risk assessment panel

    risk_text = Paragraph(
        f'<font color="{assessment["color"].hexval()}">'
        f'<b>{escape(assessment["risk"])}</b>'
        f'</font>',
        styles["Table"]
    )

    summary_text = Paragraph(
        safe_text(assessment["summary"]),
        styles["Body"]
    )

    risk_table = Table(
        [[
            Paragraph(
                "<b>PRELIMINARY RISK LEVEL</b>",
                styles["TableLabel"]
            ),
            risk_text
        ], [
            Paragraph(
                "<b>ASSESSMENT</b>",
                styles["TableLabel"]
            ),
            summary_text
        ]],
        colWidths=[1.65 * inch, 5.45 * inch]
    )

    risk_table.setStyle(
        TableStyle([
            ("BACKGROUND", (0, 0), (-1, -1), PALE_BLUE),

            ("BOX", (0, 0), (-1, -1), 0.8, LIGHT_GREY),

            ("LINEBELOW", (0, 0), (-1, 0), 0.4, LIGHT_GREY),

            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),

            ("LEFTPADDING", (0, 0), (-1, -1), 10),

            ("RIGHTPADDING", (0, 0), (-1, -1), 10),

            ("TOPPADDING", (0, 0), (-1, -1), 8),

            ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
        ])
    )

    elements.append(risk_table)
    elements.append(Spacer(1, 13))

    # -------------------------------------------------
    # Evidence Image
    # -------------------------------------------------

    image_path = data.get("image_path")

    if image_path and os.path.isfile(image_path):

        elements.append(
            make_section_heading(
                "Submitted Evidence Image",
                styles
            )
        )

        try:

            evidence_image = Image(
                image_path,
                width=5.8 * inch,
                height=4.0 * inch,
                kind="proportional"
            )

            evidence_image.hAlign = "CENTER"

            image_table = Table(
                [[evidence_image]],
                colWidths=[7.1 * inch]
            )

            image_table.setStyle(
                TableStyle([
                    ("BACKGROUND", (0, 0), (-1, -1), PALE_BLUE),

                    ("BOX", (0, 0), (-1, -1), 0.7, LIGHT_GREY),

                    ("ALIGN", (0, 0), (-1, -1), "CENTER"),

                    ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),

                    ("TOPPADDING", (0, 0), (-1, -1), 10),

                    ("BOTTOMPADDING", (0, 0), (-1, -1), 10),
                ])
            )

            elements.append(image_table)
            elements.append(Spacer(1, 12))

        except Exception:

            elements.append(
                Paragraph(
                    "The submitted image could not be embedded "
                    "in this PDF report.",
                    styles["Small"]
                )
            )

    # -------------------------------------------------
    # Image Metadata
    # -------------------------------------------------

    elements.append(
        make_section_heading(
            "Image Metadata",
            styles
        )
    )

    metadata_rows = [
        ["Filename", safe_text(data.get("filename"))],
        [
            "Resolution",
            safe_text(
                f'{data.get("width", "N/A")} × '
                f'{data.get("height", "N/A")}'
            )
        ],
        ["Image Format", safe_text(data.get("format"))],
        ["Color Mode", safe_text(data.get("mode"))],
        ["File Size", format_file_size(data.get("size"))],
        [
            "Inference Time",
            (
                f'{safe_text(data.get("time_taken"))} seconds'
                if data.get("time_taken") is not None
                else "Not available"
            )
        ]
    ]

    metadata_table = Table(
        [
            [
                Paragraph(
                    safe_text(row[0]),
                    styles["TableLabel"]
                ),
                Paragraph(
                    row[1],
                    styles["Table"]
                )
            ]
            for row in metadata_rows
        ],
        colWidths=[1.65 * inch, 5.45 * inch]
    )

    apply_data_table_style(metadata_table)

    elements.append(metadata_table)
    elements.append(Spacer(1, 13))

    # -------------------------------------------------
    # Cryptographic Hashes
    # -------------------------------------------------

    elements.append(
        make_section_heading(
            "Cryptographic Hash Values",
            styles
        )
    )

    hashes = data.get("hashes") or {}

    hash_rows = [
        ["Algorithm", "Calculated Hash"],
        [
            "MD5",
            hashes.get("md5", "Not available")
        ],
        [
            "SHA-1",
            hashes.get("sha1", "Not available")
        ],
        [
            "SHA-256",
            hashes.get("sha256", "Not available")
        ]
    ]

    hash_table_data = [
        [
            Paragraph(
                safe_text(row[0]),
                styles["TableLabel"]
            ),
            Paragraph(
                safe_text(row[1]),
                styles["Hash"]
            )
        ]
        for row in hash_rows
    ]

    hash_table = Table(
        hash_table_data,
        colWidths=[1.3 * inch, 5.8 * inch],
        repeatRows=1
    )

    hash_table.setStyle(
        TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), NAVY),

            ("TEXTCOLOR", (0, 0), (-1, 0), WHITE),

            ("GRID", (0, 0), (-1, -1), 0.4, LIGHT_GREY),

            ("BACKGROUND", (0, 1), (-1, -1), PALE_BLUE),

            ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),

            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),

            ("LEFTPADDING", (0, 0), (-1, -1), 8),

            ("RIGHTPADDING", (0, 0), (-1, -1), 8),

            ("TOPPADDING", (0, 0), (-1, -1), 8),

            ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
        ])
    )

    elements.append(hash_table)

    elements.append(
        Paragraph(
            "Hash values are calculated from the submitted file "
            "bytes. They can be used for later comparison to check "
            "whether a file's contents have changed. Hash values "
            "alone do not establish the source or authenticity "
            "of an image.",
            styles["Small"]
        )
    )

    elements.append(Spacer(1, 13))

    # -------------------------------------------------
    # Recommendations
    # -------------------------------------------------

    elements.append(
        make_section_heading(
            "Forensic Recommendations",
            styles
        )
    )

    recommendations = generate_recommendations(
        real_fake,
        manipulation
    )

    recommendation_content = []

    for index, recommendation in enumerate(
        recommendations,
        start=1
    ):

        recommendation_content.append(
            Paragraph(
                f"<b>{index}.</b> {safe_text(recommendation)}",
                styles["Recommendation"]
            )
        )

    recommendation_table = Table(
        [[recommendation_content]],
        colWidths=[7.1 * inch]
    )

    recommendation_table.setStyle(
        TableStyle([
            ("BACKGROUND", (0, 0), (-1, -1), PALE_BLUE),

            ("BOX", (0, 0), (-1, -1), 0.7, LIGHT_GREY),

            ("LEFTPADDING", (0, 0), (-1, -1), 12),

            ("RIGHTPADDING", (0, 0), (-1, -1), 12),

            ("TOPPADDING", (0, 0), (-1, -1), 12),

            ("BOTTOMPADDING", (0, 0), (-1, -1), 7),

            ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ])
    )

    elements.append(recommendation_table)
    elements.append(Spacer(1, 13))

    # -------------------------------------------------
    # Disclaimer
    # -------------------------------------------------

    elements.append(
        make_section_heading(
            "Important Disclaimer",
            styles
        )
    )

    disclaimer = (
        "This report was generated automatically by "
        "<b>Forensic AI (FAI)</b> using its implemented "
        "deep-learning classification models. The reported "
        "classification and confidence values are automated "
        "model outputs and may contain errors. They should not "
        "be treated as conclusive proof of authenticity, "
        "manipulation, defamation, intent or wrongdoing. "
        "The preliminary risk level is an application-defined "
        "assessment category, not a legal determination. "
        "Independent verification and review by a qualified "
        "digital forensic examiner are recommended before "
        "any consequential or legal use."
    )

    elements.append(
        Paragraph(
            disclaimer,
            styles["Small"]
        )
    )

    elements.append(Spacer(1, 10))

    # -------------------------------------------------
    # Final Report Note
    # -------------------------------------------------

    elements.append(
        Paragraph(
            "<b>END OF REPORT</b>",
            ParagraphStyle(
                "EndReport",
                parent=styles["Small"],
                alignment=TA_CENTER,
                textColor=BLUE,
                fontName="Helvetica-Bold",
                spaceBefore=8
            )
        )
    )

    # -------------------------------------------------
    # Build PDF
    # -------------------------------------------------

    def footer(canvas, document):

        draw_page_footer(
            canvas,
            document,
            report_id
        )

    pdf.build(
        elements,
        onFirstPage=footer,
        onLaterPages=footer
    )
