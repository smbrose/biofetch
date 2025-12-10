# biofetch/main.py

import argparse
from .core import run_main

def parse_args():
    parser = argparse.ArgumentParser(description="Biomass Product Search and Download")
    
    parser.add_argument(
        '--ID',
        type=str,
        required=True,
        help="Selected collection (e.g. 'BiomassLevel2')"
    )
    
    parser.add_argument(
        "--time",
        type=str,
        help="Time range in the format 'start_date/end_date' (e.g., '2024-01-01/2025-08-19'). Use 'start_date/..' for open-ended ranges.",
        required=False,
    )

    parser.add_argument(
        '--bbox', 
        type=str, 
        help="(Optional) Bounding box: 'westlon, minlat, eastlon, maxlat'"
    )
    
    return parser.parse_args()

def main():
    args = parse_args()

    run_main(id=args.ID, time=args.time, bbox=args.bbox)

if __name__ == "__main__":
    main()
