import subprocess, sys, os
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor, black, white
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, PageBreak,
                                HRFlowable, Table, TableStyle)
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

EXPERIMENTS_DIR = os.path.dirname(os.path.abspath(__file__))

EXPERIMENTS = [
    {
        "no": 3,
        "title": "Descriptive Statistics, Correlation Analysis and Predictive Model",
        "folder": "3_Descriptive_Stats_Predictive_Model",
        "aim": "To perform descriptive statistics (mean, standard deviation, median) and correlation analysis, and build a predictive model using a dataset created as a Pandas DataFrame.",
        "algorithm": [
            "Import required libraries.",
            "Create a dataset using a Pandas DataFrame.",
            "Compute descriptive statistics using describe().",
            "Calculate correlation matrix using corr().",
            "Split dataset into training and testing data.",
            "Train a Linear Regression model.",
            "Predict the output."
        ],
        "result": "Thus descriptive statistics, correlation analysis, and predictive modeling were successfully performed using a Pandas DataFrame."
    },
    {
        "no": 4,
        "title": "OLAP Operations using Pandas",
        "folder": "4_OLAP_Operations",
        "aim": "To perform OLAP operations (Drill-down, Slice, Dice) using Pandas DataFrame.",
        "algorithm": [
            "Create a sales dataset using DataFrame.",
            "Perform drill-down using groupby().",
            "Perform slice operation using filtering.",
            "Perform dice operation using pivot_table()."
        ],
        "result": "Thus OLAP operations such as Drill-down, Slice, and Dice were successfully simulated using Pandas DataFrame."
    },
    {
        "no": 5,
        "title": "Data Preprocessing (Missing Values & Normalization)",
        "folder": "5_Data_Preprocessing",
        "aim": "To perform data preprocessing operations including handling missing values and normalization.",
        "algorithm": [
            "Create DataFrame containing missing values.",
            "Replace missing values with mean.",
            "Normalize data using MinMaxScaler."
        ],
        "result": "Thus missing values were handled and the dataset was normalized successfully."
    },
    {
        "no": 6,
        "title": "Dimensionality Reduction using PCA, KPCA and SVD",
        "folder": "6_Dimensionality_Reduction",
        "aim": "To perform dimensionality reduction using PCA, Kernel PCA, and SVD.",
        "algorithm": [
            "Create dataset using DataFrame.",
            "Apply PCA.",
            "Apply Kernel PCA.",
            "Apply SVD.",
            "Display reduced features."
        ],
        "result": "Thus dimensionality reduction was performed using PCA, KPCA, and SVD successfully."
    },
    {
        "no": 7,
        "title": "Bivariate and Multivariate Analysis",
        "folder": "7_Bivariate_Multivariate_Analysis",
        "aim": "To perform bivariate and multivariate analysis using visualization techniques.",
        "algorithm": [
            "Create dataset using DataFrame.",
            "Plot scatter plot for bivariate analysis.",
            "Plot pairplot for multivariate analysis."
        ],
        "result": "Thus bivariate and multivariate analysis was successfully performed."
    },
    {
        "no": 8,
        "title": "Classification Model (Customer Churn)",
        "folder": "8_Classification_Churn",
        "aim": "To build a classification model using Logistic Regression.",
        "algorithm": [
            "Create dataset using DataFrame.",
            "Split dataset into training and testing sets.",
            "Train logistic regression model.",
            "Predict churn values."
        ],
        "result": "Thus a Logistic Regression classification model was successfully implemented."
    },
    {
        "no": 9,
        "title": "Customer Segmentation",
        "folder": "9_Customer_Segmentation",
        "aim": "To segment customers based on purchase behavior using K-Means clustering.",
        "algorithm": [
            "Create customer dataset.",
            "Select features.",
            "Apply KMeans clustering.",
            "Assign clusters."
        ],
        "result": "Thus customers were successfully segmented using K-Means clustering."
    },
    {
        "no": 10,
        "title": "Employee Attrition Prediction",
        "folder": "10_Decision_Tree_Attrition",
        "aim": "To predict whether an employee will leave the company using Decision Tree classification.",
        "algorithm": [
            "Create employee dataset.",
            "Split dataset.",
            "Train Decision Tree model.",
            "Predict employee attrition."
        ],
        "result": "Thus employee attrition prediction was successfully implemented using a Decision Tree classifier."
    },
]


def capture_output(script_path, exp_folder=""):
    env = os.environ.copy()
    if exp_folder == "7_Bivariate_Multivariate_Analysis":
        env["MPLBACKEND"] = "Agg"
    try:
        result = subprocess.run(
            [sys.executable, script_path],
            capture_output=True, text=True, timeout=30,
            cwd=EXPERIMENTS_DIR, env=env
        )
        if result.returncode != 0:
            return f"Error running script:\n{result.stderr[:1500]}"
        return result.stdout
    except subprocess.TimeoutExpired:
        return "Output not available (timeout)"


def read_code(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()

def code_to_html(code_text):
    lines = code_text.split("\n")
    result = []
    for line in lines:
        stripped = line.lstrip()
        leading = line[:len(line) - len(stripped)]
        leading = leading.replace(" ", "&nbsp;").replace("\t", "&nbsp;&nbsp;&nbsp;&nbsp;")
        stripped = stripped.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        result.append(leading + stripped)
    return "<br/>".join(result)


HEADER_COLOR = HexColor("#1a237e")
ACCENT_COLOR = HexColor("#283593")
LIGHT_BG = HexColor("#f5f5f5")
BORDER_COLOR = HexColor("#e0e0e0")


def make_section_box(section_name, items, style):
    """Wrap items in a bordered box with section header."""
    rows = []
    header_cell = Paragraph(f"<b>{section_name}</b>", ParagraphStyle(
        "sectionHead", fontSize=11, leading=15, textColor=white,
        alignment=TA_CENTER, spaceBefore=1*mm, spaceAfter=1*mm
    ))
    rows.append([header_cell])
    for item in items:
        rows.append([item])
    t = Table(rows, colWidths=[460])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), HEADER_COLOR),
        ("BACKGROUND", (0, 1), (-1, -1), HexColor("#fafafa")),
        ("BOX", (0, 0), (-1, -1), 0.5, BORDER_COLOR),
        ("TOPPADDING", (0, 0), (-1, -1), 2),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 2),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
        ("LINEBELOW", (0, 0), (-1, 0), 0.5, BORDER_COLOR),
    ]))
    return t


def build_pdf():
    pdf_path = os.path.join(EXPERIMENTS_DIR, "Business_Analytics_Lab_Manual.pdf")
    doc = SimpleDocTemplate(
        pdf_path, pagesize=A4,
        leftMargin=20*mm, rightMargin=20*mm,
        topMargin=18*mm, bottomMargin=18*mm
    )

    styles = getSampleStyleSheet()

    # --- Custom styles ---
    body = ParagraphStyle("body", parent=styles["Normal"],
                          fontSize=10, leading=14, spaceAfter=2*mm, alignment=TA_JUSTIFY)
    code_s = ParagraphStyle("codeS", parent=styles["Code"],
                            fontSize=7.5, leading=10, spaceAfter=1*mm,
                            leftIndent=2*mm, backColor=LIGHT_BG,
                            borderWidth=0.5, borderColor=BORDER_COLOR, borderPadding=4,
                            fontName="Courier", alignment=TA_LEFT)
    output_s = ParagraphStyle("outS", parent=styles["Code"],
                              fontSize=7, leading=9.5, spaceAfter=1*mm,
                              leftIndent=2*mm, backColor=HexColor("#fafafa"),
                              borderWidth=0.5, borderColor=HexColor("#eeeeee"), borderPadding=4,
                              fontName="Courier", alignment=TA_LEFT)
    center = ParagraphStyle("center", parent=body, alignment=TA_CENTER)
    step_s = ParagraphStyle("step", parent=body, leftIndent=8*mm,
                            spaceBefore=0.5*mm, spaceAfter=0.5*mm)

    story = []

    # ===================== TITLE PAGE =====================
    story.append(Spacer(1, 50*mm))
    story.append(Paragraph("Business Analytics", ParagraphStyle(
        "t1", parent=styles["Title"], fontSize=26, leading=32,
        textColor=HEADER_COLOR, alignment=TA_CENTER, spaceAfter=4*mm)))
    story.append(Paragraph("Lab Manual", ParagraphStyle(
        "t2", parent=styles["Title"], fontSize=22, leading=28,
        textColor=HEADER_COLOR, alignment=TA_CENTER, spaceAfter=12*mm)))
    story.append(HRFlowable(width="50%", thickness=2, color=HEADER_COLOR, spaceAfter=12*mm))
    story.append(Paragraph("Experiments 3 - 10", ParagraphStyle(
        "sub", parent=styles["Normal"], fontSize=14, leading=18,
        textColor=ACCENT_COLOR, alignment=TA_CENTER, spaceAfter=8*mm)))

    topics = [
        "3. Descriptive Statistics, Correlation Analysis & Predictive Model",
        "4. OLAP Operations (Drill-down, Slice, Dice)",
        "5. Data Preprocessing (Missing Values & Normalization)",
        "6. Dimensionality Reduction (PCA, KPCA, SVD)",
        "7. Bivariate & Multivariate Analysis",
        "8. Classification Model (Customer Churn)",
        "9. Customer Segmentation",
        "10. Employee Attrition Prediction",
    ]
    for t in topics:
        story.append(Paragraph(t, ParagraphStyle(
            "tlist", parent=center, fontSize=11, leading=16, spaceAfter=1*mm)))
    story.append(Spacer(1, 20*mm))
    story.append(Paragraph("Each experiment includes: Aim, Algorithm, Code, Output, Result", center))
    story.append(Spacer(1, 40*mm))

    # ===================== EXPERIMENTS =====================
    for exp in EXPERIMENTS:
        story.append(PageBreak())

        # --- Experiment Header ---
        story.append(Paragraph(
            f"Experiment {exp['no']}: {exp['title']}",
            ParagraphStyle("expH", fontSize=16, leading=22, spaceBefore=0,
                           spaceAfter=1*mm, textColor=HEADER_COLOR, bold=1)))
        story.append(HRFlowable(width="100%", thickness=2, color=HEADER_COLOR, spaceAfter=6*mm))

        # --- AIM ---
        aim_box = make_section_box("AIM", [Paragraph(exp["aim"], body)], body)
        story.append(aim_box)
        story.append(Spacer(1, 4*mm))

        # --- ALGORITHM ---
        algo_items = []
        for i, step in enumerate(exp["algorithm"], 1):
            algo_items.append(Paragraph(f"<b>Step {i}:</b>  {step}", step_s))
        algo_box = make_section_box("ALGORITHM", algo_items, body)
        story.append(algo_box)
        story.append(Spacer(1, 4*mm))

        # --- CODE ---
        folder_path = os.path.join(EXPERIMENTS_DIR, exp["folder"], "code.py")
        if os.path.exists(folder_path):
            code_text = read_code(folder_path)
            code_html = code_to_html(code_text)
            code_lines_html = code_html.split("<br/>")
            code_chunks = []
            for i in range(0, len(code_lines_html), 50):
                chunk = "<br/>".join(code_lines_html[i:i+50])
                code_chunks.append(Paragraph(chunk, code_s))
            code_box = make_section_box("CODE", code_chunks, body)
            story.append(code_box)
            story.append(Spacer(1, 4*mm))

        # --- OUTPUT ---
        script_path = os.path.join(EXPERIMENTS_DIR, exp["folder"], "code.py")
        if os.path.exists(script_path):
            output_text = capture_output(script_path, exp["folder"])
            if len(output_text) > 4000:
                output_text = output_text[:4000] + "\n\n... [truncated]"
            output_html = code_to_html(output_text)
            out_lines = output_html.split("<br/>")
            out_chunks = []
            for i in range(0, len(out_lines), 40):
                chunk = "<br/>".join(out_lines[i:i+40])
                out_chunks.append(Paragraph(chunk, output_s))
            out_box = make_section_box("OUTPUT", out_chunks, body)
            story.append(out_box)
            story.append(Spacer(1, 4*mm))

        # --- RESULT ---
        res_box = make_section_box("RESULT", [Paragraph(exp["result"], body)], body)
        story.append(res_box)

    doc.build(story)
    return pdf_path


if __name__ == "__main__":
    path = build_pdf()
    print(f"PDF generated: {path}")
