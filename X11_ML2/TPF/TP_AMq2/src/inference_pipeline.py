import subprocess
import pandas as pd
import os

"""
Como se aclaró en el pipeline de entrenamiento, el preprocesamiento debe ocurrir sobre el dataset entero (train y test).
Por lo tanto, usamos 'merged_dataset.csv' como input para el preprocesamiento, pero luego solo utilizamos test.
"""
data_dir_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../data/')
dataset_name = 'merged_BigMart.csv'
pipeline_dir_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../pipeline/')
model_path = pipeline_dir_path + 'model.pkl'
output_test_path = pipeline_dir_path + 'test_clean.csv'
output_prediction_path = pipeline_dir_path + 'predictions.csv'

# Ahora si, preprocesamos el archivo entero (en un archivo temporal para luego borrarlo)
temp_filename = './tempLocal.csv'
subprocess.run(['Python', 'feature_engineering.py', data_dir_path + dataset_name,  temp_filename])

# Leemos el archivo preprocesado y lo dividimos en test para guardar por separado
from split_datasets import DatasetSplitter
splitter = DatasetSplitter(temp_filename)
splitter.save_test(output_test_path)

# Borramos el archivo temporal
os.remove(temp_filename)

# Ahora hacemos las predicciones solo con el set de test preprocesado
subprocess.run(['Python', 'predict.py', output_test_path,  output_prediction_path, model_path])