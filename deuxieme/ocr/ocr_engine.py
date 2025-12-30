import numpy as np
import cv2
import re
from paddleocr import PaddleOCR

ocr = PaddleOCR(use_angle_cls=True, lang='en')

def clean_text(text):
    text = text.strip()
    text = re.sub(r"\s+", " ", text)
    text = re.sub(r"[|_•]+", "", text)
    return text

def run_ocr(pil_image):
    image = np.array(pil_image)
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    results = ocr.ocr(image)
    lines = []

    for line in results[0]:
        text = clean_text(line[1][0])
        confidence = float(line[1][1])
        if confidence < 0.5 or len(text) < 3:
            continue
        lines.append({
            "text": text,
            "confidence": confidence,
            "bbox": line[0]
        })
    return lines
