from fpdf import FPDF, XPos, YPos
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")

df = pd.read_csv("topics.csv")

for _, row in df.iterrows():
    topic = row["Topic"]
    pages = int(row["Pages"])

    pdf.add_page()

    # ===== HEADER =====
    pdf.set_font("Times", style="B", size=24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(0, 12, topic, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.line(10, 22, 200, 22)

    # ===== FOOTER =====
    pdf.set_y(287)  # bottom of A4 page
    pdf.set_font("Times", style="I", size=8)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(0, 10, topic, align="R")

    # ===== EXTRA PAGES =====
    for _ in range(pages - 1):
        pdf.add_page()

        pdf.set_y(287)
        pdf.set_font("Times", style="I", size=8)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(0, 10, topic, align="R")

pdf.output("output.pdf")
print("PDF generated: output.pdf")

import os
os.startfile("output.pdf") # make sure default app is set for PDFs

