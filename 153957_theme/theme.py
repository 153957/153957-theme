"""Use the 153957-theme as theme for the gallery"""

from pathlib import Path
from shutil import rmtree

from sigal import signals


def get_path():
    return str(Path(__file__).resolve().parent)


def theme(gallery):
    """Set theme settings to this theme"""

    gallery.settings['theme'] = get_path()


def remove_leaflet(gallery):
    """Remove Leaflet which is part of the default static files in sigal, but not used by this theme"""

    leafet_path = Path(gallery.settings['destination']) / 'static/leaflet'
    rmtree(leafet_path)


def register(settings):
    signals.gallery_initialized.connect(theme)
    signals.gallery_build.connect(remove_leaflet)
