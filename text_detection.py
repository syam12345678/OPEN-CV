import cv2
from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Users\saket\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

def detect_text(image_path):
    img = Image.open(image_path)
    text = pytesseract.image_to_string(img)
    return text

if __name__ == "__main__":
    image_path = r"C:\Users\Syam Prakash\OneDrive\Pictures\stop2.jpg"
    try:
        img = cv2.imread(image_path)
        if img is None:
            raise FileNotFoundError(f"Image not found at path: {image_path}")
        cv2.imshow("Image", img)
        detected_text = detect_text(image_path)
        print("Detected Text:")
        print(detected_text)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    except Exception as e:
        print(f"Error: {e}")
