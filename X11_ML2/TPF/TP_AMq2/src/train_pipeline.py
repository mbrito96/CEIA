from split_datasets import DatasetSplitter
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
src_dir = os.path.dirname(os.path.abspath(__file__))
merge_script = os.path.join(src_dir,'merge_datasets.py')
subprocess.run(['Python', merge_script], check=False)

data_dir_path = os.path.join(src_dir,'../data/')
dataset_name = 'merged_BigMart.csv'
pipeline_dir_path = os.path.join(src_dir,'../pipeline/')
output_train_path = pipeline_dir_path + 'train_clean.csv'
output_model_path = pipeline_dir_path + 'model.pkl'

# Chequeo si existe el directorio "pipeline" y si no, lo creo. Aquí
# pondremos todos nuestros archivos del pipeline
if not os.path.exists(pipeline_dir_path):
    os.makedirs(pipeline_dir_path)

# Ahora si, preprocesamos el archivo entero (en un archivo temporal para
# luego borrarlo)
TEMP_FILENAME = src_dir+'/tempLocal.csv'
subprocess.run(['Python', src_dir+'/feature_engineering.py',
               data_dir_path + dataset_name, TEMP_FILENAME])

# Leemos el archivo preprocesado y lo dividimos en train para guardar por
# separado
splitter = DatasetSplitter(TEMP_FILENAME)
splitter.save_train(output_train_path)

# Borramos el archivo temporal
os.remove(TEMP_FILENAME)

# Entrenamos el modelo solo con el set de train preprocesado
subprocess.run(['Python', src_dir+'/train.py', output_train_path, output_model_path])
print("Modelo guardado en: " + output_model_path)