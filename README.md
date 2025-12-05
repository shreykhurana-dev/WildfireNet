# WildfireNet: Forest Fire Detection Using CNN-Based Multiclass Image Classification with Web-Augmented Training Data

This project contains my complete pipeline for classifying images into fire, smoke, and no_fire. I built the dataset, trained the model, evaluated it, and generated visualizations to understand its behavior.

## 1. Dataset Collection

I used a combination of:

- A Kaggle dataset of fire, smoke, and non-fire images
- My own web-crawled data from Unsplash

I wrote a Python crawler that queries Unsplash with keywords (e.g., “wildfire flames”, “smoke plume”, “forest landscape”). After downloading, I manually removed duplicates and irrelevant images.  
In total, I collected about 1,060 images per class, and I used a 70/15/15 split for train/val/test.

## 2. Preprocessing and Augmentation

In my training pipeline, I applied augmentations such as:

- Random crops  
- Flips  
- Rotations  
- Color jitter  
- Perspective transforms  
- Gaussian blur  

Validation and test images were only resized and center-cropped.

## 3. Model

I fine-tuned EfficientNet-B0 with ImageNet weights.  
I replaced the classifier with:

- `Dropout(0.3)`  
- A linear layer with 3 output classes  

I trained using AdamW, learning-rate scheduling, and early stopping. Training stopped at epoch 10.

## 4. Evaluation

I computed precision, recall, and F1-score for all three classes and also reported macro averages.  
My final macro F1 score was 0.9517, showing balanced performance across the classes.

## 5. Visualizations

I generated:

- A confusion matrix  
- Loss and accuracy curves  
- Grad-CAM heatmaps to show where the model focuses  
- Sample predictions on test images  

These help verify that the model is behaving as expected.

## 6. Files

- `WildfireNet Project Notebook.ipynb` — full training and evaluation code  
- `web crawler.py` — my Unsplash image-collection script  
- `best_model.pth` — saved weights
