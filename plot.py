import xarray as xr
import numpy as np
from numpy import sqrt, power, arccos, pi
from matplotlib import use
from matplotlib.colors import Normalize
import matplotlib.pyplot as plt
import seaborn as sns

use("Agg")

data = xr.open_dataset("data/data.grib", filter_by_keys={'dataType': 'em'}, engine="cfgrib")
data = data.sel(latitude=54.5057778, longitude=11.9419167, method="nearest")
#data = data.sel(time=slice("2020-12-01", "2021-12-31"))
data = data.resample(time='ME').mean()
df = data.to_dataframe()
del data

df['speed'] = sqrt(power(df['u10'], 2) + power(df['v10'], 2))
df['wind_heading'] = arccos(df['v10']/df['speed'])*180/pi

norm = Normalize(vmin=min(df['speed']+df['wind_heading']),
                 vmax=max(df['speed']+df['wind_heading']), clip=True)

sns.jointplot(data=df, x='speed', y='wind_heading', kind='hist', marginal_ticks=True,
              xlim=(0, 30), ylim=(0, 180), binwidth=(2, 20),
              hue_norm=norm, color='r')
plt.gca().invert_yaxis()
plt.savefig("gedser-rostock.png")
