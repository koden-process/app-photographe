import os
import pandas as pd
from PIL import Image

import streamlit as st

batch = '8209f2a0-892a-407e-bde6-497213b3b1ef'
date = '2025-02-18'
csv_file = f'../artefacts/photos/{batch}/{date}/done.csv'
image_base_path =  f'../artefacts/miniatures/{batch}/{date}'

# Charger le fichier CSV
df = pd.read_csv(csv_file)

# Convertir la colonne datetime en type datetime pour le tri
df['datetime'] = pd.to_datetime(df['datetime'])

# Trier le DataFrame par folder et datetime
df = df.sort_values(by = ['folder', 'datetime'])

# Interface Streamlit
st.title("Visualisation des Images Groupées par Folder")

# Obtenir la liste unique des folders
folders = df['folder'].unique()

# Parcourir tous les folders
for folder in folders:
    # Créer une section pour chaque folder
    st.subheader(f"Folder : {folder}")

    # Filtrer les données pour ce folder
    folder_data = df[df['folder'] == folder]

    # Liste des images à afficher
    images = []
    captions = []

    for _, row in folder_data.iterrows():
        image_path = os.path.join(image_base_path, row['uuid'])

        # Vérifier si l'image existe
        if os.path.exists(image_path):
            images.append(image_path)
            captions.append(str(row['datetime']))
        else:
            st.warning(f"Image manquante : {row['uuid']}")

    # Afficher les images 5 par ligne
    for i in range(0, len(images), 5):
        cols = st.columns(5)  # Créer 5 colonnes
        for col, image, caption in zip(cols, images[i:i + 5], captions[i:i + 5]):
            with col:
                st.image(Image.open(image), caption = caption, use_column_width = True)