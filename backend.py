import pandas as pd
pd.set_option('mode.use_inf_as_na', True)
import os
import sys 
import time
import numpy as np
import matplotlib.pyplot as plt

def LoadData(file_path):
  if not os.path.exists(file_path):
    print('%s not existed' % (file_path))
    sys.exit(1)
  return AddLabel(pd.read_csv(file_path, dtype={'ticker':str}))

def AddLabel(df):
  df['yr'] = df.groupby('ticker')['close'].apply(lambda x: x.diff(-1) / x)
  df = df[df['date'] > '2006']
  return df

def AddFactorLabel(df, num_class, factor_name):
    d = df.groupby('date', as_index=False).apply(lambda x: pd.qcut(x[factor_name], q=num_class, labels=False, duplicates='drop'))
    label = d.reset_index(level=0)[factor_name]
    df[factor_name + '_label'] = label

def PlotFactor(df, num_class, factor_name):
    temp = df.groupby(factor_name+'_label')['yr'].mean().to_dict()
    print(temp)
    plt.title('%s corr %lf' %(factor_name, df['yr'].corr(df[factor_name])))
    plt.bar(range(len(temp.keys())), [temp[i] for i in temp.keys()])
    plt.show()
    return df
