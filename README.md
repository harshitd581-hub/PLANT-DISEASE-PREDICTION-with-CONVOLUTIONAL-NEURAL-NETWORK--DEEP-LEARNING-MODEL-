# Plant Disease Prediction using CNN and Deep Learning

This project is a **Plant Disease Prediction System** built using **Convolutional Neural Network (CNN)** and **Deep Learning**.  
The main goal of this project is to identify plant diseases from leaf images and help in early detection of crop health problems.



## Project Overview

In agriculture, plant diseases can reduce crop quality and production.  
If a disease is detected early, farmers or users can take action quickly and reduce damage.

This project solves that problem by using an **image classification model**.  
The user uploads a leaf image, and the system predicts the disease class of that plant.


## Aim of the Project

The main aim of this project is:

 To build an intelligent system that can detect plant diseases from leaf images
 To use **CNN and Deep Learning** for automatic image classification
 To reduce manual effort in identifying plant diseases
 To provide a simple and user-friendly prediction system



## What this Model Does

This model takes an image of a plant leaf as input and predicts:

 whether the leaf is healthy, or
 which disease is present in that leaf

So in simple words, this system acts like an **AI-based plant disease checker**.



## Project Files

The main files used in this project are:

## main.py → Main Streamlit application file (model deploy ka manin file pycharm per karenge)
## class_indices.json → Contains class label mapping
## requirements.txt → Required Python libraries
## plant_disease_prediction_model.h5 → Trained deep learning model(## trained model file ye file uploded nahi ho raha tha due to more then 25Mb tho uska mai google drive link diya hai niche)
##  PLANT DISEASE PREDICTION with CNN- DEEP LEARNING SYSTEM(1).ipynb =  model ka starting se end tak ka code jupyter notebbok




## How the System Works

The system works in the following steps:

### 1. Image Input
The user uploads a plant leaf image into the system.

### 2. Image Preprocessing
The input image is resized and converted into the required format so that the model can process it properly.

### 3. CNN Model Prediction
The trained CNN model analyzes image patterns such as:
 color changes
 leaf spots
texture
 damage marks
 disease-related visual features

### 4. Class Mapping
The predicted output is matched with the disease labels using the `class_indices.json` file.

### 5. Final Result
The system displays the predicted disease name to the user.



## Why CNN is Used

CNN (Convolutional Neural Network) is very useful for image-related tasks because it can automatically learn important visual features from images.

In this project, CNN helps in:
 detecting patterns from leaf images
 learning disease-specific features
 improving prediction accuracy



## Technologies Used

This project is built using the following technologies:

- **Python**
- **TensorFlow / Keras**
- **NumPy**
- **Pillow (PIL)**
- **Streamlit**
- **JSON**


## Dataset Used

This project is trained on the PlantVillage dataset.

**Kaggle Dataset Link:**  
[PlantVillage Dataset](https://www.kaggle.com/datasets/abdallahalidev/plantvillage-dataset)


## Trained Model Link

Since the trained model file is large, it may not be uploaded directly to GitHub.

You can access the trained model from the link below:

**Model Link:**  
[Download Trained Model]: https://drive.google.com/file/d/1DWAvRnj11bju0OdxUtDJ-wB6FUuW4n2x/view?usp=drive_link

---

## Features of the Project

- Predicts plant disease from leaf images
- User-friendly interface using Streamlit
- Fast and simple image upload system
- Deep learning based classification
- Helpful for agriculture and crop monitoring


## Applications

This project can be useful in:

- smart agriculture
- crop disease monitoring
- early disease detection
- academic and research projects
- AI-based farming solutions


## Advantages

- Reduces manual inspection
- Saves time in disease identification
- Supports early treatment decisions
- Easy to use
- Useful for students and researchers


## Limitations

- Prediction depends on image quality
- Wrong lighting or blurry images can affect accuracy
- Model performance depends on training data quality
- It may not perfectly predict completely unseen disease patterns


## Future Improvements

This project can be improved in future by adding:

- more plant disease classes
- better model accuracy
- mobile app integration
- real-time camera-based detection
- treatment suggestions for predicted diseases
- multilingual support for users


## How to Run the Project
as .h5 trained model file not uploded on github (more then 25mb) so you have to download the file first i already given google drive link above 
then

### 1. Clone the repository
```bash
git clone YOUR_GITHUB_REPO_LINK

## 2. go to the project folder
cd your_project_folder

## 3. install the requaired libraries
pip install -r requirements.txt

## 4.⁠ ⁠Download the trained model
Download the trained model file from the Google Drive link provided in this README.
### 5.⁠ ⁠Place the model file in the project folder
Put the downloaded .h5 model file inside the main project folder.

## 6. run the streamlit app
streamlit run main.py
