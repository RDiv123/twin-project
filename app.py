import streamlit as st
import json
import requests
import base64
from PIL import Image
import io

#creating the web app
#st.set_page_config(layout="wide")

#setting up the title
st.title('*Diseased Crop Detector*')
st.subheader("Web Application to detect *Healthy/Diseased* Tomatoes, Apples, and Potato Crop")
col1, col2 = st.tabs(['**Fruit Detector**:tomato:','**Leaf Detector**:leaves:'])

count = 0
# Healthy and Rotten fruit column
with col1:
  st.header("***Rotten Healthy Fruit Classifier***")
  PREDICTED_LABELS = ["Rotten Potato", "Fresh Potato","Rotten Apple","Fresh Apple","Rotten Tomato","Fresh Tomato"]

  def get_prediction(image_data):
    #replace your image classification ai service URL
    #url = 'https://askai.aiclub.world/d6c4acde-66ce-4783-97ba-f6ea1795b3aa'
    url = 'https://askai.aiclub.world/a021b8b4-4c2a-4c9e-ba4c-3b1d8e011079'
    r = requests.post(url, data=image_data)
    response = r.json()['predicted_label']
    score = r.json()['score']
    print("Predicted_label: {} and confidence_score: {}".format(response,score))
    return response, score

  #file uploader
  image = st.file_uploader(label="Upload an image",accept_multiple_files=False, help="Upload an image to classify them", key= count)
  count += 1
  if image:
      #converting the image to bytes
      img = Image.open(image)
      buf = io.BytesIO()
      img.save(buf,format = 'JPEG')
      byte_im = buf.getvalue()

      #converting bytes to b64encoding
      payload = base64.b64encode(byte_im)

      #file details
      file_details = {
      "file name": image.name,
      "file type": image.type,
      "file size": image.size
    }

    #predictions
      response, scores = get_prediction(payload)

    #if you are using the model deployment in navigator
    #you need to define the labels
      response_label = PREDICTED_LABELS[response]

      st.metric("*Prediction Label*",response_label)

    #setting up the image
      st.image(img)

# column2 : Healthy/diseased leaves
with col2:

#these are main classes your image is trained on
#you can define the classes in alphabectical order
  PREDICTED_LABELS = ['apple diseased', 'apple healthy', 'potato diseased', 'potato healthy', 'tomato diseased', 'tomato healthy']


  def get_prediction(image_data):
  #replace your image classification ai service URL
    #url = 'https://askai.aiclub.world/864afd49-b5dc-479a-9f22-04dbe82fa944'
    url = 'https://askai.aiclub.world/74b3c536-0e90-4f2a-afee-ca8c95e2a56e'
    r = requests.post(url, data=image_data)
    response = r.json()['predicted_label']
    score = r.json()['score']
    return response, score

  #setting up the header
  st.header("***Leaf Disease Classifier***                                                               ")#change according to your project

  #file uploader
  image = st.file_uploader(label="Upload an image",accept_multiple_files=False, help="Upload an image to classify them", key=count)
  if image:
      #converting the image to bytes
      img = Image.open(image)
      buf = io.BytesIO()
      img.save(buf,format = 'JPEG')
      byte_im = buf.getvalue()

      #converting bytes to b64encoding
      payload = base64.b64encode(byte_im)

      #file details
      file_details = {
        "file name": image.name,
        "file type": image.type,
        "file size": image.size
      }

    #predictions
      response, scores = get_prediction(payload)

    #if you are using the model deployment in navigator
    #you need to define the labels
      response_label = PREDICTED_LABELS[response]

      st.metric("*Prediction Label*",response_label)

    #setting up the image
      st.image(img)





