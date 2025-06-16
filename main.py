"""
main.py - Civic Interconnect Mapping Agent

This script serves as the main entry point for the Civic Interconnect Mapping Assistant Agent.
It pulls OCD divisions, manages mappings, extracts counties, and generates daily reports.
It uses environment variables for configuration and logging, and it is designed to run daily.
"""

import os
import yaml
import pandas as pd
from datetime import datetime, timezone
from dotenv import load_dotenv
from parsers import ocd_parser, ocd_county_extractor
from loguru import logger

# Initialize logger
os.makedirs("logs", exist_ok=True)
logger.add("logs/{time:YYYY-MM-DD}.log", rotation="1 day", retention="7 days", level="INFO")

logger.info("===== Starting Mapping Assistant Agent =====")

# Load environment variables
load_dotenv()

# Load config
with open("config.yaml", "r") as f:
    config = yaml.safe_load(f)

# Load agent version
with open("VERSION") as f:
    version = f.read().strip()
logger.info(f"Agent version: {version}")

# Today's timestamp
today = datetime.now(timezone.utc).strftime("%Y-%m-%d")

# Setup folders
daily_storage_path = os.path.join(config["storage_path"], today)
os.makedirs(daily_storage_path, exist_ok=True)

# OCD pull
try:
    logger.info("Pulling OCD Divisions...")
    ocd_changes = ocd_parser.run(daily_storage_path, config)
    logger.info(ocd_changes)
except Exception as e:
    logger.error(f"OCD pull failed: {str(e)}")
    ocd_changes = f"OCD pull failed: {str(e)}"

# Load current mapping CSV
mapping_path = os.path.join("mapping", "ocd-to-openstates.csv")
if os.path.exists(mapping_path):
    mapping = pd.read_csv(mapping_path)
    logger.info(f"Loaded mapping file with {len(mapping)} records.")
else:
    logger.warning("Mapping file not found — starting empty.")
    mapping = pd.DataFrame(columns=["ocd_id", "openstates_jurisdiction"])

# Extract county scaffold from country-us.csv
try:
    county_df = ocd_county_extractor.extract_counties(daily_storage_path, config)
    logger.info(f"Extracted {len(county_df)} county scaffold rows.")
except Exception as e:
    logger.error(f"County extraction failed: {str(e)}")
    county_df = pd.DataFrame()

# Write daily report
os.makedirs("reports", exist_ok=True)
report_path = os.path.join("reports", f"{today}-mapping-report.yaml")

report = {
    "date": today,
    "OCD Divisions": ocd_changes,
    "Mapping Records": len(mapping),
    "County Scaffold Rows": len(county_df)
}

with open(report_path, "w") as f:
    yaml.dump(report, f, sort_keys=False)

logger.info(f"Report written: {report_path}")
