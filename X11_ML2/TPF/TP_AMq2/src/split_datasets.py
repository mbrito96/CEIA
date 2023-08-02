"""
split_datasets.py

DESCRIPCIÓN: Este modulo de python es util para dividir el dataset en train y test.
AUTOR: Paula Centioni y Marcos Brito
FECHA: 01/08/2023
"""
import pandas as pd
import argparse

class DatasetSplitter():
    def __init__(self, input_path) -> None:
        self.data = pd.read_csv(input_path)

    def get_train(self):
        return self.data[self.data['Set'] == 'train'].drop(columns=['Set'])

    def get_test(self):
        return self.data[self.data['Set'] == 'test'].drop(columns=['Set', 'Item_Outlet_Sales'])
    
    def save_train(self, output_path):
        self.get_train().to_csv(output_path, index=False)
    
    def save_test(self, output_path):
        self.get_test().to_csv(output_path, index=False)
    
    def save_all(self, output_path):
        self.data.drop(columns=['Set']).to_csv(output_path, index=False)
  