import PyPDF2
import os

def extract_text_from_pdf(path):
    text = ""
    try:
        if not os.path.exists(path):
            print(f"[ERROR] File not found: {path}")
            return ""

        with open(path, 'rb') as f:
            reader = PyPDF2.PdfReader(f)
            print(f"[INFO] Number of pages in {path}: {len(reader.pages)}")
            for page_num, page in enumerate(reader.pages):
                page_text = page.extract_text() or ""
                print(f"[INFO] Extracted {len(page_text)} characters from page {page_num + 1}")
                text += page_text
    except Exception as e:
        print(f"[ERROR] Error reading PDF: {e}")

    if not text.strip():
        print(f"[WARNING] No text extracted from {path}")
    return text


def extract_text_from_txt(path):
    text = ""
    try:
        if not os.path.exists(path):
            print(f"[ERROR] File not found: {path}")
            return ""

        with open(path, 'r', encoding='utf-8') as f:
            text = f.read()
        print(f"[INFO] Extracted {len(text)} characters from {path}")
    except Exception as e:
        print(f"[ERROR] Error reading TXT file: {e}")
    return text


if __name__ == "__main__":
    print("[DEBUG] Running utils.py as main")

    pdf_path = "../resumes/resume3.pdf"
    txt_path = "../job_descriptions/job3.txt"

    print("\n--- Testing PDF Extraction ---")
    pdf_text = extract_text_from_pdf(pdf_path)
    print(f"\nPreview from PDF:\n{pdf_text[:300]}")

    print("\n--- Testing TXT Extraction ---")
    txt_text = extract_text_from_txt(txt_path)
    print(f"\nPreview from TXT:\n{txt_text[:300]}")


