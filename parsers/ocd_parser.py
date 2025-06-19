"""
parsers/ocd_parser.py

This module monitors the Open Civic Data (OCD) repository for changes in civic divisions.
It clones the OCD repository if not present, pulls updates, and reports completion.

MIT License — Civic Interconnect
"""

from pathlib import Path
import git

from civic_lib import log_utils
from civic_lib.path_utils import ensure_dir

logger = log_utils.logger


def run(storage_path: str | Path, config: dict) -> str:
    """
    Clone or update the OCD Divisions repository.

    Args:
        storage_path (str | Path): Local storage path for this polling run.
        config (dict): Loaded configuration containing 'ocd_repo_url'.

    Returns:
        str: Status message confirming repository update.
    """
    path = ensure_dir(Path(storage_path))
    repo_path: Path = path / "ocd-division-ids"

    if not repo_path.exists():
        logger.info("Cloning OCD repository...")
        git.Repo.clone_from(config["ocd_repo_url"], repo_path)
    else:
        logger.info("Pulling latest OCD updates...")
        repo = git.Repo(repo_path)
        repo.remotes.origin.pull()

    return "OCD repository updated"
