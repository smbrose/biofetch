# biofetch 
[BIOMASS MAAP Portal](https://portal.maap.eo.esa.int/biomass/)

This package allows you to download biomass data via CLI. 

You just provide the collection ID that you want, and, optionally a date and bounding box. If the products
are supported and you have provided your access token they are directly download the product from ESA MAAP. 


## Prerequisities 

To run the main script and notebook, you must have the following dependencies installed:

- requests: For making HTTP requests to download products.
- tqdm: For progress bars during product download.
- pystac-client and pystac: For interacting with the STAC API and handling metadata.
- ... 


## Available (IOC) Biomass Colleciton IDs: 

- BiomassAuxIOC
- BiomassLevel0IOC
- BiomassLevel1alOC
- BiomassLevel1bIOC
- BiomassLevel1cIOC
- BiomassLevel2a, BiomassLevel2alOC
- BiomassLevel2bIOC
- BiomassSimulated 

## Download mode: Examples 

**From the command line:**

--ID (required): The collection ID to search within. A multi-collection search is currently not possible. 

--time (optional): Find the products that were acquired in a specific time range start_time/end_time

--bbox (optional): Finds products within a rectangular spatial extent on the globe, defined by four edges: 

> West longitude: left boundary

> Minimum latitude: bottom boundary

> East longitude: right boundary

> Maximum latitude: top boundary

To fetch Biomass Level 1a products acquired between 2025-07-03 00:00 and 2025-07-04 23:59 within a bounding box around Borneo (108.0,-4.66,119.0,8.05), an example CLI input would look like this:

```
python -m biofetch --ID BiomassLevel1aIOC --time 2025-07-03/2025-07-03 --bbox 108.0,-4.66,119.0,8.05
```

-------------------------------
Questions: saskia.brose@esa.int 

