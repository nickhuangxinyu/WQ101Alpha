from backend import *

if __name__ == '__main__':
  file_path = './merge.csv.gz'
  num_class = 10
  df = LoadData(file_path)
  df['alpha6'] = df.groupby('ticker', as_index=False).apply(lambda x : -x['open'].rolling(10).corr(x['volume'].rolling(10))).reset_index(level=0)[0]
  AddFactorLabel(df, num_class, 'alpha6')
  df['alpha33'] = df.groupby('ticker', as_index=False).apply(lambda x: (x['open']/x['close']).rank()).reset_index(level=0)[0]
  AddFactorLabel(df, num_class, 'alpha33')
  PlotFactor(df, num_class, 'alpha6')
  df['alpha4'] = 
