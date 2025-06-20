"""
parsers/ocd_county_extractor.py

Extracts OCD county-level divisions from the cloned ocd-division-ids repository.
Builds a scaffold mapping list for state and county-level identifiers.

MIT License — Civic Interconnect
"""

from pathlib import Path
import pandas as pd

from civic_lib_core import log_utils

logger = log_utils.logger


def extract_counties(storage_path: str | Path, config: dict) -> pd.DataFrame:
    """
    Extract county-level OCD identifiers and build a scaffold DataFrame.

    Args:
        storage_path (str | Path): Root path to today's storage folder.
        config (dict): Config dictionary (unused but accepted for consistency).

    Returns:
        pd.DataFrame: County scaffold with ocd_id, state, county_slug, and empty OpenStates column.
    """
    logger.info("Starting OCD county extraction...")

    csv_path = (
        Path(storage_path) / "ocd-division-ids" / "identifiers" / "country-us.csv"
    )
    if not csv_path.exists():
        logger.error(f"OCD country-us.csv not found: {csv_path}")
        return pd.DataFrame()

    df = pd.read_csv(csv_path, low_memory=False)
    logger.info(f"Loaded OCD country-us.csv with {len(df)} rows.")

    county_rows = df[df["id"].str.contains("/county:")].copy()
    logger.info(f"Extracted {len(county_rows)} county divisions.")

    county_rows["state"] = county_rows["id"].apply(extract_state_code)
    county_rows["county_slug"] = county_rows["id"].apply(extract_county_slug)
    county_rows["openstates_jurisdiction"] = ""

    county_rows = county_rows.rename(columns={"id": "ocd_id"})
    return county_rows[["ocd_id", "state", "county_slug", "openstates_jurisdiction"]]


def extract_state_code(ocd_id: str) -> str:
    """
    Extract the state code from an OCD division ID.

    Example:
        'ocd-division/country:us/state:mn/county:st_louis' -> 'mn'
    """
    return next(
        (part.split(":")[1] for part in ocd_id.split("/") if part.startswith("state:")),
        "",
    )


def extract_county_slug(ocd_id: str) -> str:
    """
    Extract the county slug (lowercase, underscore form) from an OCD division ID.

    Example:
        'ocd-division/country:us/state:mn/county:st_louis' -> 'st_louis'
    """
    return next(
        (
            part.split(":")[1]
            for part in ocd_id.split("/")
            if part.startswith("county:")
        ),
        "",
    )
