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

