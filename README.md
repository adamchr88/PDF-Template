# PDF Topic Template Generator (CSV → PDF)

A Python program that reads topics from a CSV file and automatically generates a clean multi-page **A4 PDF template**.

Each topic becomes its own section in the PDF:
- The first page includes a **header title** and a **line separator**
- Every page includes a **footer** showing the topic name
- The number of pages per topic is controlled using the `Pages` column in the CSV

The program saves the PDF as `output.pdf` and opens it automatically (Windows).

---

## ✅ Features

- Generates an **A4 PDF** (`output.pdf`)
- Reads topics from **topics.csv**
- First page per topic contains:
  - Large topic title header
  - Separator line
- All pages contain a footer with the topic name (bottom-right)
- Adds extra blank pages per topic based on `Pages`
- Automatically opens the PDF after generation (Windows)

---

## 📁 Project Structure

PdfTemplate/
│
├── main.py
├── topics.csv
└── output.pdf (generated after running)

---

## 🧾 CSV Format (topics.csv)

Your CSV file must be named **topics.csv** and contain these exact columns:

- `Topic`
- `Pages`

Example `topics.csv`:

```csv
Topic,Pages
Algebra,3
Calculus,2
Computer Networks,4

## ⚙️ Requirements

Install dependencies:

pip install fpdf2 pandas

## ▶️ How to Run

Run the program from the folder containing main.py and topics.csv:

python main.py


Output:

output.pdf is created in the same folder

The PDF auto-opens after generating

## 🖨️ Output Example

For a row like:

Topic,Pages
Algebra,3


The PDF will contain:

Page 1: Topic header + line + footer

Page 2: Blank page + footer

Page 3: Blank page + footer

## 🛠️ Notes / Common Issues

✅ Deprecation Warnings

This project uses the updated FPDF syntax:

new_x=XPos.LMARGIN, new_y=YPos.NEXT


So it avoids the deprecated ln=1 parameter.

⚠️ Windows PDF Opening Issue (os.startfile)

This line is used to open the PDF automatically:

os.startfile("output.pdf")


It works on Windows only and requires a default PDF viewer.

If you get a WinError, set a default PDF app:

Right click any .pdf file

Open with → choose Edge / Chrome / Adobe Reader

Tick ✅ Always use this app

## 🚀 Possible Improvements

Add page numbers (e.g. Page 3 of 20)

Add a cover page

Add a table of contents

Support different PDF themes (fonts, spacing, colors)

Export each topic as its own PDF file

Web version (Streamlit upload CSV → generate PDF)
