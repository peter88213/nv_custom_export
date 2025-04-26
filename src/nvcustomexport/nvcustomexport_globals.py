"""Provide global constants.

Copyright (c) 2025 Peter Triesberger
For further information see https://github.com/peter88213/nv_custom_export
License: GNU GPLv3 (https://www.gnu.org/licenses/gpl-3.0.en.html)
"""
from pathlib import Path

HOME_DIR = str(Path.home()).replace('\\', '/')
INSTALL_DIR = f'{HOME_DIR}/.novx'
TEMPLATE_FOLDER = 'nv_custom_export'
