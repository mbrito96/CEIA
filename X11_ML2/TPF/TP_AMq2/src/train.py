"""
train.py

DESCRIPCIÓN: Este script se encarga de entrenar el modelo de machine learning.
AUTOR: Paula Centioni y Marcos Brito
FECHA: 01/08/2023
"""

# Imports
import pandas as pd
from sklearn.model_selection import train_test_split, cross_validate, cross_val_score
from sklearn import metrics
from sklearn.linear_model import LinearRegression
import logging
import matplotlib.pyplot as plt
import argparse

# Logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

log = logging.getLogger('train')

class ModelTrainingPipeline(object):

    def __init__(self, input_path, model_path):
        self.input_path = input_path
        self.model_path = model_path

    def read_data(self) -> pd.DataFrame:
        """
        Lee el dataset de entrada y lo carga en un DataFrame de Pandas.
        
        :return pandas_df: El dataset de entrada como un DataFrame
        :rtype: pd.DataFrame
        """
        pandas_df = pd.read_csv(self.input_path)
        return pandas_df

    
    def model_training(self, df: pd.DataFrame) -> LinearRegression:
        """
        Entrena el modelo utilizando el dataset de entrada.
        
        :param pandas_df: El dataset de entrada
        :type pandas_df: pd.DataFrame
        :return model: The trained model
        """
        seed = 28
        model = LinearRegression()

        # División de dataset de entrenaimento y validación
        X = df.drop(columns='Item_Outlet_Sales') 
        x_train, x_val, y_train, y_val = train_test_split(X, df['Item_Outlet_Sales'], test_size = 0.3, random_state=seed)

        # Entrenamiento del modelo
        model.fit(x_train,y_train)

        # Predicción del modelo ajustado para el conjunto de validación
        pred = model.predict(x_val)

        # Cálculo de los errores cuadráticos medios y Coeficiente de Determinación (R^2)
        mse_train = metrics.mean_squared_error(y_train, model.predict(x_train))
        R2_train = model.score(x_train, y_train)
        log.debug('Métricas del Modelo:')
        log.debug('ENTRENAMIENTO: RMSE: {:.2f} - R2: {:.4f}'.format(mse_train**0.5, R2_train))

        mse_val = metrics.mean_squared_error(y_val, pred)
        R2_val = model.score(x_val, y_val)
        log.debug('VALIDACIÓN: RMSE: {:.2f} - R2: {:.4f}'.format(mse_val**0.5, R2_val))

        log.debug('\nCoeficientes del Modelo:')
        # Constante del modelo
        log.debug('Intersección: {:.2f}'.format(model.intercept_))

        # Coeficientes del modelo
        coef = pd.DataFrame(x_train.columns, columns=['features'])
        coef['Coeficiente Estimados'] = model.coef_
        log.debug(coef, '\n')
        coef.sort_values(by='Coeficiente Estimados').set_index('features').plot(kind='bar', title='Importancia de las variables', figsize=(12, 6))
        if logging.DEBUG >= logging.root.level:
            plt.show()
        return model

    def model_dump(self, model_trained: LinearRegression) -> None:
        """
        Toma el modelo entrenado y lo guarda en un archivo pickle.
        
        :return None
        """
        try:
            import pickle
            with open(self.model_path, 'wb') as file:
                pickle.dump(model_trained, file)
        except Exception as e:
            log.error('Error dumping the model: {}'.format(e))
        return None

    def run(self):
        """
        Ejecuta el pipeline de entrenamiento del modelo.
        """
        df = self.read_data()
        model_trained = self.model_training(df)
        self.model_dump(model_trained)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Feature Engineering')
    parser.add_argument('input_path', type=str, help='Input path')
    parser.add_argument('output_path', type=str, help='Output path')
    args = parser.parse_args()

    ModelTrainingPipeline(input_path = args.input_path,
                          model_path = args.output_path).run()