import os
os.environ["DISABLE_MODEL_SOURCE_CHECK"] = "True"

from processing.text_cleaning import group_lines_to_paragraphs
from ocr.pdf_to_image import pdf_to_images
from ocr.ocr_engine import run_ocr
import json
import os
from processing.table_extractor import build_table



PDF_PATH = "data/raw-pdfs/input.pdf"
POPPLER_PATH = r"C:\poppler\Library\bin"
OUTPUT_JSON = "data/outputs/output.json"


pages = pdf_to_images(PDF_PATH, POPPLER_PATH)
#pages = convert_from_path(PDF_PATH, dpi=300)
document_data = {"document": os.path.basename(PDF_PATH), "pages": []}

for i, page in enumerate(pages):
    print(f"OCR page {i+1}...")
    lines = run_ocr(page)

    table = build_table(lines)

    paragraphs = group_lines_to_paragraphs(lines)

    document_data["pages"].append({
        "page_number": i + 1,
        "table": table
    })


with open(OUTPUT_JSON, "w", encoding="utf-8") as f:
    json.dump(document_data, f, ensure_ascii=False, indent=2)

print("✅ OCR terminé → output.json")
