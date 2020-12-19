import json
import pytesseract
from PIL import Image


def ocr(event, context):

    body = {
        "text": pytesseract.image_to_string(Image.open('test.jpg')),
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response