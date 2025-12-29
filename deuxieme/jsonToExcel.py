import json
import pandas as pd

# Fichiers
INPUT_JSON = r"C:\Users\ASUS\projects\PaddleOCR\deuxieme\data\outputs\output.json"
OUTPUT_EXCEL = r"C:\Users\ASUS\projects\PaddleOCR\deuxieme\data\outputs\output.xlsx"

import pandas as pd
import json

def json_to_excel_simple(json_file_path, excel_file_path):
    # Charger le JSON
    with open(json_file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    
    # Récupérer les données
    table_data = data['pages'][0]['table']
    
    # Convertir en DataFrame
    # On va créer une liste de lignes avec le nombre maximum de colonnes
    max_cols = max(len(row) for row in table_data)
    
    # Préparer les données pour le DataFrame
    formatted_data = []
    for row in table_data:
        if len(row) < max_cols:
            # Étendre la ligne avec des cellules vides si nécessaire
            extended_row = row + [''] * (max_cols - len(row))
            formatted_data.append(extended_row)
        else:
            formatted_data.append(row)
    
    # Créer le DataFrame
    df = pd.DataFrame(formatted_data)
    
    # Sauvegarder en Excel
    df.to_excel(excel_file_path, index=False, header=False)
    print(f"Fichier Excel créé avec succès : {excel_file_path}")

# Utilisatio
json_to_excel_simple(INPUT_JSON, OUTPUT_EXCEL)
