# biofetch 
[BIOMASS MAAP Portal](https://portal.maap.eo.esa.int/biomass/)

This package allows you to download biomass data via CLI. 
It is currently still under development and for now supports bulk download of products given a datetimerange and bounding box. 

You just provide the collection ID that you want, and, optionally a date and bounding box. If the products
are supported and you have provided your access token they are directly downloaded from ESA MAAP. 

## Prerequisities 

## Credentials

After downloading this repository add a credentials.txt in the same directory as the python module biofetch. 

### Creating `credentials.txt`

1. Create a plain text file called `credentials.txt`.
2. Populate it with your keys and tokens in this format:
```
CLIENT_ID=offline-token
CLIENT_SECRET=p1eL7uonXs6MDxtGbgKdPVRAmnGxHpVE
OFFLINE_TOKEN=your_longlasting_token_here
```
### Important

- Do **not** use quotes around the values.  
- Ensure there are no trailing spaces or extra characters.
Here you will need to store ESA MAAP's CLIENT_ID, CLIENT_SECRET, and your 90-day personal offline token.

The latter can be generated here: [ESA MAAP 90 day token](https://portal.maap.eo.esa.int/ini/services/auth/token/index.php)

## PREREQUISITES
To run the main script and notebook, you will need to install specific python libraries. 

## Download mode: Examples 

**From the command line:**

--ID (required): The collection ID to search within. A multi-collection search is currently not possible. 

--time (optional): Find the products that were acquired in a specific time range start_time/end_time

To fetch Biomass Level 1a products acquired between 2025-05-03 00:00 and 2025-12-03 23:59 within a bounding box around Borneo (108.0,-4.66,119.0,8.05), an example CLI input would look like this:

```
python -m biofetch --ID BiomassLevel1aIOC --time 2025-05-03/2025-12-03 --bbox 108.0 -4.66 119.0 8.05
```

-------------------------------
Questions: saskia.brose@esa.int 

