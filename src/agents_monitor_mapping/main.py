"""
main.py - Civic Interconnect Monitor Mapping Agent

This agent monitors mapping changes and generates daily reports.

MIT License — Civic Interconnect
"""

import sys
from pathlib import Path

import pandas as pd
from civic_lib_core import config_utils, log_utils
from civic_lib_core.date_utils import today_utc_str
from civic_lib_core.path_utils import ensure_dir
from civic_lib_core.yaml_utils import write_yaml
from dotenv import load_dotenv

from agents_monitor_mapping.parsers import ocd_county_extractor, ocd_parser


def main():
    """
    Main function to run the mapping agent.
    Expects config.yaml to include:
    - storage_path
    - report_path
    - ocd_repo_url
    """

    log_utils.init_logger()
    logger = log_utils.logger

    logger.info("===== Starting Monitor Mapping Agent =====")
    load_dotenv()

    root_dir = Path.cwd()
    config = config_utils.load_yaml_config("config.yaml", root_dir=root_dir)
    version = config_utils.load_version("VERSION", root_dir=root_dir)
    today = today_utc_str()
    logger.info(f"Polling date: {today}")

    storage_path = ensure_dir(Path(config["storage_path"]) / today)
    report_path = ensure_dir(Path(config["report_path"]) / today)
    logger.info(f"Storage path: {storage_path}")
    logger.info(f"Report path: {report_path}")

    # Clone or pull OCD repository
    try:
        logger.info("Pulling OCD Divisions...")
        ocd_changes = ocd_parser.run(storage_path, config)
        logger.info("OCD Divisions completed.")
    except Exception as e:
        ocd_changes = f"OCD pull failed: {str(e)}"
        logger.error(ocd_changes)

    # Load existing mapping CSV (if present)
    mapping_file = Path("mapping") / "ocd-to-openstates.csv"
    if mapping_file.exists():
        mapping = pd.read_csv(mapping_file)
        logger.info(f"Loaded mapping file with {len(mapping)} records.")
    else:
        logger.warning("Mapping file not found — starting with empty DataFrame.")
        mapping = pd.DataFrame(columns=["ocd_id", "openstates_jurisdiction"])

    # Extract scaffold from latest country-us.csv
    try:
        county_df = ocd_county_extractor.extract_counties(storage_path, config)
        logger.info(f"Extracted {len(county_df)} county scaffold rows.")
    except Exception as e:
        logger.error(f"County extraction failed: {str(e)}")
        county_df = pd.DataFrame()

    # Compose and write YAML report
    report = {
        "date": today,
        "version": version,
        "OCD Divisions": ocd_changes,
        "Mapping Records": len(mapping),
        "County Scaffold Rows": len(county_df),
    }

    report_file = report_path / f"{today}-mapping-report.yaml"
    write_yaml(report, report_file)
    logger.info(f"Report written: {report_file}")


if __name__ == "__main__":
    try:
        main()
        sys.exit(0)
    except Exception:
        sys.exit(1)
