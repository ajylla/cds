import xarray as xr

data = xr.open_dataset("data/data.grib", engine="cfgrib")
print(data.attrs)
