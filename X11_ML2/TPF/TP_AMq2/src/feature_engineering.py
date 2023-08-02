"""
feature_engineering.py

DESCRIPCIÓN: Este script ejecuta el preprocesamiento de los datos.
AUTOR: Paula Centioni y Marcos Brito
FECHA: 01/08/2023
"""

# Imports
import pandas as pd
import argparse


class FeatureEngineeringPipeline(object):

    def __init__(self, input_path, output_path):
        self.input_path = input_path
        self.output_path = output_path

    def read_data(self) -> pd.DataFrame:
        """
        Read the input data from the DataLake and load it into a Pandas DataFrame.
        
        :return pandas_df: The desired DataLake table as a DataFrame
        :rtype: pd.DataFrame
        """
            
        pandas_df = pd.read_csv(self.input_path)
        return pandas_df

    
    def data_transformation(self, data: pd.DataFrame) -> pd.DataFrame:
        """
        Transform the input data into the desired output data.
        """
        data['Outlet_Establishment_Year'] = 2020 - data['Outlet_Establishment_Year']
        # Unificando etiquetas para 'Item_Fat_Content'
        data['Item_Fat_Content'] = data['Item_Fat_Content'].replace({'low fat':  'Low Fat', 'LF': 'Low Fat', 'reg': 'Regular'})
        
        productos = list(data[data['Item_Weight'].isnull()]['Item_Identifier'].unique())
        for producto in productos:
            moda = (data[data['Item_Identifier'] == producto][['Item_Weight']]).mode().iloc[0,0]
            data.loc[data['Item_Identifier'] == producto, 'Item_Weight'] = moda

        # LIMPIEZA: de faltantes en el tamaño de las tiendas
        outlets = list(data[data['Outlet_Size'].isnull()]['Outlet_Identifier'].unique())
        for outlet in outlets:
            data.loc[data['Outlet_Identifier'] == outlet, 'Outlet_Size'] =  'Small'


        # FEATURES ENGINEERING: asignación de nueva categorías para 'Item_Fat_Content'
        data.loc[data['Item_Type'] == 'Household', 'Item_Fat_Content'] = 'NA'
        data.loc[data['Item_Type'] == 'Health and Hygiene', 'Item_Fat_Content'] = 'NA'
        data.loc[data['Item_Type'] == 'Hard Drinks', 'Item_Fat_Content'] = 'NA'
        data.loc[data['Item_Type'] == 'Soft Drinks', 'Item_Fat_Content'] = 'NA'
        data.loc[data['Item_Type'] == 'Fruits and Vegetables', 'Item_Fat_Content'] = 'NA'

        # FEATURES ENGINEERING: creando categorías para 'Item_Type'
        data['Item_Type'] = data['Item_Type'].replace({'Others': 'Non perishable', 'Health and Hygiene': 'Non perishable', 'Household': 'Non perishable',
        'Seafood': 'Meats', 'Meat': 'Meats',
        'Baking Goods': 'Processed Foods', 'Frozen Foods': 'Processed Foods', 'Canned': 'Processed Foods', 'Snack Foods': 'Processed Foods',
        'Breads': 'Starchy Foods', 'Breakfast': 'Starchy Foods',
        'Soft Drinks': 'Drinks', 'Hard Drinks': 'Drinks', 'Dairy': 'Drinks'})

        # FEATURES ENGINEERING: asignación de nueva categorías para 'Item_Fat_Content'
        data.loc[data['Item_Type'] == 'Non perishable', 'Item_Fat_Content'] = 'NA'

        # FEATURES ENGINEERING: Codificando los niveles de precios de los productos
        data['Item_MRP'] = pd.qcut(data['Item_MRP'], 4, labels = [1, 2, 3, 4])

        # Codificación de variables ordinales:
        dataframe = data.drop(columns=['Item_Type', 'Item_Fat_Content']).copy()

        # FEATURES ENGINEERING: Codificación de variables ordinales
        dataframe['Outlet_Size'] = dataframe['Outlet_Size'].replace({'High': 2, 'Medium': 1, 'Small': 0})
        dataframe['Outlet_Location_Type'] = dataframe['Outlet_Location_Type'].replace({'Tier 1': 2, 'Tier 2': 1, 'Tier 3': 0}) # Estas categorias se ordenaron asumiendo la categoria 2 como más lejos

        # FEATURES ENGINEERING: Codificación de variables nominales
        dataframe = pd.get_dummies(dataframe, columns=['Outlet_Type'])
        
        dataframe = dataframe.drop(columns=['Item_Identifier', 'Outlet_Identifier'])

        return dataframe

    def write_prepared_data(self, transformed_dataframe: pd.DataFrame) -> None:
        """
        Write the prepared data to the DataLake.
        """
        print('writing prepared data to {}'.format(self.output_path))
        transformed_dataframe.to_csv(self.output_path, index=False)
        return None

    def run(self):
        """
        Run the Feature Engineering pipeline.
        """

        df = self.read_data()
        df_transformed = self.data_transformation(df)
        self.write_prepared_data(df_transformed)

  
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Feature Engineering')
    parser.add_argument('input_path', type=str, help='Input path')
    parser.add_argument('output_path', type=str, help='Output path')
    args = parser.parse_args()
        
    FeatureEngineeringPipeline(input_path = args.input_path,
                               output_path = args.output_path).run()
    
    
