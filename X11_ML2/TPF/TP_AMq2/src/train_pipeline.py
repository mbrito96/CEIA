import subprocess
import pandas as pd
import os

"""
Primero se debe ejecutar el script "merge_datasets.py" para unir los datasets de train y test en uno solo.
Esto se debe a que el preprocesamiento debe ocurrir sobre el dataset entero (train y test).
En el archivo 'notebook_analysis_train.ipynb', el machine learning engineer realiza el procesamiento
sobre el dataset de entrenamiento y el de testeo en conjunto. Este proceso funciona correctamente. 
Sin embargo, al ejecutar la linea 'moda = (data[data['Item_Identifier'] == producto][['Item_Weight']]).mode().iloc[0,0]'
(que forma parte del preprocesamiento de 'notebook_analysis_train') sobre el set de train solamente, el código devuelve un error.
Por lo tanto, para poder ejecutar el train_pipeline y simplificar el trabajo, se unen ambos datasets para tratarlos juntos.
En el train_pipeline, no haría falta preprocesar el set de test, dado que solo queremos entrenar el modelo.
"""
subprocess.run(['Python', 'merged_datasets.py'])

data_dir_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../data/')
dataset_name = 'merged_BigMart.csv'
pipeline_dir_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../pipeline/')
output_train_path = pipeline_dir_path + 'train_clean.csv'
output_model_path = pipeline_dir_path + 'model.pkl'

# Chequeo si existe el directorio "pipeline" y si no, lo creo. Aquí pondremos todos nuestros archivos del pipeline
if not os.path.exists(pipeline_dir_path):
    os.makedirs(pipeline_dir_path)

# Ahora si, preprocesamos el archivo entero (en un archivo temporal para luego borrarlo)
temp_filename = './tempLocal.csv'
subprocess.run(['Python', 'feature_engineering.py', data_dir_path + dataset_name,  temp_filename])

# Leemos el archivo preprocesado y lo dividimos en train para guardar por separado
from split_datasets import DatasetSplitter
splitter = DatasetSplitter(temp_filename)
splitter.save_train(output_train_path)

# Borramos el archivo temporal
os.remove(temp_filename)

# Entrenamos el modelo solo con el set de train preprocesado
subprocess.run(['Python', 'train.py', output_train_path, output_model_path])