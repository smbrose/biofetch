# biofetch/core.py

from .fetch import download_products
from .find import search_products

def run_main(id: str, time: str = None, bbox: str = None, prompt_download: bool = True):

    """
    This function drives the main functionality and does xyz. 

    Parameters: 

    Returns: 
    """
  
    print(f"Running with ID={id}, Time={time}, BBOX={bbox}")

    # Select pre-op or normal catalog URL 
    catalog_url = 'https://catalog.maap.eo.esa.int/catalogue/'
    print(catalog_url)
    
    # Find products, retrieve token, and download products
    download_targets = search_products(id, time, bbox)
    print(download_products)
    
    if prompt_download:
        proceed = input("\nWould you like to download all found products now? (yes/no): ").strip().lower()
        if proceed in ['yes', 'y']:
            download_products(download_targets)
        else:
            print("Download skipped.")
    else:
        download_products(download_targets)
    
