import rasterio
from rasterio.env import Env

def read_data_vsicurl(url, access_token): 
    headers = f"Authorization: Bearer {access_token}"
    with Env(GDAL_HTTP_HEADERS=headers):
        with rasterio.open(f'/vsicurl/{url}') as ds:
            data_array = ds.read()  
    return data_array
