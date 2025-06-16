""" 
parsers/ocd_parser.py

This module handles the pulling and updating of the OCD Divisions repository.
It clones the repository if it doesn't exist, or pulls the latest changes if it does.
"""

import os
import git
from loguru import logger

def run(storage_path, config):
    repo_path = os.path.join(storage_path, "ocd-division-ids")

    if not os.path.exists(repo_path):
        git.Repo.clone_from(config["ocd_repo_url"], repo_path)
        logger.info("OCD repository cloned successfully.")
        os.system(f"cd {repo_path} && git lfs pull")
    else:
        repo = git.Repo(repo_path)
        repo.remotes.origin.pull()
        logger.info("OCD repository updated successfully.")
        os.system(f"cd {repo_path} && git lfs pull")

    return "OCD repository updated"
