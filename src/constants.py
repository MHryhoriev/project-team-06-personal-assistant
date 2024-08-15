"""
This module contains constants used throughout the application.
"""

from pathlib import Path

# File paths
BASE_DIR = Path(__file__).resolve().parent.parent
CONTACT_DATA_FILE_PATH = BASE_DIR.joinpath('data', 'contacts_data.json')
NOTE_DATA_FILE_PATH = BASE_DIR.joinpath('data', 'note.json')

# List of valid commands for the application
COMMANDS = ["add", "search", "remove", "exit", "close", "all"]