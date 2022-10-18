## PUT THIS INTO colab or jupyter if you work online

import pandas as pd

def download_dataset():
  !curl https://storage.googleapis.com/atomic-bird-188013.appspot.com/archive.zip -o archive.zip
  !unzip 'archive.zip'

def load_dataset():
  df = pd.read_csv('MBTI 500.csv')
  return df
