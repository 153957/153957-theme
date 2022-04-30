# 153957 theme

[![PyPI](https://img.shields.io/pypi/v/153957-theme)](https://pypi.org/project/153957-theme/)
[![License](https://img.shields.io/github/license/153957/153957-theme)](https://github.com/153957/153957-theme/blob/master/LICENSE)
[![Build](https://img.shields.io/github/workflow/status/153957/153957-theme/Run%20tests)](https://github.com/153957/153957-theme/actions)

[View demo album here](https://153957.github.io/153957-theme/)


## Photo gallery template

Web photo gallery templates adapted to my personal preferences.


## Usage

This section describes how to install an use this theme.


### Installation

Install the `153597-theme` package:

    $ pip install 153957-theme


### Configure

In `sigal.conf.py` configuration for an album the `theme` setting should be
a path to a theme directory. However, since this theme is provided as a Python
package its location might be harder to get. Two options are available for
configuration:

The theme can be configured as a plugin or you can get the path by importing
the package. By setting is as plugin the theme is automatically set.

Set `theme` to an empty string and add the theme and menu plugins:

    theme = ''
    plugins = ['153957_theme.theme', '153957_theme.full_menu', …]

The alternative:

    from 153957_theme import theme
    theme = theme.get_path()
    plugins = ['153957_theme.full_menu', …]


## Sources

Based on [sigal](https://sigal.saimon.org/) version of Galleria theme, which is
distributed under the MIT License.

Theme based on [Galleria Classic](https://github.com/GalleriaJS/galleria/),
which is distributed under the MIT License.