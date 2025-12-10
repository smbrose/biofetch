# biofetch/fetch.py
import requests
import time
from tqdm import tqdm

def download_products(download_targets):
    """
    Prompt user for access token and downloads all products that were passed as a list of URLs in download_targets.

    Args:
        download_targets (list): List of (url, name) tuples.
    """
    from biofetch.authorize import get_token
    access_token = get_token()
    if not access_token:
        print("❌ No access token provided. Aborting download.")
        return

    # We loop, download products successively and do not perform a bulk download. 
    print(f"\nStarting download of {len(download_targets)} products...")
    start = time.time()

    for url, name in download_targets:
        print(f"⬇️  Downloading {name} ...")
        download_file_with_bearer_token(url, access_token, f"{name}.ZIP")

    end = time.time()
    print(f"\n✅ All downloads completed in {end - start:.2f} seconds.")

def download_file_with_bearer_token(url, token, file_path, disable_bar=False):
    """
    Downloads a file from a given URL using a Bearer token.
    The bearer token can be retrieved here: 
    https://portal.maap.eo.esa.int/ini/services/auth/token/index.php

    Args:
        url (str): URL of the file to download.
        token (str): Bearer token to authenticate the request.
        file_path (str): Local path where the file will be saved.
        disable_bar (bool): Whether to disable the progress bar.
    """

    try:
        headers = {"Authorization": f"Bearer {token}"}  # Adds the Bearer token to the HTTP headers so the server knows you're allowed to access the file.

        # GET request, stream = TRUE (download in chunks), and raises an exception for bad status codes
        response = requests.get(url, headers=headers, stream=True) 
        response.raise_for_status()  

        file_size = int(response.headers.get('content-length', 0))
        chunk_size = 8 * 1024 * 1024  # 8 MB (File will be downloaded in 8 MB pieces)

        # Writes to file with progress bar (tqdm) and print success/error message
        with open(file_path, "wb") as f, tqdm(
            desc=file_path,
            total=file_size,
            unit='iB',
            unit_scale=True,
            unit_divisor=1024,
            disable=disable_bar,
        ) as bar:
            for chunk in response.iter_content(chunk_size=chunk_size):
                read_size = f.write(chunk)
                bar.update(read_size)

        if disable_bar:
            print(f"File downloaded successfully to {file_path}")

    except requests.exceptions.RequestException as e:
        print(f"Error downloading file: {e}")

