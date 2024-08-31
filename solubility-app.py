import numpy as np
import pandas as pd
import streamlit as st
import pickle
from rdkit import Chem
from rdkit.Chem import Descriptors

# Calculate aromatic proportion
def AromaticProportion(mol):
    aromatic_atoms = sum([atom.GetIsAromatic() for atom in mol.GetAtoms()])
    heavy_atoms = Descriptors.HeavyAtomCount(mol)
    return aromatic_atoms / heavy_atoms if heavy_atoms else 0

# Generate molecular descriptors
def generate(smiles):
    descriptors = []
    for sm in smiles:
        mol = Chem.MolFromSmiles(sm)
        if mol:
            descriptors.append([
                Descriptors.MolLogP(mol),
                Descriptors.MolWt(mol),
                Descriptors.NumRotatableBonds(mol),
                AromaticProportion(mol)
            ])
    return pd.DataFrame(descriptors, columns=["MolLogP", "MolWt", "NumRotatableBonds", "AromaticProportion"])

# App title and description
st.image('solubility-logo.jpg', use_column_width=True)
st.write("""
# Molecular Solubility Prediction Web App
Predict **Solubility (LogS)** values of molecules!
""")

# Input molecules
st.sidebar.header('User Input Features')
SMILES_input = "NCCCC\nCCC\nCN"
SMILES = st.sidebar.text_area("SMILES input", SMILES_input).split('\n')
st.header('Input SMILES')
st.write(SMILES)

# Compute and display molecular descriptors
st.header('Computed molecular descriptors')
X = generate(SMILES)
st.write(X)

# Load and apply pre-built model to make predictions
load_model = pickle.load(open('solubility_model.pkl', 'rb'))
st.header('Predicted LogS values')
st.write(load_model.predict(X))
