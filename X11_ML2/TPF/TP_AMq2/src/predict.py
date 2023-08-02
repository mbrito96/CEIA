"""
predict.py

DESCRIPCIÓN: Este script se encarga de realizar las predicciones sobre el dataset.
AUTOR: Paula Centioni y Marcos Brito
FECHA: 01/08/2023
"""

# Imports
import pandas as pd
from pandas import DataFrame
import argparse
import pickle as pkl

class MakePredictionPipeline(object):
    
    def __init__(self, input_path, output_path, model_path: str = None):
        self.input_path = input_path
        self.output_path = output_path
        self.model_path = model_path
                
                
    def load_data(self) -> pd.DataFrame:
        """
        Cargar el dataset de entrada en un DataFrame de Pandas.
        """
        data = pd.read_csv(self.input_path) 
        return data

    def load_model(self) -> None:
        """
        Cargar el modelo de inferencia.
        """    

        with open(self.model_path, 'rb') as file:
            self.model = pkl.load(file)

        return None


    def make_predictions(self, data: DataFrame) -> pd.DataFrame:
        """
        Realizar las predicciones sobre el dataset de entrada.
        """
   
        if self.model is None:
            raise Exception("Model not loaded")
        
        new_data = pd.DataFrame(self.model.predict(data))

        return new_data


    def write_predictions(self, predicted_data: DataFrame) -> None:
        """ 
        Guardar las predicciones en el path de salida.
        """
        predicted_data.to_csv(self.output_path, index=False)
        print(predicted_data)
        return None


    def run(self):
        """ 
        Ejecutar el pipeline completo.
        """ 
        data = self.load_data()
        self.load_model()
        df_preds = self.make_predictions(data)
        self.write_predictions(df_preds)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Feature Engineering')
    parser.add_argument('input_path', type=str, help='Input path')
    parser.add_argument('output_path', type=str, help='Output path')
    parser.add_argument('model_path', type=str, help='Model path')
    args = parser.parse_args()
    
    # spark = Spark()
    
    pipeline = MakePredictionPipeline(input_path = args.input_path,
                                      output_path = args.output_path,
                                      model_path = args.model_path)
    pipeline.run()  