#!/usr/bin/env python3

import pkg_resources

dist = pkg_resources.get_distribution('nba')
__title__ = dist.project_name
__version__ = dist.version

