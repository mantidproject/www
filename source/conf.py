# -*- coding: utf-8 -*-

# Configuration file for the Sphinx documentation builder.
import datetime

# -- Project information -----------------------------------------------------
project = "MantidProject landing page"
copyright = (
    f"2007-{datetime.datetime.now().year} ISIS Rutherford Appleton Laboratory UKRI, "
    "NScD Oak Ridge National Laboratory, European Spallation Source, "
    "Institut Laue - Langevin & CSNS, Institute of High Energy Physics, CAS"
)

# -- General configuration ---------------------------------------------------

extensions = ["mantid_sphinx_theme"]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store", "nightly_build_warning.rst"]

# -- Options for HTML output -------------------------------------------------

# Use our custom mantid Sphinx theme.
html_theme = "mantid_sphinx_theme"

# Path to static assets to copy to final build
html_static_path = ["_static"]

# Additional css files to include in the pages
html_css_files = ["css/custom.css"]

# Context to pass to all page builds
html_context = {
    "default_mode": "light",
}

# Next/previous don't really appy here
html_theme_options = {
    "show_toc_level": 2,
    "show_prev_next": False,
}

# Turn the left bar into news reel
html_sidebars = {
    "**": [
        "sidebar-news.html",
        "sidebar-nav-bs.html",
    ],
}
