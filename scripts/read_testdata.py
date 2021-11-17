import pandas as pd
import numpy as np

data = pd.read_csv('https://github.com/nflverse/nflfastR-data/blob/master/data/play_by_play_2021.csv.gz?raw=True', compression='gzip', low_memory=False)

passers = pd.unique(data['passer'])

df = pd.DataFrame()

for p in passers:
    d = data.query('passer == "{}" & play == 1 & play_type_nfl == "PASS"'.format(p))
    d = pd.pivot_table(d, index=['passer', 'game_date'], aggfunc={'pass_attempt': np.sum}).reset_index()
    df = df.append(d)

df.to_csv('data/test_passatt_2021.csv')
