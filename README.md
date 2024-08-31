# Molecular_solubility_checker
## Project Overview
This project is designed to predict the solubility (LogS) of molecules based on their molecular structure, represented by SMILES strings. The prediction model is based on a Linear Regression model trained on a dataset of molecular descriptors. The model has been deployed using a Streamlit web application, allowing users to input SMILES strings and receive solubility predictions.
## Key Features

Molecular Descriptor Calculation: Extracts important molecular features such as LogP, Molecular Weight, Number of Rotatable Bonds, and Aromatic Proportion.

Machine Learning Model: A Linear Regression model trained on a dataset of molecular descriptors.

Web Application: A user-friendly interface built with Streamlit, enabling real-time predictions of molecular solubility.

## Files in the Repository

solubility-app.py: The main Streamlit application script that allows users to input SMILES strings and view predicted solubility values.

solubility-web-app.ipynb: Jupyter notebook used to train the Linear Regression model, evaluate its performance, and save the model as a pickle file.

solubility_model.pkl: The serialized (pickled) Linear Regression model used in the web application for predictions.

solubility-logo.jpg: A logo image used in the Streamlit web application.

requirements.txt: A list of Python dependencies required to run the application.

A csv file containing data

## Project Structure

Data Preparation and Model Training (solubility-web-app.ipynb):

Loads and preprocesses a dataset of molecular descriptors.

Trains a Linear Regression model to predict solubility based on these descriptors.

Evaluates the model’s performance using metrics such as Mean Squared Error (MSE) and R² Score.

Visualizes the model’s predictions against experimental values.

Saves the trained model as a solubility_model.pkl file.

## Streamlit Web App (solubility-app.py):

Loads the trained model from solubility_model.pkl.

Takes user input (SMILES strings) via a text area.

Computes molecular descriptors for each input molecule.

Predicts the solubility (LogS) using the pre-trained model.

Displays the computed descriptors and the predicted solubility values.
