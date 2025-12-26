import os
os.environ["DISABLE_MODEL_SOURCE_CHECK"] = "True"

from paddleocr import PaddleOCR
from pdf2image import convert_from_path
import cv2
import numpy as np

# 1️⃣ Initialiser PaddleOCR
ocr = PaddleOCR(
    use_angle_cls=True,
    lang='fr'  # 'en' pour anglais, 'fr' pour français
)

# 2️⃣ Convertir le PDF en images
pdf_path = "input.pdf"
pages = convert_from_path(pdf_path, dpi=300)

all_text = ""

# 3️⃣ OCR sur chaque page
for i, page in enumerate(pages):
    print(f"Traitement de la page {i+1}...")

    # Convertir PIL Image → OpenCV
    img = np.array(page)
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

    # OCR
    result = ocr.ocr(img, cls=True)



    for line in result[0]:
        text = line[1][0]
        all_text += text + "\n"

# 4️⃣ Sauvegarder le texte dans un fichier
with open("output.txt", "w", encoding="utf-8") as f:
    f.write(all_text)

print("✅ Extraction terminée ! Texte sauvegardé dans output.txt")
