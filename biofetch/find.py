from pystac_client import Client
from datetime import datetime
from typing import Optional, List, Tuple

def search_products(
    id: str,
    time_range: Optional[str] = None,
    bbox: Optional[List[float]] = None
) -> List[Tuple[str, str]]:
    """
    Search a STAC API catalog for products in a given collection,
    optionally filtered by datetime range and bounding box.

    Args:
        start_date (Optional[str]): Start date for the datetime filter (format: YYYY-MM-DD)
        end_date (Optional[str]): End date for the datetime filter (format: YYYY-MM-DD)
        bbox (Optional[List[float]]): Optional bounding box as [minLon, minLat, maxLon, maxLat] 

    Returns:
        List[Tuple[str, str]]: A list of (product_url, product_name) tuples.
    """
    catalog_url = 'https://catalog.maap.eo.esa.int/catalogue/'
    collection_id = id
    
    try:
        # Open STAC catalog
        print("Opening STAC catalog...")
        catalog = Client.open(catalog_url)
        print("Catalog opened successfully.")
    except Exception as e:
        print(f"Error opening catalog: {e}")
        return []

    # Define query by setting up the search parameters
    search_kwargs = {
        "collections": [collection_id],
        "method": "GET"  # this could also be changed to the POST method  
    }

    # Add datetime filter if provided
    if time_range:
        try:
            time_parts = time_range.split("/")
            if len(time_parts) != 2:
                raise ValueError("Time range must be in the format 'start_date/end_date'.")

            start_date = time_parts[0] if time_parts[0] != ".." else None
            end_date = time_parts[1] if time_parts[1] != ".." else None

            # Validate the date formats
            if start_date:
                datetime.fromisoformat(start_date)  # Validate start_date format
            if end_date:
                datetime.fromisoformat(end_date)  # Validate end_date format

            # Construct datetime filter
            if start_date and end_date:
                search_kwargs["datetime"] = f"{start_date}T00:00:00Z/{end_date}T23:59:59Z"
            elif start_date:
                search_kwargs["datetime"] = f"{start_date}T00:00:00Z/.."
            elif end_date:
                search_kwargs["datetime"] = f"../{end_date}T23:59:59Z"

            print(f"Using datetime filter: {search_kwargs['datetime']}")
        except ValueError as e:
            print(f"Invalid time range: {e}")
            return []

    # Add spatial filter if provided
    if bbox:
        try:
            if len(bbox) != 4:
                raise ValueError("BBOX must have exactly 4 values: [minLon, minLat, maxLon, maxLat]")
            bbox_list = [float(coord) for coord in bbox]
            search_kwargs["bbox"] = bbox_list
            print(f"Using spatial filter: {search_kwargs['bbox']}")
        except ValueError as e:
            print(f"Invalid BBOX format: {e}")
            return []

    # Perform the search
    try:
        print("Performing search with parameters:", search_kwargs)
        results = catalog.search(**search_kwargs)
        items = list(results.items())
        print(f"Search completed. Found {len(items)} item(s).")
    except Exception as e:
        print(f"Error during search: {e}")
        return []

    # Show item previews
    if len(items) <= 20:
        print(f"\nShowing all {len(items)} item(s):")
        preview_items = items
    else:
        print(f"\nMore than 20 items found ({len(items)} total). Showing the first 10:")
        preview_items = items[:10]

    for i, item in enumerate(preview_items):
        print(f"\n[{i}] ID: {item.id}")
        try:
            product_href = item.assets['product'].href
            print(f"    Full Product URL: {product_href}")
        except KeyError:
            print(f"    Warning: No 'product' asset found for item {item.id}")

    # Collect all download targets
    download_targets = []
    for item in items:
        try:
            product_url = item.assets['product'].href
            product_name = f"{item.id}"
            download_targets.append((product_url, product_name))
        except KeyError:
            print(f"Skipping item {item.id}: No 'product' asset found.")
            continue

    print(f"\n{len(download_targets)} product URLs collected and ready for download.")
    return download_targets

