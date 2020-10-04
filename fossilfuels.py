import xarray as xr 
import datetime

def get_fossilfuels(lon, lat, date):
    """
    Retrives CO2 emissions data from NASA fossil fuels dataset

    Data only available for the year 2018

    Unit: gC/m2/d
    """

    dateobj = datetime.datetime.strptime(date, "%Y-%m-%d")

    year = dateobj.year
    
    if year == 2018:
        month = dateobj.month

        ds = xr.open_dataset('NASAfossilfuels.nc')

        data = ds.land.sel(month=month, lon=lon, lat=lat, method='nearest')

        data = data.values

        data = data.tolist()

        return data
    
    else:
        data = "NA"
        return data