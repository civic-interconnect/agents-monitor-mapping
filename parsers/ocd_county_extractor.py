"""
parsers/ocd_county_extractor.py

Extracts OCD county-level divisions from the cloned ocd-division-ids repository.
Builds a scaffold mapping list for state and county-level identifiers.
"""

import os
import pandas as pd
from loguru import logger

def extract_counties(storage_path, config):
    logger.info("Starting OCD county extraction...")

    # Correct new CSV path (OCD now uses CSV structure)
    csv_path = os.path.join(storage_path, "ocd-division-ids", "identifiers", "country-us.csv")
    
    if not os.path.exists(csv_path):
        logger.error(f"OCD country-us CSV not found: {csv_path}")
        return pd.DataFrame()

    # Load full US divisions CSV
    df = pd.read_csv(csv_path, low_memory=False)
    logger.info(f"Loaded OCD country-us.csv with {len(df)} rows.")

    # Filter to county-level rows
    county_rows = df[df['id'].str.contains("/county:")].copy()
    logger.info(f"Extracted {len(county_rows)} county divisions.")

    # Apply state and county_slug extraction
    county_rows["state"] = county_rows["id"].apply(extract_state_code)
    county_rows["county_slug"] = county_rows["id"].apply(extract_county_slug)
    county_rows["openstates_jurisdiction"] = ""

    # Return scaffold dataframe
    county_rows = county_rows.rename(columns={"id": "ocd_id"})
    return county_rows[["ocd_id", "state", "county_slug", "openstates_jurisdiction"]]


def extract_state_code(ocd_id):
    """
    Example:
    ocd-division/country:us/state:mn/county:st_louis
    --> state:mn --> mn
    """
    parts = ocd_id.split("/")
    for part in parts:
        if part.startswith("state:"):
            return part.split(":")[1]
    return ""

def extract_county_slug(ocd_id):
    """
    Extract the county slug (lowercase underscore form)
    """
    parts = ocd_id.split("/")
    for part in parts:
        if part.startswith("county:"):
            return part.split(":")[1]
    return ""