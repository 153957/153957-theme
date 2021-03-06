# This configuration has been configured for this demo, not all
# normal sigal settings have an effect in this theme.

# ---------------------
# General configuration
# ---------------------

source = 'source'
destination = 'output'
theme = ''  # theme is automatically set by the theme plugin.
title = 'Photography'
author = '153957 Photography'
author_link = 'http://arne.delaat.net/'
use_orig = True

# --------------------
# Thumbnail generation
# --------------------

make_thumbs = True
thumb_dir = 'thumbnails'
thumb_size = (280, 140)
thumb_fit = False
albums_sort_attr = 'name'
medias_sort_attr = 'date'
ignore_directories = []
ignore_files = []

# --------
# Plugins
# --------

plugins = ['153957_theme.full_menu', '153957_theme.theme']
