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


# def generate_report(data, output_path):

#     # =====================================================
#     # Styles
#     # =====================================================

#     styles = getSampleStyleSheet()

#     title_style = styles["Heading1"]
#     title_style.alignment = TA_CENTER
#     title_style.textColor = colors.white

#     heading = styles["Heading2"]
#     heading.textColor = colors.HexColor("#0B3C91")

#     normal = styles["BodyText"]

#     small = styles["BodyText"]
#     small.fontSize = 9


#     # =====================================================
#     # PDF Setup
#     # =====================================================

#     pdf = SimpleDocTemplate(
#         output_path,
#         rightMargin=35,
#         leftMargin=35,
#         topMargin=35,
#         bottomMargin=35
#     )

#     elements = []


#     # =====================================================
#     # Report Information
#     # =====================================================

#     report_id = "FAI-" + str(uuid.uuid4())[:8].upper()

#     now = datetime.datetime.now()

#     report_date = now.strftime("%d %B %Y")
#     report_time = now.strftime("%I:%M:%S %p")


#     # =====================================================
#     # Logo
#     # =====================================================

#     logo_path = "static/images/logo.png"

#     if os.path.exists(logo_path):

#         logo = Image(
#             logo_path,
#             width=0.9 * inch,
#             height=0.9 * inch
#         )

#     else:

#         logo = Paragraph("", normal)



#     # =====================================================
#     # Header
#     # =====================================================

#     header = Table(
#         [[

#             logo,

#             Paragraph(
#                 "<font size=22><b>FORENSIC AI</b></font><br/>"
#                 "<font size=11>"
#                 "AI-Based Digital Image Authentication System"
#                 "</font>",
#                 title_style
#             )

#         ]],

#         colWidths=[
#             1.2 * inch,
#             5.8 * inch
#         ]
#     )


#     header.setStyle(TableStyle([

#         (
#             "BACKGROUND",
#             (0,0),
#             (-1,-1),
#             colors.HexColor("#0B3C91")
#         ),

#         (
#             "VALIGN",
#             (0,0),
#             (-1,-1),
#             "MIDDLE"
#         ),

#         (
#             "TOPPADDING",
#             (0,0),
#             (-1,-1),
#             15
#         ),

#         (
#             "BOTTOMPADDING",
#             (0,0),
#             (-1,-1),
#             15
#         )

#     ]))


#     elements.append(header)

#     elements.append(
#         Spacer(1,20)
#     )


#     # =====================================================
#     # Case Information
#     # =====================================================

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


#     case_table.setStyle(TableStyle([

#         (
#             "GRID",
#             (0,0),
#             (-1,-1),
#             0.5,
#             colors.grey
#         ),

#         (
#             "BACKGROUND",
#             (0,0),
#             (0,-1),
#             colors.HexColor("#E8F1FF")
#         ),

#         (
#             "FONTNAME",
#             (0,0),
#             (-1,-1),
#             "Helvetica-Bold"
#         )

#     ]))


#     elements.append(case_table)

#     elements.append(
#         Spacer(1,20)
#     )


#     # =====================================================
#     # Evidence Image
#     # =====================================================

#     elements.append(
#         Paragraph(
#             "Evidence Image",
#             heading
#         )
#     )


#     if os.path.exists(data["image_path"]):

#         evidence_image = Image(
#             data["image_path"],
#             width=4.5 * inch,
#             height=4.5 * inch
#         )


#         image_table = Table(
#             [[evidence_image]],
#             colWidths=[
#                 5 * inch
#             ]
#         )


#         image_table.setStyle(TableStyle([

#             (
#                 "GRID",
#                 (0,0),
#                 (-1,-1),
#                 1,
#                 colors.HexColor("#0B3C91")
#             ),

#             (
#                 "ALIGN",
#                 (0,0),
#                 (-1,-1),
#                 "CENTER"
#             )

#         ]))


#         elements.append(image_table)

#         elements.append(
#             Spacer(1,10)
#         )


#     # =====================================================
#     # Detection Summary
#     # =====================================================

#     elements.append(
#         Paragraph(
#             "Detection Summary",
#             heading
#         )
#     )


#     detection = Table([

#         [
#             "Real / Fake",
#             data.get("real_fake")
#         ],

#         [
#             "Manipulation",
#             data.get("manipulation")
#         ],

#         [
#             "Confidence",
#             f'{data.get("real_fake_confidence")}%'
#         ],

#         [
#             "Manipulation Confidence",
#             (
#                 "N/A"
#                 if data.get("manipulation_confidence") is None
#                 else
#                 f'{data.get("manipulation_confidence")}%'
#             )
#         ]

#     ],
#     colWidths=[
#         2.5 * inch,
#         3.8 * inch
#     ])


#     detection.setStyle(TableStyle([

#         (
#             "GRID",
#             (0,0),
#             (-1,-1),
#             0.5,
#             colors.grey
#         ),

#         (
#             "BACKGROUND",
#             (0,0),
#             (0,-1),
#             colors.HexColor("#E8F1FF")
#         ),

#         (
#             "FONTNAME",
#             (0,0),
#             (-1,-1),
#             "Helvetica-Bold"
#         )

#     ]))


#     elements.append(detection)

#     elements.append(
#         Spacer(1,20)
#     )


#     # =====================================================
#     # Metadata
#     # =====================================================

#     elements.append(
#         Paragraph(
#             "Image Metadata",
#             heading
#         )
#     )


#     metadata = Table([

#         [
#             "Filename",
#             data.get("filename")
#         ],

#         [
#             "Resolution",
#             f'{data.get("width")} × {data.get("height")}'
#         ],

#         [
#             "Format",
#             data.get("format")
#         ],

#         [
#             "Color Mode",
#             data.get("mode")
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


#     metadata.setStyle(TableStyle([

#         (
#             "GRID",
#             (0,0),
#             (-1,-1),
#             0.5,
#             colors.grey
#         ),

#         (
#             "BACKGROUND",
#             (0,0),
#             (0,-1),
#             colors.HexColor("#E8F1FF")
#         )

#     ]))


#     elements.append(metadata)

#     elements.append(
#         Spacer(1,20)
#     )


#     # =====================================================
#     # Recommendation
#     # =====================================================

#     elements.append(
#         Paragraph(
#             "Recommendation",
#             heading
#         )
#     )


#     elements.append(
#         Paragraph(
#             data.get(
#                 "recommendation",
#                 ""
#             ),
#             normal
#         )
#     )


#     elements.append(
#         Spacer(1,20)
#     )


#     # =====================================================
#     # Disclaimer
#     # =====================================================

#     elements.append(
#         Paragraph(
#             "Disclaimer",
#             heading
#         )
#     )


#     elements.append(
#         Paragraph(

#             "This forensic report was generated automatically by "
#             "<b>Forensic AI (FAI)</b>. "
#             "The results are based on deep learning models and "
#             "should be reviewed by a qualified forensic examiner "
#             "before legal use.",

#             small
#         )
#     )


#     # =====================================================
#     # Build PDF
#     # =====================================================

#     pdf.build(elements)

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    Image
)

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.enums import TA_CENTER
from reportlab.lib import colors
from reportlab.lib.units import inch

import datetime
import uuid
import os
import sys


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
# Generate Report
# =====================================================

def generate_report(data, output_path):


    # =================================================
    # Styles
    # =================================================

    styles = getSampleStyleSheet()


    title_style = styles["Heading1"]

    title_style.alignment = TA_CENTER

    title_style.textColor = colors.white


    heading = styles["Heading2"]

    heading.textColor = colors.HexColor(
        "#0B3C91"
    )


    normal = styles["BodyText"]


    small = styles["BodyText"]

    small.fontSize = 9


    # =================================================
    # PDF Setup
    # =================================================

    pdf = SimpleDocTemplate(

        output_path,

        rightMargin=35,

        leftMargin=35,

        topMargin=35,

        bottomMargin=35

    )


    elements = []


    # =================================================
    # Report Information
    # =================================================

    report_id = (

        "FAI-"
        +
        str(
            uuid.uuid4()
        )[:8].upper()

    )


    now = datetime.datetime.now()


    report_date = now.strftime(
        "%d %B %Y"
    )


    report_time = now.strftime(
        "%I:%M:%S %p"
    )


    # =================================================
    # Logo
    # =================================================

    logo_path = resource_path(
        os.path.join(
            "static",
            "images",
            "logo.png"
        )
    )


    if os.path.exists(
        logo_path
    ):

        logo = Image(

            logo_path,

            width=0.9 * inch,

            height=0.9 * inch

        )

    else:

        logo = Paragraph(
            "",
            normal
        )


    # =================================================
    # Header
    # =================================================

    header = Table(

        [[

            logo,

            Paragraph(

                "<font size=22>"
                "<b>FORENSIC AI</b>"
                "</font><br/>"

                "<font size=11>"
                "AI-Based Digital Image "
                "Authentication System"
                "</font>",

                title_style

            )

        ]],

        colWidths=[

            1.2 * inch,

            5.8 * inch

        ]

    )


    header.setStyle(
        TableStyle([

            (

                "BACKGROUND",

                (0, 0),

                (-1, -1),

                colors.HexColor(
                    "#0B3C91"
                )

            ),

            (

                "VALIGN",

                (0, 0),

                (-1, -1),

                "MIDDLE"

            ),

            (

                "TOPPADDING",

                (0, 0),

                (-1, -1),

                15

            ),

            (

                "BOTTOMPADDING",

                (0, 0),

                (-1, -1),

                15

            )

        ])
    )


    elements.append(
        header
    )


    elements.append(
        Spacer(1, 20)
    )


    # =================================================
    # Case Information
    # =================================================

    elements.append(
        Paragraph(
            "Case Information",
            heading
        )
    )


    case_table = Table([

        [
            "Report ID",
            report_id
        ],

        [
            "Examiner",
            data.get(
                "examiner",
                "FAI System"
            )
        ],

        [
            "Date",
            report_date
        ],

        [
            "Time",
            report_time
        ],

        [
            "System",
            "FAI Version 1.0"
        ],

        [
            "Classification",
            "Confidential"
        ]

    ],

    colWidths=[

        2.1 * inch,

        4.2 * inch

    ])


    case_table.setStyle(
        TableStyle([

            (

                "GRID",

                (0, 0),

                (-1, -1),

                0.5,

                colors.grey

            ),

            (

                "BACKGROUND",

                (0, 0),

                (0, -1),

                colors.HexColor(
                    "#E8F1FF"
                )

            ),

            (

                "FONTNAME",

                (0, 0),

                (-1, -1),

                "Helvetica-Bold"

            )

        ])
    )


    elements.append(
        case_table
    )


    elements.append(
        Spacer(1, 20)
    )


    # =================================================
    # Evidence Image
    # =================================================

    elements.append(
        Paragraph(
            "Evidence Image",
            heading
        )
    )


    image_path = data.get(
        "image_path"
    )


    if image_path and os.path.exists(
        image_path
    ):

        evidence_image = Image(

            image_path,

            width=4.5 * inch,

            height=4.5 * inch

        )


        image_table = Table(

            [[evidence_image]],

            colWidths=[

                5 * inch

            ]

        )


        image_table.setStyle(
            TableStyle([

                (

                    "GRID",

                    (0, 0),

                    (-1, -1),

                    1,

                    colors.HexColor(
                        "#0B3C91"
                    )

                ),

                (

                    "ALIGN",

                    (0, 0),

                    (-1, -1),

                    "CENTER"

                )

            ])
        )


        elements.append(
            image_table
        )


        elements.append(
            Spacer(1, 10)
        )


    # =================================================
    # Detection Summary
    # =================================================

    elements.append(
        Paragraph(
            "Detection Summary",
            heading
        )
    )


    detection = Table([

        [
            "Real / Fake",
            data.get(
                "real_fake"
            )
        ],

        [
            "Manipulation",
            data.get(
                "manipulation"
            )
        ],

        [
            "Confidence",
            f'{data.get("real_fake_confidence")}%'
        ],

        [
            "Manipulation Confidence",

            (

                "N/A"

                if data.get(
                    "manipulation_confidence"
                ) is None

                else

                f'{data.get("manipulation_confidence")}%'

            )

        ]

    ],

    colWidths=[

        2.5 * inch,

        3.8 * inch

    ])


    detection.setStyle(
        TableStyle([

            (

                "GRID",

                (0, 0),

                (-1, -1),

                0.5,

                colors.grey

            ),

            (

                "BACKGROUND",

                (0, 0),

                (0, -1),

                colors.HexColor(
                    "#E8F1FF"
                )

            ),

            (

                "FONTNAME",

                (0, 0),

                (-1, -1),

                "Helvetica-Bold"

            )

        ])
    )


    elements.append(
        detection
    )


    elements.append(
        Spacer(1, 20)
    )


    # =================================================
    # Metadata
    # =================================================

    elements.append(
        Paragraph(
            "Image Metadata",
            heading
        )
    )


    metadata = Table([

        [
            "Filename",
            data.get(
                "filename"
            )
        ],

        [
            "Resolution",

            f'{data.get("width")} × '
            f'{data.get("height")}'
        ],

        [
            "Format",
            data.get(
                "format"
            )
        ],

        [
            "Color Mode",
            data.get(
                "mode"
            )
        ],

        [
            "File Size",
            f'{data.get("size")} MB'
        ],

        [
            "Inference Time",
            f'{data.get("time_taken")} sec'
        ]

    ],

    colWidths=[

        2.5 * inch,

        3.8 * inch

    ])


    metadata.setStyle(
        TableStyle([

            (

                "GRID",

                (0, 0),

                (-1, -1),

                0.5,

                colors.grey

            ),

            (

                "BACKGROUND",

                (0, 0),

                (0, -1),

                colors.HexColor(
                    "#E8F1FF"
                )

            )

        ])
    )


    elements.append(
        metadata
    )


    elements.append(
        Spacer(1, 20)
    )


    # =================================================
    # Recommendation
    # =================================================

    elements.append(
        Paragraph(
            "Recommendation",
            heading
        )
    )


    elements.append(
        Paragraph(

            data.get(
                "recommendation",
                ""
            ),

            normal

        )
    )


    elements.append(
        Spacer(1, 20)
    )


    # =================================================
    # Disclaimer
    # =================================================

    elements.append(
        Paragraph(
            "Disclaimer",
            heading
        )
    )


    elements.append(
        Paragraph(

            "This forensic report was generated "
            "automatically by <b>Forensic AI (FAI)</b>. "
            "The results are based on deep learning "
            "models and should be reviewed by a qualified "
            "forensic examiner before legal use.",

            small

        )
    )


    # =================================================
    # Build PDF
    # =================================================

    pdf.build(
        elements
    )