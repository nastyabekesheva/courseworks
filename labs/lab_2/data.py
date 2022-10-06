import pandas as pd
import urllib.request
from datetime import datetime
from pathlib import Path
import numpy as np

NOAAIndex = {
        1:24,
        2:25,
        3:5,
        4:6,
        5:27,
        6:23,
        7:26,
        8:7,
        9:11,
        10:13,
        11:14,
        12:15,
        13:16,
        14:17,
        15:18,
        16:19,
        17:21,
        18:22,
        19:8,
        20:9,
        21:10,
        22:1,
        23:3,
        24:2,
        25:4,
        26:12,
        27:20
}

def _download_data(index, min_year=1991, max_year=2022):
    time = f"{datetime.now().month}-{datetime.now().day}-{datetime.now().year}--{datetime.now().hour}:{datetime.now().minute}"
    url = f"https://www.star.nesdis.noaa.gov/smcd/emb/vci/VH/get_TS_admin.php?country=UKR&provinceID={NOAAIndex[index]}&year1={min_year}&year2={max_year}&type=Mean"
    path = f"assets/vhi_{index}--{time}.csv"
    urllib.request.urlretrieve(url, path)
    print(f"File {path} downloaded successfully")
    
def _load_data_to_df(index):
  columns = ['Year', 'Week', 'SMN', 'SMT', 'VCI', 'TCI', 'VHI', 'None']
  df = pd.read_csv(Path(f"assets/vhi_{index}--10-6-2022--0:27.csv"), names = columns)
  df = df.iloc[: , :-1]
  df.drop(index=df.index[0],
        axis=0,
        inplace=True)
  df.drop(index=df.index[0],
        axis=0,
        inplace=True)
  df = df.dropna()

  df['Region'] = np.repeat(str(index), len(df['Week']))
  df['Week'] = [int(i) for i in df['Week']]
  df['Year'][2] = '1991'
  df['Year'] = [int(i) for i in df['Year']]
  return df
  
  
def _merge_df(data):
  df = pd.concat(data, ignore_index = True)
  df.reset_index()

  return df
    
