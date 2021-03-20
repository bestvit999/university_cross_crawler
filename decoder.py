
import base64
from PIL import Image # image to text
import pytesseract # image to text

def save_image_base64(raw, path_to_file):
    img_data = raw.replace('data:image/png;base64,', '')
    img_data_bytes = img_data.encode()
    with open("{path}".format(path=path_to_file), "wb") as fh:
        fh.write(base64.decodebytes(img_data_bytes))

def image_to_text(path_to_file):
    img = Image.open(path_to_file)
    text = pytesseract.image_to_string(img, lang='eng')
    return text

def base64_to_text(raw, path_to_file='tmp.png'):
    save_image_base64(raw=raw, path_to_file=path_to_file)
    return image_to_text('tmp.png')[:-2]