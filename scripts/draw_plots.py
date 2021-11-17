import pandas as pd
from plotnine import ggplot, aes, geom_line, scale_x_timedelta, labs, geom_point
import re
import warnings
from datetime import datetime
warnings.filterwarnings('ignore')

start = datetime.now()

data = pd.read_csv('data/test_passatt_2021.csv')
data['game_date'] = pd.to_datetime(data['game_date'])

passer = pd.unique(data['passer'])

for p in passer:
    print('Saving plot for {}.'.format(p))
    d = data.query('passer == "{}"'.format(p))
    plot = (
        ggplot(d) #dataset we're plotting
        + aes(x='game_date', y='pass_attempt') #set x and y
     #   + scale_x_timedelta(name = 'Game Date')
        + labs(title = '{} Pass Attempts in 2021'.format(p), subtitle = p, y = 'Pass Attempts', x = 'Game Date')
        + geom_line() #draw the line
        + geom_point(size = 2)
    )
    plot.save('plots/{}.png'.format(re.sub('\W+','',p)),dpi=150,width=11,height=8,units='in',verbose = False)

print('completed {} plots in {}'.format(len(passer),datetime.now()-start))