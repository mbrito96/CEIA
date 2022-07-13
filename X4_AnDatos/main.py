PATH_EXPERIMENT = "./2nd_test/2nd_test"
PATH_DATASET = "./Dataset/dataset_2.csv"
import os
import numpy as np
import pandas as pd
from os import listdir
from os.path import isfile, join

from matplotlib.pyplot import axis

# onlyfiles = [f for f in listdir(PATH_EXPERIMENT) if isfile(join(PATH_EXPERIMENT, f))]

def GetAccFeatures(df):
    mean = pd.DataFrame(np.array(df.mean(axis=0)).reshape(1,4),columns=['0', '1', '2', '3'])
    std = pd.DataFrame(np.array(df.std(axis=0)).reshape(1, 4),columns=['4', '5', '6', '7'])
    mean_std = pd.concat([mean, std], axis=1)
    #print(mean_std.shape)
    return mean_std


files = os.listdir(PATH_EXPERIMENT)
txt = [x for x in files if x.endswith('.39')]
df = None
df_out = pd.DataFrame(columns=['0', '1', '2', '3', '4', '5', '6', '7'])
idx=0
for label in txt:
    idx+=1
    pathText = PATH_EXPERIMENT + '\\' + label
    df = pd.read_csv(pathText, delimiter='\t', header=None)
    df_out = pd.concat([df_out, GetAccFeatures(df)], axis=0)
    #out_p=GetAccFeatures(df)
    #df_out.append(GetAccFeatures(df))
    # df_out.loc[len(df_out.index)] = GetAccFeatures(df)
    id = 0
    if idx==10:
        break
df_out=df_out.reset_index(inplace=False, drop=True)
print(df_out.head())
print("shape:",df_out.shape)


# Forma de nuestro dataset:
# #sample | mean_0 | std_0 | .... | mean_1 | std_1 | ..... | mean_4 | std_4 | ... ||| failure_0 | failure_1 | ... | failure_3
                                                                #                       None    | outer_race| ... | None