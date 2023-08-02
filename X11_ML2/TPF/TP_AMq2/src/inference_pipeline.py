"""
inference_pipeline.py

DESCRIPCIÓN: Este script ejecuta el pipeline de inferencia de los datos.
AUTOR: Paula Centioni y Marcos Brito
FECHA: 01/08/2023
"""
import subprocess
import os
from split_datasets import DatasetSplitter

# Como se aclaró en el pipeline de entrenamiento, el preprocesamiento debe ocurrir
# sobre el dataset entero (train y test).
# Por lo tanto, usamos 'merged_dataset.csv' como input para el
# preprocesamiento, pero luego solo utilizamos test.
src_dir = os.path.dirname(os.path.abspath(__file__))
data_dir_path = os.path.join(src_dir, '../data/')
DATASET_NAME = 'merged_BigMart.csv'
pipeline_dir_path = os.path.join(src_dir, '../pipeline/')
model_path = pipeline_dir_path + 'model.pkl'
output_test_path = pipeline_dir_path + 'test_clean.csv'
output_prediction_path = pipeline_dir_path + 'predictions.csv'

# Ahora si, preprocesamos el archivo entero (en un archivo temporal para
# luego borrarlo)
TEMP_FILENAME = src_dir+'/tempLocal.csv'
subprocess.run(['Python', src_dir+'/feature_engineering.py',
               data_dir_path + DATASET_NAME, TEMP_FILENAME], check=False)

# Leemos el archivo preprocesado y lo dividimos en test para guardar por
# separado
splitter = DatasetSplitter(TEMP_FILENAME)
splitter.save_test(output_test_path)

# Borramos el archivo temporal
os.remove(TEMP_FILENAME)

# Ahora hacemos las predicciones solo con el set de test preprocesado
subprocess.run(['Python', src_dir+'/predict.py', output_test_path,
               output_prediction_path, model_path], check=False)
print("Predicciones guardadas en: " + output_prediction_path)
