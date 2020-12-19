import base64
import io
import json
import os
import pytesseract

import logging
logging.getLogger().setLevel(logging.INFO)

logging.info("---START---")

try:
    logging.error("Importing PIL libraries")

    import PIL
    logging.info("PIL Version: " + str(PIL.__version__))

    # import PIL.Image as Image
    # from PIL import Image
    # from PIL.Image import core as image

    logging.error("Successfully imported PIL libraries")
except Exception as e:
    logging.error("Failed to import PIL libraries")
    logging.exception(e)

if os.getenv('AWS_EXECUTION_ENV') is not None:
    os.environ['LD_LIBRARY_PATH'] = '/opt/lib'
    os.environ['TESSDATA_PREFIX'] = '/opt/tessdata'
    pytesseract.pytesseract.tesseract_cmd = '/opt/tesseract'


def ocr(event, context):

    request_body = json.loads(event['body'])
    image = io.BytesIO(base64.b64decode(request_body['image']))

    text = pytesseract.image_to_string(PIL.Image.open(image))

    body = {
        "text": text
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response

