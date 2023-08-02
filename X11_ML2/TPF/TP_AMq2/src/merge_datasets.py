"""
merge_datasets.py

DESCRIPCIÓN: Este script es util para unir los datasets de train y test en un solo script.
AUTOR: Paula Centioni y Marcos Brito
FECHA: 01/08/2023
"""

import os
import pandas as pd

data_dir_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../data/')
dataset_train = data_dir_path + 'Train_BigMart.csv'
dataset_test = data_dir_path + 'Test_BigMart.csv'

data_train = pd.read_csv(dataset_train)
data_test = pd.read_csv(dataset_test)
data_train['Set'] = 'train'
data_test['Set'] = 'test'
data = pd.concat([data_train, data_test], ignore_index=True, sort=False)
data.to_csv(data_dir_path + 'merged_BigMart.csv', index=False)