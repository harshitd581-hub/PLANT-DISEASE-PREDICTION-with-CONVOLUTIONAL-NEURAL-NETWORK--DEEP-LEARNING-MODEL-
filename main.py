import os
import json
import numpy as np
import tensorflow as tf
import streamlit as st
from PIL import Image


# ----------------------------
# Load model and class indices
# ----------------------------
working_dir = os.path.dirname(os.path.abspath(__file__))

model_path = os.path.join(working_dir, "plant_disease_prediction_model.h5")
class_indices_path = os.path.join(working_dir, "class_indices.json")

model = tf.keras.models.load_model(model_path,compile=False)

with open(class_indices_path, "r") as f:
    class_indices = json.load(f)

# Reverse mapping if json is like:
# {"Apple___healthy": 0, "Tomato___Early_blight": 1}
if isinstance(list(class_indices.values())[0], int):
    idx_to_class = {v: k for k, v in class_indices.items()}
else:
    idx_to_class = {int(k): v for k, v in class_indices.items()}


# ----------------------------
# Image preprocessing function
# ----------------------------
def load_and_preprocess_image(image_file, target_size=(224, 224)):
    img = Image.open(image_file).convert("RGB")
    img = img.resize(target_size)
    img_array = np.array(img).astype("float32") / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    return img, img_array


# ----------------------------
# Prediction function
# ----------------------------
def predict_image_class(model, image_file, class_labels):
    _, processed_img = load_and_preprocess_image(image_file)
    prediction = model.predict(processed_img)
    predicted_index = int(np.argmax(prediction, axis=1)[0])
    predicted_class_name = class_labels[predicted_index]
    confidence = float(np.max(prediction)) * 100
    return predicted_class_name, confidence


# ----------------------------
# Streamlit UI
# ----------------------------
st.set_page_config(page_title="Plant Disease Classifier", page_icon="🌿")

st.title("🌿 Plant Disease Classifier")
st.write("Leaf image upload karo aur disease predict karo.")

uploaded_image = st.file_uploader(
    "Upload an image...",
    type=["jpg", "jpeg", "png"]
)

if uploaded_image is not None:
    image = Image.open(uploaded_image).convert("RGB")

    col1, col2 = st.columns(2)

    with col1:
        st.image(image, caption="Uploaded Image", use_container_width=True)

    with col2:
        if st.button("Classify"):
            prediction, confidence = predict_image_class(model, uploaded_image, idx_to_class)
            st.success(f"Prediction: {prediction}")
            st.info(f"Confidence: {confidence:.2f}%")

