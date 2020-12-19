#docker build -t tesseract .
#
#rm -rf tesseract
#mkdir tesseract
#docker run -v $PWD/tesseract:/tmp/build tesseract sh /tmp/build_tesseract.sh

rm -rf layer
mkdir layer

unzip tesseract/tesseract.zip -d layer
mkdir -p layer/python/lib/python3.7/site-packages/

# pip3 install image pytesseract -t layer/python/lib/python3.7/site-packages/
# pip3 install image pytesseract -t layer/

pip3 install -r requirements.txt -t layer/python/lib/python3.7/site-packages/

# pip3 install -r requirements.txt -t layer/

serverless deploy --stage dev

# python3 use_ocr_as_a_service.py

# serverless remove --stage dev

