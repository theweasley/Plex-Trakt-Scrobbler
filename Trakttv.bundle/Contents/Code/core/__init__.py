import sys

# submodules for Plex plugins "hack"

import logger
sys.modules['core.logger'] = logger

import helpers
sys.modules['core.helpers'] = helpers

import update_checker
sys.modules['core.update_checker'] = update_checker
