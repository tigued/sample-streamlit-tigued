import streamlit as st
from PIL import Image 
import requests
from PIL import ImageDraw
import io #inputoutputの略

st.title('顔検出アプリ')

subscription_key = '004557bd9162439b99eec4da1957cc75'
assert subscription_key
face_api_url = 'https://20201204tigued.cognitiveservices.azure.com/face/v1.0/detect'

uploaded_file = st.file_uploader("Choose an image...", type="jpg")
if uploaded_file:
    img = Image.open(uploaded_file)
    
    with io.BytesIO() as output:
        img.save(output, format='JPEG')
        binary_img = output.getvalue() # バイナリ取得
        # バイナリファイルに変換する必要がある
        headers = {
            'Content-Type': 'application/octet-stream',
            'Ocp-Apim-Subscription-Key': subscription_key}

        params = {
            'returnFaceId': 'true',
            'returnFaceAttributes': 'age,gender,headPose,smile,facialHair,glasses,emotion,hair,makeup,occlusion,accessories,blur,exposure,noise'
        }# 単純な顔検出ならOpenCVでもできるが、このAPIだと色々判別できる

        res = requests.post(face_api_url, params=params,
                                headers=headers, data=binary_img)
        # tutorialでは画像のurlを送っているが(json={"url": image_url})、
        # 今回はバイナリイメじを送る
        results = res.json()
        for result in results:
            rect = result['faceRectangle']# 一つだけしか顔が検出されていないので[0]
            draw = ImageDraw.Draw(img)
            draw.rectangle([(rect['left'], rect['top']), (rect['left']+rect['width'], rect['top']+rect['height'])], fill=None, outline='green', width=5)
        st.image(img, caption='Uploaded Image', use_column_width=True)